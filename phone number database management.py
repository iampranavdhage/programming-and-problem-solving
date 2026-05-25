n = int(input())
contacts = {}

for _ in range(n):
	operation = input().split()

	if operation [0] == "ADD":
		name = operation[1]
		phone = operation[2]
		contacts[name] = phone 
		
	elif operation[0] == "REMOVE":
		name = operation[1]
		if name in contacts:
			del contacts[name]

	elif operation[0] == "DISPLAY":
			if not contacts:
				print("No contacts")
			else:
				for name in sorted(contacts):
					print(f"{name}: {contacts[name]}")
