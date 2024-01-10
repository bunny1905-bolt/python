password=input("enter the strong password:")
numalpha=0
numdigit=0
numupper=0
numlower=0
specialcharacter=0
for  enter in password:
    if enter.isalpha():
        if enter.isupper():
            numupper+=1
        elif enter.islower():
            numlower+=1
    elif enter.isdigit():
        numdigit+=1
    
    else:
       specialcharacter+=1
result = numalpha + numdigit + numupper
if (numalpha>=1 and numdigit>=1 and numupper>=1):
    print ("password is set") 
else:
    print("enter the password ")