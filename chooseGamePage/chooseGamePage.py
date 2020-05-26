
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

import chooseGamePage_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    chooseGamePage_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    chooseGamePage_support.init(w, top, *args, **kwargs)
    w.protocol("WM_DELETE_WINDOW", on_close)
    return (w, top)

def on_close():
    print ("chooseGamePage closing")
    chooseGamePage_support.on_close()
    w.destroy()

def set_close_callback(abort_user):
    chooseGamePage_support.set_close_callback(abort_user)

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
        font10 = "-family {Tw Cen MT} -size 48 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Tw Cen MT} -size 30 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Tw Cen MT} -size 40 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("600x450+650+150")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(0, 0)
        top.title("Choose Game")
        top.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.05, rely=0.044, relheight=0.878, relwidth=0.925)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#678fed")

        self.label_choose = tk.Label(self.Frame1)
        self.label_choose.place(relx=0.15, rely=0.08, height=61, width=354)
        self.label_choose.configure(activeforeground="#678fed")
        self.label_choose.configure(background="#678fed")
        self.label_choose.configure(disabledforeground="#a3a3a3")
        self.label_choose.configure(font=font9)
        self.label_choose.configure(foreground="#ffffff")
        self.label_choose.configure(text='''Choose a game''')

        self.label_top_XO_scores = tk.Label(self.Frame1)
        self.label_top_XO_scores.place(relx=0.11, rely=0.65, height=174, width=187)
        self.label_top_XO_scores.configure(activeforeground="#678fed")
        self.label_top_XO_scores.configure(background="#678fed")
        self.label_top_XO_scores.configure(disabledforeground="#a3a3a3")
        self.label_top_XO_scores.configure(font="-family {Tw Cen MT} -size 11 -weight bold")
        self.label_top_XO_scores.configure(foreground="#ffffff")
        self.label_top_XO_scores.configure(text='''''')
        self.label_top_XO_scores.configure(anchor='n')

        self.label_top_four_in_a_row_scores = tk.Label(self.Frame1)
        self.label_top_four_in_a_row_scores.place(relx=0.58, rely=0.65, height=174, width=187)
        self.label_top_four_in_a_row_scores.configure(activeforeground="#678fed")
        self.label_top_four_in_a_row_scores.configure(background="#678fed")
        self.label_top_four_in_a_row_scores.configure(disabledforeground="#a3a3a3")
        self.label_top_four_in_a_row_scores.configure(font="-family {Tw Cen MT} -size 11 -weight bold")
        self.label_top_four_in_a_row_scores.configure(foreground="#ffffff")
        self.label_top_four_in_a_row_scores.configure(text='''''')
        self.label_top_four_in_a_row_scores.configure(anchor='n')

        self.button_XO = tk.Button(self.Frame1)
        self.button_XO.place(relx=0.14, rely=0.28, height=120, width=150)
        self.button_XO.configure(activebackground="#ececec")
        self.button_XO.configure(activeforeground="#000000")
        self.button_XO.configure(background="#ffffff")
        self.button_XO.configure(command=chooseGamePage_support.startXOPage)
        self.button_XO.configure(disabledforeground="#a3a3a3")
        self.button_XO.configure(font="-family {Tw Cen MT} -size 40 -weight bold")
        self.button_XO.configure(foreground="#678fed")
        self.button_XO.configure(highlightbackground="#d9d9d9")
        self.button_XO.configure(highlightcolor="black")
        self.button_XO.configure(pady="0")
        self.button_XO.configure(text='''X/O''')

        self.button_4InARow = tk.Button(self.Frame1)
        self.button_4InARow.place(relx=0.62, rely=0.28, height=120, width=150)
        self.button_4InARow.configure(activebackground="#ececec")
        self.button_4InARow.configure(activeforeground="#000000")
        self.button_4InARow.configure(command=chooseGamePage_support.startFourInARowPage)
        self.button_4InARow.configure(background="#ffffff")
        self.button_4InARow.configure(disabledforeground="#a3a3a3")
        self.button_4InARow.configure(font="-family {Tw Cen MT} -size 20 -weight bold")
        self.button_4InARow.configure(foreground="#678fed")
        self.button_4InARow.configure(highlightbackground="#d9d9d9")
        self.button_4InARow.configure(highlightcolor="black")
        self.button_4InARow.configure(pady="0")
        self.button_4InARow.configure(text='''4 In A Row''')

        self.label_waiting_xo = tk.Label(self.Frame1)
        self.label_waiting_xo.place(relx=0.126, rely=0.950, height=51, width=187)
        self.label_waiting_xo.configure(activebackground="#f9f9f9")
        self.label_waiting_xo.configure(activeforeground="black")
        self.label_waiting_xo.configure(anchor='c')
        self.label_waiting_xo.configure(background="#678fed")
        self.label_waiting_xo.configure(disabledforeground="#a3a3a3")
        self.label_waiting_xo.configure(font="-family {Tw Cen MT} -size 12 -weight bold")
        self.label_waiting_xo.configure(foreground="#ffffff")
        self.label_waiting_xo.configure(highlightbackground="#d9d9d9")
        self.label_waiting_xo.configure(highlightcolor="black")
        self.label_waiting_xo.configure(text="")

        self.label_waiting_4_in_a_row = tk.Label(self.Frame1)
        self.label_waiting_4_in_a_row.place(relx=0.577, rely=0.950, height=51, width=187)
        self.label_waiting_4_in_a_row.configure(activebackground="#f9f9f9")
        self.label_waiting_4_in_a_row.configure(activeforeground="black")
        self.label_waiting_4_in_a_row.configure(anchor='c')
        self.label_waiting_4_in_a_row.configure(background="#678fed")
        self.label_waiting_4_in_a_row.configure(disabledforeground="#a3a3a3")
        self.label_waiting_4_in_a_row.configure(font="-family {Tw Cen MT} -size 12 -weight bold")
        self.label_waiting_4_in_a_row.configure(foreground="#ffffff")
        self.label_waiting_4_in_a_row.configure(highlightbackground="#d9d9d9")
        self.label_waiting_4_in_a_row.configure(highlightcolor="black")
        self.label_waiting_4_in_a_row.configure(text="")


if __name__ == '__main__':
    vp_start_gui()





