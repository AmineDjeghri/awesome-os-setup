# Laptop as a server

## Ubuntu Server 24.04

### Setup

- Set up an Ubuntu Server on a laptop.
  - Configure the network (`wlo1 for example`) and wait for the IP address to be assigned.
  - Wait for mirror to be configured.
  - Assign a partition (format `ext4` and mount it to `/`).
  - Install `openssh-server` and manage it remotely using SSH from another machine so you can copy-paste commands from the documentation.

### First checks / updates

- Run updates:

```bash
sudo apt-get update && sudo apt-get upgrade
```

- Run `ip addr` to check the IP address. This is your HOST-IP.
- Run `ping google.com` to check the connection.

- Connect remotely in the same network using SSH and the HOST-IP.

```bash
ssh username@192.168.x.x
```

- I customized the shell environment by installing Zsh and tools from the [Awesome OS](https://github.com/AmineDjeghri/awesome-os-setup) to improve usability and productivity.

### Lid closed

- File: `/etc/systemd/logind.conf`
- Change this line: `HandleLidSwitch=ignore`
- Restart:

```bash
sudo systemctl restart systemd-logind
```

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



- Create the VM:

```bash
sudo virt-install --name haos --description "Home Assistant OS" --os-variant=generic --ram=4096 --vcpus=2 --disk /var/lib/libvirt/images/haos_ova-16.3.qcow2,bus=scsi --controller type=scsi,model=virtio-scsi --import --graphics none --boot uefi
```

- Once you see `Welcome to Home Assistant homeassistant login:`, you can quit and close the terminal. Open a new terminal.

- Now we need to check if HAOS is running:
  - `sudo virsh list --all`, you should see the VM running named `haos`
  - Check HAOS IP: `sudo virsh domifaddr haos`
  - The default port is `8123`
  - Check if HAOS is running:

```bash
curl http://<HAOS-IP>:8123
```

  Example:

```bash
curl -v 192.168.122.243:8123
```

  - Activate the autostart: `sudo virsh autostart haos`
  - Check autostart in: `sudo virsh dominfo haos`


You need to differentiate between:

- HOST IP (the IP of the laptop): `ip addr` example: `192.168.1.86`
- VM-IP or HAOS-IP (the IP of the HAOS VM): `sudo virsh domifaddr haos` example: `192.168.122.243`
- HAOS-IP runs on the HOST-IP

### 1. First accessing HAOS from LAN
To access Home Assistant from your phone without SSH tunnels, we can enable port forwarding inside the HOST (ubuntu-server).

#### Enable IP Forwarding

Linux defaults to blocking traffic passing through it (router mode). We need to enable it.

On the host machine, enable it immediately:

```bash
sudo sysctl -w net.ipv4.ip_forward=1
```

Make it permanent (so it survives a reboot):

```bash
echo "net.ipv4.ip_forward = 1" | sudo tee -a /etc/sysctl.conf
```

We need to tell Ubuntu: "If anyone knocks on my Wi-Fi IP on port 8123, send them to the internal VM (HAOS-IP: 192.168.xx.xx.)"

Run these commands exactly:

1. Forward incoming TCP traffic on `wlo1` port `8123` -> VM IP, replace the address with your VM IP (`<HAOS-IP>`):

```bash
sudo iptables -t nat -A PREROUTING -i wlo1 -p tcp --dport 8123 -j DNAT --to-destination 192.168.122.xx:8123
```

2. Allow the forwarded traffic to pass through the firewall, replace the address with your VM-IP:

```bash
sudo iptables -I FORWARD -d 192.168.122.xx -p tcp --dport 8123 -j ACCEPT
```

3. Try to reach HAOS from your computer using the HOST IP:

```bash
curl -v http://<HOST-IP>:8123
```

Example:

```bash
curl -v 192.168.1.86:8123
```

Open a browser and go to `http://<HOST-IP>:8123`, for example `http://192.168.1.86:8123`.

If you can't, check  Firewalls (UFW): Since you are on Ubuntu Server, `ufw` (Uncomplicated Firewall) might be active. If it is, it will block port `8123` before iptables even sees it.
Run this to check status:

```bash
sudo ufw status
```


#### Discovering devices
Switch from "NAT" to "Bridged" Networking
For Home Assistant to work properly with Matter (and HomeKit), it needs to be "on the same level" as your other devices. You need to change your KVM network settings from Default (NAT) to a Bridge (br0).

Bridging over Wi-Fi is notoriously difficult on Linux because most Wi-Fi drivers do not support "Multiple MAC addresses" on a single connection. That's we didn't use it.
Since Matter and HomeKit rely on Multicast (mDNS) to "find" each other, and NAT blocks those discovery packets, your VM is essentially "deaf" to the Aqara M100.

Here is how to fix it:

Install "Avahi Reflector" on your Ubuntu Host
If you want Matter/HomeKit to work through the NAT, you need to tell your Ubuntu Server to "reflect" discovery signals from the physical Wi-Fi into the VM's private network.

- On your Ubuntu Server host, install Avahi: `sudo apt update && sudo apt install avahi-utils avahi-daemon -y`

- Edit the configuration:`sudo nano /etc/avahi/avahi-daemon.conf`
- Find the [reflector] section and change it to:
`  [reflector]
  enable-reflector=yes`

- Restart Avahi: `sudo systemctl restart avahi-daemon`
- This helps "Multicast" jump across the IP forwarding gap.


### Summary of NAT, Port-forwarding and Avahi Reflector
**What is NAT?**
NAT (Network Address Translation) is like a receptionist at a large office building.

The Problem: Your router only has one "Public" IP address from your ISP, but you have 20 devices (laptop, phone, VM, etc.) in your house.

The NAT Solution: Your router gives every device a "Private" IP (like 192.168.x.x or 10.0.x.x). When your VM wants to talk to the internet, the router swaps the VM's private address for its own public address, sends the data, and remembers who it belongs to so it can hand the reply back to the right device.

In your case, KVM created a second NAT inside your server.

Home Network: 192.168.1.x (Physical router)

VM Network: 192.168.122.x (Virtual router inside your Ubuntu server)

Because your Home Assistant (HA) is behind that second NAT, it's in a "private room" and can't hear the "shouts" of smart devices in your main house.

**What is Port Forwarding?**
If NAT is a receptionist who handles outgoing mail, Port Forwarding is a specific instruction for incoming mail.

You told your Ubuntu server: "If anyone knocks on Port 8123, send them straight to the VM's room." This is why you can open the HA dashboard from your laptop, but it doesn't help with Matter or HomeKit because those protocols don't just "knock" on one port—they "shout" to everyone at once.

**Avahi Trick Worked**
The Avahi Reflector Fix: The avahi-daemon with the reflector enabled acts like a repeater.

It sits on your Ubuntu host (which has "one foot" in the Wi-Fi and "one foot" in the VM network).

When it hears a "shout" from your Aqara M100 on the Wi-Fi, it instantly repeats that shout inside the VM's network.

Home Assistant hears the repeated shout, realizes the M100 is there, and responds.

**What if I had Ethernet instead of Wi-Fi?**
If you had Ethernet, everything would become much simpler, more stable, and more "professional."

With Ethernet, you could move away from the "NAT + Port Forwarding + Avahi" workaround and switch to Bridged Networking.

#### inside HA in your browser or mobile app:

- In your browser, go to `http://<HOST-IP>:8123`, for example `http://192.168.1.86:8123`.
- Create an account.
- In the addon store, add this repository: https://github.com/homeassistant-apps/repository

### 2. Accessing HAOS from WAN — Cloudflare Tunnel Setup
- Create a Domain or your domain is already managed by **Cloudflare**
- Follow this video: https://youtu.be/JGAKzzOmvxg
- On you phone, when you add home assistant, add both local and external URL, so you can connect when you are outside

**Add Cloudflare Access (Zero Trust) ⭐⭐⭐**

This is the single biggest security upgrade. Before showing your Home Assistant app in your browser or mobile, it will force the user to first login via an email or something.
If the User can't log in, he won't be able to see the app.

You’re on the Cloudflare Zero Trust -> Access Application screen:
- You are protecting for example `ha.yourdomain.com`


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

- Visiting `ha.yourdomain.com` should show Cloudflare Access login. If it doesn't force refresh the page.
- Only after login -> Home Assistant loads

#### Activate MFA
- In profile -> security, activate MFA

You should now have:

- ✅ Cloudflare Tunnel (no ports open)
- ✅ Cloudflare Access login in front of HA
- ✅ Email or Google login
- ✅ MFA
- ✅ 24h session

---

### Home Assistant Configuration

- User settings: language, date format, number format, etc.


#### Matter devices
- Since I usee a VM inside ubuntu-server and this server is connected via Wifi, and I can't use a bridge, I needed to activate avahi-daemon. Check in this [section](#discovering-devices)
- You need a matter controller to add matter devices like the Aqara M100. Aqara M100 needs to be added to the Aqara app, updated to the latest framework beefore adding it with Matter to HA.
- Use the Home Assistant mobile app to add the Aqara M100 to HA via Matter, and also all the other accessories.
- Some accessories need their app to work properly or to display more functionalities.
