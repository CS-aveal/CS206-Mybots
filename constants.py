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

populationSize = 10