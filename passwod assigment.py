int_string=input("enter the password:")
num_alp=0
num_digit=0
num_space=0
for entries in int_string:
    if entries.isalpha():
        num_alp+=1
    elif entries.isdigit():
        num_digit+=1
    elif entries.isspace():
        num_space+=1
        print(f"num of alphe:{num_alp}")
        print(f"num of digit:{num_digit}")
        print(f"no of space:{num_space}")