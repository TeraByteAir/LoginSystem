#Thomas Basta
#4/22/2021
#Login System
import time
adminuserstore= ['Admin']
adminpassstore= ['TheMastercard']
adminuser= input("Please enter admin username: ")

if adminuser in adminuserstore:
    print('Welcome Admin')
    time.sleep(2)

if adminuser not in adminuserstore:
    print("Incorrect username")
    time.sleep(3)
    exit()

adminpass= input("Please enter password: ")

if adminpass in adminpassstore:
    print("Successuful Login!")
    time.sleep(2)

if adminpass not in adminpassstore:
    print("Incorrect password")
    time.sleep(3)
    exit()


user_input= input("Do you want to create or view a login information already recorded? View/Create (Case-sensitive): ")
if user_input == "View":
    print("View")
    print(" ")
    Logins= open('Logins.txt', 'r')
    print(Logins.read())


if user_input == "Create":
    print("Create")
    new_login= open('Logins.txt', 'a')
    new_name= input("Type the new name of the login: ")
    new_user= input("Type the new username: ")
    new_pass= input("Type the new password: ")
    new_login.write("\n"+ new_name+ ", " + new_user + ', ' + new_pass)
    print("Saved!")
