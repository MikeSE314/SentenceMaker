# with is like your try .. finally block in this case
with open('names_02.txt', 'r') as file:
    # read a list of lines into data
    data = file.readlines()

list = []
add = True
for line in data:
	add = True
	for name in list:
		if line == name:
			add = False
	if add:
		list.append(line)

# and write everything back
with open('names_02.txt', 'w') as file:
	file.writelines(data)