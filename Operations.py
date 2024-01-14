# Initialize an empty list to store operations
operations = []

while True:
    print("\n===== Simple Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Display Operations")
    print("6. Quit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        operations.append(f"{num1} + {num2} = {result}")
        print(f"\nResult: {num1} + {num2} = {result}")
    elif choice == '2':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 - num2
        operations.append(f"{num1} - {num2} = {result}")
        print(f"\nResult: {num1} - {num2} = {result}")
    elif choice == '3':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 * num2
        operations.append(f"{num1} * {num2} = {result}")
        print(f"\nResult: {num1} * {num2} = {result}")
    elif choice == '4':
        num1 = float(input("Enter the dividend: "))
        num2 = float(input("Enter the divisor: "))
        if num2 != 0:
            result = num1 / num2
            operations.append(f"{num1} / {num2} = {result}")
            print(f"\nResult: {num1} / {num2} = {result}")
        else:
            print("\nError: Division by zero")
    elif choice == '5':
        print("\n===== Operations =====")
        if not operations:
            print("No operations performed yet.")
        else:
            count=1
            for operation in operations:
                print(f"{count}.{operation}")
                count+=1
        print("=====================")
    elif choice == '6':
        break
    else:
        print("\nInvalid choice. Please try again.")
