#armstrong number checker
num=int(input("enter the number:"))
num_digit=len(str(num))
sum_of_cubes=0
temp=num

while temp>0:
    digit = temp%10
    sum_of_cubes+=digit**num_digit
    temp//=10

if num==sum_of_cubes:
      print(f"{num} is armstrong num")
else:
     print(f"{num} is not armstrong num")