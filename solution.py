import numpy as np
import time
import random
import constants
import os
import pyrosim.pyrosim as pyrosim

class SOLUTION:

    def __init__(self, nextAvailableID):
        self.weights = np.random.rand(constants.numSensorNeurons,constants.numMotorNeurons) * 2 - 1
        self.myID = nextAvailableID
        self.col = nextAvailableID % constants.populationSize
        print("col is ")
        print(self.col)



        self.weights = self.weights * 2 - 1


    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        strID = str(self.myID)

        fitnessFile = "fitness" + strID + ".txt"


        os.system("python3 simulate.py " + directOrGUI + " " + strID + "2&>1 &")

        while not os.path.exists(fitnessFile):
            time.sleep(0.01)
        f = open(fitnessFile, "r")
        x = f.read()
        self.fitness = float(x)
        f.close()
        print("fitness = ")
        print(self.fitness)


    def Mutate(self):
        randomRow = random.randint(0,2)
        randomColumn = random.randint(0,1)
        self.weights[randomRow][randomColumn] = random.random() * 2 - 1



    def Create_World(self):

        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()



    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0, .5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, -.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute", position=[0.5, 0, 1],jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute", position=[-0.5, 0, 1],jointAxis="1 0 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name="FrontLeg_LowerFrontLeg", parent="FrontLeg", child="LowerFrontLeg", type="revolute", position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="BackLeg_LowerBackLeg", parent="BackLeg", child="LowerBackLeg", type="revolute", position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerBackLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="LeftLeg_LowerLeftLeg", parent="LeftLeg", child="LowerLeftLeg", type="revolute", position=[1, 0, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerLeftLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="RightLeg_LowerRightLeg", parent="RightLeg", child="LowerRightLeg", type="revolute", position=[-1, 0, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerRightLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.End()





    def Create_Brain(self):


        strID = str(self.myID)

        pyrosim.Start_NeuralNetwork("brain" + strID + ".nndf")

        # Sensor neurons
        sensor1 = pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        sensor2 = pyrosim.Send_Sensor_Neuron(name=1, linkName="FrontLeg")
        sensor3 = pyrosim.Send_Sensor_Neuron(name=2, linkName="BackLeg")
        sensor4 = pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLeg")
        sensor5 = pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLeg")
        sensor6 = pyrosim.Send_Sensor_Neuron(name=5, linkName="LowerFrontLeg")
        sensor7 = pyrosim.Send_Sensor_Neuron(name=6, linkName="LowerBackLeg")
        sensor8 = pyrosim.Send_Sensor_Neuron(name=7, linkName="LowerLeftLeg")
        sensor9 = pyrosim.Send_Sensor_Neuron(name=8, linkName="LowerRightLeg")

        # Motor neurons
        motor1 = pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_FrontLeg")
        motor2 = pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_BackLeg")
        motor3 = pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_LeftLeg")
        motor4 = pyrosim.Send_Motor_Neuron(name=12, jointName="Torso_RightLeg")
        motor5 = pyrosim.Send_Motor_Neuron(name=13, jointName="FrontLeg_LowerFrontLeg")
        motor6 = pyrosim.Send_Motor_Neuron(name=14, jointName="BackLeg_LowerBackLeg")
        motor7 = pyrosim.Send_Motor_Neuron(name=15, jointName="LeftLeg_LowerLeftLeg")
        motor8 = pyrosim.Send_Motor_Neuron(name=16, jointName="RightLeg_LowerRightLeg")


        # for x in range(0,len(sensors)):
        #   for y in range(len(sensors),len(sensors) + len(motors) - 1):
        #     pyrosim.Send_Synapse(sourceNeuronName=x, targetNeuronName=y, weight=random.random())

        for currentRow in range(0, constants.numSensorNeurons):
            for currentColumn in range(0, constants.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + 3 , weight=self.weights[currentRow][currentColumn])



        pyrosim.End()



    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        strID = str(self.myID)

        os.system("python3 simulate.py " + directOrGUI + " " + strID + " &")


    def Wait_For_Simulation_To_End(self, directOrGUI):

        strID = str(self.myID)

        fitnessFile = "fitness" + strID + ".txt"

        while not os.path.exists(fitnessFile):
            time.sleep(0.01)
        f = open(fitnessFile, "r")
        x = f.read()
        try:
            self.fitness = float(x)
        except ValueError:
            self.fitness = constants.defaultFit

        f.close()
        os.system("rm fitness" + strID + ".txt")


    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID