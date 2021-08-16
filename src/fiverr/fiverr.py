import matplotlib.pyplot as plt
import numpy as np


x1 = [0, 1, 2, 3, 4, 5, 6]
y1 = [0, 7, 4, 7, 2, 5, 8]


plt.plot(x1, y1, label = "impressions")

x2 = [0, 1, 2, 3, 4, 5, 6]
y2 = [0, 0, 3, 0, 0, 0, 1]

plt.plot(x2, y2, label = "clicks")

plt.xlabel('days')
plt.ylabel('no.')

plt.title('Fiverr gig')

plt.legend()

plt.show()
