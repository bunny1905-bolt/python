limit = 1000
f_s=[0,1]
while True:
    next_number=f_s[-1] + f_s[-2]
    if next_number >limit:
        break
    f_s +=[next_number]

print("f_s")
print(f_s)