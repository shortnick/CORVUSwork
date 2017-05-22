!# python

import os 


workPath = 'ABSOLUTEfilePATHinsideQUOTES' #this is where your people files are stored
htmlFile = 'NEWfileNAMEhere'+'.html' #this will be your new file

#set up logging paths

os.chdir(workPath)

content = os.listdir(workPath)
tempCont = []

def newLink(nameEntry):
	#this is the html for the link, using "Lastname, Firstname"
	organize.append('person html code for link, nameEntry = "Last, First"')

def neighborhood(iterable):
	# this function is used for comparing last/current/next items in an iterable 
    iterator = iter(iterable)
    prev_item = None
    current_item = next(iterator)  # throws StopIteration if empty.
    for next_item in iterator:
        yield (prev_item, current_item, next_item)
        prev_item = current_item
        current_item = next_item
    yield (prev_item, current_item, None)




with open(htmlFile, 'a') as organize:
	organize.append('HTML AND INDEX LINKING CODE')

	for filename in content:
		first, last, fileIdExt =filename.split("_")
		iD, ext = fileIdExt.split(".")
	if ext == "CORRECT FILE EXTENSION/NO PERIOD":
		# 
		personIn = Last+','+First
		tempCont.append(personIn)
	else: #(bad file type)
		# log 'bad file'
		continue

	tempCont.sort()
	for person in tempCont:
		if organize[:-'XX'] == "LAST CHARS OF HTML LINK CODE" # replace 'XX' with number of char in Last Line
			newLink(person)
		else: 
			for prev,item,next in neighborhood(person):
    			if prev[0] == item[0]:
    				newLink(person)
    			else: 
				oranize.append('HTML FOR LINE BREAK')
				newLink(person)

	organize.append('FOOTER AND CLOSING HTML')
