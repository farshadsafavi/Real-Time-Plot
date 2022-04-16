import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

def animate(i):
	data = pd.read_csv('data.csv')
	x = data['x_value']
	y1 = data['total_1']
	y2 = data['total_2']

	plt.cla()

	plt.plot(x, y1, label= 'Power Consumption')
	plt.plot(x, y2, label= 'Inference')
	plt.fill_between(y2.index, y2, color='red', alpha=0.3)
	plt.xlabel("Frames")
	plt.ylabel("Power")

	# plt.legend(loc = 'upper left')
	plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.plot(x_vals, y_vals)
plt.tight_layout()
plt.show()



