print("Compound Interest Calculate")
print("-" * 40)

principal = 0
rate = 0
time =0

while principal <= 0:
    principal = int(input("Enter the Principal: "))
    if principal <= 0:
        print("Principal should not be less than or equal to zero")
while rate <= 0:
    rate = float(input("Enter the rate: "))
    if rate <= 0:
        print("Rate should not be less than or equal to zero")
while time <= 0:
    time = int(input("Enter the year:"))
    if principal <= 0:
        print("Years should not be less than or equal to zero")

compound_interest = principal * (1 + rate/100)**time
interest = compound_interest - principal

print("Results")
print("-" * 20)
print("\n")
print(f"Principal is {principal}")
print(f"Rate is {rate}")
print(f"The number of years {time}")
print(f"Compound Interest is {round(interest,2)}")
