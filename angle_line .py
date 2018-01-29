import numpy as np
from detect_angle_lida import line_angle
import random 
import matplotlib.pyplot as plt
import csv


num_angle = 0
log_angle = []

while True:

	x = random.randrange(1, 20)
	num_angle += 1

	if num_angle != 10:
		point = line_angle(x)
		log_angle.append(point)

	else:
		break

with open('angle_log.csv', 'w', newline='') as f:

	angle_writer = csv.writer(f)
	angle_writer.writerow(log_angle)

plt.plot(log_angle, 'r.-')
plt.ylabel("degree")
plt.xlabel("frame")
plt.grid()
plt.show()

print("angle : {}".format(log_angle))