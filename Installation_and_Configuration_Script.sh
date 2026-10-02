# (c) 2026 Pilz GmbH & Co. KG
# License CC0-1.0txt 

#!/usr/bin/env bash
set -euo pipefail
set -x

#############################################
# IndustrialPI 4 + PSENrd3.1 Setup Script
# Based on Pilz README – Debian 12 (bookworm)
#############################################

#########################
# USER CONFIGURATION
#########################

# --- System ---
# your Timezone for example:
TIMEZONE="Europe/Berlin"

# --- Firewall ---
# Ports list. two ports are in the list in the cockpit under firwalld, automatically.
#SSH_PORT=22
#COCKPIT_PORT=41443
MQTT_TLS_PORT="8883/tcp"
NTP_PORT="123/udp"
DNSMASQ_PORT="67/udp"
RDP_PORT="3389/tcp"

# --- MQTT / Mosquitto ---
# Please enter your correct path of your certificate here. For example:
MOSQUITTO_CERT_DIR="/etc/mosquitto/certs"

MOSQUITTO_USER_SENSOR="PSENrd3_sensor"
MOSQUITTO_USER_ADMIN="PSENrd3_admin"
MOSQUITTO_USER_CONSUMER="PSENrd3_consumer"

# Please set your passwords
MOSQUITTO_PASSWD_SENSOR="00000"
MOSQUITTO_PASSWD_ADMIN="00000"
MOSQUITTO_PASSWD_CONSUMER="00000"

MOSQUITTO_PASSFILE="/etc/mosquitto/passwd"
MOSQUITTO_ACLFILE="/etc/mosquitto/aclfile"

# --- WiFi / Access Point ---
# Important password with special characters for WPA2.
WLAN_INTERFACE="wlan0"
WIFI_SSID="AP-name"
WIFI_PASSPHRASE="your_password"

# Please enter your desired IP address and the network configuration for your environment here. For example:
AP_IP_ADDRESS="192.168.2.102"
AP_NETMASK="255.255.255.0"
AP_NETWORK="192.168.2.0"
AP_BROADCAST="192.168.2.255"

DHCP_RANGE_START="192.168.2.50"
DHCP_RANGE_END="192.168.2.150"
DHCP_LEASE_TIME="12h"


# --- Certificate ---
# Enter your location. For example:
COUNTRY="DE"
STATE="Baden-Württemberg"
CITY="Stuttgart"
ORG="Your_company GmbH & Co.KG"
OU="Your_department"
CN="${AP_IP_ADDRESS}"
EMAIL="testemail@your_company.com"
#########################
# HELPER FUNCTIONS
#########################

log() {
  echo -e "\n\033[1;32m[INFO]\033[0m $1"
}

#########################
# SYSTEM UPDATE
#########################

log "Updating system packages"
sudo apt-get update -y
sudo apt-get upgrade -y
# Important it is not seperate Firwall necessary
echo ">>> Installing required packages"
sudo apt-get install -y \
  mosquitto mosquitto-clients \
  openssl \
  ntpsec \
  dnsmasq \
  hostapd \
  python3-tk \
  python3-matplotlib \
  xorg \
  openbox
#########################
# FIREWALL 
#########################

log "Configuring Firewall (firewalld)"

# Make sure the firewall is working
sudo systemctl enable firewalld
sudo systemctl start firewalld

# add Ports 
sudo firewall-cmd --permanent --add-port="${MQTT_TLS_PORT}"
sudo firewall-cmd --permanent --add-port="${NTP_PORT}"
sudo firewall-cmd --permanent --add-port="${DNSMASQ_PORT}"
sudo firewall-cmd --permanent --add-port="${RDP_PORT}"

#Apply changes
sudo firewall-cmd --reload

#########################
# MOSQUITTO MQTT
#########################

log "Installing Mosquitto broker"

log "Creating certificate directory"
sudo mkdir -p "${MOSQUITTO_CERT_DIR}"
cd "${MOSQUITTO_CERT_DIR}"

# Optional: self-signed certificates
log "Creating self-signed TLS certificates (optional)"
openssl genrsa -out server.key 2048

openssl req -new \
-key server.key \
-out server.csr \
-subj "/C=$COUNTRY/ST=$STATE/L=$CITY/O=$ORG/OU=$OU/CN=$CN/emailAddress=$EMAIL"

openssl x509 -req \
-days 365 \
-in server.csr \
-signkey server.key \
-out server.crt

sudo chown -R mosquitto:mosquitto "${MOSQUITTO_CERT_DIR}"

#########################
# MOSQUITTO USERS
#########################

log "Creating Mosquitto users (interactive password entry)"
sudo mosquitto_passwd -c -b "${MOSQUITTO_PASSFILE}" "${MOSQUITTO_USER_SENSOR}" "${MOSQUITTO_PASSWD_SENSOR}"
sudo mosquitto_passwd -b "${MOSQUITTO_PASSFILE}" "${MOSQUITTO_USER_ADMIN}" "${MOSQUITTO_PASSWD_ADMIN}"
sudo mosquitto_passwd -b "${MOSQUITTO_PASSFILE}" "${MOSQUITTO_USER_CONSUMER}" "${MOSQUITTO_PASSWD_CONSUMER}"

#########################
# MOSQUITTO ACL
#########################

log "Creating Mosquitto ACL file"
sudo tee "${MOSQUITTO_ACLFILE}" > /dev/null <<EOF
# ${MOSQUITTO_USER_SENSOR}
user PSENrd3_sensor
topic read /PSENrd3/+/commands
topic read /PSENrd3/+/handoff
topic read /PSENrd3/+/config
topic read /PSENrd3/+/details
topic read /PSENrd3/+/positionData
topic write /PSENrd3/+/details
topic write /PSENrd3/+/positionData
topic write /PSENrd3/+/handoff

# ${MOSQUITTO_USER_ADMIN}
user PSENrd3_admin
topic read /PSENrd3/+/commands
topic read /PSENrd3/+/config
topic read /PSENrd3/+/details
topic read /PSENrd3/+/positionData
topic write /PSENrd3/+/commands
topic write /PSENrd3/+/config

# ${MOSQUITTO_USER_CONSUMER}
user PSENrd3_consumer
topic read /PSENrd3/+/details
topic read /PSENrd3/+/positionData
EOF

#########################
# MOSQUITTO CONFIG
#########################

# Security Note:
# This default configuration allows cennections without a username and password.
# To enable authentication:
# 1. Set 'allow_anonymous' to 'false'
# 2. Remove the '#' before 'password_file'
# 3. Optionally, remove the '#' before 'acl_file' to define

# Info: Check the storage location of your certificate; it must match the “USER CONFIGURATION” entry under “MQTT Mosquitto.”

log "Configuring Mosquitto broker"
sudo tee -a /etc/mosquitto/mosquitto.conf > /dev/null <<EOF
listener 8883
certfile /etc/mosquitto/certs/server.crt
keyfile /etc/mosquitto/certs/server.key
require_certificate false
#use_identity_as_username false
allow_anonymous true
#password_file ${MOSQUITTO_PASSFILE}
#acl_file ${MOSQUITTO_ACLFILE}
EOF

sudo systemctl enable mosquitto
sudo systemctl restart mosquitto

#########################
# NTP / TIME
#########################

log "Installing and configuring NTP"

sudo tee /etc/ntpsec/ntp.conf > /dev/null <<EOF
server 127.127.1.0
fudge 127.127.1.0 stratum 10
restrict 127.0.0.1
restrict ::1
EOF

sudo timedatectl set-timezone "${TIMEZONE}"
sudo systemctl enable ntpsec
sudo systemctl restart ntpsec

#########################
# DNSMASQ (DHCP)
#########################

log "Installing and configuring dnsmasq"
sudo apt-get install -y dnsmasq

#Set here your dhcp-range and omit the IP address you use for your access point.

sudo tee /etc/dnsmasq.conf > /dev/null <<EOF
interface=wlan0
dhcp-range=192.168.2.2,192.168.2.101,12h
dhcp-range=192.168.2.103,192.168.2.254,12
EOF

sudo systemctl enable dnsmasq
sudo systemctl restart dnsmasq

#########################
# HOSTAPD (WiFi AP)
#########################

#Set your AP-name 
#Please use for the wpa_passphrase the variable.

sudo tee /etc/hostapd/hostapd.conf > /dev/null <<EOF
interface=wlan0
driver=nl80211
ssid=AP-name
hw_mode=g
channel=6
wmm_enabled=1
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase="${WIFI_PASSPHRASE}"
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
ap_max_inactivity=5
disassoc_low_ack=1
EOF

log "Unmasking hostapd"
sudo systemctl unmask hostapd

log "Enabling hostapd"
sudo systemctl enable hostapd

#########################
# WLAN NETWORK CONFIG
#########################

log "Configuring WLAN static IP"
sudo tee /etc/network/interfaces.d/wlan0 > /dev/null <<EOF
auto wlan0
iface wlan0 inet static
 address 192.168.2.102
 netmask 255.255.255.0
 network 192.168.2.0
 broadcast 192.168.2.255

EOF

#########################
# NETWORK MANAGER OVERRIDE
#########################

log "Disabling NetworkManager control for wlan0"
sudo tee /etc/NetworkManager/conf.d/99-unmanaged-devices.conf > /dev/null <<EOF
[keyfile]
unmanaged-devices=interface-name:wlan0

[device]
wifi.scan-rand-mac-address=no
EOF

sudo tee /home/pi/.xinitrc > /dev/null <<EOF
exec openbox-session
EOF

#########################
# XRDP
#########################

log "Installing XRDP"
sudo apt-get install -y xrdp xorgxrdp
sudo systemctl enable xrdp

log "Setup complete - reboot recommended"
echo "Please reboot the system: sudo reboot"

#########################
# START SERVICEs
#########################

sudo systemctl restart NetworkManager
sudo systemctl restart hostapd