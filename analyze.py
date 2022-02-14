import matplotlib.pyplot as plt
import numpy

backLegSensorValues = numpy.load('./data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('./data/frontLegSensorValues.npy')

plt.plot(backLegSensorValues, label='Back Leg Sensor', linewidth=5)
plt.plot(frontLegSensorValues, label='Front Leg Sensor')
plt.legend()
plt.show()

