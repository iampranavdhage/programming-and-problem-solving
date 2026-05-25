a,b,c,d = map(int,input().split())
total = a+b+c+d

percentage = ((total)/4)
if percentage > 75:
	print(total)
	print(f"{percentage:.2f}")
	print("Distinction")
elif percentage >= 60 and percentage<75:
	print(total)
	print(f"{percentage:.2f}")
	print("First Division")
elif percentage >= 50 and percentage<60:
	print(total)
	print(f"{percentage:.2f}")
	print("Second Division")
elif percentage >= 40 and percentage<50:
	print(total)
	print(f"{percentage:.2f}")
	print("Third Division")
elif percentage <40 :
	print(total)
	print(f"{percentage:.2f}")
	print("Fail")
	
