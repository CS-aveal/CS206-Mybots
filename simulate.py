import random
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import time
import numpy as np

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)
y = np.linspace(0,2 * np.pi, num=1000)
targetAnglesFL = np.sin(y)
targetAnglesBL = np.sin(y)

#change to -pi/4 to pi/4
a = -1
b = 1
c = -np.pi/4
d = np.pi/4

amplitudeFL = np.pi/4
frequencyFL = 20
phaseOffsetFL = np.pi/4

amplitudeBL = np.pi/4
frequencyBL = 20
phaseOffsetBL = 0

for x in range(1000):
  time.sleep(1/240)
  print(x)
  p.stepSimulation()
  
  #gettingtargetvalues

  #z = targetAngles[x]
  #val=(z-a)/(b-a) * (d-c) + c
  #print("Val = ")
  #print(val)
  

  #overwrite the other targetAngles[]
  targetAnglesFL[x] = amplitudeFL * np.sin(frequencyFL * targetAnglesFL[x] + phaseOffsetFL)
  targetAnglesBL[x] = amplitudeBL * np.sin(frequencyBL * targetAnglesBL[x] + phaseOffsetBL)
  #sensorCode
  
  backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
  frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
  
  #motorCode_BackLeg_Torso

  pyrosim.Set_Motor_For_Joint(
  bodyIndex = robotId,
  jointName = "BackLeg_Torso",
  controlMode = p.POSITION_CONTROL,
  targetPosition = targetAnglesBL[x],
  maxForce = 50)

  #motorCode_Torso_FrontLeg

  pyrosim.Set_Motor_For_Joint(
  bodyIndex = robotId,
  jointName = "Torso_FrontLeg",
  controlMode = p.POSITION_CONTROL,
  targetPosition = targetAnglesFL[x],
  maxForce = 50)


p.disconnect()
np.save('./data/backLegSensorValues.npy', backLegSensorValues)
np.save('./data/frontLegSensorValues.npy', frontLegSensorValues)
np.save('./data/targetAnglesFL.npy', targetAnglesFL)
np.save('./data/targetAnglesBL.npy', targetAnglesBL)
