import numpy as np
from csv_helper import CSVHelper

c_matrix = np.zeros((2001,2001), dtype=int)
print(c_matrix.shape)

for i in range(9):
    list_clasification = CSVHelper.load_csv("k"+str(i+2)+".csv")
    for x, val1 in enumerate(list_clasification):
        for y, val2 in enumerate(list_clasification):
            if val1 == val2:
                c_matrix[x][y] += 1

print(c_matrix)
np.savetxt("conse.csv", c_matrix, fmt='%i',delimiter=",")
