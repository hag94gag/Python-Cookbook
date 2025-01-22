country = input("Input Your Country")
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

if country in countries:
    print("Your Country Eligible For Discount And The Price After Discount Is $",str(price-discount))
else:
    print("Your Country Not Eligible For Discount And The Price Is $",str(price))

# Needed Output
"Your Country Eligible For Discount And The Price After Discount Is $70" # Egypt Example
"Your Country Not Eligible For Discount And The Price Is $" # Ghana Example