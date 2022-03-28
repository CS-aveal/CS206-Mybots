import world as wor
import robot as rob
import sensor
import time
import numpy as np
import pybullet_data
import constants
import pybullet as p
import pyrosim.pyrosim as pyrosim

class SIMULATION:
    def __init__(self, directOrGUI, solutionID):

        self.solutionID = solutionID

        self.directOrGUI =  directOrGUI
        #self.physicsClient = p.connect(p.GUI)
        if (directOrGUI == "DIRECT"):
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        self.world = wor.WORLD()
        # for x in range(5):
        #     self.robot = rob.ROBOT()
        self.robot = rob.ROBOT(solutionID)



    def Run(self):
        if (self.directOrGUI == "GUI"):
            for x in range(constants.loop):
                time.sleep(1/10000)
                #print(x)
                p.stepSimulation()
                self.robot.Sense(x)
                self.robot.Think()
                self.robot.Act(x)
        else:
            for x in range(constants.loop):
                print(x)
                p.stepSimulation()
                self.robot.Sense(x)
                self.robot.Think()
                self.robot.Act(x)


    def __del__(self):
        p.disconnect()


    def Get_Fitness(self):
        self.robot.Get_Fitness()