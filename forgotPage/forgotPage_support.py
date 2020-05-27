import sqlite3
import sys
import clientBL


def fe_forgot_password_res(status_code, status_txt, password):
    global w
    print('forgot_password_Res')
    sys.stdout.flush()
    src = w.error_label
    if int(status_code) == 0:
        src.configure(text="your password: " +password)
    else:
        src.configure(text="error:"+status_txt + " (" + status_code + ")")

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


def backEntryPage():
    sys.stdout.flush()
    destroy_window()


def forgotPassword(p1):
    global w
    print('forgotPage_support.xxx')
    username = w.username_entry.get()
    city = w.city_entry.get()
    birthYear = w.birthYear_entry.get()
    mothersName = w.motherName_entry.get()
    print(username + " " + city + " " + birthYear + " " + mothersName)
    if not birthYear.isdigit():
        src = w.error_label
        src.configure(text="Error: Year must be a number between 1900 and 2020")
    elif int(birthYear) < 1900 or int(birthYear) > 2020: #the year should be between 1900-2020
        src = w.error_label
        src.configure(text="Error: Year must be a number between 1900 and 2020")
    elif username == "" or city == "" or birthYear == "" or mothersName == "" or username.isspace() == True or city.isspace() == True or birthYear.isspace() == True or mothersName.isspace() == True:
        src = w.error_label
        src.configure(text="Error: The fills cannot be empty")
    else:
        clientBL.forgot_password(fe_forgot_password_res, username, city, birthYear, mothersName)


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import forgotPage
    forgotPage.vp_start_gui()




