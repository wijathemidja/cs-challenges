input1 = float(input("enter first number"))
input2 = float(input("enter second number"))
input3 = float(input("enter third number"))
if ((input1 > input2) & (input1 > input3)):
    c = input1
    a = input2
    b = input3
elif ((input2 > input1) & (input2 > input3)):
    c = input2
    a = input1
    b = input3
else:
    c = input3
    

