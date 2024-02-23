#rough sketch of the car class

engineSpeed = 0 # value of 0 to 2000 with resolution of 1
brake = 0       # value of 0 to 1 with resolution of 0.1
throttle = 0    # value of 0 to 1 with resolution of 0.1

clutch = 0
gear = 0

steeringAngle = 0
carVelocityX = 0
carVelocitY = 0

def throttleUp():
    throttle = 1
    brake = 0
