#sum of First N natural number 
n=int(input("enter number(N)"))
sum_of_number=0
for i in range (1,n+1):
    sum_of_number+=i
    print(f"the sum of first (n) natural number is: {sum_of_number}")