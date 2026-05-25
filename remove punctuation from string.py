# Type Content here...
text = input()
result =""
for i in text:
	if i.isalnum() or i.isspace():
		result += i

print(result)
