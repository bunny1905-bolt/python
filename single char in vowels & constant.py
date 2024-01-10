

user_input=input("enter a single character:")
if len (user_input)==1:
    print(user_input)
else:
    print("please enter single character to continue")
    
character = input("Enter a character: ").lower()
if character in "aeiou":
   print("It's a vowel.")
else:
    print("It's a consonant.")