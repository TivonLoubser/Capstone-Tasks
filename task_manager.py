# ===== Task Manager =====

#=====importing libraries===========
from datetime import date
from time import strftime

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
        print(user_list)
        print(password_list)
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
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r':
        if username == "admin":             # Only admin granted clearance for this section
            
            credfile = open('user.txt','a')         
            file_content = credfile.readlines()    
            y = 0

            while y == 0:

                new_username = input("Enter a new username\n")

                new_password = input("Enter a new password\n")              
                check_pword = input("Re-enter password\n")

                if new_password == check_pword:             # Checking password is correct
                    print("Password confirmed\n")
                    credfile.write("\n"+new_username+", "+new_password)
                    y += 1
                    credfile.close()
                else:
                    print("Passwords do not match\nTry again\n")
        else:               # No clearance granted if username != admin
            print("Clearance not granted")
    
    elif menu == 'a':
        
            task_file = open('tasks.txt','a')
            
            Username_TF = input("Who is the task assigned to:\n")
        
            z = 0
        
            while z == 0:
                    if Username_TF in user_list:

                        tasktitle_TF = input("Title of task:\n")
                        descrip_TF = input("Description of task:\n")
                        duedate_TF = input("Due date of task (D/M/Y):\n")
                        today = date.today()
                        to_day = today.strftime("%d %b %Y")             # Using function to print out todays date
                        task_file.write(Username_TF+", "+tasktitle_TF+", "+descrip_TF+", "+duedate_TF+", "+to_day+", "+"No"+"\n")
                        task_file.close()
                        print("\nTask update complete\n")
                        z += 1
                    
                    else:               # No task can be assigned to a non-existent user
                        print("No user found")
                        


    
    elif menu == 'va':
        
        task_file = open('tasks.txt','r')
        file_content = task_file.readlines()
        
        for line in file_content:               # Reading through each line of task file
            indi = line.split(", ")             # Splitting lines into components
            print("Task\t\t\t"+indi[1]+"\nAssigned to:\t\t"+indi[0]+"\nDate assigned:\t\t"+indi[4]+"\nDue date:\t\t"+indi[3]+"\nTask complete?\t\t"+indi[5]+
            "Task description:\n"+indi[2]+"\n")             # Printing in correct order
        task_file.close()
    

    elif menu == 'vm':
        
        task_file = open('tasks.txt','r')
        file_content = task_file.readlines()

        for line in file_content:
            indi2 = line.split(", ")
            if indi2[0] == username:
                print("Task\t\t\t"+indi2[1]+"\nAssigned to:\t\t"+indi2[0]+"\nDate assigned:\t\t"+indi2[4]+"\nDue date:\t\t"+indi2[3]+"\nTask complete?\t\t"+indi2[5]+
            "Task description:\n"+indi2[2]+"\n")
        task_file.close()
        

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")



