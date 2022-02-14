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
for x in range(1000):
  time.sleep(1/60)
  print(x)
  p.stepSimulation()
  
  #sensorCode
  
  backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
  frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
  
  #motorCode

  pyrosim.Set_Motor_For_Joint(
  bodyIndex = robotId,
  jointName = "BackLeg_Torso",
  controlMode = p.POSITION_CONTROL,
  targetPosition = 0.0,
  maxForce = 500)

p.disconnect()
np.save('./data/backLegSensorValues.npy', backLegSensorValues)
np.save('./data/frontLegSensorValues.npy', frontLegSensorValues)
