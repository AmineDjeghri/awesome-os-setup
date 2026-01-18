
# laptop as a server
### Ubuntu Server 24.04
- Set up an Ubuntu Server on a laptop (doesn't have Ethernet, only Wi-Fi). Configure the network (wlo1) and wait for the IP address to be assigned.
- Wait for mirror to be configured.
- Assign a partition (format ext4 and mount it to /)
- Installed openssh-server and managed it remotely using SSH from another machine so I can copy-paste commands from the documentation.
- run apt update and apt upgrade
- run ip addr to check the IP address
- run ping google.com to check the connection
- connect remotely using SSH
- I customized the shell environment by installing Zsh and tools from the [Awesome OS](https://github.com/AmineDjeghri/awesome-os-setup)  to improve
usability and productivity.

# Home Assistant OS
- I verified that virtualization was supported on the system, checked Secure Boot status
to ensure compatibility, and installed and validated KVM with libvirt to enable virtual machine support. This prepared
the server for running virtualized workloads such as Home Assistant OS in a headless environment.



- lid closed :



# Wifi limitation and solution:

In standard Ethernet setups, we would simply create a "Bridge" (br0) so your Home Assistant (HA) VM acts like a physical
device on your network, getting its own IP from your router. However, the 802.11 (Wi-Fi) standard strictly forbids
bridging (it rejects packets with MAC addresses that don't match the Wi-Fi card's own hardware address).

To access Home Assistant from your phone without SSH tunnels, you have two main solutions.

Enable IP Forwarding
Linux defaults to blocking traffic passing through it (router mode). We need to enable it.
on the host machine:
Enable it immediately:

sudo sysctl -w net.ipv4.ip_forward=1
Make it permanent (so it survives a reboot)
echo "net.ipv4.ip_forward = 1" | sudo tee -a /etc/sysctl.conf

We need to tell Ubuntu: "If anyone knocks on my Wi-Fi IP on port 8123, send them to the internal VM 192.168.122.36."

Run these three commands exactly:

# 1. Forward incoming TCP traffic on wlo1 port 8123 -> VM IP

sudo iptables -t nat -A PREROUTING -i wlo1 -p tcp --dport 8123 -j DNAT --to-destination 192.168.122.36:8123

# 2. Allow the forwarded traffic to pass through the firewall

sudo iptables -I FORWARD -d 192.168.122.36 -p tcp --dport 8123 -j ACCEPT

# 3. Allow return traffic (VM -> Phone)

sudo iptables -I FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT

Phase 3: Check Firewalls (UFW)
Since you are on Ubuntu Server, ufw (Uncomplicated Firewall) might be active. If it is, it will block port 8123 before
IPTables even sees it.

Run this to check status:

Bash
sudo ufw status
