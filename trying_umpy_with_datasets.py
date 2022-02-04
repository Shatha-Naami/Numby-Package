import numpy as np

wines = np.genfromtxt('datasets/winequality-red.csv', delimiter=';', skip_header=1)
print(wines)

# So all rows combined but only the first column from them would be
print("one integer 0 for slicing: ", wines[:, 0])
print("0 to 1 for slicing: \n", wines[:, 0:1])

# the aggregation functions on this data.
print(wines[:, -1].mean())
