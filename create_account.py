import json

num_of_user_lines = 1
num_of_pass_lines = 1
filer = ""
def repeat():
    rp = input("repeat? y or n")
    if rp == "y":
        username_adder()
    else:
        SystemExit
def username_adder():
    global filer
    uname = input("enter username: ")
    pwd = input("enter password: ")
    #get the dictionary from logins.txt
    dictionary = json.load(open("logins.txt"))
    #append new username and password to the dictionary
    usr_pass = {uname:pwd}
    dictionary.update(usr_pass)
    with open("logins.txt", "w") as filer:
        filer.write(json.dumps(usr_pass) + "\n")
        






    

username_adder()


