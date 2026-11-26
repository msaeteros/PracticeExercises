# Bean & Brew - Week 7, Module 1
import numpy as np
print('NumPy is ready!')

cups = np.array([
    [120,135,150],
    [98,110,104]
    
])


for row in cups:
    print(row)

for row in cups:
    for value in row:
        print(value) 

seaport = np.array([[143, 128, 161]])

# Joining Stores
all_stores = np.concatenate((cups, seaport))
print(all_stores)

thu_fri = np.array([[140, 172],
                    [101, 95],
                    [150, 166]])

week = np.concatenate((all_stores, thu_fri), axis=1)

print(week)

mon = np.array([120, 98, 143])
tue = np.array([135, 110, 128])

print(np.hstack((mon, tue)))

print(np.vstack((mon, tue)))

print(np.stack((mon, tue), axis=1))

# Task 1.3: Predict, then run
seaport_week = np.array([143, 128, 161, np.nan, 166])

print(seaport_week)

print(seaport_week.dtype)

print(np.sum(seaport_week))

seaport_none = np.array([143, 128, 161, None, 166])
print(seaport_none.dtype)

print(seaport_week + 1)

days = np.array([140, 152, 138, 160, 171, 199, 185])
halves = np.array_split(days, 2)

print(halves)

# Print only the second half
print(halves[1])

# Split the weekly table into 3 parts (one per store)
by_store = np.array_split(week, 3)

# Print the third part (Seaport)
print(by_store[2])

# Creating Target 

TARGET = 150

# Find positions of days below the target
print(np.where(days < TARGET))

# Label each day as below or met
print(np.where(days < TARGET, 'below', 'met'))

# Add 15 cups to days below the target
print(np.where(days < TARGET, days + 15, days))

# Step 1: Sort days from smallest to largest
print(np.sort(days))

# Step 2: Check whether the original days array changed
print(days)

# Step 3: Predict how text numbers will be sorted
# Prediction: '100', '120', '9', '95'
codes = np.array(['95', '100', '9', '120'])
print(np.sort(codes))

# Step 4: Sort the weekly table
print(np.sort(week))

# Step 5: Create a Boolean mask for busy days
busy = days > 160
print(busy)

# Step 6: Use the mask to show only busy days
print(days[busy])

# Set the random seed
np.random.seed(7)

# Generate 2 rows and 5 columns of random integers
test_orders = np.random.randint(1, 6, size=(2, 5))
print(test_orders)

# Generate 2 rows and 3 columns of random decimal numbers
tips = np.random.rand(2, 3)
print(tips)

drink_sizes = np.random.choice(
    ['small', 'medium', 'large'],
    size=10,
    p=[0.2, 0.5, 0.3]
)
print(drink_sizes)

# Filter and print only large drinks
large_orders = drink_sizes[drink_sizes == 'large']
print(large_orders)

# Pick one random drink size
print(np.random.choice(['small', 'medium', 'large']))

# Set the random seed
np.random.seed(7)

# Generate 1,000 customer wait times
waits = np.random.normal(loc=4, scale=1, size=1000)

# Calculate the mean, rounded to 2 decimals
print(np.round(np.mean(waits), 2))

# Calculate the standard deviation, rounded to 2 decimals
print(np.round(np.std(waits), 2))

# Find waits within 1 minute of 4 minutes
within_1 = waits[np.absolute(waits - 4) < 1]
print(len(within_1))

# Find waits within 2 minutes of 4 minutes
within_2 = waits[np.absolute(waits - 4) < 2]
print(len(within_2))

# Task 3.1: Shuffle the barista rota
np.random.seed(7)

# Create an array containing the five baristas
baristas = np.array(['Ana', 'Ben', 'Cho', 'Dev', 'Eli'])

# Create and print a shuffled copy (original stays unchanged)
print(np.random.permutation(baristas))

# Print the original array to check that it has not changed
print(baristas)

# Shuffle the original array itself
np.random.shuffle(baristas)

# Print the shuffled original array
print(baristas)

# Task 3.3: Predict, then run — five ways to round
changes = np.array([-2.7, -0.5, 0.5, 1.5, 2.5, 3.46])

# Remove decimal places (towards zero)
print(np.trunc(changes))

# Same as trunc()
print(np.fix(changes))


print(np.floor(changes))


print(np.ceil(changes))

print(np.round(changes))


print(np.round(changes, 1))

# Task 3.4: Totals per store, per day and running totals

print(week)

# Calculate the grand total of all sales
print(np.sum(week))

# Calculate the total for each store (each row)
print(np.sum(week, axis=1))

# Calculate the total for each day (each column)
print(np.sum(week, axis=0))

# Calculate the running total for the days
print(np.cumsum(days))

# Task 3.5: Growth and day-to-day change

growth = np.array([1.10, 1.05, 1.20])

# Calculate the total growth
print(np.round(np.prod(growth), 3))

# Calculate the running growth
print(np.round(np.cumprod(growth), 3))

# Calculate the daily changes in sales
print(np.diff(days))

# Calculate the changes between the daily changes
print(np.diff(days, n=2))


