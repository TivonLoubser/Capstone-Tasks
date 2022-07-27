# ===== Task Manager =====

#=====importing libraries===========

from datetime import date, datetime

from time import strftime

#==== Global Variables ====

credfile = open('user.txt','r+')   

file_content = credfile.readlines() 

task_file = open('tasks.txt','r+')

task_content = task_file.readlines()

individual_lines = []

#==== Functions ====

# function for main menu:


def menu():
    menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    : ''').lower()      # making sure that the user input is coneverted to lower case.


# function for add user:


def add_user():
    
    while True:

            if username == "admin":             # Only admin granted clearance for this section
            
                credfile = open('user.txt','a')         
                global file_content 

                new_username = input("Enter a new username\n")
                
                if new_username in user_list:
                    
                    print("User already exists.\nTry Again:")  
                
                else:
                    
                    while True:  
                        
                        new_password = input("Enter a new password\n")              
                        check_pword = input("Re-enter password\n")
                        
                        if new_password == check_pword:
                            print("Password confirmed\n")
                            
                            credfile.write("\n"+new_username+", "+new_password)
                            credfile.close()
                           
                            break
                        
                        else:
                            print("Passwords do not match, try again:")
                
                break
            
            else:               # No clearance granted if username != admin
                print("Clearance not granted")
                break
            

# function for add task:


def add_task():
    
    task_file = open('tasks.txt','a')
            
    Username_TF = input("Who is the task assigned to:\n")
        
    z = 0
        
    while z == 0:
        
        if Username_TF in user_list:

            tasktitle_TF = input("Title of task:\n")
            descrip_TF = input("Description of task:\n")
            duedate_TF = input("Due date of task (D/M/Y):\n")
            today = date.today()
            to_day = today.strftime("%d %B %Y")             # Using function to print out todays date
            
            task_file.write(Username_TF+", "+tasktitle_TF+", "+descrip_TF+", "+duedate_TF+", "+to_day+", "+"No"+"\n")
            task_file.close()
            
            print("\nTask update complete\n")
            
            z += 1
                    
        else:               # No task can be assigned to a non-existent user
            
            print("No user found")
            break


# Function to view all:


def view_all():
    
    for line in file_content:               # Reading through each line of task file
        
        VA_splt = line.split(", ")             # Splitting lines into components
        
        print("Task\t\t\t"+VA_splt [1]+"\nAssigned to:\t\t"+VA_splt [0]+"\nDate assigned:\t\t"+VA_splt [4]+"\nDue date:\t\t"+VA_splt [3]+"\nTask complete?\t\t"+VA_splt [5]+
            "Task description:\n"+VA_splt [2]+"\n")             # Printing in correct order
    
    task_file.close()


# Function to view my:


def view_my():

    task_file = open('tasks.txt','r')
    file_content = task_file.readlines()

    # Creating list of private tasks
    
    my_list = []        # Creating a list to store all own users own tasks in organizeed manner
    basic_list = []     # A list just for the basic components of the specific users tasks

    x = 0               # Setting variable to number list (starting at) 
    for line in file_content:

        VM_splt = line.split(", ")

        if VM_splt[0] == username:
            
            basic_list.append(line)
            my_list.append("\n"+str(x+1) + ". Task\t\t\t"+VM_splt[1]+"\nAssigned to:\t\t"+VM_splt[0]+"\nDate assigned:\t\t"+VM_splt[4]+"\nDue date:\t\t"+VM_splt[3]+"\nTask complete?\t\t"+VM_splt[5]+"Task description:\n"+VM_splt[2]+"\n")
            
            x += 1
            
            task_file.close()
            

    view_my_choice = input("Do you want to:\nView All(enter VA):\nor\nView Specific(enter VS):\nor\nReturn to main menu(enter -1):").lower()
    

    # If user wants to view all their tasks
    if view_my_choice == "va":
        
        x = 0
        
        for line in my_list:
                print(line)
                x +=1
                task_file.close()
    
    elif view_my_choice == "-1":
        print("")           # Just printing a blank line to revert back to main menu
    

    # If user wants to view specific task
    elif view_my_choice == "vs":
            
            task_num_choice = int(input("\nEnter the specific number you want to see:"))
            
            if task_num_choice < 0 or task_num_choice > len(my_list):       # Setting the range
                print("\nChoice out of range, try agian:")
            
            else:
                
                    global chosen_task
                    chosen_task = my_list[task_num_choice-1]
                    print("\n"+chosen_task+"\n")     

                    edit_action_choice = input("Would you like to edit(e),\nmark as complete(m),\nor exit(x)\n:").lower()            # Option to edit/mark as done
                    
                    task_file = open('tasks.txt','w')
                    
                    global individual_lines
                    
                    for line in file_content:                           
                        individual_lines.append(line)
                                                
                    # To mark as read
                    if edit_action_choice == "m":

                        chosen_basic_task =(basic_list[task_num_choice-1])   # Specific chosen task line
                        
                        # Creating a list of all the tasks
                                               
                        # If the chosen task = task from entire task list, it will replace 'no' with 'yes'    
                        for line in individual_lines:
                            if line == chosen_basic_task:
                                line_index = individual_lines.index(line)
                                line = line.split(", ")
                                line[-1] = line[-1].replace("No", "Yes")
                                individual_lines[line_index] = ", ".join(line)
                                print("Succesfully edited\n")
                                                                                  
                    # To edit
                    elif edit_action_choice == "e":

                        name_date_choice = input("Would you like to edit name, or date:").lower()

                        # Edit the name

                        if name_date_choice == "name":

                            new_name = input("Enter new user name:")
                            
                            chosen_basic_task =(basic_list[task_num_choice-1])   # Specific chosen task line
                            
                            for line in individual_lines:
                                if line == chosen_basic_task:
                                    line_index = individual_lines.index(line)
                                    line = line.split(", ")
                                    line[0] = line[0].replace(line[0], new_name)
                                    individual_lines[line_index] = ", ".join(line)
                                    print("Succesfully edited\n")                                                                   

                        # Edit the date

                        elif name_date_choice == "date":

                            new_date = input("Enter new due date:")
                            
                            chosen_basic_task =(basic_list[task_num_choice-1])   # Specific chosen task line
                            
                            for line in individual_lines:
                                if line == chosen_basic_task:
                                    line_index = individual_lines.index(line)
                                    line = line.split(", ")
                                    line[3] = line[3].replace(line[3], new_date)
                                    individual_lines[line_index] = ", ".join(line)
                                    print("Succesfully edited\n")
                           
                        else:
                            print("Incorrect entry")
                             
                    # To exit    
                    elif edit_action_choice == "x":
                        
                        print('Goodbye!!!')
                        
                        exit()
                    
                    # Writing action into txt file
                    for line in individual_lines:
                            task_file.write(line)            
                    
                    task_file.close()


# Function to generate report:


def generate_report():

    # Creating text files and lists variables
    task_ov = open('task_overview.txt','w+')
    user_ov = open('user_overview.txt','w+')

    completed = []
    uncompleted = []
    overdue = []
    
    credfile = open('user.txt','r+')        
    file_content = credfile.readlines() 
    
    task_file = open('tasks.txt','r+')
    task_content = task_file.readlines()

    # For task overview

    for line in task_content:
        
        split_task_cont = line.strip().split(", ")
        if split_task_cont[5] == "Yes":
            completed.append(line)
        else:
            uncompleted.append(line)
    
    for line in task_content:

        # Getting todays date to compare to due date
        today = datetime.today()

        # Getting due date to compare to todays date
        split_task_cont = line.split(", ")

        date_str = datetime.strptime(split_task_cont[3],"%d %B %Y")

        # Comparing the two dates
        if today > date_str:
            overdue.append(line)

    # Calculating the length of all the created lists  

    length_task = len(task_content)
    length_completed = len(completed)
    length_uncompleted = len(uncompleted)
    length_overdue = len(overdue)
    percentage_incomplete = (length_uncompleted/length_task)*100
    percent_overdue = (length_overdue/length_task)*100

    # Writing the values into the txt file

    task_ov.write(f"The total number of tasks is {length_task}\n")
    task_ov.write(f"The total number of completed tasks is {length_completed}\n")
    task_ov.write(f"The total number of uncompleted tasks is {length_uncompleted}\n")
    task_ov.write(f"The percentage of uncompleted tasks is {percentage_incomplete}%\n")
    task_ov.write(f"The total number of overdue tasks is {length_overdue}\n")
    task_ov.write(f"The percentage of overdue tasks is {percent_overdue}%")

    task_ov.close()

    # For user overview
    
    length_user = len(file_content)
 
    # Writing the values into the txt file

    user_ov.write(f"The total number of users is {length_user}\n")
    user_ov.write(f"The total number of tasks is {length_task}\n")
    
    # looping through each user in the user file and comparing it to the task file
    for line in file_content:
        
        split_task_cont = line.split(", ")
        
        user_name = split_task_cont[0].strip()
        total_user_task = 0
       
        for task_line in task_content:
            split_task_line = task_line.split(", ")
            if user_name == split_task_line[0]:
                total_user_task += 1

        # Writing the total number of task for each user into the file

        user_ov.write(f"The total number of tasks for {user_name} is: {str(total_user_task)}\n")
    
    print("\nUser and task over view generated. Please find reports in the files\n")
    

# Function to view statistics:


def display_stats():
    
    # Opening and reading txt files

    task_ov = open('task_overview.txt','r')
    user_ov = open('user_overview.txt','r')

    task_ov_read = task_ov.readlines()
    user_ov_read = user_ov.readlines()

    print("\nThe task overview is:\n")

    for line in task_ov_read:
        print(line)
    
    print("\nThe user overview is:\n")

    for line in user_ov_read:
        print(line)


#====Login Section====

print("Welcome to task manager! \n\n")

credfile = open('user.txt','r')             # Opening the relevant file for this section
file_content = credfile.readlines()             # Reading the relevant file


username = input("Please enter your username:\t")               # Requesting user input for username and password
password = input("Please enter your password:\t")

user_list = []              # Opening lists for username and password to be split into
password_list = []

for lines in file_content:
    
    a,b = lines.split(", ")         # Splitting into variables a,b
    user_list.append(a)             # Appending username list with a
    password_list.append(b.replace("\n", ""))         # Appending username list with b
 
credfile.close()                # Closing the file    

while True:             # Creating a while list to determine if password and username is correct
    
    if username in user_list and password == password_list[user_list.index(username)]:      # If both right
        print("\nUsername and password correct!\n")
        break
    elif username not in user_list and password in password_list:       # If username wrong - re-enter username and password
        print("\nIncorrect username.\nTry again\n")
        username = input("Please enter your username:\t")
        password = input("Please enter your password:\t")
    elif username in user_list and password not in password_list:       # Only password wrong - only re-enter password
        print("\nIncorrect password.\nTry again\n")
        password = input("Please enter your password:\t")
    else:                                                               # Both wrong - re-enter both
        print("\nIncorrect username and password.\nTry again\n")
        username = input("Please enter your username:\t")
        password = input("Please enter your password:\t")

if username == "admin":             # Admin only menu
    option_1 = input("Would you like to see the admin menu:\t").lower()
    if option_1 == "yes":
        ad_menu = input('''Select one of the following
        tu - Total number of users
        tt - Total number of tasks
        :''')
        if ad_menu == "tu":
            credfile = open('user.txt','r')         # Opening the relevant file for this section
            file_content = credfile.readlines()
            user_tot = len(file_content)                # Counting the readlines number of lines
            print("Total users:", user_tot,"\n")
            credfile.close()

        elif ad_menu == "tt":
            task_file = open('tasks.txt','r')
            file_content = task_file.readlines()
            task_tot = len(file_content)                # Counting the readlines number of lines
            print("Total tasks:",task_tot,"\n")
            task_file.close()
      
while True:
    #presenting the menu to the user through function
    
    menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    gr - generate report
    ds - display statistics
    e - Exit
    : ''').lower()      # making sure that the user input is coneverted to lower case.

    if menu == 'r':
            
            add_user()     # Using function to add user
                   
    elif menu == 'a':
        
        add_task( )      # Using function to add task
                                   
    elif menu == 'va':
        
        task_file = open('tasks.txt','r')
        file_content = task_file.readlines()
        
        view_all()
    
    elif menu == 'vm':
        
        view_my()

    elif menu == 'gr':
        
        generate_report()

    elif menu == 'ds':
        
        display_stats()
        
    elif menu == 'e':
        
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")



