import sys
from datetime import date
args = sys.argv
length = len(args)
tasks = []
today = str(date.today())
	
commands=("add","ls","del","done","help","report")
usage = "Usage :-\b\n\b$ ./todo add \"todo item\"  # Add a new todo\b\n\b$ ./todo ls               # Show remaining todos\b\n\b$ ./todo del NUMBER       # Delete a todo\b\n\b$ ./todo done NUMBER      # Complete a todo\b\n\b$ ./todo help             # Show usage\b\n\b$ ./todo report           # Statistics"

#if the user writes only "./todo"
if(length==1):			
	print(usage)


#if the user gives some command "./todo <command> "
if(length>=2):
	#Parsing the command
	command = args[1]
	
	#if the command is not found
	if command not in commands:
		print(usage)
		sys.exit(1)

	#Add to todo list
	if command == "add":
		if(len(args)==2):
			print("Error: Missing todo string. Nothing added!")
		else:
			file = open("todo.txt", "a")
			file.write(args[2]+"\n")
			file.close()
			print ("Added todo: \"{}\"".format(args[2]))
	#List all the tasks
	elif command == "ls":
		try:
			file = open("todo.txt", "r")
		except IOError as e:
			print(str(e))
			sys.exit(1)
		tasks = []
		tasks = file.readlines()
		if not tasks:
			print("There are no pending todos!")
		else:
			tasks = [task.strip() for task in tasks]
			i=len(tasks)
			for task in reversed(tasks):
				print("["+str(i)+"] " + task)
				i=i-1
		file.close()
	
	#Delete a Specific task from todo.txt
	elif command == "del":
		if(len(args)==2):
			print("delete does not have enough arguments")
			sys.exit(1)
		try:
			file = open("todo.txt", "r")
		except IOError as e:
			print(str(e))
			sys.exit(1)

		tasks = file.readlines()
		file.close()
		
		tasks = [task.strip() for task in tasks]
		
		pos=int(args[2])
		if (pos<=0 or pos>len(tasks)):
			print("Error: todo #"+args[2]+" does not exist. Nothing deleted.")
			sys.exit(1)
		else:
			del tasks[pos-1]
			file = open("todo.txt", "w")
			tasks = [task + "\n" for task in tasks]
			file.writelines(tasks)
			print ("Deleted todo #"+args[2])
	#Mark a task as done and move it to done.txt
	elif command == "done":
		try:
			file = open("todo.txt", "r")
		except IOError as e:
			print(str(e))
			sys.exit(1)

		tasks = file.readlines()
		file.close()
		if(len(args)==2):
			print("Error: Missing NUMBER for marking todo as done.")
			sys.exit(1)
		pos=int(args[2])
		if (pos<=0 or pos>len(tasks)):
			print("Error: todo #"+args[2]+" does not exist.")
			sys.exit(1)
		else:
			tasks = [task.strip() for task in tasks]
			file = open("done.txt", "a")
			file.write("x "+ today + " " +tasks[pos-1]+"\n")
			file.close()
			print ("Marked todo #"+args[2]+" as done.")
			del tasks[pos-1]
			file = open("todo.txt", "w")
			tasks = [task + "\n" for task in tasks]
			file.writelines(tasks)
			
	#Help 
	elif command == "help":
		print(usage)
	
	#Report
	elif command == "report":
		file = open("todo.txt", "r")
		tasks = file.readlines()
		pending=len(tasks)
		file = open("done.txt", "r")
		tasks = file.readlines()
		completed=len(tasks)
		print(today+" "+"Pending : "+str(pending)+" "+"Completed : "+str(completed))



