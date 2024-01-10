#concise way to create lists
squares=[x**2 for x in range(6)]
print(squares)

even=[x for x in range(10) if x%2==0]
print(even)

results=['pass' if score>=60 else'fail' for score in [75,90,95,60]]
print(results)

names=['Jimmy','John','Jim']
name_length=[len(name) for name in names ]
print(name_length)