# Marilyn Saeteros 
# 11/17/2026

import statistics

days = [
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'
]

sales = [1250, 1480, 1100, 1650, 1850,
1420, 1700, 1300, 2100, 1950]

print ('DAILY SALES REPORT')
print('---------------------')

for index, day in enumerate (days):
   print(f'{day}: ${sales[index]:,.2f}')

# Task 2 : Calculate Descriptive Statistics 

print('\n DESCRIPTIVE STATISTICS CALCULATIONS')
print('------------------------------------')
# Mean(Average)
print(f'Mean: {statistics.mean(sales)}')
print(f'Median: {statistics.median(sales)}')
print(f'Mode: {statistics.mode(sales)}')
print(f'Standard deviatio: {statistics.stdev(sales):,.2f}')

print('\n')

print(f'Total sales is {sum(sales):,.2f}')
print(f'The lowest sales is {min(sales):,.2f}')
print(f'The highest sales amount is {max(sales):,.2f}')

# Task 3: Evaluate Sales Performance 
print('\n SALES PERFORMANCE')
print('----------------------')

for index, day in enumerate (days):
         
    if sales[index] >= 1800:
        print(f"{day}: ${sales[index]:,.2f} - Excellent")

    elif sales[index] >= 1500:
        print(f"{day}: ${sales[index]:,.2f} - Good")

    elif sales[index] >= 1200:
        print(f"{day}: ${sales[index]:,.2f} - Average")

    else:
        print(f"{day}: ${sales[index]:,.2f} - Needs Improvement")

# Task 4: Count Sales Performance Categories 

excellent = 0
good = 0
average = 0
needs_improvement = 0

for index, day in enumerate(days):
    if sales[index] >= 1800:
        excellent +=1
    elif sales[index] >= 1500:
        good += 1
    elif sales[index] >= 1200:
        average +=1 
    else:
        needs_improvement += 1

print('SALES CATEGORY SUMMARY')
print("------------------------")

print(f'Excellent sales days: {excellent}')
print(f'Good sales days: {good}')
print(f'Average slaes days: {average}')
print(f'Needs Improvment sales days: {needs_improvement}')

# Task 5: Identify Days That Meet the Sales Target 

target_days = 0

print("SALES TARGET REPORT")
print("-----------------")

for index, day in enumerate(days):

    if sales[index] >= 1500:
        print(f"{day}: ${sales[index]:,.2f}")
        target_days += 1

print("-----------------")
print(f"Total days that met the target: {target_days}")

# Task 6: Generate a Final Analysis 
         



   
