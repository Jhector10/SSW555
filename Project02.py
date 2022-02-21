"""
Names: Joshua Hector
Pledge: I pledge my honor that I have abided by the Stevens Honor System
Date: Feb 21st, 2022
Assignment: Project 02
Professor: Ens
Course: SSW 555 Agile Methods

Note: 
please install with:
	pip3 install tabulate
"""

tags = ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", 
        "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL", 
        "DIV", "DATE", "HEAD", "TRLR", "NOTE"]


def eval():
	try:
		file = open("Project02.ged", 'r')
	except:
		print("Could not open file!")
		exit()
	
	#reading lines 
	lines = file.readlines()
	for line in lines:
		#store the level, tag, and arg
		tokens = line.split()
		level = tokens[0]
		tag = tokens[1]
		args = tokens[2:]

		new_list = [str(i) for i in args]

		#convert list to str
		string = ' '.join(new_list)
		
		for i in range(len(args)):
			print("-->" + line)
			if args[0] in tags:
				print("<--" + level + "|" + args[0] + "|Y|" + tag)
			if tag in tags:
				print("<--" + level + "|" + tag + "|Y|" + string)
			else:
				print("<--" + level + "|" + tag + "|N|" + string)

	file.close()
	return

eval()