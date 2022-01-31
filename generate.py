import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")
i = 0
j = 0
l = 0
x = 1
y = 1
z = 1

while j < 5:
  while l < 5:
    while i < 10:
      pyrosim.Send_Cube(name="Box2", pos=[j,l,i + 0.5] , size=[x,y,z])
      x = x * .9
      y = y * .9
      z = z * .9
      i = i + 1
    i = 0
    x = 1
    y = 1
    z = 1
    l = l + 1
  l = 0
  j = j + 1
pyrosim.End()
