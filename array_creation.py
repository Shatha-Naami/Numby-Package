import numpy as np

aList = np.array([[1, 3, 7], [9, 0, 3]])
print(aList)

# To Get Number Of Dimensions of a list
numOfDimensions = aList.ndim
print(numOfDimensions)

# length of each dimension
print(aList.shape)

# ZERO List
z = np.zeros((2, 2))
print(z)

# One List
o = np.ones((2, 4))
print(o)

# array of every even number from ten (inclusive) to fifty (exclusive)
ourList = np.arange(10, 50, 3)
print(ourList)

# Other Function Maybe Important
np.random.rand(2, 5)  # -> generate an array with random numbers from 2 to 5
np.linspace(0, 2, 15)  # -> 15 numbers from 0 (inclusive) to 2 (inclusive)
