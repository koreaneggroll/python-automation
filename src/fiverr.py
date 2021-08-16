import matplotlib.pyplot as plt
import numpy as np


x1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y1 = [0, 12, 4, 2, 5, 1, 5, 17, 4]


plt.plot(x1, y1, label = "impressions")

x2 = [0, 1, 2, 3, 4, 5, 6]
y2 = [0, 2, 0, 0, 0, 1, 0 ]

plt.plot(x2, y2, label = "clicks")

plt.xlabel('days')
plt.ylabel('no.')

plt.title('Fiverr gig')

plt.legend()

plt.show()
