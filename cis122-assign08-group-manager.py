def create_group(d):
	while True:
		group_name = input("Enter group name (empty to cancel): ")
		if(group_name in myGroup):
			print("Group name already exists")
			continue
		elif(group_name == ""):
			break
		else:
			myGroup[group_name] = {}
			myGroup[group_name]["_keys_"] = []
			myGroup[group_name]["_data_"] = []
			while True:
				key = input("Enter field name (empty to stop): ")
				if(key == ""):
					break
				else:
					myGroup[group_name]["_keys_"].append(key)
					continue

def list_groups(d):
	print("** List of groups **")
	for item in list(myGroup):
		print(item + " : ", len(myGroup[item]["_keys_"]), " properties ", tuple(myGroup[item]["_keys_"]))

def add_group_data(d):
	print("** Add group data **")
	list_groups(myGroup)
	while True:
		g = input("Enter group (empty to cancel): ")
		if(g == ""):
			break
		elif(g not in myGroup):
			print("No group named ", g)
			continue
		else:
			for item in myGroup[g]["_keys_"]:
				prop = input("Enter " + str(item) + ": ")
				myGroup[g]["_data_"].append({item: prop})

def list_group_data(d):
	print("** List group data **")
	list_groups(myGroup)
	while True:
		g = input("Enter group (empty to cancel): ")
		if(g == ""):
			break
		elif(g not in myGroup):
			print("No group named ", g)
			continue
		else:
			count = 0
			val = []
			string = ""
			for item in myGroup[g]["_keys_"]:
				string += (myGroup[g]['_keys_'][count] + " = " + myGroup[g]["_data_"][count][item] + ", ")
				val.append((count, string))
				count += 1
			for item in val:
				print(item)



myGroup = {}

while True:
	user = input("Command (empty or X to quit, ? for help): ")
	user = user.upper()
	if(user == "?"):
		print("?: list commands\nC: Create a new group\nG: List Groups\nA: Add data to a group\nL: List data for a group\nX: Exit")
	elif(user == "X" or user == ""):
		break
	elif(user == "C"):
		create_group(myGroup)
	elif(user == "G"):
		list_groups(myGroup)
	elif(user == "A"):
		add_group_data(myGroup)
	elif(user == "L"):
		list_group_data(myGroup)
	else:
		print("I do not understand")
		continue