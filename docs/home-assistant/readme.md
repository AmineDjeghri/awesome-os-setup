# Laptop as a server

## Ubuntu Server 24.04

### Setup

- Set up an Ubuntu Server on a laptop.
  - You better have Ethernet connection. If you only have wifi, buy a usb  ethernet adapter. It's worth it and you will be able to use the bridge mode which is not available with wifi.
  - boot up ubuntu from a usb drive, select the language, keyboard layout, and timezone. In the network section, select the Ethernet connection, an IP 192.168.x.x will be assigned.
  - Wait for mirror to be configured.
  - Assign some partitions : `ext4` 100GB for `/` and some space for var/lib. `/var/lib` is where most application data lives. KVM/Libvirt stores virtual machine disks in /var/lib/libvirt/images. Docker (if you use it for AdGuard) stores everything in /var/lib/docker.
  - Install `openssh-server` and manage it remotely using SSH from another machine so you can copy-paste commands from the documentation.

### First checks / updates

- Run updates:

```bash
sudo apt update && sudo apt upgrade
```

- Run `ip addr` to check the IP address. This is your HOST-IP. It looks like `192.168.x.x`
- Run `ping google.com` to check the connection.

- Connect remotely in the same network using SSH and the HOST-IP from another machine that has a GUI and a browser so you can copy-paste commands from the documentation.

```bash
ssh username@192.168.x.x
```

- I customized the shell environment by installing Zsh and tools from the [Awesome OS](https://github.com/AmineDjeghri/awesome-os-setup) to improve usability and productivity.

### Lid closed (Laptop)

- File: `/etc/systemd/logind.conf`
- Change this line: `HandleLidSwitch=ignore`
- Restart with `sudo systemctl restart systemd-logind`

## Home Assistant

### Virtualization

- I verified that virtualization was supported on the system, checked Secure Boot status:
  - Run:

```bash
egrep -c '(vmx|svm)' /proc/cpuinfo
```

  Should return a number `> 0`.
- Sometimes it returns `0`. In that case you need to check if Virtualization is enabled in your BIOS to ensure compatibility.
- If you still have `0`, and you are sure that Virtualization is enabled in your BIOS, ignore the `0`.

### Install KVM (Kernel-based Virtual Machine) and libvirt

- Install:

```bash
sudo apt-get install qemu-system-x86 libvirt-daemon-system virtinst \
ovmf swtpm qemu-utils guestfs-tools libosinfo-bin -y
```

- Verify:

```bash
lsmod | grep kvm
sudo kvm-ok
lscpu | grep Virtualization
```

- Check libvirt:

```bash
sudo systemctl status libvirtd
sudo usermod -aG libvirt $USER
sudo usermod -aG kvm $USER
```

#### Create a bridge configuration
A network bridge in KVM allows your virtual machines to appear directly on the same network as your host.

- Without a bridge: VMs often use NAT (Network Address Translation). They can access the internet, but other devices on your LAN cannot access the VMs directly.

- With a bridge: VMs act like physical machines on your network. They get an IP from your router (or DHCP server) just like your host, and other devices can communicate with them directly.

- This works only with Ethernet, not with wifi.

How to:
- Identify your network interface with `ip addr`, it should look like `enp0s31f6` or `enx001`  It is where you can see eth0.
- Create a bridge configuration file in `/etc/netplan/` with the following content:

- Create a bridge configuration file in  `/etc/netplan/01-bridge.yaml`, replace `enx001cc253c478` with your interface name:
```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    enx001cc253c478:
      dhcp4: no
  bridges:
    br0:
      interfaces: [enx001cc253c478]
      dhcp4: yes
      parameters:
        stp: false
        forward-delay: 0
```


- Before applying the configuration, connect physically to the server because the next command will change the ip address of the SSH and your SSH connection will be lost.
- Your host’s IP will move from enx001cc253c478 to br0
- Apply the configuration:

```bash
sudo netplan apply
```
If you are connected via SSH, you will be disconnected.
Go physically to the server and get the new IP address:

```bash
ip addr
```
Your `interface name` will no longer have a direct IP. All traffic goes through `br0`.
To connect to the server via SSH, you will need to use the ``br0`` address.

### Home Assistant OS in a VM

- Doc: https://www.home-assistant.io/installation/alternative#virtual-machines

- Download the Home Assistant OS image:

```bash
wget https://github.com/home-assistant/operating-system/releases/download/16.3/haos_ova-16.3.qcow2.xz
```

- Move the image to the libvirt directory:

```bash
sudo mv haos_ova-16.3.qcow2.xz /var/lib/libvirt/images/
```

- Uncompress the image:

```bash
sudo xz -d /var/lib/libvirt/images/haos_ova-16.3.qcow2.xz
```

- important: we will use sudo so with all the commands later like `virsh list --all` should use sudo ``sudo virsh list --all`` otherwise it will show nothing.
- HAOS runs under system libvirt  and needs to be managed by root and uses /var/lib/libvirt
-

| Feature                      | system (`root`) | user        | Notes / Explanation                                                                                                   |
|------------------------------|-----------------|-------------|-----------------------------------------------------------------------------------------------------------------------|
| Autostart on boot            | ✅               | ⚠️ Possible | Root/systemd can autostart VMs easily. Users can use `systemd --user` or autostart scripts, but extra setup required. |
| USB passthrough              | ✅               | ⚠️ Possible | Root can attach any USB device. Users can do it if they’re in `libvirt`/`kvm` groups and udev rules allow access.     |
| Bluetooth / Zigbee           | ✅               | ⚠️ Possible | Needs hardware access; root can do it directly. Users need correct groups and permissions.                            |
| Headless server use          | ✅               | ✅           | Works for both. Headless VM does not require GUI.                                                                     |
| Network bridges              | ✅               | ⚠️ Possible | Root can create bridges freely. Users need pre-made bridges or `sudo` for creation.                                   |
| IP forwarding / port mapping | ✅               | ❌           | Modifying `sysctl` and `iptables` requires root. Users cannot forward ports without `sudo`.                           |
| Cloudflare tunnel stability  | ✅               | ✅           | Independent of root vs user. Tunnels are stable as long as service runs correctly.                                    |



- Create the VM: ( we are adding --network bridge=br0) to use the bridge.

```bash
sudo virt-install --name haos --description "Home Assistant OS" --os-variant=generic --ram=4096 --vcpus=2 --disk /var/lib/libvirt/images/haos_ova-16.3.qcow2,bus=scsi --controller type=scsi,model=virtio-scsi --import --graphics none --boot uefi --network bridge=br0,model=virtio --console pty,target_type=serial
```

- Once you see `Welcome to Home Assistant homeassistant login:`, you can quit leave the console using `Ctrl + Alt Gr +]` or Open a new terminal.

- Now we need to check if HAOS is running:
  - `sudo virsh list --all`, you should see the VM running named `haos`
  - Find the IP address of the HAOS VM: From your router’s DHCP table (recommended) on your router app/website. As you can understand, the VM is like a device that is connected to the router, that is why the router assigned it an IP address.
  - The default port is `8123`
  - Check if HAOS is running : open a browser and go to `http://<HAOS-IP>:8123` or use curl: ``curl -v http://<HAOS-IP>:8123``
  - You should see the Home Assistant login page.
  - Back on your terminal, activate the autostart: `sudo virsh autostart haos`
  - Check autostart in: `sudo virsh dominfo haos`


You need to differentiate between:

- HOST IP (the IP of the laptop): `ip addr` example: `192.168.1.86`
- VM-IP or HAOS-IP (the IP of the HAOS VM) example: `192.168.122.243`
- Both have IPs assigned from the router. The HAOS VM uses a bridge, so it gets an IP from the router just like a regular device.
- These IPs can change if we restart the router, we will assign static ip to the VM.

#### inside HA in your browser or mobile app:

- In your browser, go to `http://<HOST-IP>:8123`, for example `http://192.168.1.86:8123`.
- Create an account.
- User settings: Profile -> General-> language, date format, number format, etc.
- Check Advanced mode in General settings.
- in User settings, go to Security -> Enable MFA
- In Settings, check for an update for HAOS. After the update it will restart the server.
- In the addon store, click on the three dots on the top right and add this repository: https://github.com/homeassistant-apps/repository
- Set up a static IP for the VM: in HAOS website go to Settings -> System -> Network -> and change IPv4 from auto to static and IPv6 too. You can keep the default ip that is assigned to the VM.

### 2. Accessing HAOS from outside your local network  — Cloudflare Tunnel Setup
- Create a Domain or your domain is already managed by **Cloudflare**
- In HAOS, add the addon `file editor`.
- Follow this video: https://youtu.be/JGAKzzOmvxg
- Don't forget to update and save configuration.yaml
- Restart HAOS
- On you phone, when you add home assistant, add both local and external URL, so you can connect when you are outside
- Adding both local and external URL is important because the external URL is the one that will be used when you are outside your local network.

**Add Cloudflare Access (Zero Trust) ⭐⭐⭐**

This is the single biggest security upgrade. Before showing your Home Assistant app in your browser or mobile, it will force the user to first login via an email or something.
If the User can't log in, he won't be able to see the app.

- You are protecting for example `ha.yourdomain.com`
Go to  Cloudflare Zero Trust -> Access Controls -> Applications -> Self-hosted:

##### 1️⃣ Basic Information (Top Section)

Application name

Use something clear:

- Home Assistant
- (or Home Assistant – Production if you like)

Session Duration

Recommended:

- 24 hours or You can put more

##### 2️⃣ Add Public Hostname (IMPORTANT)

Click Add public hostname.

Fill in:

- Hostname: `ha.yourdomain.com`
- Path: `/*`
- Type: HTTP

👉 This is what actually puts the Access login page in front of Home Assistant.

Do NOT add private IP unless you know you need it.

##### 3️⃣ Browser Rendering Settings

Leave this OFF / untouched.

(Home Assistant does NOT need SSH/RDP/VNC rendering)

##### 4️⃣ Policies (MOST IMPORTANT PART)

Click Add a policy. It will open a new page, and need to go back to this page and refresh it to show the policies.

Policy 1 — Allow yourself (and family)

- Policy name: Allow Home Assistant Users
- Action: Allow

Rules (choose ONE of these methods):

✅ Best option: Email-based

- Include -> Emails -> `your@email.com`
- You can add multiple emails (family members).

✅ Alternative: Identity provider

If using Google / Microsoft / GitHub:

- Include -> Identity Provider -> Google
- Include -> Emails ending in -> `@gmail.com`

❌ Do NOT use:

- “Allow everyone”
- IP-only rules (unless combined with email)
- Country-only rules alone

(Optional but recommended)

- Add Require MFA if available in your plan.

##### 5️⃣ (Optional) Add a Second Policy – Emergency Lockdown

Advanced but useful:

- Policy name: Block High Risk Countries
- Action: Block
- Rule:
  - Include -> Countries -> (countries you NEVER travel to)

Cloudflare evaluates Block after Allow, so this is safe.

##### 6️⃣ Login Methods

You’ll see:

- Accept all available identity providers -> ON

Recommended setting:

✅ Leave this ON if:

- You trust future IdPs
- You are the only admin

OR

🔒 Turn OFF and explicitly select:

- Google
- Email OTP

This is slightly more secure, less future surprise.

##### Go back to the previous page to see the policies
Where you put your domain, choose the policies you added.

##### 7️⃣ Save the Application ✅

Once saved:

- Visiting `ha.yourdomain.com` should show Cloudflare Access login. If it doesn't force refresh the page or clear cookies.
- Only after login -> Home Assistant loads

If you do a restoration, or change something in cloudflare, and you see that you can't view home assistant, delete the cookies and try again.

#### Activate MFA
- In profile -> security, activate MFA

You should now have:

- ✅ Cloudflare Tunnel (no ports open)
- ✅ Cloudflare Access login in front of HA
- ✅ Email or Google login
- ✅ MFA
- ✅ 24h session

---

### Home Assistant Devices and integrations
- Integrations
- Addons
- Other repositories like : HACS
- Always search for an open source integration before using a proprietary app. For example TP-link, Dreame, LG ThinQ, Bosch Home connect have open sources integrations and are far better than the proprietary apps.
- Some devices need their app to work properly or to display more functionalities. For example LG, Bosch. I always advice to install the app for these devices even if you can control them later in Home Assistant..

#### Matter over Wi-Fi
- You don't need a matter controller for that, you just need matter devices and Home Assistant.

#### Matter Over thread devices
- If the device does Matter over Thread though, you will need a Thread Border Router (TBR) on your network like the [Sonoff MG24](https://www.amazon.fr/SONOFF-Dongle-PMG24-Dongle-Plus-MG24/dp/B0FMJD288B) or Apple HomePod Mini or latest Amazon Echo devices that have a thread router capability.
- Do not use Aqara M100 because it is proprietary and not well-supported in Home Assistant.

- How to setup Sonoff MG24
  - Attach to usb port, run `usb-devices` on ubuntu and get Vendor and  ProdID
  - Run
````sh
sudo virsh attach-device haos /dev/stdin --persistent <<EOF
<hostdev mode='subsystem' type='usb' managed='yes'>
  <source>
    <vendor id='0x10c4'/>
    <product id='0xea60'/>
  </source>
</hostdev>
EOF
````

or using the bus and device:
````
sudo virsh attach-device haos /dev/stdin --persistent <<EOF
<hostdev mode='subsystem' type='usb' managed='yes'>
  <source>
    <address bus='1' device='12'/>
  </source>
</hostdev>
EOF
````
  - Run `sudo virsh reboot haos`
  - Go to Home Assistant -> Settings -> System -> Hardware -> All Hardware -> search for 'Sonoff'
  - Flash it using this [tutorial](https://blog.dautek.fr/comment-installer-le-dongle-zigbee-et-thread-sonoff-mg24-sur-home-assistant)

#todo:
- backup vm, HAOS,


## Other stuff
- **HAOS backup & restoration** with google drive: https://github.com/sabeechen/hassio-google-drive-backup
  - Test the backup at least once to see it everything works: https://youtu.be/xXXW7sQ9rqs?t=274
  - Backup keeps everything, even cloudflare configuration (delete the cookies if you see that the login page is not showing using your domaine name)
  - Samba backup addon: https://github.com/thomasmauerer/hassio-addons/tree/master/samba-backup
  - After a restoration, everything should work as expected,
    - you need to clean the cookies on your broswer because of cloudflare.
    - the Sonoff MG24, can be unrecoginized, just wait a bit, if it is not recognized, detach it and attach it again.
- **SAMBA** to access HA files from windows, macOS etc.. , this is useful for uploading backups for example: https://www.youtube.com/watch?v=Vu_oxefjd0I
- Read about common tasks : https://www.home-assistant.io/common-tasks/os/#installing-and-using-the-samba-add-on
- **Alexa Media player** : https://www.youtube.com/watch?v=TDdREzkigIE&t
- **Dreame vaccum**:
  - Dreame : : "dreame vacuum home assistant" https://share.google/frXsgWNgnjGPGeMQM
  - Use version >2 , it supports multiple account (dreamehome, xiaomi etc..)
- **LG**: Better use the integration from HACS
