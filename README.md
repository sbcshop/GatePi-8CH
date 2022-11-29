# GatePi-8CH
The 8-Channel GatePi Relay Board based on LoRa™ and RP2040 MCU is a low-power data transmission board and has all the features exactly similar to the 4 Channel Relay Board, except it has 8 relay channels for an increased capacity and efficiency. It is a low-power consumption data transmission board, that comes with an onboard CH340 USB TO UART converter, Voltage Level Translator(74HC125V), E22-400T22S/E22-900T22S SMA antenna connector that covers 433/868/915 MHz frequency band, 8-Ch Relays, IPEX antenna connector, LoRa™ Spread Spectrum Modulation technology with auto multi-level repeating. GatePi is developed to enable data transmission up to 5 KM through the serial port.

## Features
* It has 8ch relays for controlling 8-Outputs connections
* 8 Status LED's for showing the current status of relays
* LoRa Mudule
* RP2040 MCU
* Antenna Connector 
* Range upto 5KM
* Supports Multiple frequency bands such as(433MHz, 868MHz, 915MHz)

## Hardware Specifications

image

## RP2040
Raspberry Pi RP2040 Microcontroller Chip is the debut microcontroller from Raspberry Pi. It brings high performance, low cost, and ease of use to the microcontroller space. The RP2040 has a large on-chip memory, symmetric dual-core processor complex, deterministic bus fabric, and rich peripheral set. It's augmented with a unique Programmable I/O (PIO) subsystem and provides unrivaled power and flexibility.

## LoRa Module(E22-400T22S)
LoRa stands for Long Range Radio and is mainly targeted for M2M and IoT networks. This technology will enable public or multi-tenant networks to connect a number of applications running on the same network. E22-400T22S1B is a wireless serial port module (UART) based on SEMTECH's SX1268 RF chip. It has multiple transmission modes,working in the (410.125MHz~493.125MHz) frequency band (default 433.125MHz), LoRa spread spectrum technology, TTL level output,compatible with 3.3V and 5V IO port.

## Relays
The GatePi 8channel board is consist of 8 relay modules for connecting the four different appliances or any devices you want to control through our GatePi board.

## USB Port, and Boot Button
USB port is used for debugging python programmes in our this board, and for powering up this board. Boot button is used to make GatePi 8Ch board in Boot mode for updating firmware to it.

## Instruction Manual of GatePi
* For the instruction manual of GatePi please click on the link : https://github.com/sbcshop/GatePi-4CH/blob/main/GatePi%20instruction%20manual.pdf and download it. 

   * In this manual you will see:
      * how to setup GatePi 
      * How to use "LoRa Home Automation Application(App)
      

## Working With GatePi 8Ch

For working with this board you will need two or more than two loara product, it can be same products or may be our other LoRa products to establish the communication between them.

* ***The "main.py" is the reciever example code for controlling 8 relays. This code should be saved in RP2040 of GatePi 8ch so that when it recieve data from transmitter it will operate realys one by one according to data recieved at this end.

* ***The "Transmit.py" file is the code for sending the data for the purpose of controlling relays of GatePi. This code can be saved in any of our LoRa devices(such as RangePi)to send data. It will send "1relay1" to operate "relay-1" and so on for other relays, you can replace this by any keywords you want but this should be change in reciever code also.


## Our Other LoRa Products

* GatePi 4Channel
* GatePi 8channel*
* RangePi(USB Dongle)
* LoRA HAT for RPi
* PICO LoRa Expansion

You will simply need to make one device to work as reciever and another one is as a transmitter. So that you can communicate to each other and this can be done with any of our LoRa products mentioned above. For working with our other products please follow the below link:

* GatePi 4Channel
https://github.com/sbcshop/GatePi-4CH

* GatePi 8channel* (Itself)
* RangePi
https://github.com/sbcshop/RangePi
* LoRA HAT for RPi
https://github.com/sbcshop/Lora-HAT-for-Raspberry-Pi
* PICO LoRa Expansion
https://github.com/sbcshop/PICO-LORA-EXPANSION



