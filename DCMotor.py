import RPi.GPIO as GPIO
import time

# Set pin values
ena = 40
in1 = 38
in2 = 36

# Board and pin setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ena, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

# Set all pins low to start to prevent rotation on run
GPIO.output(ena, GPIO.LOW)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)

# Create PWM instance on enable pin A at 50 Hz
motor1 = GPIO.PWM(ena, 50)

try:
    while True:
        # Set in1 high for counter-clockwise rotation
        GPIO.output(in1, GPIO.HIGH)

        # Start motor with 25% duty cycle
        motor1.start(25)
        time.sleep(5)

        # Set in1 low and in2 high for clockwise rotation
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)

        # Change to 100% duty cycle
        motor1.ChangeDutyCycle(100)
        time.sleep(10)

        # Stop motor
        motor1.stop()
        time.sleep(5)

except KeyboardInterrupt:
    # Stop motor
    motor1.stop()
    
    # Cleanup pins
    GPIO.cleanup()
