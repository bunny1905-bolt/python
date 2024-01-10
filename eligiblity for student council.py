grade = int(input("Enter your grade (9-12): "))
disciplinary_record = input("Do you have a clean disciplinary record? (yes/no):").lower()
if grade >= 9 and grade <= 12 and disciplinary_record == "yes":
    print("You are eligible to run for the student council.")
else:
   print("You are not eligible to run for the student council.")