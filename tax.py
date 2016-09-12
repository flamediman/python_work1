income = int(input("Введите доход "))

if income < 35000:
	tax_1 = (income / 100) * 15
elif income <= 100000:
    tax_1 = (income / 100) * 25
elif income > 100000:
    tax_1 = (income / 100) * 35

if income > 50000:
    tax_2 = (income / 100) * 5
else:
    tax_2 = 0

tax = tax_1 + tax_2
print(tax)
