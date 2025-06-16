# PSENrd 3.1 live and IndustrialPI 4

<div style="display: flex; flex-direction: column; align-items: center;">
    <a href="https://www.pilz.com" rel="nofollow">
        <img src="/img/pilz-logo.png" alt="Pilz Logo">
    </a><br/>
</div>

## Exclusion of Liability 

We have taken great care in compiling our documentation. It contains information about our company and our products. All statements are made in accordance with the current status of technology and to the best of our knowledge and belief.
While every effort has been made to ensure the information provided is accurate, we cannot accept liability for the accuracy and entirety of the information provided, except in the case of gross negligence. In particular, all information on applicable standards, safety-related classifications and time characteristics should be viewed as provisional. In particular it should be noted that statements do not have the legal quality of assurances or assured properties.
We are grateful for any feedback on the contents.<br/>
February 2025<br/>
All rights to this publication are reserved by Pilz GmbH & Co. KG.
We reserve the right to amend specifications without prior notice. Copies may be made for the user’s internal purposes.
The names of products, goods and technologies used in this manual are trademarks of the respective companies. Please note the current information about the products, their licenses and registered trademarks in the documents listed in [Useful documentation](#1-useful-documentation).<br/>

## Industrial Security

To secure plants, systems, machines and networks against cyberthreats it is necessary to implement (and continuously maintain) an overall [Industrial Security concept](https://www.pilz.com/en-INT/products/industrial-security) that is state of the art.
Perform a risk assessment in accordance with VDI/VDE 2182 or IEC 62443-3-2 and plan the security measures with care. If necessary, seek advice from<br/>
[Pilz Customer Support](https://www.pilz.com/en-INT/support/technical-support).<br/>

## Definition of Symbols

Information that is particularly important is identified as follows:<br/>

>[!Caution]
>Advises about risks or negative outcomes of certain actions.

>[!Important]
>Key information users need to know to achieve their goal.

>[!Tip]
>Helpful advice for doing things better or more easily.

>[!Note]
>Useful information that users should know, even when skimming content.

## Contents and Setup steps

1.  [Useful documentation](#1-useful-documentation)<br/>
1.1 [Documentation form Pilz GmbH & Co. KG](#11-documentation-from-pilz-gmbh--co-kg)<br/>
2.  [Hardware and software used](#2-hardware-and-software-used)<br/>
2.1 [Pilz products](#21-pilz-products)<br/>
2.2 [Third-party products](#22-third-party-products)<br/>
2.3 [Structure of the application (schematic)](#23-structure-of-the-application-schematic)<br/>
3.  [Preface](#3-preface)<br/>
4.  [Application description](#4-application-description)<br/>
5.  [First steps to start IndustrialPI 4](#5-first-steps-to-start-industrialpi-4)<br/>
5.1 [Password](#51-password)<br/>
5.2 [Instructions for changing the keyboard settings](#52-instructions-for-changing-the-keyboard-settings)<br/>
5.3 [Update System packages](#53-update-system-packages)<br/>
5.4 [Install Firewall](#54-install-firewall)<br/>
6.  [Install Mosquitto and Mosquitto-Clients](#6-install-mosquitto-and-mosquitto-clients)<br/>
6.1 [Create certificates (optional)](#61-create-certificates-optional)<br/>
6.2 [Create users and passwords for accessing to the broker ](#62-create-users-and-passwords-for-accessing-to-the-broker)<br/>
6.3 [Create an ACL (Access control list)](#63-create-an-acl-access-control-list)<br/>
6.4 [Configurate Mosquitto Broker](#64-configurate-mosquitto-broker)<br/>
6.5 [Start mosquitto service](#65-start-mosquitto-service)<br/>
7.  [Setup and Configuration NTP Server](#7-setup-and-configuration-ntp-server)<br/>
8.  [WiFi Configuration](#8-wifi-configuration)<br/>
8.1 [Install dnsmasq](#81-install-dnsmasq)<br/>
8.2 [Set up WiFi connection](#82-set-up-wifi-conncetion)<br/>
8.3 [Set up Cockpit-IndustrialPI](#83-set-up-cockpit-industrialpi)<br/>
9.  [Testing of Data exchange](#9-testing-of-data-exchange)<br/>
10. [Integration of the supplied python program example](#10-integration-of-the-supplied-python-program-example)<br/>
10.1 [Work with USB-Stick](#101-work-with-usb-stick)<br/>
10.2 [Install additional Python package and graphical packages for the Version V1](#102-install-additional-python-package-and-graphical-packages-for-the-version-v1)<br/>
10.3 [Start the GUI in the graphical interface](#103-start-the-gui-in-the-graphical-interface)<br/>
11. [Work with Remotedesktop-Connection (RDP)](#11-work-with-remotedesktop-connection-rdp)<br/>
11.1 [Create a new network IP-Address](#111-create-a-new-network-ip-address)<br/>
11.2 [Install xrdp and xorg xrdp](#112-install-xrdp-and-xorg-xrdp)<br/>
11.3 [Using the remote desktop connection](#113-using-the-remotedesktop-connection)<br/>
12. [License Inforamtion](#11-license-inforamtion)<br/>

<!--1.2 [Documentation form other sources](#12-documentation-form-other-sources)<br/>-->
<!--10.4[Work with GitHub directly](#104-work-with-github-directly)<br/>-->
<!--10.3[Install additional Python packages for the Version V4](#102-install-additional-python-packages-for-the-version-v4)<br/>-->
## 1. Useful documentation

Reading the documentations listed below is necessary for understanding this Application.<br/>
The availability of the software used, and its safe handling are also presupposed for the user.

### 1.1 Documentation from Pilz GmbH & Co. KG

|Nr.| Discription | Part number/ Download|
|---| ------------| ---------------------|
| 1 | Pilz international website, download section | [www.pilz.com >EN Support >Downloads](https://www.pilz.com/en-INT/support/downloads)<br/> [www.pilz.com > DE Support > Downloads](https://www.pilz.com/de-INT/support/downloads)<br/> |
| 2 | Operating manual of PSEN rd3.1 live| The documentation is currently still being prepared and will be made available at a later date. We will inform you as soon as it is available. |                                                
| 3 | Operating manual of IndutrialPI 4 |[www.pilz.com >EN Operat.Man. 1006970-01](https://www.pilz.com/en-INT/search#currentPage=1&SEARCH=1006970)<br/>[www.pilz.com >DE Bed.anl. 1006970-01](https://www.pilz.com/de-INT/search#currentPage=1&SEARCH=1006970)<br/> |
<!--[www.pilz.com >EN Operat.Man. XXXXX](http://Link_fehlt_noch.com)<br/>[www.pilz.com > DE Bed.anl. 1006933-01](http://Link_fehlt_noch.com)<br>-->
<!--### 1.2 Documentation form other sources of information

|Nr.| Discription | Part number/ Download|
|---| ------------| ---------------------|
| 1 |             |                      |-->

## 2. Hardware and software used

### 2.1 Pilz products

|Nr.| Discription | Order number| Version| Quantity|
|---| ------------|-------------| -------| --------|
| 1 | IndustrialPI| A1000003    |   4    |    1    |
| 2 | PSENrd      | 6B000017    |  3.1   |    1    |
| 3 | PSEN op cable axial M12 5-pole, 3m| 630310 | - | 1 |

> [!IMPORTANT]
> We only use the IndustrialPI 4 (A1000003) here for the application with WiFi network. Because only the IndustrialPI 4 has a WiFi antenna connection.<br/> 

### 2.2 Third-party products

|Nr.| Discription | Order number| Version| Quantity|
|---| ------------|-------------| -------| --------|
| 1 |   Monitor   |      -      |    -   |    1    |
| 2 |   Keyboard  |      -      |    -   |    1    |
| 3 |   Mouse     |      -      |    -   |    1    |
| 4 | Micro-HDMI adapter |  -   |    -   |    1    |
| 5 | HDMI cable for the Monitor| -  | - |    1    |
| 6 | Antenna (optional)|   -   |    -   |    1    |
| 7 | Ethernet cable |      -   |    -   |    1    |

### 2.3 Structure of the application (schematic)

<div style="display: flex; flex-direction: column; align-items: center;">
        <img src="/img/IndustrialPI_4_and_PSENrd_3_1.png" alt="Structure of the application (schematic)" width="800">
    </a><br/>
</div>

## 3. Preface

This application basically describes the commissioning process of a PSENrd 3.1 with an IndustrialPI 4. Both devices communicate with each other using MQTT.
Data is sent from the PSENrd 3.1 to the internal access point of the IndustrialPI 4. This data is sent to the Python program provided and processed there.<br/>
The basic procedure for successful basic configuration is shown here step-by-step, mostly using command lines. The operating system used is Debain GNU/Linux 12.<br/> 

> [!IMPORTANT]
> This document only describes the procedure for using the IndustrialPI 4 (A1000003) and PSENrd 3.1 (6B000017) and does not constitute technical documentation on the general use of the operating system Linux and the program language Python. The operating system and the programming language are basic requirements for this application.

## 4. Application description

The example here shows people counting to determine whether one or more people are present in a monitored area.<br/>

There are several requirements for the realization of this application:<br/>

+ Data transmission takes place via MQTT.<br/>
+ Evaluation of the sensor data in the IndustrialPI 4 in real time.<br/>
+ Recording of personal data in a specific area.<br/>
+ All persons detected by the PSENrd 3.1 sensor are recorded and processed by the IndustrialPI 4.<br/>

Non-functional requirements:<br/>

+ Stability and reliability of the system.<br/>
+ Simple setup and handling of the operating system on the IndustrialPI 4.<br/>

The structure of the system and components is based on:<br/>
[2.3 Structure of the application (schematic)](#23-structure-of-the-application-schematic)<br/>

## 5. First Steps to start IndustrialPI 4 

### 5.1 Password 

> [!Important]
> Depending on how this network access is secured, strangers may also be able to log into the device and gain access to data and all functions. Therefore, always choose a
<ins>"strong"</ins> password and work in "headless" mode, i.e. only access the network from devices that you know. Unknown devices could, for example, log keystrokes and thus spy on your login data. 

+ First of all, connect the IndustrialPI 4 to a monitor. A micro HDMI is available on the IndustrialPI 4.<br/>
+ Connect a keyboard via the IndustrialPI 4 USB ports.<br/>
+ Start the IndustrialPI 4 with the 24VDC supply. The IndustrialPI 4 then boots up.<br/>
+ Enter the password shown on the sticker on the side of the IndustrialPI 4.

> [!Important]
> After the first login, change the default password in the command line and in the web application, immediately.
```
sudo raspi-config
```
+ Select system options.<br/>
+ Under system options select S3 password.<br/>
+ You will asked to enter a new password.<br/>
+ Click OK.<br/>
+ choose a <ins>strong<ins> password.<br/>
+ retype the new password.<br/>
+ The password changed successfully.<br/>

> [!Tip]
><ins>Installation after a new Image:</ins><br/>
The first login of the IndustrialPI 4 is:<br/>
Username: pi <br/> Password: raspberry<br/>
Information comes: The device configuration was detected automatically.
Manual configuration is therefore not necessary.<br/>
Press okay.<br/> 
You will now be asked to use the password on the sticker.<br/>

> [!Tip]
> When you enter password, the letters and special characters are not displayed.

> [!Tip]
> Please note that the standard keyboard is set to English (US). This means that the Z and Y keys are reversed, for example on German keyboards. Please note this when entering the password.

> [!Tip]
> The letter l (small L) can easily be confused with the number 1 (one). Make sure you use the correct character.<br/>

### 5.2 Instructions for changing the keyboard settings

Open the RaspberryPI Software Configuration Tool (raspi-config):<br/>

> [!Tip]
> On the English keyboard, the character - (hyphen) corresponds to the character ? (question mark). Make sure you take this into account when entering.
```
sudo raspi-config
```
+ Select localisation options.<br/>
+ Then select L3 Keyboard.<br/>
+ Select the model of your keyboard.<br/>
+ Go to the sub-item other.<br/>
+ Select your language.<br/>
+ Select the default for the keyboard layout as the next step.<br/>
+ Deselect compose key in the last step.<br/>
+ Exit the configuration tool with the esc key.<br/>

> [!Tip]
> Try whether the setting has worked. for example press Y or Z.

### 5.3 Update System packages

> [!Tip]
> + Connect your IndustrialPI 4 to the Internet for the first time via the Ethernet interface.
> + If you connect your IndustrialPI 4 with a WiFi- Hotspot follow the points of [Set up Cockpit-IndustrialPI 4](#83-set-up-cockpit-industrialpi-4).

+ get all updates with the commando:
```
sudo apt-get update
```
```
sudo apt-get upgrade
```
> [!Tip]
> Both commands will ask you to continue. Confirm both commands with Y. Press q when requested for upgrade information.

### 5.4 Install Firewall 

> [!Important]
> The Lite Version Debain GNU/Linux 12 doesn´t have a Firewall preinstalled. You must install the ufw package. You will find a description of this function in the following steps.
+ Install the package:
```
sudo apt-get install ufw
```
>[!Tip]
> Confirm with Y key.

> [!Tip]
> ufw allows you to add rules before you activate the firewall. If you activate ufw without rules, the firewall closes the necessary ports of the application.
 + list of general ports:<br/>
 
 1. Port 22 is for ssh (for example: Putty)
 ```
 sudo ufw allow 22
 ```
 2. Port 41443/tcp for the browser view.
 ```
 sudo ufw allow 41443/tcp
 ```

+ After to activate the first rules, you must to activate ufw:
```
sudo ufw enable
```
+ You can check the status of the ufw, to ensure that it is active without errors:
```
sudo systemctl status ufw
```
+ Check the rules list:
```
sudo ufw status
```
> [!Important]
> In the following discriptions are more several port numbers are mentioned, please make sure to include these port numbers in the rules list.

## 6. Install Mosquitto and Mosquitto-Clients

+ Install Mosquitto and Mosquitto-Clients:
```
sudo apt-get install mosquitto mosquitto-clients
```
<!--+ Please use the installation of Mosquitto and Mosquitto-Clients from the README.md PilzForwarder:<br/>
[Install Mosquitto and Mosquitto-Clients](https://github.com/PilzDE/PilzForwarder?tab=readme-ov-file#32-install-mosquitto-and-mosquitto-clients)<br/>-->

### 6.1 Create certificates (optional)

> [!Tip]
> This step is required only when using self-signed certificates.

+ Install OpenSSL:
```
sudo apt-get install openssl
```
1. Create a folder on your broker/server for example in your home directory in which you save the Certificates:<br/>
```
mkdir certs
```
```
cd certs
```
2. Generate the CA certificate:<br/>
```
openssl req -new -x509 -days 365 -extensions v3_ca -keyout ca.key -out ca.crt
```
> [!Note]
> The argument <ins>-days</ins> sets the valid period of the certificate.

> [!Caution]
> The Common Name (CN) for CA must not be the same as for the broker/server later.

3. Generate the certificate signing request for the broker/server:<br/>
```
openssl genrsa -out server.key 2048
```
```
openssl req -out server.csr -key server.key -new
```
> [!Important]
> The Common Name (CN) for the broker/server should be set as the IP Adreses of broker/server.

4. Sign the broker/server request with the CA certificate:<br/>
```
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 365
```
### 6.2 Create users and passwords for accessing to the broker 
```
mosquitto_passwd -c /etc/mosquitto/passwd PSENrd3_sensor
```
```
mosquitto_passwd -b /etc/mosquitto/passwd PSENrd3_admin <password for that user>
```
```
mosquitto_passwd -b /etc/mosquitto/passwd PSENrd3_consumer <password for that user>
```
> [!Tip]
> We recommend using the suggested usernames.

> [!Important]
> If you use other usernames, please customize the usernames in the step [6.3 Create an ACL list](#63-create-an-acl-access-control-list)

<!--+ Also install the necessary additional conditions that are only required if you want to use self-signed certificates,<br/>
including the creation of certificates and the creation of access control lists:<br/>
[Install OpenSLL and create certificates](https://github.com/PilzDE/PilzForwarder?tab=readme-ov-file#33-install-openssl-optional)<br/>-->

### 6.3 Create an ACL (Access control list)

1. Create an ACL-File:<br/>
```
sudo nano /etc/mosquitto/aclfile
```
2. Write the ACL-Rules in the ACL-File:
```
# PSENrd3_sensor: Read (commands, config, details, positionData); Write (details, positionData, handoff)
user PSENrd3_sensor
topic read /PSENrd3/+/commands
topic read /PSENrd3/+/config
topic read /PSENrd3/+/details
topic read /PSENrd3/+/positionData
topic write /PSENrd3/+/details
topic write /PSENrd3/+/positionData
topic write /PSENrd3/+/handoff

# PSENrd3_admin: Read (commands, config, details, positionData); Write (commands, config)
user PSENrd3_admin
topic read /PSENrd3/+/commands
topic read /PSENrd3/+/config
topic read /PSENrd3/+/details
topic read /PSENrd3/+/positionData
topic write /PSENrd3/+/commands
topic write /PSENrd3/+/config

# PSENrd3_consumer: Read (details, positionData)
user PSENrd3_consumer
topic read /PSENrd3/+/details
topic read /PSENrd3/+/positionData
```
> [!Important]
> If you used another usernames, please customize the usernames in the ACL-File.

### 6.4  Configurate Mosquitto Broker

1. Open the config-file:<br/>
```
sudo nano /etc/mosquitto/mosquitto.conf
```
2. Add or change following lines:<br/>
```
listener 8883

cafile </path/to/certs>/ca.crt
certfile </path/to/certs>/server.crt
keyfile </path/to/certs>/server.key

require_certificate false
use_identity_as_username false
allow_anonymous false

password_file /etc/mosquitto/passwd
acl_file /etc/mosquitto/aclfile
```
> [!Important]
> Make sure that you enter the correct path to the <ins>certs</ins> folder where the certificates can be found.

> [!Tip]
> Remember the previous note in the last topic. Integrate the Port Number 8883 in the rules list of ufw.
 ```
 sudo ufw allow 8883
 ```

### 6.5 Start mosquitto service
```
sudo systemctl start mosquitto
```
```
sudo systemctl enable mosquitto
```
```
sudo systemctl status mosquitto
```
> [!Note]
> If the mosquitto service shows an error on starting then it could be that you should make sure that the certificates have the correct authorizations and are readable for the Mosquitto service. To do that you can try:
```
sudo chown mosquitto:mosquitto </path/to/certs>/ca.crt
```
```
sudo chown mosquitto:mosquitto </path/to/certs>/server.crt
```
```
sudo chown mosquitto:mosquitto </path/to/certs>/server.key
```
```
sudo systemctl restart mosquitto
```

<!--### 6.6 Copy the <ins>ca.crt</ins> Certificate 

Copy the <ins>ca.crt</ins> Certificate created in step 2 of [Create Certificates](#61-create-certificates-optional) to the server and set up the config file:<br/>

1. If not already present, create the folder <ins>certs<ins> in the main folder (this folder)
```
mkdir certs
```
```
cd certs
```
2. Create the folder <ins>broker</ins> within the folder <ins>certs</ins>
```
mkdir broker
```
3. Paste the <ins>ca.crt</ins> file in the folder <ins>broker</ins><br/>

4. If not already present, create the file <ins>config.json</ins> in the folder <ins>broker</ins><br/>
5. Fill the file <ins>config.json</ins>:
```
{
    	"broker_ip": "<IP-Address of your MQTT Broker>",
    	"port": 8883,
    	"ca_cert": "ca.crt"
}
```
> [!Important]
> The value of the key <ins>ca_cert</ins> must be exactly the same as the name of the <ins>ca.crt</ins> certificate!-->

<!--+ The next step describes the configuration of the MQTT-broker, this step is necessary, so follow the instructions:<br/>
[Configurate Mosquitto Broker](https://github.com/PilzDE/PilzForwarder?tab=readme-ov-file#37-configurate-mosquitto-broker)<br/>-->

## 7. Setup and Configuration NTP Server

+ Install NTP:
```
sudo apt-get install ntp
```
> [!Note]
> An additional security package is automatically installed in this Linux system (Debain GNU/Linux 12). The next steps are therefore carried out with an ntpsec command.  

+ Open the NTP config file:
```
sudo nano /etc/ntpsec/ntp.conf
```
+ Add the following configuration to the ntp.config file:
```
server 127.127.1.0
fudge 127.127.1.0 stratum 10
restrict 127.0.0.1
restrict ::1
```
> [!Tip]
> Comment out all other commands.

+ Save the file and restart the ntp:
```
sudo systemctl restart ntp
```
```
sudo systemctl enable ntp
```
+ Control whether your system clock is synchronized:
```
timedatectl status
```
+ If you need the list to find your correct time zone, enter the following command:
```
timedatectl list-timezones
```
+ For example, to set the time zone to Berlin:
```
sudo timedatectl set-timezone Europe/Berlin
```
> [!Tip]
> The local time is now the same time as at your location. “Yes” should be displayed behind the synchronized system clock. The time zone has been changed to Europe/Berlin for this example. 

+ To check the synchronization of the local system:<br/>
```
ntpq -p
```
> [!Note]
> The ntpq -p command displays a list of the NTP servers (Network Time Protocol) with which your local system is synchronized. This list contains important information such as the IP address of the server, the status of the connection and the synchronization quality.<br/>
An asterisk (*) at the beginning of a line means that this NTP server is the main synchronization partner of your system. You can find an example of this in the following table:
 
 |remote         |refid       |st| t| when| poll| reach|   delay|   offset|  jitter|
 |---------------|------------|--|--|------|---- |-----|--------|---------|--------|
 |*ntp.example.LOCAL| .LOCL.  |10| l |  18 |  64 | 377 |   0.000|   0.000 |   0.000|

>[!Tip]
>This synchronization can take a long time after a restart of the IndustrialPI 4 and the PSENrd 3.1. (It can take up to 6 minutes).

## 8. WiFi configuration 

### 8.1 Install dnsmasq

+ To enable the automatic connection of WiFi devices, we need the dnsmasq package, which acts as a DHCP server.

Install package:
```
sudo apt install dnsmasq
```
>[!Tip]
> Confirm with Y key.

+ Open the configuration file: 
```
sudo nano /etc/dnsmasq.conf
```
+ Add the following example configuration in this file: (scroll all the way down with the down button)
```
interface=wlan0
dhcp-range=192.168.0.50,192.168.0.150,12h
```
+ Save the config.file and exit to start dnsmasq:
```
sudo systemctl restart dnsmasq
```
```
sudo systemctl enable dnsmasq
```
+ Control the dnsmasq.service via status:
```
sudo systemctl status dnsmasq
```
+ The status shows you that the dnsmasq service is active.

### 8.2 Set up WiFi Conncetion 
<!--```
sudo nmtui
```
+ Go to the menu item “edit a connection”.
+ Navigate to the "Add"-button.
+ Select: Wi-Fi.
+ Assign a profile name.
+ Write under device: wlan0.
+ Next up assign the SSID. You can use the same name as in profile name.
+ Select mode: Access Point.
+ Select channel: Automatic.
+ Select security: WPA & WPA2 Personal.
+ Assign your password.
+ Select "Manual" for the IPv4 configuration.
+ Assign the address for example 192.168.0.102/24.
+ At the gateway, assign 192.168.0.1, for example.
+ Then accept everything with OK.
+ Restart your System.
```
sudo reboot
```-->

>[!Important]
>To use a secure WLAN network, please install the hostapd package. This is required to use the WPA2 security protocol. The procedure is explained in detail in the following section.

+ Install packages:
```
sudo apt update
```
```
sudo get upgrade
```
```
sudo apt install hostapd
```
[Text for hostapd here]
+ Create a configuration file:
```
sudo nano /etc/hostapd/hostapd.conf
```
+ Please write the following settings in this file:
```
interface=wlan0
driver=nl80211
ssid=YourNetworkName
hw_mode=g
channel=6
wmm_enabled=1
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=YourPassword
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
```
>[!Note]
>In your application, make sure that the settings for commissioning are sufficiently secure (security).<br/>

+ Save the file an exit the file.

+ Create a new file for the Configuration of wlan0:
```
sudo nano /etc/network/interfaces.d/wlan0
```
+ Please write the following settings in this new file:
```
auto wlan0
iface wlan0 inet static
    address 192.168.0.1
    netmask 255.255.255.0
    network 192.168.0.0
    broadcast 192.168.0.255
    hostapd /etc/hostapd/hostapd.conf
```    
+ Save the file an exit the file.<br/>

The next step is to create a new file in the NetworkManager folder. Please follow the instructions.

>[!Note]
>The 99-unmanaged-devices.conf file is used to configure certain network devices so that they are ignored by NetworkManager. This setting forces the use of the WPA2 security protocol.

+ Create the following configuration file:
```
sudo nano /etc/NetworkManager/conf.d/99-unmanaged-devices.conf
```
+ Please write the following settings in this file:
```
[keyfile] 
unmanaged-devices=interface-name:wlan0

[device]
wifi.scan-rand-mac-address=no
```
+ Save the file an exit the file.

+ Please restart the NetworkManager:
```
sudo systemctl restart NetworkManager.service
```
+ Control the status of the NetworkManager to see if it is activated.
```
sudo systemctl status NetworkManager.service
```
[Text here]
>[!Note]
>The WPA2 security protocol is now guatanteed to be used.

### 8.3 Set up Cockpit-IndustrialPI 4
+ To connect a notebook to your IndustrialPI 4, use an Ethernet cable to connect the notebook to one of the Industrial PI's Ethernet ports. Open your browser and enter<br/> 
http://industrialpiXXXXXX.local in your search bar. For XXXXXX, enter the six-digit serial number of the IndustrialPI 4. You will find this number on the front of the IndustrialPI 4.
+ Log in with the data provided on the sticker on the side of the IndutrialPI 4.
+ The dashboard of your IndustrialPI 4 will open and is called Cockpit.
+ Under Tools you will find the item IndustrialPI Configuration. Click on it.
+ Now you will see various setting options.
+ To be on the safe side, please deactivate the bluetooth cennection.
+ Select the external antenna (SMA) under select antenna.
+ then restart the IndustrialPI 4:
```
sudo reboot
```
>[!Tip]
>When you connect the WiFi the first time, please control in your Network Mangager "sudo nmtui" whether the IndustrialPI 4 find your desired WiFi. This Tip belongs to the subitem [5.3 Update System packages](#53-update-system-packages).

>[!Tip]
>Use a WiFi endpoint device, e.g. a smartphone, and check whether you can see the new WiFi connection in your WiFi settings. Click on it and connect and see if you are then in the WiFi. You can see this by the checkmark and the WiFi icon.

>[!Tip]
>The next test is to try out the browser cockpit of your IndustrialPI 4. First connect your mobile phone or notebook to the existing Wifi connection as described in the previous tip. Then open any browser and enter the same hostname as in the settings in the previous chapter. If you are asked for a user name and password, everything is correct.

## 9. Testing of Data exchange 

+ You can start by checking whether you can connect the IndustrialPI 4 system to the PSENrd 3.1. First restart the IndustrialPI 4:
```
sudo reboot
```
>[!Tip]
>General tip, restarting the system is very important for many new installations. Restart the IndustrialPI 4 from time to time.

>[!Tip]
>Again, remember the synchronization time of the NTP service.

+ The tail -f command is used to display the last lines of a file in real time. If you use it with Mosquitto, you can monitor the log file of the Mosquitto broker to see current activities and messages.
```
sudo tail -f /var/log/mosquitto/mosquitto.log
```
+ You can find for example the information in the table:

New client connection from IP-Address:Portnumber as ID (p2, c1, k120).

+ The next step is to press Ctrl + C to exit the currently running command or process and return to the command line to enter new commands.
+ We need the first test whether the sensor sends data to the Industrial PI 4.
```
mosquitto_sub -p 8883 -h <IP-Address> --cafile <Path to the CA file> -t '/PSENrd3/<ID of your Sensor>/positionData'-u <username> -P <password> 
```
>[!Tip]
>You will find the 12-digit ID on the back of the sensor (The Mac-Adress without colon).

+  Position data should then gradually appear on your shell.

## 10. Integration of the supplied python program example

>[!Note]
>We greate a graphical python program for this application. This graphical Python program displays recognized people and counts them. The program can be found in the table at the top of this repository.

### 10.1 Work with USB-stick

>[!Important]
>Make sure that the USB stick comes from a trustworthy source and has not been used before on potentially compromised systems. The stick should be checked or reformatted before use to ensure maximum security.

>[!Note]
>The follow description shows how to copy the Python program from the GitHub repository (https://github.com/PilzDE/PSENrd3.1_live_and_IndustrialPI_4) of your workstation notebook to any USB stick and then integrate it into your IndustrialPI 4 system. Please copy the raw file of the Python program from the GitHub repository Samples and insert it into a suitable tool. Save the file and copy the program to your USB stick.

+ Python is already available on this oparting system. You can view the current Python version with the following command:
```
python3 --version
```
+ Create a new folder for your python-program for example in your home directory:
```
mkdir ~/my_python_program
```
+ Insert your USB stick into one of the two USB ports. Check the name of the USB with the command:
```
lsblk
```
>[!Tip]
>In the last column of this table you will see the name of the mount point for your USB device, e.g. /media/usb.

+ Mount the example USB into your system:
```
sudo mount /dev/sda1 /media/usb
```
+ Copy the supplied program in this new folder for example from a stick:
```
sudo cp /media/usb/PSENrd3_DetectPeople_GUI_V1.py /home/pi/my_python_program
```
+ After you have copied your program you could umount the USB stick:
```
sudo umount /dev/sda1
```
The next step is to change the correct mac-address and path.<br/>
+ Open the python program:
```
sudo nano /home/pi/my_python_program/PSENrd3_DetectPeople_GUI_V1.py
```
+ Change the mac-address where the "XXXXXXXXXXXX" are located.

>[!Tip]
>You will find the 12-digit Mac address on the back of the sensor.

+ Change the path of your certificates markes with "/XXX/XXX/XXX/XXX" as well.

+ Save the file and exit.

### 10.2 Install additional Python package and graphical packages for the Version V1 
For the program Version 1 you need a Python package for installation for execution.<br/>
+ Install tkinter:
```
sudo apt-get install python3-tk
```
>[!Tip]
>Confirm with Y.

Several steps are required for the graphical interface.

+ Open the file bash.bashrc:
```
sudo nano /etc/bash.bashrc
```
+ Write the line "export DISPLAY=:0.0" at the bottom after the content of this file.<br/>
```
export DISPLAY=:0.0
```
+ Save the file and exit.
+ Restart this file:
```
source /etc/bash.bashrc
```
+ Control whether the $DISPLAY varibale is set correctly:
```
echo $DISPLAY
```
+ This Commando should return :0.0.

+ Next step is to install the so called x Sever for the graphical window of your Linux system.
```
sudo apt update
```
```
sudo apt upgrade
```
```
sudo apt install xorg
```
>[!Tip]
>Requests that are answered with y or n must continue with y. Press q if when asked.

### 10.3 Start the GUI in the graphical interface
+ Start the graphical interface with:
```
startx
```
+ There will open a new window with a new commando line. Now you can use a mouse in this shell. Click behind the Commoando line.
+ Change at first your keyboard language again. For example Germany (de):
```
setxkbmap de
```
>[!Tip]
>Try whether the setting has worked. For example press Y or Z.

Enlarge the display:<br/>
+ Held down with the ctrl key and right mouse button, a menu with unicode fonts will appear.
+ Navigate with the mouse to your desired font size.<br/>(Hold down the ctrl key and the right mouse button the whole time.)

+ Change into the directory: 
```
cd /home/pi/my_python_program
```
+ Execute the python program:
```
python3 PSENrd3_DetectPeople_GUI_V1.py
```
+ You should now see a yellow GUI with a gray range area showing whether your sensor is connected. You have a counter in the yellow area.

## 11. Work with remote desktop connection (RDP)

In this discription, you will use the system via remotedesktop at your workstation with an Ethernet connection. The Requirement for this is that you need a terminal program for example PuTTY. The Remotdesktop- Connection is available on a Windows PC by default.<br/>
>[!Important]
>Observe the specifications of commissioning (security) for your application, in particular the removal of the separation of networks with defferent IP addresses. 

## 11.1 Create a new Network IP-Address

First of all, you need a new Network IP-Address for the Remotedesktop Connection. For example change the third number in your IP-Address, as before. The reason in this case is, if you have the IP-Address in the same network the WLAN connection will be interrupt between PSENrd 3.1 and IndustrialPI 4.<br/> 

+ Please use the Network Manager:
```
sudo nmtui
```
+ Select the option edit a connection.
+ In this case select under Ethernet the first wired connection.
+ Enter the automatic behind the IPv4 configuration and select manual.
+ One line will show up for the new IP-Address.
+ Please enter your Ethernet IP-Address in this line. For example 192.168.1.109/24.
+ Then you can click OK in the right corner.
+ Reboot the system:
```
sudo reboot
```

### 11.2 Install xrdp and xorg xrdp

+ Install the packages xrdp and xorg xrdp:
```
sudo apt install xrdp xorgxrdp
```
+ Reboot the system:
```
sudo reboot
```
>[!Tip]
>Integrate the Port Number 3389/tcp in the rules list of ufw. The Port number is the typical standard Port number of the RDP (Remote Desktop Protokoll) from Windows.
 ```
 sudo ufw allow 3389/tcp
 ```

### 11.3 Using the Remotedesktop-Connection

Connect the IndustrialPI 4 to your laptop via Ethernet cable. Then search for the Remote Desktop Connection in your saerch bar in your operating system.<br/>
+ A small Window with an input line opens. 
+ Please enter your Ethernet IP-Address there.
+ An identity question is displayed.
>[!Important]
>In your application, make sure that the settings for commissioning are sufficiently secure (security).
+ Please click Yes.
+ After that a login query will open.
+ Please enter your Username and your password of your IndustrialPI 4.
+ Now the graphical desktop opens directly.
+ If you want to use the python program you need a different display number.
+ You can find this number in a file it names "xrdp-sesman.log". 
```
sudo nano /var/log/xrdp-sesman.log
```
+ In the fourth line you will find the IP address of your PC. At the bottom of this file you will find the display number, in this case the number 10 is available.
+ Exit this file with ctrl + X.
+ Change the DISPLAY number:
```
export DISPLAY=:10.0
```
+ Control the change with:
```
echo $DISPLAY
```
Now you can start the python program on the remote desktop connection.<br/>

## 12. License Inforamtion

>[!Note]
>This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details. You find the LICENSE file in the main branch.


<!--### 10.3 Install additional Python packages for the Version V4 

First of all, we need packages of Python before we start the python program in the lite version of the IndustrialPI4. Pip3 is a package management tool for Python that is used specifically for Python 3. It allows you to install, manage and update Python packages from the Python Package Index (PyPI). It is a central repository where Python packages are stored and distributed.

+ Install pip3:
```
sudo apt-get install python3-pip
```
>[!Tip]
>Confirm with Y.-->

<!--### 10.4 Work with GitHub directly
+ An other way is to copy the python program from GitHub directly. The condition is that you are connected to the IndustrialPI 4 in your network and you have an Ethernet connection.
```
git clone https://github.com/PilzDE/Samples.git
```
```
cd repository
```
+ Run program on the remote system:
```
cd /pfad/zu/repository
```
+ If the program has dependencies, install them with pip:
```
pip install -r requirements.txt
```
+ Execute the Python program:
```
python3 programm.py
```
>[!Tip]
>Replace program.py with the name of the Python file you want to execute.<br/>

>[!Note]
>The condition here is that you have to install git and pip for this method.<br/>-->