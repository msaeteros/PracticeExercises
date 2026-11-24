# Marilyn Saeteros 
# 11/23/2026

import numpy as np 

# This is a 2d array becaue it had rows and columns

# Create a 2D array with 3 rows and 4 columns 
sales_data = np.array([
    [150,200,250,300],
    [175,225,275,325],
    [130,240,290,340]
])

# Display the 2D array 
print('sales Data:')
print(sales_data)

# Display the number of dimensions
print('Number of dimensions:',sales_data.ndim)

# Display the shows shape
print('Array shape:', sales_data.shape)

# Display the number if elements 
print('Number of elements', sales_data.size)