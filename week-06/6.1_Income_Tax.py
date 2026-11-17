# Mailyn Saeteros 
# 11/16/2026 
# Income Tax Calculator 

# Business Rules 

tax_rate = 0.20
Standard_deduction = 10000
Dependent_dedcution= 2000

# Print Title 

print('INCOME TAX CALCULATOR')
print('-----------------------')

# Inputs 
Gross_income = float(input('Enter your annual gross income: '))
Number_of_Dependents = int(input('Enter the number of dependents: '))

Dependent_dedcutions = Dependent_dedcution * Number_of_Dependents
Total_Deductions = Standard_deduction + Dependent_dedcutions
Taxable_income = Gross_income - Total_Deductions 
Estimated_income_tax = Taxable_income * tax_rate

print("\n INCOME TAX SUMMARY" )
print ('----------------------')

print(f'Gross income: $ {Gross_income:,.2f}')
print(f"Standard Deduction: ${Standard_deduction:,.2f}")
print(f"Dependent Deductions: ${Dependent_dedcution:,.2f}")
print(f"Total Deductions: ${Total_Deductions:,.2f}")
print(f"Taxable Income: ${Taxable_income:,.2f}")
print(f'Tax Rate: {tax_rate} %')
print(f"Estimated Income Tax: ${Estimated_income_tax:,.2f}")


