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

          # #gettingtargetvalues
          #
          # #z = targetAngles[x]
          # #val=(z-a)/(b-a) * (d-c) + c
          # #print("Val = ")
          # #print(val)
          #
          #
          #
          #
          # #overwrite the other targetAngles[]
          #
          # targetAnglesFL[x] = amplitudeFL * np.sin(frequencyFL * targetAnglesFL[x] + phaseOffsetFL)
          # targetAnglesBL[x] = amplitudeBL * np.sin(frequencyBL * targetAnglesBL[x] + phaseOffsetBL)
          # #sensorCode
          #
          # backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
          # frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
          #
          # #motorCode_BackLeg_Torso
          #
          # pyrosim.Set_Motor_For_Joint(
          # bodyIndex = robotId,
          # jointName = "BackLeg_Torso",
          # controlMode = p.POSITION_CONTROL,
          # targetPosition = targetAnglesBL[x],
          # maxForce = 50)
          #
          # #motorCode_Torso_FrontLeg
          #
          # pyrosim.Set_Motor_For_Joint(
          # bodyIndex = robotId,
          # jointName = "Torso_FrontLeg",
          # controlMode = p.POSITION_CONTROL,
          # targetPosition = targetAnglesFL[x],
          # maxForce = 50)

    def __del__(self):
        p.disconnect()