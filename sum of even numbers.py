start=int(input("start the range:"))
end=int(input("end the range:"))
sum_of_even=0
sum_of_odd=0
for num in range(start,end+1):
    if num %2==0:
        sum_of_even +=num
    else:
        sum_of_odd +=num
print(f"the sum is{sum_of_even}")
print(f"the sum is{sum_of_odd}")


