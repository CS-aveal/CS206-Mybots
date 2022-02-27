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
    def __init__(self):

        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        self.world = wor.WORLD()
        self.robot = rob.ROBOT()



    def Run(self):
        for x in range(constants.loop):
          time.sleep(1/240)
          print(x)
          p.stepSimulation()
          self.robot.Sense(x)
          self.robot.Act(x)


    def __del__(self):
        p.disconnect()