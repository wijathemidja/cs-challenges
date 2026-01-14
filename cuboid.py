a = float(input("Please enter length \n"))
b = float(input("Please enter width \n"))
c = float(input("Please enter height \n"))
vol = a*b*c
sa = (2*a*b)+(2*a*c)+(2*b*c)
edges = 4*a+4*b+4*c
print("Volume = ",vol,"Surface Area = ",sa,"Edge length = ", edges)