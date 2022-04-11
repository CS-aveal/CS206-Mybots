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
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0.25, .5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0.25, -.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute", position=[0.5, 0.25, 1],jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute", position=[-0.5, 0.25, 1],jointAxis="1 0 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])

        #second legs

        pyrosim.Send_Joint(name="Torso_FrontLeg1", parent="Torso", child="FrontLeg1", type="revolute", position=[-0.25, .5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg1", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])
        pyrosim.Send_Joint(name="Torso_BackLeg1", parent="Torso", child="BackLeg1", type="revolute", position=[-0.25, -.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg1", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])
        pyrosim.Send_Joint(name="Torso_LeftLeg1", parent="Torso", child="LeftLeg1", type="revolute", position=[0.5, -0.25, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LeftLeg1", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name="Torso_RightLeg1", parent="Torso", child="RightLeg1", type="revolute", position=[-0.5, -0.25, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="RightLeg1", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])

        #lower legs

        pyrosim.Send_Joint(name="FrontLeg_LowerFrontLeg", parent="FrontLeg", child="LowerFrontLeg", type="revolute", position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="BackLeg_LowerBackLeg", parent="BackLeg", child="LowerBackLeg", type="revolute", position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerBackLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="LeftLeg_LowerLeftLeg", parent="LeftLeg", child="LowerLeftLeg", type="revolute", position=[1, 0, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerLeftLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="RightLeg_LowerRightLeg", parent="RightLeg", child="LowerRightLeg", type="revolute", position=[-1, 0, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerRightLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        #second lower legs

        pyrosim.Send_Joint(name="FrontLeg1_LowerFrontLeg1", parent="FrontLeg1", child="LowerFrontLeg1", type="revolute", position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerFrontLeg1", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="BackLeg1_LowerBackLeg1", parent="BackLeg1", child="LowerBackLeg1", type="revolute", position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerBackLeg1", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="LeftLeg1_LowerLeftLeg1", parent="LeftLeg1", child="LowerLeftLeg1", type="revolute", position=[1, 0, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerLeftLeg1", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="RightLeg1_LowerRightLeg1", parent="RightLeg1", child="LowerRightLeg1", type="revolute", position=[-1, 0, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerRightLeg1", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])


        pyrosim.End()





    def Create_Brain(self):


        strID = str(self.myID)

        pyrosim.Start_NeuralNetwork("brain" + strID + ".nndf")

        # Sensor neurons
        sensor1 = pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        sensor2 = pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        sensor3 = pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

        # Motor neurons
        motor1 = pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        motor2 = pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

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