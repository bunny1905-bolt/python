my=[12,3,54,67,100,30,97]
max=my[0]
smallest=my[0]
if smallest<max:
    max,smallest=smallest,max
for num in my[1:]:
    if num<max:
        smallest=max
        max=num
    elif max>num>smallest:
        smallest=num
print(smallest)