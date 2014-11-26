from random import randint
 
#gram = randint(0,3482)

pea_i = open('nam.txt')
pepper_o = open('names_01.txt', "w")

potato = 0
for row in pea_i:
	potato = 0
	for cheese in range(len(row)):
		if row[cheese] == '"' and potato == 0:
			pepper_o.write(row[:cheese] + "\n")
			potato += 1
pea_i.close()
pepper_o.close()

'''import string

print string.ascii_letters
print "nope" in string.ascii_letters'''