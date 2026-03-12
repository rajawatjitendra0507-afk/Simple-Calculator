Num_1 = int(input("Enter The First Number: "))
Operation = input("Enter The Operand : +-*/**: ")
Num_2 = int(input("Enter The Second Number: "))

if Operation =="+" : 
    results = Num_1+Num_2
elif Operation == "-":
    results = Num_1 - Num_2
elif Operation == "*":
    results = Num_1*Num_2
elif Operation == "/":
    results = Num_1/Num_2
elif Operation == "**" and Num_1==Num_2:
    results = Num_1**Num_2
else :
    print("enter valid inputs")

print(results)
