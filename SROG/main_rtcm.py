# importing csv module
import csv
from datetime import datetime, timedelta
import numpy as np
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox
import pandas as pd
import csv
import matplotlib.pyplot as plt
from scipy.stats import sem
from sklearn.metrics import mean_squared_error


# csv file name
filename = "BMHR21020352C_05-07-2021_15-46-00.gps"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    # extracting field names through first row
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

#  printing first 5 rows
print('\nFirst 5 rows are:\n')
new_pos = list()

for row in rows:
    # parsing each column of a row
    new_pos.append(float(row[13]) + float(row[14]))
    print(float(row[13]) + float(row[14]))
    # for col in row:
    #     print(col(10))
    # print('\n')

# Given values
Y_true = new_pos

# calculated values
Y_pred = 2.17*(np.ones(len(new_pos)))

# Calculation of Mean Squared Error (MSE)
print(mean_squared_error(Y_true, Y_pred))

print(len(new_pos))
print(sem(new_pos))
time = list(range(0, len(new_pos), 1))
plt.figure()
plt.plot(time, new_pos)
plt.axis([0, 1822, 1.5, 2.5])
plt.grid()
plt.show()