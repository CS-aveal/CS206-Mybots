import pyrosim.pyrosim as pyrosim

def create_World():
  pyrosim.Start_SDF("world.sdf")
  pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[1,1,1])
  pyrosim.End()

def create_Robot():
  pyrosim.Start_URDF("body.urdf")
  pyrosim.Send_Cube(name="Torso", pos=[0,0,0.5] , size=[1,1,1])
  pyrosim.Send_Joint( name = "Torso_Leg" , parent= "Torso" , child = "Leg" ,type = "revolute", position = [0,0,1])
  pyrosim.Send_Cube(name="Leg", pos=[0,0,0.5] , size=[1,1,1])
  pyrosim.End()



def main():
  create_Robot()
  create_World()

main()
