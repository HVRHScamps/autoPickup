# inclue code to help us talk to the robot
from tracemalloc import stop
import libhousy

def pickup(robot):
    print("running pickup mode")
    robot.pickupMotor.Set(1)
    robot.pickupPneumatic.Extend()
    robot.beltZ1(-0.8)
    robot.beltZ2(0)
    robot.beltZ3(0)
    robot.upperTension.retract()
    robot.lowerTension.retract()

def main(robot: libhousy.robot):
    # Here is where your recurring code will go
    if robot.controller.getAxis(robot.controller.Axis.lTrigger) > 0.8:
        pickup(robot)
   
    else:
        robot.pickupMotor.Set(0)
        robot.pickupPneumatic.Retract()
        robot.beltZ1(0)
        robot.beltZ2(0)
        robot.beltZ3(0)

    # After everything is done, we tell the main program to stop us