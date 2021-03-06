import sys

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

import forgotPage_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    forgotPage_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    forgotPage_support.init(w, top, *args, **kwargs)
    return (w, top)

def on_close():
    w.destroy()

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font12 = "-family {Tw Cen MT} -size 14 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family {Tw Cen MT} -size 13 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font14 = "-family {Tw Cen MT} -size 30 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+650+150")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(0, 0)
        top.title("Forgot password")
        top.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.067, rely=0.044, relheight=0.896
                , relwidth=0.872)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d5c0fa")

        self.username_entry = tk.Entry(self.Frame1)
        self.username_entry.place(relx=0.402, rely=0.422, height=30
                , relwidth=0.39)
        self.username_entry.configure(background="white")
        self.username_entry.configure(disabledforeground="#a3a3a3")
        self.username_entry.configure(font="TkFixedFont")
        self.username_entry.configure(foreground="#000000")
        self.username_entry.configure(insertbackground="black")

        self.city_entry = tk.Entry(self.Frame1)
        self.city_entry.place(relx=0.402, rely=0.521,height=30, relwidth=0.39)
        self.city_entry.configure(background="white")
        self.city_entry.configure(disabledforeground="#a3a3a3")
        self.city_entry.configure(font="TkFixedFont")
        self.city_entry.configure(foreground="#000000")
        self.city_entry.configure(insertbackground="black")

        self.birthYear_entry = tk.Entry(self.Frame1)
        self.birthYear_entry.place(relx=0.402, rely=0.62, height=30
                , relwidth=0.39)
        self.birthYear_entry.configure(background="white")
        self.birthYear_entry.configure(disabledforeground="#a3a3a3")
        self.birthYear_entry.configure(font="TkFixedFont")
        self.birthYear_entry.configure(foreground="#000000")
        self.birthYear_entry.configure(insertbackground="black")

        self.motherName_entry = tk.Entry(self.Frame1)
        self.motherName_entry.place(relx=0.402, rely=0.72, height=30
                , relwidth=0.39)
        self.motherName_entry.configure(background="white")
        self.motherName_entry.configure(disabledforeground="#a3a3a3")
        self.motherName_entry.configure(font="TkFixedFont")
        self.motherName_entry.configure(foreground="#000000")
        self.motherName_entry.configure(highlightbackground="#d9d9d9")
        self.motherName_entry.configure(highlightcolor="black")
        self.motherName_entry.configure(insertbackground="black")
        self.motherName_entry.configure(selectbackground="#c4c4c4")
        self.motherName_entry.configure(selectforeground="black")

        self.forgot_label = tk.Label(self.Frame1)
        self.forgot_label.place(relx=0.115, rely=0.099, height=51, width=394)
        self.forgot_label.configure(background="#d5c0fa")
        self.forgot_label.configure(disabledforeground="#a3a3a3")
        self.forgot_label.configure(font=font14)
        self.forgot_label.configure(foreground="#ffffff")
        self.forgot_label.configure(text='''forgot your password?''')

        self.inst_label = ttk.Label(self.Frame1)
        self.inst_label.place(relx=0.057, rely=0.273, height=39, width=435)
        self.inst_label.configure(background="#d5c0fa")
        self.inst_label.configure(foreground="#ffffff")
        self.inst_label.configure(font=font13)
        self.inst_label.configure(relief="flat")
        self.inst_label.configure(text='''In order to get your password, you should fill those details:''')

        self.return_button = tk.Button(self.Frame1)
        self.return_button.place(relx=0.138, rely=0.88, height=44, width=131)
        self.return_button.configure(activebackground="#ececec")
        self.return_button.configure(activeforeground="#000000")
        self.return_button.configure(background="#ffffff")
        self.return_button.configure(command=forgotPage_support.backEntryPage)
        self.return_button.configure(disabledforeground="#a3a3a3")
        self.return_button.configure(font=font12)
        self.return_button.configure(foreground="#d5c0fa")
        self.return_button.configure(highlightbackground="#d9d9d9")
        self.return_button.configure(highlightcolor="black")
        self.return_button.configure(pady="0")
        self.return_button.configure(text='''return''')

        self.finish_button = tk.Button(self.Frame1)
        self.finish_button.place(relx=0.7, rely=0.88, height=44, width=131)
        self.finish_button.configure(activebackground="#ececec")
        self.finish_button.configure(activeforeground="#000000")
        self.finish_button.configure(background="#ffffff")
        self.finish_button.configure(disabledforeground="#a3a3a3")
        self.finish_button.configure(font=font12)
        self.finish_button.configure(foreground="#d5c0fa")
        self.finish_button.configure(highlightbackground="#d9d9d9")
        self.finish_button.configure(highlightcolor="black")
        self.finish_button.configure(pady="0")
        self.finish_button.configure(text='''finish''')
        self.finish_button.bind('<Button-1>', lambda e: forgotPage_support.forgotPassword(e))

        self.username_label = tk.Label(self.Frame1)
        self.username_label.place(relx=0.138, rely=0.422, height=31, width=84)
        self.username_label.configure(background="#d5c0fa")
        self.username_label.configure(disabledforeground="#a3a3a3")
        self.username_label.configure(font=font12)
        self.username_label.configure(foreground="#ffffff")
        self.username_label.configure(text='''username''')

        self.city_label = tk.Label(self.Frame1)
        self.city_label.place(relx=0.191, rely=0.521, height=31, width=34)
        self.city_label.configure(background="#d5c0fa")
        self.city_label.configure(disabledforeground="#a3a3a3")
        self.city_label.configure(font=font12)
        self.city_label.configure(foreground="#ffffff")
        self.city_label.configure(text='''city''')

        self.birthYear_label = tk.Label(self.Frame1)
        self.birthYear_label.place(relx=0.134, rely=0.62, height=21, width=86)
        self.birthYear_label.configure(background="#d5c0fa")
        self.birthYear_label.configure(cursor="fleur")
        self.birthYear_label.configure(disabledforeground="#a3a3a3")
        self.birthYear_label.configure(font=font12)
        self.birthYear_label.configure(foreground="#ffffff")
        self.birthYear_label.configure(text='''birth year''')

        self.mothername_label = tk.Label(self.Frame1)
        self.mothername_label.place(relx=0.115, rely=0.72, height=28, width=123)
        self.mothername_label.configure(background="#d5c0fa")
        self.mothername_label.configure(disabledforeground="#a3a3a3")
        self.mothername_label.configure(font=font12)
        self.mothername_label.configure(foreground="#ffffff")
        self.mothername_label.configure(text='''mother's name''')

        self.error_label = tk.Label(self.Frame1)
        self.error_label.place(relx=0.015, rely=0.82, height=20, width=500)
        self.error_label.configure(background="#d5c0fa")
        self.error_label.configure(disabledforeground="#a3a3a3")
        self.error_label.configure(font=font12)
        self.error_label.configure(foreground="red")
        self.error_label.configure(text="")

if __name__ == '__main__':
    vp_start_gui()





