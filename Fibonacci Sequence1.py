#Fibonacci Sequence
a=0
b=1
R=int(input("give the range:"))
for i in range(1,R+1):
    c=a+b
    a=b
    b=c
    print(f"the fabincci series of range :{c}")