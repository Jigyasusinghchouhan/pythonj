principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (%): "))
years = int(input("Enter the number of years: "))

balance = principal * (1 + (rate/100)) ** years

print("The balance after", years, "years is:", balance)
