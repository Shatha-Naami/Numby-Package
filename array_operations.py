import numpy as np
from PIL import Image
from IPython.display import display

# Let's create a couple of arrays
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

# Now let's look at a minus b
c = a - b
print(c)

# And let's look at a times b
d = a * b
print(d)

# Example
# array of typical Ann Arbor winter fahrenheit values
fahrenheit = np.array([0, -10, -5, -15, 0])
celcius = (fahrenheit - 31) * (5 / 9)
print(celcius)
# Other Process
print(celcius > -20)
print(celcius % 2 == 0)

#################################

im = Image.open('datasets/person.tiff')
display(im)

myArray = np.array(im)
print(myArray)
print(myArray.shape)

# Let's create an array the same shape
mask = np.full(myArray.shape, 255)
print(mask)

# PROCESS
# Now let's subtract that from the modified array
modified_array = myArray - mask

# And let's convert all the negative values to positive values
modified_array = modified_array * -1

# And as a last step, let's tell numpy to set the value of the datatype correctly
modified_array = modified_array.astype(np.uint8)
print(modified_array)
