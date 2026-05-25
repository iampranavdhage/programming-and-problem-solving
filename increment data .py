# Type Content here...
day = int(input())
month = int(input())
year = int(input())
if year<=0:
	print("Invalid Date")
elif month<1 and month>12:
	print("Invalid Date")
else:
	leap=False
	if(year%400==0)or(year%4==0 and year%100!=0):
		leap=True
if month in {1,3,5,7,8,10,12}:
	max_day=31
elif month in {4,6,9,11}:
	max_day=30
elif month==2:
	if leap:
		max_day =29
	else:
		max_day=28
if day<1 or day>max_day:
	print("Invalid Date")
else:
	day=day+1
	if day>max_day:
		day=1
		month=month+1
		if month>12:
			month=1
			year=year+1
	print(f"{day:02d}-{month:02d}-{year}")



