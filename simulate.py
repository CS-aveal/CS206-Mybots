from simulation import SIMULATION
import random
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import time
import numpy as np
import constants as c


simulate = SIMULATION()
simulate.Run()
# #connecting to the engine
# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.setGravity(0,0,-9.8)
#
# #loading all of the simulation data
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")
# p.loadSDF("world.sdf")
# pyrosim.Prepare_To_Simulate(robotId)
#
# #sensor values
# backLegSensorValues = np.zeros(1000)
# frontLegSensorValues = np.zeros(1000)
#
# y = np.linspace(0,2 * np.pi, num=1000)
#
# targetAnglesBL = np.sin(y)
#
#
#
#
# #front leg sensor variables
# amplitudeFL = c.amplitudeFL
# frequencyFL = c.frequencyFL
# phaseOffsetFL = c.phaseOffsetFL
#
# #back leg sensor variables
# amplitudeBL = c.amplitudeBL
# frequencyBL = c.frequencyBL
# phaseOffsetBL = c.phaseOffsetBL
#
#
#
# for x in range(1000):
#   time.sleep(1/240)
#   print(x)
#   p.stepSimulation()
#
#   #gettingtargetvalues
#
#   #z = targetAngles[x]
#   #val=(z-a)/(b-a) * (d-c) + c
#   #print("Val = ")
#   #print(val)
#
#
#
#
#   #overwrite the other targetAngles[]
#   print(c.amplitudeFL)
#   targetAnglesFL[x] = amplitudeFL * np.sin(frequencyFL * targetAnglesFL[x] + phaseOffsetFL)
#   targetAnglesBL[x] = amplitudeBL * np.sin(frequencyBL * targetAnglesBL[x] + phaseOffsetBL)
#   #sensorCode
#
#   backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#   frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#
#   #motorCode_BackLeg_Torso
#
#   pyrosim.Set_Motor_For_Joint(
#   bodyIndex = robotId,
#   jointName = "BackLeg_Torso",
#   controlMode = p.POSITION_CONTROL,
#   targetPosition = targetAnglesBL[x],
#   maxForce = 50)
#
#   #motorCode_Torso_FrontLeg
#
#   pyrosim.Set_Motor_For_Joint(
#   bodyIndex = robotId,
#   jointName = "Torso_FrontLeg",
#   controlMode = p.POSITION_CONTROL,
#   targetPosition = targetAnglesFL[x],
#   maxForce = 50)
#
#
# p.disconnect()
# np.save('./data/backLegSensorValues.npy', backLegSensorValues)
# np.save('./data/frontLegSensorValues.npy', frontLegSensorValues)
# np.save('./data/targetAnglesFL.npy', targetAnglesFL)
# np.save('./data/targetAnglesBL.npy', targetAnglesBL)
