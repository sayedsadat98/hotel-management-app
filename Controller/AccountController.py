# import modules
from View import main
from tkinter import *
import os

from View.Account import Account

# Designing window for registration

class AccountController():




    # Designing window for login

    def login():
        Account.login()

    def register(self):
        Account.register()

    # Implementing event on register button


   #popup for success

    def login_sucess():
        global login_success_screen
        login_success_screen = Toplevel(login_screen)
        login_success_screen.title("Success")
        login_success_screen.geometry("150x100")
        Label(login_success_screen, text="Login Success").pack()
        Button(login_success_screen, text="OK", command=viewGUI).pack()

    # Designing popup for login invalid password



    # Designing popup for user not found




    def main_account_screen():

        global main_screen
        main_screen = Tk()
        main_screen.geometry("300x250")
        main_screen.title("Account Login")
        Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Timesnewroman", 13)).pack()
        Label(text="").pack()
        Button(text="Login", height="2", width="30", command=login).pack()
        Label(text="").pack()
        Button(text="Register", height="2", width="30", command=register).pack()

        main_screen.mainloop()

    # main_account_screen()