import csv

def csv_log(log, name_file):
    with open('{}.csv'.format(name_file), 'w', newline='') as f:
        angle_writer = csv.writer(f)
        angle_writer.writerow(log)

if __name__ == '__main__':
    csv_log([1, 2, 3],"test")
