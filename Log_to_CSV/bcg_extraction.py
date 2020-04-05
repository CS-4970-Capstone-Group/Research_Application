import sys
import os
import os.path
import csv
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
from scipy import interpolate

directory = os.path.dirname(__file__)
for filename in os.listdir(directory):
    if filename.endswith(".CSV"):
        outfilename = filename + ".csv"

    with open(outfilename, "r") as file:
        buffer = csv.reader(file)
        data_list = list(buffer)

    bcg_list = []
    time_list = []

    for i in range(len(data_list)):
        if (data_list[i][1] != ''):
            bcg_list.append(data_list[i][1])
            time_list.append(data_list[i][0])
    for j in range(3):
        bcg_list.remove(bcg_list[0])
        time_list.remove(time_list[0])

    for k in range(len(bcg_list)):
        if bcg_list[k] == '':
            bcg_list[k] = 0

    bcg_arr = np.array(bcg_list, dtype="double")
    time_arr = np.array(time_list, dtype="double")
    print(bcg_arr.size)
    xnew = np.arange(0, 30, .001)
    interpolation = interpolate.interp1d(time_arr, bcg_arr, fill_value="extrapolate", kind='cubic')
    x = np.linspace(0, 30)
    results = interpolation(xnew)
    np.savetxt(filename + "_bcg" + ".csv", results)
    file.close()
