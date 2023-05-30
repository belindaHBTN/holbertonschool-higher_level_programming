tall = input("Enter the tall of the tree: ")

tall = int(tall)
i = 0
hash = 1
space = tall
while i < tall:
	for j in range(1, space):
		print(" ", end = "")
	for k in range(1, hash + 1):
		print("#", end = "")
	print()
	space = space - 1
	hash = hash + 2
	i = i + 1
for n in range(1, tall):
	print(" ", end = "")
print("#")
