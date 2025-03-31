# Samples

<div style="display: flex; flex-direction: column; align-items: center;">
    <a href="https://www.pilz.com" rel="nofollow">
        <img src="/img/pilz-logo.png" alt="Pilz Logo">
    </a><br/>
    <strong>Application IndustrialPI 4 and PSENrd 3.1</strong>
</div>

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
6.  [Install Mosquitto and Mosquitto-Clients](#6-install-mosquitto-and-mosquitto-clients)<br/>
6.1 [Create certificates (optional)](#61-create-certificates-optional)<br/>
6.2 [Configurate Mosquitto Broker](#62-configurate-mosquitto-broker)<br/>
7.  [Setup and Configuration NTP Server](#7-setup-and-configuration-ntp-server)<br/>
8.  [WiFi Configuration](#8-wifi-configuration)<br/>
8.1 [Install dnsmasq](#81-install-dnsmasq)<br/>
8.2 [Set up Wifi connection](#82-set-up-wifi-conncetion)<br/>
8.3 [Set up Cockpit-IndustrialPI](#83-set-up-cockpit-industrialpi)<br/>
9.  [Testing of Data exchange](#9-testing-of-data-exchange)<br/>
10. [Integration of the supplied python program example](#10-integration-of-the-supplied-python-program-example)<br/>
10.1[Work with USB-Stick](#101-work-with-usb-stick)<br/>
10.2[Install additional Python package and graphical packages for the Version V1](#102-install-additional-python-package-and-graphical-packages-for-the-version-v1)<br/>
10.3[Start the GUI in the graphical interface](#103-start-the-gui-in-the-graphical-interface)<br/>
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
| 2 | Operating manual of PSEN rd3.1 live| [www.pilz.com >EN Operat.Man. XXXXX](http://Link_fehlt_noch.com)<br/>[www.pilz.com > DE BA 1006933-01](http://Link_fehlt_noch.com)<br> |                                                
| 3 | Operating manual of IndutrialPI 4 |[www.pilz.com >EN Operat.Man. 1006970-01](https://www.pilz.com/en-INT/search#currentPage=1&SEARCH=1006970)<br/>[www.pilz.com >DE BA 1006970-01](https://www.pilz.com/de-INT/search#currentPage=1&SEARCH=1006970)<br/> |

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
> We only use the IndustrialPI 4 here for the application with WiFi network. Because only the IndustrialPI 4 has a WiFi antenna connection.<br/> 

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

+ First of all, connect the IndustrialPI 4 to a monitor. A micro HDMI is available on the IndustrialPI 4.<br/>
+ Connect a keyboard via the IndustrialPI 4 USB ports.<br/>
+ Start the IndustrialPI 4 with the 24VDC supply. The IndustrialPI 4 then boots up.<br/>

> [!IMPORTANT]
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


## 6. Install Mosquitto and Mosquitto-Clients

+ Please use the installation of Mosquitto and Mosquitto-Clients from the README.md PilzForwarder:<br/>
[Install Mosquitto and Mosquitto-Clients](https://github.com/PilzDE/PilzForwarder?tab=readme-ov-file#32-install-mosquitto-and-mosquitto-clients)<br/>

### 6.1 Create certificates (optional)

+ Also install the necessary additional conditions that are only required if you want to use self-signed certificates,<br/>
including the creation of certificates and the creation of access control lists:<br/>
[Install OpenSLL and create certificates](https://github.com/PilzDE/PilzForwarder?tab=readme-ov-file#33-install-openssl-optional)<br/>

### 6.2 Configurate Mosquitto Broker

+ The next step describes the configuration of the MQTT-broker, this step is necessary, so follow the instructions:<br/>
[Configurate Mosquitto Broker](https://github.com/PilzDE/PilzForwarder?tab=readme-ov-file#37-configurate-mosquitto-broker)<br/>

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

### 8.2 Set up Wifi Conncetion 
+ Use this command:
```
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
```
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
> [!Tip]
> When you connect the WiFi the first time, please control in your Network Mangager "sudo nmtui" whether the IndustrialPI 4 find your desired WiFi. This Tip belongs to the subitem [5.3 Update System packages](#53-update-system-packages).

> [!Tip]
> Use a WiFi endpoint device, e.g. a smartphone, and check whether you can see the new WiFi connection in your WiFi settings. Click on it and connect and see if you are then in the WiFi. You can see this by the checkmark and the WiFi icon.

> [!Tip]
> The next test is to try out the browser cockpit of your IndustrialPI 4. First connect your mobile phone or notebook to the existing Wifi connection as described in the previous tip. Then open any browser and enter the same hostname as in the settings in the previous chapter. If you are asked for a user name and password, everything is correct.

## 9. Testing of Data exchange 

+ You can start by checking whether you can connect the IndustrialPI 4 system to the PSENrd 3.1. First restart the IndustrialPI 4:
```
sudo reboot
```
>[!Tip]
> General tip, restarting the system is very important for many new installations. Restart the IndustrialPI 4 from time to time.

>[!Tip]
> Again, remember the synchronization time of the NTP service.

+ The tail -f command is used to display the last lines of a file in real time. If you use it with Mosquitto, you can monitor the log file of the Mosquitto broker to see current activities and messages.
```
sudo tail -f /var/log/mosquitto/mosquitto.log
```
+ You can find for example the information in the table:

New connection from IP-Address:Portnumber as MAC-Address(of your sensor) (p2, c1, k120).

+ The next step is to press Ctrl + C to exit the currently running command or process and return to the command line to enter new commands.
+ We need the first test whether the sensor sends data to the Industrial PI 4.
```
mosquitto_sub -p 8883 -h <IP-Address> --cafile <Path to the CA file> -t '/PSENrd3/<MAC-Address of your Sensor>/positionData'
```
>[!Tip]
>You will find the 12-digit Mac address on the back of the sensor.

+  Position data should then gradually appear on your shell.

## 10. Integration of the supplied python program example

>[!Note]
>We greate a graphical python program for this application. This graphical Python program displays recognized people and counts them. The program can be found in the table at the top of this repository.

### 10.1 Work with USB-stick
>[!Note]
>The follow description shows how to copy the Python program from the GitHub repository (https://github.com/PilzDE/Samples) of your workstation notebook to any USB stick and then integrate it into your IndustrialPI 4 system. Please copy the raw file of the Python program from the GitHub repository Samples and insert it into a suitable tool. Save the file and copy the program to your USB stick.

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
> [!Tip]
> Try whether the setting has worked. For example press Y or Z.

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