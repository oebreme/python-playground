# import modules
import RPi.GPIO as GPIO
import time

# Define Input and Output Pins
inputs = [27, 29, 31, 33]
outputs = [22, 24, 26, 28]
# Define State Array
state = [0, 0, 0, 0]

# setup pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inputs, GPIO.IN)
GPIO.setup(outputs, GPIO.OUT)

while True:
    for i in range(4):

        if GPIO.input(inputs[i]) == GPIO.HIGH:
            GPIO.output(outputs[i], GPIO.HIGH)
            if state[i] != 1:
                print("Änderung Erfolgt")
            state[i] = 1
        else:
            GPIO.output(outputs[i], GPIO.LOW)
            if state[i] != 0:
                print("Änderung Erfolgt")
            state[i] = 0

        print(state)

        time.sleep(1)