import pyrosim.pyrosim as pyrosim
import constants
import pybullet as p
import numpy as np

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()


    def Prepare_To_Act(self):
        self.amplitude = constants.amplitudeFL
        self.frequency = constants.frequencyFL
        self.offset = constants.phaseOffsetFL


        if (self.jointName == "BackLeg_Torso"):
            self.targetAngles = self.amplitude * np.sin((self.frequency / 2) * constants.targetAngles + self.offset)
        else:
            self.targetAngles = self.amplitude * np.sin(self.frequency * constants.targetAngles + self.offset)


    def Set_Value(self, robotId, t):

        #motorCode_Torso_FrontLeg

        pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = self.jointName,
        controlMode = p.POSITION_CONTROL,
        targetPosition = self.targetAngles[t],
        maxForce = 50)


    def Save_Values(self):
        np.save('./data/refractoredRobotMotor.npy', self.targetAnglesFL)