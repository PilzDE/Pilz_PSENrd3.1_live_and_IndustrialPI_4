# Samples
Application IndustrialPi and PSENrd 3

## Contents and Setup steps

1.  [Useful documentation](#1-useful-documentation).
1.1 [Documentation form Pilz GmbH & Co. KG](#11-documentation-from-pilz-gmbh--co-kg)
1.2 [Documentation form other sources](#12-documentation-form-other-sources)
2.  [Hardware and software used](#2-hardware-and-software-used)
2.1 [Pilz products](#21-pilz-products)
2.2 [Third-party products](#22-third-party-products)
2.3 [Stucture of the applaction (schematic)](#23-stucture-of-the-applaction-schematic)
3.  [Foreword](#3-foreword)
4.  [Application description](#4-application-description)
5.  [Setup MQTT](#5-setup-mqtt)

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
| 1 |      X      |      X      |    X   |    X    |
| 2 |      X      |      X      |    X   |    X    |

### 2.3 Stucture of the applaction (schematic)

Bild [hier]

## 3. Foreword

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

## 5. Setup MQTT


