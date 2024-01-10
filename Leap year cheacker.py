#leap year checker
start_year=int(input("enter the start year:"))
end_year=int(input("enter the end year:"))

leap_year=[]
for year in range (start_year,end_year+1):
    if (year %4==0 and year % 100!=0) or (year%400==0):
        leap_year.append(year)

if len(leap_year)>0:
    print(f"the leap year between {start_year} and {end_year}:")
    print(leap_year)
else:
    print (f"there sre no leap year betwwen{start_year} and {end_year}")