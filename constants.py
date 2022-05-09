import numpy as np

#front leg sensor values
amplitudeFL = np.pi/4
frequencyFL = 20
phaseOffsetFL = np.pi/4

#backleg sensor values
amplitudeBL = np.pi/4
frequencyBL = 20
phaseOffsetBL = 0

minRange = 0

maxRange = 2 * np.pi

loop = 1000

y = np.linspace(0,2 * np.pi, num=1000)
targetAngles = np.sin(y)

numberOfGenerations = 10

defaultFit = -0.018336037653125914

numSensorNeurons = 8

numMotorNeurons = 8

populationSize = 10

motorJointRange = 0.2

rownum = 0

colnum = 0

a = 0

matrix = []

rowavg = 0

row1 = []
row2 = []
row3 = []
row4 = []
row5 = []
row6 = []
row7 = []
row8 = []
row9 = []
row10 = []