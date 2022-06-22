import libhousy
#You can define helper functions here, make sure to but them *above* the main function
def pickup(self):
    self.robot.pickupMotor.Set(1)
    self.robot.pickupPneumatic.Extend()
    self.robot.beltZ1.Set(-0.8)
    self.robot.beltZ2.Set(0)
    self.robot.beltZ3.Set(0)
    self.robot.upperTension.Retract()
    self.robot.lowerTension.Extend()

def main(robot: libhousy.robot):
    #Here is where your recurring code will go
    if robot.controller.getAxis(robot.controller.Axis.lTrigger) > 0.8:
        pickup()
        return libhousy.DONE

    # This tells the robot we're done and it can move on
       
