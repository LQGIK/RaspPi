from gpiozero import Robot, LineSensor
from time import sleep, time



# Set GPIO PINS
# If motor is rotating in opposite direction, switch the given (right or left) GPIO pins
robby = Robot(left=(w, x), right=(y, z))

# Sensors
left_sensor = LineSensor(_)
right_sensor= LineSensor(_)
left = left_sensor.when_no_line
right = right_sensor.when_no_line

#left_sensor.when_line = function_name_to_call
#left_sensor.when_no_line = other_function_name_to_call

count = 0
while True:

    # On track
    if left and right:
        robby.forward(0.5)
        count = 0

    # Curve to the right
    elif not right:
        robby.left(0.5)
        robby.right(-0.5)
        print("Adjusting to the right")

    # Curve to the left
    elif not left:
        robby.left(-0.5)
        robby.right(0.5)
        print("Adjusting to the left")