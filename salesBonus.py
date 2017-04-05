"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))
while 0< sales < 1000:
    bouns = 0.1 * sales
    print(bouns)
    sales = float(input("Enter sales: $"))
    continue
while sales >= 1000:
    bouns = 0.15 * sales
    print (bouns)
    sales = float(input("Enter sales: $"))
    continue



