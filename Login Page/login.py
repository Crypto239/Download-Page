from tkinter import *

def LoginPage():
    login_screen=Tk()
    login_screen.title("Login Page By Jeroen Bak")
    login_screen.geometry("300x250")

    Label(login_screen, text="Please Enter Login Credentials").pack()
    Label(login_screen).pack()
    Label(login_screen, text="Username").pack()

    username_login_entry = Entry(login_screen,textvariable="Username")
    username_login_entry.pack()

    Label(login_screen).pack()
    Label(login_screen, text="Password").pack()

    password__login_entry = Entry(login_screen,textvariable="Password")
    password__login_entry.pack()

    Label(login_screen).pack()
    Button(login_screen, text="Login", width=10, height=1).pack()
    login_screen.mainloop()
LoginPage()
