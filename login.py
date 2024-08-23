import create_account as ca
def login():
    acc_check = input("do you have an account? Y or N: ")
    if acc_check == "y":
        enter_user = input("enter username: ")
        enter_pass = input("enter password")
        if enter_user == ca.filer.readline():