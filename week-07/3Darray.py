import numpy as np 

# Create a 3D array with NumPy 
sales = np.array([
    [[100,200,300],
    [400,500,600]],

    [[700,800,900],
     [1000,1100,1200]]
])

# Display the 3D array 
print('3D NumPy Array:')
print(sales)

# Display the shape of the array 
print('\nArray Shape:', sales.shape)

# Display the number of dimensions 
print('\nElemet at position [0,1,2]:', sales[0,1,2])