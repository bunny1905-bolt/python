#Discount calcuation
purchas_amount=input("enter purchas amount")
member=input("are you member?(yes/no)").lower()
if purchas_amount >100 and member=="yes":
   discount=10
   total =purchas_amount - discount
   print(f"the total amount is :{total}")
else:
    print("the total cost atten discount is :")   


