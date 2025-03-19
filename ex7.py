# student list
# Author: Xuanru Guo
# use list

# function studList
def studList():
	# create a list of first names
	studentNames = ["Lisa","Liam","Larry","Linda"]
	# iterate and add last names
	for name in studentNames:
		print(f"{name} Evans")
	return studentNames

# function addToList
def addToList():
	# call the function studList
	studentNames = studList()
	# prompt the user to enter a new name
	new_name = input("Please enter a new name: ")
	# add new name to the list
	studentNames.append(new_name)
	print("Updates List: ")
	for name in studentNames:
		print(f"{name} Evans")

# call the function addToList
addToList() 
