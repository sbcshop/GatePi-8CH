#Receiver code
import utime
from machine import Pin, UART,SPI
import time

lora = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))

relay1 = machine.Pin(18, machine.Pin.OUT)
relay2 = machine.Pin(19, machine.Pin.OUT)
relay3 = machine.Pin(20, machine.Pin.OUT)
relay4 = machine.Pin(21, machine.Pin.OUT)
relay5 = machine.Pin(22, machine.Pin.OUT)
relay6 = machine.Pin(23, machine.Pin.OUT)
relay7 = machine.Pin(17, machine.Pin.OUT)
relay8 = machine.Pin(16, machine.Pin.OUT)

relay1.value(0)#initally relay1 at LOW
relay2.value(0)#initally relay2 at LOW
relay3.value(0)#initally relay3 at LOW
relay4.value(0)#initally relay4 at LOW
relay5.value(0)#initally relay1 at LOW
relay6.value(0)#initally relay2 at LOW
relay7.value(0)#initally relay3 at LOW
relay8.value(0)#initally relay4 at LOW

request1 = 0;
flag_1=0;

request2 = 0;
flag_2=0;

request3 = 0;
flag_3=0;

request4 = 0;
flag_4=0;

request5 = 0;
flag_5=0;

request6 = 0;
flag_6=0;

request7 = 0;
flag_7=0;

request8 = 0;
flag_8=0;


while True:
    data_Read = lora.readline()#read data comming from other pico lora expansion
    print(data_Read)
    if data_Read is not None and "1relay1" in data_Read:
      #ones, turn led on!
      if flag_1 == 0:
        print("relay 1 on")
        relay1.value(1)
        flag_1=1; #change flag variable
        
        
      #twice, turn led off!
      elif flag_1 == 1:
        print("relay 1 off")
        relay1.value(0)
        flag_1=0; #change flag variable again
        
        
    if data_Read is not None and "2relay2" in data_Read:
      #ones, turn led on!
      if flag_2 == 0:
        print("relay 2 on")
        relay2.value(1)
        flag_2=1; #change flag variable
        
      #twice, turn led off!
      elif flag_2 == 1:
        print("relay 2 off")
        relay2.value(0)
        flag_2=0; #change flag variable again
        
        
    if data_Read is not None and "3relay3" in data_Read:
      #ones, turn led on!
      if flag_3 == 0:
        print("relay 3 on")
        relay3.value(1)
        flag_3=1; #change flag variable
        
      #twice, turn led off!
      elif flag_3 == 1:
        print("relay 3 off")
        relay3.value(0)
        flag_3=0; #change flag variable again
        
    if data_Read is not None and "4relay4" in data_Read:
      #ones, turn led on!
      if flag_4 == 0:
        print("relay 4 on")
        relay4.value(1)
        flag_4=1; #change flag variable
        
      #twice, turn led off!
      elif flag_4 == 1:
        print("relay 4 off")
        relay4.value(0)
        flag_4=0; #change flag variable again
        
    if data_Read is not None and "5relay5" in data_Read:
      #ones, turn led on!
      if flag_5 == 0:
        print("relay 1 on")
        relay5.value(1)
        flag_5=1; #change flag variable
        
        
      #twice, turn led off!
      elif flag_5 == 1:
        print("relay 1 off")
        relay5.value(0)
        flag_5=0; #change flag variable again
        
        
    if data_Read is not None and "6relay6" in data_Read:
      #ones, turn led on!
      if flag_6 == 0:
        print("relay 6 on")
        relay6.value(1)
        flag_6=1; #change flag variable
        
      #twice, turn led off!
      elif flag_6 == 1:
        print("relay 6 off")
        relay6.value(0)
        flag_6=0; #change flag variable again
        
        
    if data_Read is not None and "7relay7" in data_Read:
      #ones, turn led on!
      if flag_7 == 0:
        print("relay 7 on")
        relay7.value(1)
        flag_7=1; #change flag variable
        
      #twice, turn led off!
      elif flag_7 == 1:
        print("relay 7 off")
        relay7.value(0)
        flag_7=0; #change flag variable again
        
    if data_Read is not None and "8relay8" in data_Read:
      #ones, turn led on!
      if flag_8 == 0:
        print("relay 8 on")
        relay8.value(1)
        flag_8=1; #change flag variable
        
      #twice, turn led off!
      elif flag_8 == 1:
        print("relay 8 off")
        relay8.value(0)
        flag_8=0; #change flag variable again
        
    if data_Read is not None and "12status12" in data_Read:
      
      lora.write(str(relay1.value()))#send data
      lora.write(str(relay2.value()))#send data
      lora.write(str(relay3.value()))#send data
      lora.write(str(relay4.value()))#send data
      lora.write(str(relay5.value()))#send data
      lora.write(str(relay6.value()))#send data
      lora.write(str(relay7.value()))#send data
      lora.write(str(relay8.value()))#send data

        
    utime.sleep(0.4)#wait for 200ms
