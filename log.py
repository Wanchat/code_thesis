import csv
import matplotlib.pyplot as plt

def plot_log(log):
    plt.plot(log, 'r-')
    plt.plot(log, 'g.')
    plt.ylabel("degree")
    plt.xlabel("frame")
    plt.grid()
    plt.show()

def csv_log(log, name_file):
    with open('{}.csv'.format(name_file), 'w', newline='') as f:
        angle_writer = csv.writer(f)
        angle_writer.writerow(log)

