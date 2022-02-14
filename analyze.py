import matplotlib.pyplot as plt
import numpy

backLegSensorValues = numpy.load('./data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('./data/frontLegSensorValues.npy')

targetAngles = numpy.load('./data/targetAngles.npy')

targetAnglesBL = numpy.load('./data/targetAnglesBL.npy')
targetAnglesFL = numpy.load('./data/targetAnglesFL.npy')


#plt.plot(targetAngles, label='Target Angles', linewidth=5)
#plt.plot(frontLegSensorValues, label='Front Leg Sensor')
plt.plot(targetAnglesFL, label='Target Angles Front')
plt.plot(targetAnglesBL, label='Target Angles Back', linewidth=5)
plt.legend()
plt.show()

