#age validity check
age=float(input("please enter your age:"))
if age>100 and age<0:
    print("invalid age")
else:
    print("your age is valid")