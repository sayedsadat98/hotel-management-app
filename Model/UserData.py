from View.Account import Account
from tkinter import *
from tkinter import ttk
import os
class UserData():

    # Implementing event on login button

    def login_verify(self,username1,password1):


        list_of_files = os.listdir(path="C:\XXXXFILES\SEM11\CSE470\Project\Hotel Management App\View\Account")
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                Account.login_sucess()

            else:
                Account.password_not_recognised()

        else:
            Account.user_not_found()

    # Designing popup for user not found

    def user_not_found():
        global user_not_found_screen
        user_not_found_screen = Toplevel(Account.login_screen)
        user_not_found_screen.title("Success")
        user_not_found_screen.geometry("150x100")
        Label(user_not_found_screen, text="User Not Found").pack()
        Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()