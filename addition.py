num1 = input("what's number 1?\n")
if num1.isnumeric() != True:
    num1 = input("no dumbass, just use numbers. You know, 12345678? Numbnuts...\n")
num2 = input("what's number 2?\n")
if num2.isnumeric() != True:
    num2 = input("Jesus christ you're thick...\n")
num3 = float(num1) + float(num2)
print(num3)