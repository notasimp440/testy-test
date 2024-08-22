num_of_user_lines = int
num_of_pass_lines = int
def repeat():
    rp = input("repeat? y or n")
    if rp == "y":
        username_adder()
    else:
        SystemExit
def username_adder():

    filer = open('username.txt', "r")
    filew = open('username.txt', "a")
    wd = input("enter username: ")
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


