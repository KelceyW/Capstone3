#import datetime and parse
import datetime
from dateutil.parser import parse

#Define variables
allDetails = ""
allUsers = ""
allPasswords = ""
allTasks =[]
editTask = []
date = datetime.date.today().strftime('%d %b %Y')
validEntry = True 

#Open text file and save the login details as a variable
#Split string at ',' to save usernames and passwords seperately
#Save details
#Remove additional characters
with open('user.txt', 'r+') as f:
    for x in f:
        split = x.find(",")
        user = x[0:split]
        password = x[split+2:]
        allUsers = allUsers + "\n" + user
        allPasswords = allPasswords + "\n" + password
        allDetails = allDetails + x
        allDetails =allDetails.replace(",", "")
        allDetails = allDetails.replace(" ","")

#Open tasks.txt file and save full details to list
with open('tasks.txt','r+') as f:
    for x in f:
        allTasks.append(x)
        
#Define functions
        
#reg_user
#Check logged in user is 'admin'
#Check new username is not already registered
#Get new user info from user
#Write new user info to user.txt file
def reg_user():
    if username == 'admin':
        newUser = input("Please enter a new username: ")
        newPassword = input("Please enter a password: ")
        confirmPassword = input("Please confirm password: ")

        while allUsers.find(newUser) > -1:
            print(f"The username {newUser} is already registered, please try agian: ")
            newUser = input("Please enter a new username: ")
            newPassword = input("Please enter a password: ")
            confirmPassword = input("Please confirm password: ")
            
        while newPassword != confirmPassword:
            print("Your passwords do not match, please try again: ")
            newUser = input("Please enter a new username: ")
            newPassword = input("Please enter a password: ")
            confirmPassword = input("Please confirm password: ")

        with open('user.txt', 'a') as f:
            f.write("\n"+newUser+","+" "+newPassword)
         
        print(f"\nNew user {newUser} added successfully!")
        
    else:
        print("Only Admin users may select this option")

#add_task
#Get new task info from user
#Write new task information to tasks.txt.file
def add_task():
    taskName = input("What is the name of the new task: ")
    assignUser = input("Please enter the name of the user the task is assigned to: ")
    describeTask = input("Please enter a task description: ")
    dueDate = input("Please enter the due date for the task: ")
    assignDate = date
    completeTask = "No"

    with open('tasks.txt', 'a') as f:
        f.write("\n"+assignUser+", "+taskName+", "+describeTask+", "+assignDate+", "+dueDate+", "+completeTask)

        print(f"\nNew task {taskName} added successfully!")

#view_all
#view all tasks listed in tasks.txt
def view_all():
    with open('tasks.txt', 'r+')as f:
        for x in f:
            x = x.split(",")
            print("Task:\t\t"+x[1]+"\nAssigned to:\t"+x[0]+"\nDate assigned:\t"+x[3]+" \nDue date:\t"+x[4]+
                  "\nTask complete?\t"+x[5]+"\nTask description:\n"+x[2]+"\n")

#view_mine
#number each task
#view all tasks listed in tasks.txt for the logged in user
def view_mine(user):
    for task in enumerate(allTasks,1):
        editTasks = str(task[0])+" ,"+task[1]
        editTasks = editTasks.split(",")

        if editTasks[1] == user:
            print(editTasks[0]+"\nTask:\t\t"+editTasks[2]+"\nAssigned to:\t"+editTasks[1]+"\nDate assigned:\t"+editTasks[4]+" \nDue date:\t"+editTasks[5]+
                  "\nTask complete?\t"+editTasks[6]+"\nTask description:\n"+editTasks[3]+"\n")

#gen_reports
#Define variables
#open tasks.txt and user.txt files and save relevant info
#Create 2 text files displaying all info
def gen_reports():
    totalTasks = 0
    incompleteTasks = 0
    overdueTasks = 0
    userTasks = 0
    userIncomplete = 0
    userOverdue = 0
    completeTasks = 0
    userComplete = 0
    totalUsers = 0
    with open('tasks.txt','r+')as f:
        for x in f:
            totalTasks += 1

            x = x.split(",")
            x[5] = x[5].lower()
            x[5] = x[5].replace(" ","")
            x[5] = x[5].replace("\n","")
            
            if x[5] == "yes":
                completeTasks += 1
            else:
                incompleteTasks += 1

            dueDate = (parse(x[4]))
            currentDate = (parse(date))

            if x[5] == "no" and dueDate < currentDate:
                overdueTasks +=1

            if x[0] == username:
                userTasks += 1

            if x[0] == username and x[5] == "yes":
                userComplete += 1
            elif x[0] == username and x[5] == "no":
                userIncomplete += 1

            if x[0] == username and x[5] == "no" and dueDate < currentDate:
                userOverdue += 1

            incompletePercent = (incompleteTasks /totalTasks)*100
            incompletePercent = round(incompletePercent, 2)
            
            overduePercent = (overdueTasks / totalTasks)*100
            overduePercent = round(overduePercent, 2)

    with open('task_overview.txt','w') as f:
        f.write("Total number of tasks:\t\t\t"+str(totalTasks)+"\nNumber of completed tasks:\t\t"+str(completeTasks)+"\nNumber of incomplete tasks:\t\t"
                +str(incompleteTasks)+"\nNumber of incomplete, overdue tasks:\t"+str(overdueTasks)+"\nPercentage of incomplete tasks:\t\t"
                +str(incompletePercent)+"%\nPercentage of overdue tasks:\t\t"+str(overduePercent)+"%")

    with open('user.txt','r+')as f:
        for x in f:
            totalUsers += 1

    userPercent = (userTasks / totalTasks)*100
    userPercent = round(userPercent, 2)

    if userTasks == 0:
        completePercent = "No tasks assigned to this user"
        totalIncomplete = "No tasks assigned to this user"
        totalOverdue = "No tasks assigned to this user"

    else:
        completePercent = (userComplete / userTasks)*100
        completePercent = round(completePercent, 2)
    
        totalIncomplete = (userIncomplete / userTasks)*100
        totalIncomplete = round(totalIncomplete, 2)
    
        totalOverdue = (userOverdue / userTasks)*100
        totalOverdue = round(totalOverdue, 2)

    with open('user_overview.txt','w') as f:
        f.write("Total number of users:\t\t\t\t\t\t"+str(totalUsers)+"\nTotal number of tasks:\t\t\t\t\t\t"+str(totalTasks)+"\nNumber of tasks assigned to you ("
                +(username)+"):\t\t\t"+str(userTasks)+"\nPercentage of the total tasks assigned to you("+(username)+"):\t\t"+str(userPercent)+
                "%\nPercentage of your tasks, which are complete:\t\t\t"+str(completePercent)+"%\nPercentage of your tasks that still need to be completed:\t"
                +str(totalIncomplete)+"%\nPercentage of your tasks, which are incomplete and overdue:\t"+str(totalOverdue)+"%")

    print("Your reports have been generated. Please open 'task_overview' and 'user_overview' to view your reports\n")
    

#Print welcome screen, and request user details
print("Welcome to TASK MANAGER! \nPlease login below:\n")
username = input("Please enter your username: ")
userPassword = input("Please enter your password: ")

#Create loop to check login details are correct
while allDetails.find(username+userPassword) < 0:

    #Check username
    if allUsers.find(username)< 0 or len(username) < 2:
        print("Your username is incorrect, please enter a valid username: ")
        username =input("Please enter your username: ")
        userPassword = input("Please enter your password: ")
        
    #Check password
    elif allPasswords.find(userPassword) < 0 or len(userPassword) <2:
        print("Your password is incorrect, please enter a valid password ")
        username = input("Please enter your username: ")
        userPassword = input("Please enter your password: ")
        
    #Check username and password match
    elif allDetails.find(username+userPassword) < 0:
        print("Your username and password do not match, please enter valid login details: ")
        username = input("Please enter your username: ")
        userPassword = input("Please enter your password: ")

#Create loop for user to choose an option
while validEntry:
    
    #Print opening screen
    #Opening screen for admin user
    if username == "admin":
        print('''\nPlease select one of the following options: \n
    r - \t register user
    a - \t add task
    va - \t view all tasks
    vm - \t view my tasks
    gr - \t generate reports
    ds - \t display statistics
    e - \t exit \n ''')

    #Opening screen for other users
    else:
        print('''\nPlease select one of the following options: \n
    r - \t register user
    a - \t add task
    va - \t view all tasks
    vm - \t view my tasks
    e - \t exit \n ''')

    #Get user input
    #Ensure input is lower case
    choice = input("")
    choice = choice.lower()

    #Close the program if 'e' is selected
    if choice == "e":
        break
    
    #use function reg_user if 'r' is selected
    if choice == "r":
        reg_user()
        
    #use function add_task if 'a' is selected
    if choice == "a":
        add_task()

    #use function view_all if 'va' is selected
    if choice == "va":
        view_all()
        

    #use function view_mine if 'vm' is selected
    #allow user to select and edit tasks
    #re-write edited tasks back to tasks.txt
    if choice == "vm":
        view_mine(username)

        newTasks = ""
        
        selectTask = int(input("Please enter a task number, or -1 to return to the main menu: "))

        if selectTask != -1:
            with open('tasks.txt','r+')as f:
                for task in enumerate(f,1):
                    taskEdit = str(task [0]) +", "+ task[1]
                    taskEdit = taskEdit.split(", ")
                    complete = taskEdit[6].replace("\n","")

                    if selectTask == int(taskEdit[0]) and complete == "Yes":
                        print("This task is already completed, it cannot be edited")

                    elif selectTask == int(taskEdit[0]) and complete == "No":
                        edit = input("\nWhat would you like to do with this task?\n\nMC\t- Mark as complete\nE\t- Edit task\n")
                        edit = edit.lower()
                        
                        if edit == "mc":
                            taskEdit[6] = "Yes\n"
                            print(f"\nTask {task[0]} marked as complete!\n")

                        if edit == "e":
                            userEdit = input("How would you like to edit this task?\n\nCU\t- Change username assigned to the task\nCD\t- Change due date of the task\n")
                            userEdit = userEdit.lower()
                            
                            if userEdit == "cu":
                                newUsername = input("Please enter the new username to assign this task to: ")
                                taskEdit[1] = newUsername
                                print(f"Username for task {task[0]} changed to {newUsername}\n")

                            
                            if userEdit == "cd":
                                newDate = input("Please enter the new due date(dd/month/year): ")
                                taskEdit[5] = newDate
                                print(f"Due date for task {task[0]} changed to {newDate}\n")
                                  
                    newTasks =newTasks+taskEdit[1]+", "+taskEdit[2]+", "+taskEdit[3]+", "+taskEdit[4]+", "+taskEdit[5]+", "+taskEdit[6]
                       
                with open('tasks.txt', 'w') as f:
                    f.write(newTasks)

    #use function gen_reports if 'gr' is selected
    if choice == "gr":
        gen_reports()

    #if 'ds' is selected
    #use gen_reports to generate reports first
    #display reports from user_overview.txt and tasks_overview.txt
    if choice == "ds":
        gen_reports()
        with open('task_overview.txt','r+')as f:
            print("TASK OVERVIEW:\n")
            for x in f:
                x = x.replace("\n","")
                print(x)

        with open('user_overview.txt','r+')as f:
            print("\nUSER OVERVIEW:\n")
            for x in f:
                x = x.replace("\n","")
                print(x)



    

   


            
                
            
         
           
          
   
    
    
    
    

         
    



    

    

    
        
