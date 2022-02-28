import pyrosim.pyrosim as pyrosim
import constants
import pybullet as p
import numpy as np

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName



    def Set_Value(self, robotId, desiredAngle):

        #motorCode_Torso_FrontLeg

        pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = self.jointName,
        controlMode = p.POSITION_CONTROL,
        targetPosition = desiredAngle,
        maxForce = 50)


