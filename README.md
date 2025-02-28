# Samples
Application IndustrialPi and PSENrd 3
<a href="https://www.pilz.com/">
    <div class="overlayContainer" aria-hidden="false" style="width: 376px; height: 147px;" data-bm="3143"><ul><li></li><li></li></ul></div>
</a>
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
5.3 [Install Mosquitto and Mosquitto-Clients](#53-update-system-packages)<br/>

## 1. Useful documentation

### 1.1 Documentation from Pilz GmbH & Co. KG

It is important to read the dokumentation below in order to unterstand this application.<br/>
The availability of the software used and its safe handling are also assumed by the user.

|Nr.| Discription | Part number/ Download|
|---| ------------| ---------------------|
| 1 | Pilz international website, download area | [www.pilz.com >EN Support >Downloads](https://www.pilz.com/en-INT/support/downloads)<br/> [www.pilz.com > DE Support > Downloads](https://www.pilz.com/de-INT/support/downloads)<br/> |
| 2 | Operating manual of PSEN rd3.1 live| [www.pilz.com >EN Operat.Man. XXXXX](http://Link_fehlt_noch.com)<br/>[www.pilz.com > DE BA 1006933-01](http://Link_fehlt_noch.com)<br> |                                                
| 3 | operating manual of IndutrialPi 4 |[www.pilz.com >EN Operat.Man. 1006970-01](https://www.pilz.com/en-INT/search#currentPage=1&SEARCH=1006970)<br/>[www.pilz.com >DE BA 1006970-01](https://www.pilz.com/de-INT/search#currentPage=1&SEARCH=1006970)<br/> |

### 1.2 Documentation form other sources

|Nr.| Discription | Part number/ Download|
|---| ------------| ---------------------|
| 1 | Example     | [www.example.com](http://example.de) |

## 2. Hardware and software used

### 2.1 Pilz products

|Nr.| Discription | Order number| Version| Quantity|
|---| ------------|-------------| -------| --------|
| 1 | IndustrialPi| A1000003    |   4    |    1    |
| 2 | PSEN rd3.1  | X           | XXXXXXX|    1    |
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

This application basically describes the commissioning of a PSENrd 3.1 with an Industrial Pi. Both devices communicate with each other using MQTT.
Data is sent from the PSENrd 3.1 to the internal access point of the Industrial Pi. This data is sent to the Python program provided and processed there. <br/>
The basic procedure for successful basic configuration is shown here step-by-step, mostly using command lines. 
basic configuration. <br/>

> [!IMPORTANT]
> This document only describes the procedure for using the IndustrialPi (A1000003) and PSENrd 3.1 (XXX) and does not constitute technical documentation on the general use of the operating system Linux and Python.

## 4. Application description

The pattern here is people counting, to detect whether one or more people are in a monitored area, even if this area is not detected by the radar sensor. <br/>

There are several requirements for the realization of this application: <br/>

+ Data transmission takes place via MQTT <br/>
+ Evaluation of the sensor data in the IndustrialPi in real time <br/>
+ Recording of personal data in a specific area <br/>
+ All persons detected by the PSENrd sensor are recorded and processed by the IndustrialPi <br/>

Non-functional requirements: <br/>

+ Stability and reliability of the system <br/>
+ Simple setup and handling of the operating system on the IndustrialPi <br/>

The structure of the system and components is based on: <br/>
[2.3 Stucture of the applaction (schematic)](#23-stucture-of-the-applaction-schematic) <br/>

## 5. First Steps to start IndustrialPi 

### 5.1 Password 

+ First of all, connect the IndustrialPi to a monitor. A micro HDMI is available on the IndustrialPi.<br/>
+ Connect a keyboard via the USB ports on the IndustrialPi.<br/>
+ Start the IndustrialPi with the 24V DC supply. The Industrial then boots up.<br/>

The first login of the IndustrialPi is:

Username: pi

Password: raspberry

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
+ select localization options<br/>
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

### 5.4 Install Mosquitto and Mosquitto-Clients

+ Please use the installation of Mosquitto and Mosquitto-Clients from the README.md PilzForwarder:<br/>
[Install Mosquittoand Mosquitto-Clients](https://github.com/PilzDE/PilzForwarder?tab=readme-ov-file#32-install-mosquitto-and-mosquitto-clients)<br/>

### 5.5 Create certificates (optional)

+ Also install the necessary additional conditions that require, among other things, creating certificates, creating access control lists.<br/>
[Install OpenSLL and create certificates](https://github.com/PilzDE/PilzForwarder?tab=readme-ov-file#33-install-openssl-optional)<br/>




