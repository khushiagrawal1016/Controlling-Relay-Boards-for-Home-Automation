import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

GPIO.output(12, GPIO.HIGH) 
GPIO.output(24, GPIO.HIGH) 
time.sleep(0.5)

X=input("Do you wish to switch both the relays off? [YES/NO]")

if(X == "YES" or X=="yes"): 
  GPIO.output(12, GPIO.LOW) 
  GPIO.output(24, GPIO.LOW) 
  time.sleep(0.5) 
  print("Both the relays have been switched OFF") 

elif(X == "NO" or X=="no"):
  Y= input("Which switch do you want to turn off? [ONLY 1/ONLY 2]") 
  if(Y == "ONLY 1" or Y=="only 1"): 
    GPIO.output(12, GPIO.LOW) 
    GPIO.output(24, GPIO.HIGH) 
    time.sleep(0.5) 
    print("Relay 1 has been switched OFF") 
    
  elif(Y == "ONLY 2" or Y=="only 2"):
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW) 
    time.sleep(0.5) 
    print("Relay 2 has been switched OFF") 
  
  else:
    GPIO.output(12, GPIO.LOW) 
    GPIO.output(24, GPIO.LOW) 
    print("Due to invalid input , both the relays have been switched off") 

else:
  GPIO.output(12, GPIO.LOW) 
  GPIO.output(24, GPIO.LOW)
  print("Due to invalid input, both the relays have been switched")
