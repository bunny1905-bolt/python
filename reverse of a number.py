#reverse of a number
num=int(input("Enter the number:"))
reversed_num = 0

while num > 0:
    digit = num%10
    reversed_num = (reversed_num * 10) + digit
    num = num//10
    print(reversed_num)
