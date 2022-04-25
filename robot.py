import pybullet as p
import os
import constants
from pyrosim.neuralNetwork import NEURAL_NETWORK
import sensor
import motor as mot
import pyrosim.pyrosim as pyrosim


class ROBOT:

    def __init__(self, solutionID):
        self.solutionID = solutionID
        strSolutionID = str(solutionID)
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain{}.nndf".format(solutionID))
        # self.nn = NEURAL_NETWORK("brain" + strSolutionID + ".nndf")
        os.system("rm brain" + strSolutionID + ".nndf")

    def Sense(self, t):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName].Get_Value(t)


    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = sensor.SENSOR(linkName)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = mot.MOTOR(jointName)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * constants.motorJointRange
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)

    def Think(self):
        self.nn.Update()
        #self.nn.Print()


    def Get_Fitness(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]
        strSolutionID = str(self.solutionID)
        f = open("tmp" + strSolutionID + ".txt", "w")
        os.system("mv tmp" + strSolutionID + ".txt fitness" + strSolutionID + ".txt")
        strcord = str(xPosition)
        f.write(strcord)
        f.close()
        print("colnumber")
        print(constants.colnum)
        print("rownumber")
        print(constants.rownum)
        exit()
