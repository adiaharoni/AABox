import sys
sys.path.append('..\\')
import clientBL
sys.path.append('..\\chooseGamePage')
import chooseGamePage
sys.path.append('..\\forgotPage')
import forgotPage
sys.path.append('..\\newRegistrationPage')
import newRegistrationPage

from tkinter import *
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


chooseGamePageOpen = False
newRegistrationPageOpen = False
forgotPageOpen = False



def fe_communication_error():
    global chooseGamePageOpen, newRegistrationPageOpen, forgotPageOpen

    if chooseGamePageOpen is True:
        chooseGamePage.on_close()
        chooseGamePageOpen = False
    if newRegistrationPageOpen is True:
        newRegistrationPage.on_close()
        newRegistrationPageOpen = False
    if forgotPageOpen is True:
        forgotPage.on_close()
        forgotPageOpen = False
    w.Label_error.configure(text="Error: Cannot connect to server.")


def fe_login_res(status_code, status_txt):
    global w
    print('loginRes')
    sys.stdout.flush()
    src = w.Label_error
    if status_code == "00":
        sys.stdout.flush()
        src.configure(text="")
        # hide this window
        root.withdraw()
        w.Label_error.configure(text="")
        global chooseGamePageOpen
        chooseGamePageOpen = True
        chooseGamePage.create_Toplevel1(root, 'Hello', top_level)
        chooseGamePage.set_close_callback(abort_user)
    else:
        src.configure(text=status_txt + " (" + status_code + ")")


def abort_user():
    clientBL.stop()
    #show window
    root.update()
    root.deiconify()


def login(p1):
    global w
    print('loginPage_support.xxx')
    username = w.entry_username.get()
    password = w.entry_password.get()
    print(username+" "+password)
    if username == "" or password == "" or username.isspace() is True or password.isspace() is True:
        src = w.Label_error
        src.configure(text="Error: user name and password are required.")
    else:
        if clientBL.init(fe_communication_error) is False:
            w.Label_error.configure(text="Error: Cannot connect to server.")
        else:
            clientBL.login(fe_login_res, username, password)


def startNewRegistrationPage():
    sys.stdout.flush()
    if clientBL.init(fe_communication_error) is False:
        w.Label_error.configure(text="Error: Cannot connect to server.")
    else:
        global newRegistrationPageOpen
        newRegistrationPageOpen = True
        w.Label_error.configure(text="")
        newRegistrationPage.create_Toplevel1(root, 'Hello', top_level)



def startforgotPage():
    sys.stdout.flush()
    if clientBL.init(fe_communication_error) is False:
        w.Label_error.configure(text="Error: Cannot connect to server.")
    else:
        global forgotPageOpen
        forgotPageOpen = True
        w.Label_error.configure(text="")

        forgotPage.create_Toplevel1(root, 'Hello', top_level)


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    if clientBL.init(fe_communication_error) is False:
        w.Label_error.configure(text="Error: Cannot connect to server.")


def on_close():
    clientBL.stop()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import loginPage
    loginPage.vp_start_gui()





