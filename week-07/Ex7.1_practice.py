# 11/23/2026
# NumPy Practice 

import numpy as np 

sales_data = np.array([
    [
            [1200,1500,180], # Store 1 , Month 1
            [2000,2200,2500]  # Store 1, Month 2
    ],
    [
            [1400,1600,1900], # Store 2 , Month 1
            [2100,2300,2600]  # Store 2 , Month 2 
    ]
            
])

# Task 2 Display the 3D array 
print('Sales Array:')
print(sales_data)

# Task 3 Using np.nditer in for loop

for sales in np.nditer(sales_data):
    print(sales)

# Task 4 Three Nested Loop

for stores in range(2):  # layer 
    for month in range(2):  # row 
        for records in range(3): # column 
            print(sales_data[stores, month, records])

# Task 5 Total Sales

total_sales = 0 

for value in np.nditer(sales_data):
    total_sales += value

print('Total sales:', total_sales)

# Task 6 Calcualte Average Sales

total_sales = 0
count = 0

for value in np.nditer(sales):
    total_sales += value
    count += 1

average = total_sales / count

print("Number of Records:", count)
print(f"Average Sales: ${average:.2f}")

# Task 7: Identify the Highest Sales Amount

highest_sales = 0

for value in np.nditer(sales):
    if value > highest_sales:
        highest_sales = value

print("Highest Sales Amount:", highest_sales)