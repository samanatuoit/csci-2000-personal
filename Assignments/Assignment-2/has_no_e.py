def has_no_e(input):
	for x in input:
		
		if x == 'e':
			return False
	return True

reader = open("gadsby_stripped.txt")
data = reader.read()
reader.close()

print(has_no_e(data))

