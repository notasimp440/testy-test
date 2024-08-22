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
    filer = open('username.txt', "r")
    filew = open('username.txt', "a")
    wd = input("enter username: ")
    for line in filer.readlines(num_of_user_lines):
        if line == str(wd):
            print("sorry that username has already been taken, please try again.")
            repeat()
    if filer.readline(num_of_user_lines) == "":
        num_of_user_lines + 1
        filew.write(str(wd))
    else:
        num_of_user_lines + 1
        filew.write("\n" + str(wd))
    return num_of_user_lines

def password_adder():
    filer = open('passwords.txt', "r")
    filew = open('passwords.txt', "a")
    wd = input("enter password: ")
    if filer.readline(num_of_user_lines) == "":
        num_of_user_lines + 1
        filew.write(str(wd))
    else:
        num_of_user_lines + 1
        filew.write("\n" + str(wd))
    return num_of_user_lines




    

username_adder()
password_adder()


