import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module

GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
# GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)

# def forward():
#     print('forward')
#     # GPIO.output(11, GPIO.HIGH)
#     # GPIO.output(15, GPIO.HIGH)
#     # GPIO.output(37, GPIO.HIGH)#
    
    
# def reverse():
#     print('reverse')
#     # GPIO.output(11, GPIO.LOW)
#     # GPIO.output(15, GPIO.LOW)
#     # GPIO.output(37, GPIO.LOW)
    
# def Left():
#     print('left')
#     # GPIO.output(15, GPIO.HIGH)
#     # GPIO.output(11, GPIO.LOW)
#     # GPIO.output(37, GPIO.LOW)
    
    
# def Right():
#     print('right')
#     # GPIO.output(15, GPIO.LOW)
#     # GPIO.output(11, GPIO.HIGH)
#     # GPIO.output(37, GPIO.LOW)
        
    

print('ran picar script')
