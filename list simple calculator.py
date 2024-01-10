operaction=[]
while True:
    print("select the option:")
    print("1.Add")
    print("2.subtraction")
    print("3.Division")
    print("4.Multply")
    select=float(input("select your option:"))
    if select==1:
        num1=float(input("Enter your first number:"))
        num2=float(input("Enter your secound number:"))
        result=num1+num2
        operaction.append(f"(num1)+(num2)=(result)")
        print(f"\nresult: {num1}+{num2}={result}")
    elif select==2:
        num1=float(input("Enter your first number:"))
        num2=float(input("Enter your secound number:"))
        result=num1-num2
        operaction.append(f"(num1)-(num2)=(result)")
        print(f"\nresult: {num1}-{num2}={result}")
    elif select==3:
        num1=float(input("Enter your first number:"))
        num2=float(input("Enter your secound number:"))
        if num2!=0:
            result=num1/num2
            operaction.append(f"(num1)/(num2)=(result)")
            print(f"\nresult: {num1}/{num2}={result}")
    elif select==4:
        num1=float(input("Enter your first number:"))
        num2=float(input("Enter your secound number:"))
        result=num1*num2
        operaction.append(f"(num1)*(num2)=(result)")
        print(f"\nresult: {num1}*{num2}={result}")
    else:
        print(operaction)