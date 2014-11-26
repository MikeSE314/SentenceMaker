import random
import sys
from random import randint

currentWord = ""
helperString = ""
T = True
F = False


def party():
	global T, F
	
	#sentence = "The " + adj(F) + " " + noun(F) + " did " + verb(F) + " " + adv(F) + "."
	sentence = adj(True) + " " + noun(False, T) + " " + verb(F) + ", while " + adj(F) + " " + noun(F, T) + " " + verb(F) + "." 
	return sentence
	
def titles():
	names = ""
	decider = randint(0,4)
	if decider == 4 or decider == 3:
		names = name()
		names += ", the "
		names += verb()
		if not names[-1] == "e":
			names += "e"
		names += "r"
	elif decider == 2 or decider == 1:
		names = name()
		names += ", the "
		names += adj()
	else:
		names = name()
		names += ", the "
		names += noun()
	return names

def name():
	global helperString
	helperString = ""
	iname = open("name.txt")
	rname = randint(1, 2000)#2000
	#print len(iname)
	current_row_name = 0
	for row_name in iname:
		current_row_name += 1
		if current_row_name == rname:
			iname.close()
			currentWord = row_name[:len(row_name) - 1]
			for letter in currentWord:
				if letter == "_":
					helperString += " "
				else:
					helperString += letter
			return helperString

def adj(c):
	global helperString
	helperString = ""
	iadj = open("adj.txt")
	radj = randint(1, 21527)#21527
	current_row_adj = 0
	for row_adj in iadj:
		current_row_adj += 1
		if current_row_adj == radj:
			iadj.close()
			currentWord = row_adj[:len(row_adj) - 1]
			if c:
				helperString += currentWord[0].upper()
				currentWord = currentWord[1:]
			for letter in currentWord:
				if letter == "_":
					helperString += " "
				else:
					helperString += letter
			return helperString



location_of_nouns = "noun.txt"#"sentence_maker/noun.txt"

def noun(c, p):
	global helperString
	helperString = ""
	inoun = open(location_of_nouns)
	rnoun = randint(1, 112170)#117723
	current_row_noun = 0
	for row_noun in inoun:
		current_row_noun += 1
		if current_row_noun == rnoun:
			inoun.close()
			currentWord = row_noun[:len(row_noun) - 1]
			if c:
				helperString += currentWord[0].upper()
				currentWord = currentWord[1:]
			for letter in currentWord:
				if letter == "_":
					helperString += " "
				else:
					helperString += letter
			if p:
				if helperString.endswith("s"):
					helperString += "e"
				if helperString.endswith("y"):
					if not helperString.endswith("ey"):
						helperString = helperString[0:-1] + "ie"
				helperString += "s"
			return helperString

def verb(c):
	global helperString
	helperString = ""
	iverb = open("verb.txt")
	rverb = randint(1, 11529)#11529
	current_row_verb = 0
	for row_verb in iverb:
		current_row_verb += 1
		if current_row_verb == rverb:
			iverb.close()
			currentWord = row_verb[:len(row_verb) - 1]
			if c:
				helperString += currentWord[0].upper()
				currentWord = currentWord[1:]
			for letter in currentWord:
				if letter == "_":
					helperString += " "
				else:
					helperString += letter
			return helperString

def adv(c):
	global helperString
	helperString = ""
	iadv = open("adv.txt")
	radv = randint(1, 4481)#4481
	current_row_adv = 0
	for row_adv in iadv:
		current_row_adv += 1
		if current_row_adv == radv:	
			iadv.close()
			currentWord = row_adv[:len(row_adv) - 1]
			if c:
				helperString += currentWord[0].upper()
				currentWord = currentWord[1:]
			for letter in currentWord:
				if letter == "_":
					helperString += " "
				else:
					helperString += letter
			return helperString

def tof():
	if random.random() > .5:
		return T
	else:
		return F

def word(C):
	pass

if __name__ == "__main__":
	print "\n"
	print sys.argv
	for x in range(10):
		print name() + ", the " + adj(T) + str(random.randint(0, 99))
	