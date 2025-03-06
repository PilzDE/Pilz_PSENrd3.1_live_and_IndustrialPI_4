# Samples

<div style="display: flex; flex-direction: column; align-items: center;">
    <a href="https://www.pilz.com" rel="nofollow">
        <img src="/img/pilz-logo.png" alt="Pilz Logo">
    </a><br/>
    <strong>Application IndustrialPi and PSENrd 3</strong>
</div>

## Contents and Setup steps

1.  [Useful documentation](#1-useful-documentation)<br/>
1.1 [Documentation form Pilz GmbH & Co. KG](#11-documentation-from-pilz-gmbh--co-kg)<br/>
1.2 [Documentation form other sources](#12-documentation-form-other-sources)<br/>
2.  [Hardware and software used](#2-hardware-and-software-used)<br/>
2.1 [Pilz products](#21-pilz-products)<br/>
2.2 [Third-party products](#22-third-party-products)<br/>
2.3 [Stucture of the applaction (schematic)](#23-stucture-of-the-applaction-schematic)<br/>
3.  [Preface](#3-preface)<br/>
4.  [Application description](#4-application-description)<br/>
5.  [First steps to start IndustrialPi](#5-first-steps-to-start-industrialpi)<br/>
5.1 [Password](#51-password)<br/>
5.2 [Instructions for changing the keyboard settings](#52-instructions-for-changing-the-keyboard-settings)<br/>
5.3 [Update System packages](#53-update-system-packages)<br/>
6.  [Install Mosquitto and Mosquitto-Clients](#6-install-mosquitto-and-mosquitto-clients)<br/>
6.1 [Create certificates (optional)](#61-create-certificates-optional)<br/>
6.2 [Configurate Mosquitto Broker](#62-configurate-mosquitto-broker)<br/>
7.  [Setup and Configuration NTP Server](#7-setup-and-configuration-ntp-server)<br/>
8.  [WiFi Configuration](#8-wifi-configuration)<br/>

## 1. Useful documentation

Reading the documentation listed below is necessary for understanding this Application Note.<br/>
The availability of the software used, and its safe handling are also presupposed for the user.

### 1.1 Documentation from Pilz GmbH & Co. KG

|Nr.| Discription | Part number/ Download|
|---| ------------| ---------------------|
| 1 | Pilz international website, download area | [www.pilz.com >EN Support >Downloads](https://www.pilz.com/en-INT/support/downloads)<br/> [www.pilz.com > DE Support > Downloads](https://www.pilz.com/de-INT/support/downloads)<br/> |
| 2 | Operating manual of PSEN rd3.1 live| [www.pilz.com >EN Operat.Man. XXXXX](http://Link_fehlt_noch.com)<br/>[www.pilz.com > DE BA 1006933-01](http://Link_fehlt_noch.com)<br> |                                                
| 3 | operating manual of IndutrialPi 4 |[www.pilz.com >EN Operat.Man. 1006970-01](https://www.pilz.com/en-INT/search#currentPage=1&SEARCH=1006970)<br/>[www.pilz.com >DE BA 1006970-01](https://www.pilz.com/de-INT/search#currentPage=1&SEARCH=1006970)<br/> |

### 1.2 Documentation form other sources of information

|Nr.| Discription | Part number/ Download|
|---| ------------| ---------------------|
| 1 | RevolutionPi Kunbus Homepage     | [www.revolutionpiDE.com](https://revolutionpi.com/documentation/de/)<br/>[www.revolutionpiEN.com](https://revolutionpi.com/documentation/) |

## 2. Hardware and software used

### 2.1 Pilz products

|Nr.| Discription | Order number| Version| Quantity|
|---| ------------|-------------| -------| --------|
| 1 | IndustrialPi| A1000003    |   4    |    1    |
| 2 | PSENrd 3.1  | X           | XXXXXXX|    1    |
| 3 | PSEN cable axial M12 5-pole, 3m| 630310 | - | 1 |

### 2.2 Third-party products

|Nr.| Discription | Order number| Version| Quantity|
|---| ------------|-------------| -------| --------|
| 1 |   Monitor   |      -      |    -   |    1    |
| 2 |   Keyboard  |      -      |    -   |    1    |
| 3 | Micro-HDMI adapter |  -   |    -   |    1    |
| 4 | HDMI cable for the Monitor| -  | - |    1    |

### 2.3 Stucture of the applaction (schematic)

Bild [hier]

## 3. Preface

This application basically describes the commissioning process of a PSENrd 3.1 with an Industrial Pi 4. Both devices communicate with each other using MQTT.
Data is sent from the PSENrd 3.1 to the internal access point of the Industrial Pi 4. This data is sent to the Python program provided and processed there. <br/>
The basic procedure for successful basic configuration is shown here step-by-step, mostly using command lines.<br/> 

> [!IMPORTANT]
> This document only describes the procedure for using the IndustrialPi 4 (A1000003) and PSENrd 3.1 (XXX) and does not constitute technical documentation on the general use of the operating system Linux and Python.

## 4. Application description

The sample here is people counting to detect whether one or more people are in a monitored area, even if this area is not detected by the radar sensor. <br/>

There are several requirements for the realization of this application: <br/>

+ Data transmission takes place via MQTT <br/>
+ Evaluation of the sensor data in the IndustrialPi 4 in real time <br/>
+ Recording of personal data in a specific area <br/>
+ All persons detected by the PSENrd 3.1 sensor are recorded and processed by the IndustrialPi 4 <br/>

Non-functional requirements: <br/>

+ Stability and reliability of the system <br/>
+ Simple setup and handling of the operating system on the IndustrialPi 4 <br/>

The structure of the system and components is based on: <br/>
[2.3 Stucture of the applaction (schematic)](#23-stucture-of-the-applaction-schematic) <br/>

## 5. First Steps to start IndustrialPi 4 

### 5.1 Password 

+ First of all, connect the IndustrialPi 4 to a monitor. A micro HDMI is available on the IndustrialPi 4.<br/>
+ Connect a keyboard via the IndustrialPi 4 USB ports.<br/>
+ Start the IndustrialPi 4 with the 24VDC supply. The Industrial Pi 4 then boots up.<br/>

> [!IMPORTANT]
><ins>Installation after a new Image</ins><br/>
  The first login of the IndustrialPi is:<br/>
    Username: pi <br/> Password: raspberry

> [!Tip]
> When you enter password, the letters and special characters are not displayed.

> [!Tip]
> Please note that the standard keyboard is set to English (US). This means that the Z and Y keys are reversed. Please note this when entering the first password.

Information comes:<br/>

The device configuration was detected automatically. Manual configuration is therefore not necessary.<br/>

Press okay<br/> 

You will now be asked to use the password on the sticker.<br/>

> [!Tip]
> Please note that the standard keyboard is set to English (US). This means that the Z and Y keys are reversed. Please note this when entering the first password.<br/>
> The letter l (small L) can easily be confused with the number 1 (one). Make sure you use the correct character.<br/>

### 5.2 Instructions for changing the keyboard settings

Open the Raspberry Pi Software Configuration Tool (raspi-config)<br/>

> [!Tip]
> On the English keyboard, the character - (hyphen) corresponds to the character ? (question mark). Make sure you take this into account when entering.

```
sudo raspi-config
```
+ select localisation options<br/>
+ then select L3 Keyboard<br/>
+ select the model of your keyboard<br/>
+ go to the sub-item other <br/>
+ select your language<br/>
+ select the default for the keyboard layout as the next step<br/>
+ deselect compose key in the last step<br/>

Exit the configuration tool with the esc key.

> [!Tip]
> Try whether the setting has worked. press Y or Z.

### 5.3 Update System packages

> [!Tip]
> Connect your IndustrialPI to the Internet for the first time via the Ethernet interface. 

+ get all updates with the commando

 ```
 sudo apt-get update
 ```
 ```
 sudo apt-get upgrade
 ```
> [!Tip]
> Both commands will ask you to continue. confirm both commands with Y.

## 6. Install Mosquitto and Mosquitto-Clients

+ Please use the installation of Mosquitto and Mosquitto-Clients from the README.md PilzForwarder:<br/>
[Install Mosquitto and Mosquitto-Clients](https://github.com/PilzDE/PilzForwarder?tab=readme-ov-file#32-install-mosquitto-and-mosquitto-clients)<br/>

### 6.1 Create certificates (optional)

+ Also install the necessary additional conditions that are only required if you want to use self-signed certificates,<br/>
including the creation of certificates and the creation of access control lists.<br/>
[Install OpenSLL and create certificates](https://github.com/PilzDE/PilzForwarder?tab=readme-ov-file#33-install-openssl-optional)<br/>

### 6.2 Configurate Mosquitto Broker

+ The next step describes the configuration of the MQTT-broker, this step is necessary, so follow the instructions.<br/>
[Configurate Mosquitto Broker](https://github.com/PilzDE/PilzForwarder?tab=readme-ov-file#37-configurate-mosquitto-broker)<br/>

## 7. Setup and Configuration NTP Server

+ Install NTP

```
sudo apt-get install ntp
```
+ Open the NTP config file

```
sudo nano /etc/ntpsec/ntp.conf
```
+ Add the following configuration to the ntp.config file

```
nts disable
server 127.127.1.0
fudge 127.127.1.0 stratum 10
```
+ Save the file and restart the ntp service

```
sudo systemctl restart ntpsec
```
or
```
sudo service ntpsec restart
```
```
sudo systemctl enable ntpsec
```
> [!Tip]
> To activate the NTPsec service automatically at system startup, you should use the systemctl command.

+ Control whether your system clock is synchronized

```
timedatectl status
```
> [!Tip]
> All times should be displayed in the same way. “Yes” should be displayed behind the synchronized system clock.

## 8. WiFi configuration 

+ Use this command

```
sudo nmtui
```
+ Go to the menu item “edit a connection”.
+ Navigate to the "Add"-button.
+ Select: Wi-Fi.
+ Assign a profile name.
+ Next up assign the SSID. You can use the same name as in profile name.
+ Select mode: Access Point.
+ Selct security: WPA & WPA2 Personal.
+ Assign your password.
+ Selsct "Manual" for the IPv4 configuration.
+ Assign the address for example 192.168.0.102/24.
+ At the gateway, assign 192.168.0.1, for example.
+ Then accept everything with OK.
+ Restart your System.
```
sudo reboot
```
+ To connect a notebook to your Industrial Pi, use an Ethernet cable to connect the notebook to one of the Industrial Pi's Ethernet ports. Open your browser and enter http://industrialpiXXXXXX.local in your search bar. For XXXXXX, enter the six-digit serial number of the Industrial-Pi. You will find this number on the front of the Industrial Pi.
+ Log in with the data provided on the sticker on the side of the Indutrial Pi.
+ It will open a dashboard of your IndustrialPi.
+ Under Tools you will find the item RevPi Configuration. Click on it.
+ Now you will see various setting options.
+ To be on the safe side, please deactivate the bluetooth cennection.
+ Select the external antenna (SMA) under select antenna.
+ then restart the Industrial Pi.
```
sudo reboot
```
> [!Tip]
> Use a WiFi endpoint device, e.g. a smartphone, and check whether you can see the new WiFi connection in your WiFi settings. If you see a loading icon then click on Information or Settings of your WiFi- connection. Under configure IP select the manual option and use an address in this network.<br/> Example: your access point is 192.168.0.102, use the address 192.168.0.103 and the subnet mask 255.255.255.0 for your mobil phone, the Router (Gateway) in your mobil phone is 192.168.0.1..

> [!Tip]
> The next test is to try out the browser cockpit of your Industrial Pi. First connect your mobile phone or notebook to the existing Wifi connection. Then open any browser and enter the same host name as in the settings in the previous chapter. If you are asked for a user name and password, everything is correct.

## Testing of Data exchange 