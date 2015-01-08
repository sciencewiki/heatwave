import find_heat_waves as fhw
import matplotlib.pyplot as plt
import matplotlib.collections as col
import numpy as np

year = 30
threshold = 97.5
directory = '/Users/charliewhite/Documents/Year4/Thesis/climdata/ERAInterim/dailymean/t/summersurface/'
temps, time, plev, lat, lon = fhw.import_temps(directory)
heatwavedays = fhw.find_heat_waves(temps,threshold,year)
avtemp = np.zeros(time.size)
for i in range(time.size):
    avtemp[i] = np.average(temps[:,i])
yearavtemp = np.zeros(time.size)
for i in range(time.size):
    yearavtemp[i] = np.average(temps[year][i])

fig, ax = plt.subplots(1,1)
ax.plot(time,yearavtemp,'b')
ax.plot(time,avtemp,'g')
collection = col.BrokenBarHCollection.span_where(time,where=heatwavedays,
        ymin=min(yearavtemp),ymax=max(yearavtemp),facecolor='red',alpha=0.5)
ax.add_collection(collection)

plt.show()
        