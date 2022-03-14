import pyrosim.pyrosim as pyrosim

def create_World():
  pyrosim.Start_SDF("world.sdf")
  pyrosim.End()

def create_Robot():
  pyrosim.Start_URDF("body.urdf")
  pyrosim.Send_Cube(name="BackLeg", pos=[0,0,0.5] , size=[1,1,1])
  pyrosim.Send_Joint( name = "BackLeg_Torso" , parent= "BackLeg" , child = "Torso" ,type = "revolute", position = [0,0.5,1])
  pyrosim.Send_Cube(name="Torso", pos=[0,0.5,0.5] , size=[1,1,1])
  pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" ,type = "revolute", position = [0,1,0])
  pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,-0.5] , size=[1,1,1])
  pyrosim.End()


def Generate_Body():
  pyrosim.Start_URDF("body.urdf")
  pyrosim.Send_Cube(name="Torso", pos=[0, 1.5, 1.5], size=[1, 1, 1])
  pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, 1, 1])
  pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, -0.5], size=[1, 1, 1])
  pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0, 2, 1])
  pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, -0.5], size=[1, 1, 1])
  pyrosim.End()

def Generate_Brain():
  pyrosim.Start_NeuralNetwork("brain.nndf")
  pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
  pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
  pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
  pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
  pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
  # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=-.3)
  #   # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=3, weight=3)
  #   # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=4, weight=-.5)
  #   # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4, weight=4)
  pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=-4)
  pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=3, weight=3)
  pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=4, weight=-2)
  pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4, weight=1)
  pyrosim.End()


def main():
  create_World()
  Generate_Brain()
  Generate_Body()


main()
