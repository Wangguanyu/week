print("profuct1: $10, product2: $36, product3: $27")
number1 =int(input("The number of product1 is:"))
while number1< 0:
    print("Invalid number of items!")
    number1 =int(input("The number of product1 is:"))
    continue
number2 =int(input("The number of product2 is:"))
while number2< 0:
    print("Invalid number of items!")
    number2 =int(input("The number of product2 is:"))
    continue
number3 =int(input("The number of product3 is:"))
while number3< 0:
    print("Invalid number of items!")
    number3 =int(input("The number of product3 is:"))
    continue
total= number1*10 + number2*36 + number3*27
if total >100:
    realtotal = total * 0.9
    print(realtotal)
if total <=100:
    realtotal =total
    print(realtotal)
