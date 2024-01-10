string=input(("enter a letter:"))
if(string==string[::-1]):
    print("the string is palindrome")
else:
    print("the string is not palindrome")


#2nd method
string=input("enter a word or phase:")

reversed_string =''.join(reversed(string))
if string==reversed_string:
    print(f"{string} is a palindorme")
else:
    print("it is not a palindrome")