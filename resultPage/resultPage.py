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

import resultPage_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    resultPage_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    w.protocol("WM_DELETE_WINDOW", on_close)
    resultPage_support.init(w, top, *args, **kwargs)
    return (w, top)

def on_close():
    print("Results closing")
    resultPage_support.on_close(False)

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
        font10 = "-family {Tw Cen MT} -size 72 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Tw Cen MT} -size 19 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font14 = "-family {Tw Cen MT} -size 14 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font15 = "-family {Tw Cen MT} -size 19 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("600x450+365+234")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(0, 0)
        top.title("game's result")
        top.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.067, rely=0.044, relheight=0.896
                , relwidth=0.872)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#89c99f")

        self.answer_Label = tk.Label(self.Frame1)
        self.answer_Label.place(relx=0.076, rely=0.124, height=121, width=454)
        self.answer_Label.configure(background="#89c99f")
        self.answer_Label.configure(cursor="fleur")
        self.answer_Label.configure(disabledforeground="#a3a3a3")
        self.answer_Label.configure(font=font10)
        self.answer_Label.configure(foreground="#ffffff")

        self.userScore_Label = tk.Label(self.Frame1)
        self.userScore_Label.place(relx=0.268, rely=0.397, height=71, width=224)
        self.userScore_Label.configure(anchor='w')
        self.userScore_Label.configure(background="#89c99f")
        self.userScore_Label.configure(disabledforeground="#a3a3a3")
        self.userScore_Label.configure(font=font12)
        self.userScore_Label.configure(foreground="#ffffff")

        self.opponentScore_Label = tk.Label(self.Frame1)
        self.opponentScore_Label.place(relx=0.249, rely=0.521, height=71, width = 224)
        self.opponentScore_Label.configure(activebackground="#f9f9f9")
        self.opponentScore_Label.configure(activeforeground="black")
        self.opponentScore_Label.configure(anchor='w')
        self.opponentScore_Label.configure(background="#89c99f")
        self.opponentScore_Label.configure(disabledforeground="#a3a3a3")
        self.opponentScore_Label.configure(font=font15)
        self.opponentScore_Label.configure(foreground="#ffffff")
        self.opponentScore_Label.configure(highlightbackground="#d9d9d9")
        self.opponentScore_Label.configure(highlightcolor="black")

        self.playAgain_Button = tk.Button(self.Frame1)
        self.playAgain_Button.place(relx=0.153, rely=0.769, height=64, width=107)

        self.playAgain_Button.configure(activebackground="#ececec")
        self.playAgain_Button.configure(activeforeground="#ffffff")
        self.playAgain_Button.configure(background="#ffffff")
        self.playAgain_Button.configure(command=lambda: resultPage_support.on_close(True))
        self.playAgain_Button.configure(disabledforeground="#a3a3a3")
        self.playAgain_Button.configure(font=font14)
        self.playAgain_Button.configure(foreground="#89c99f")
        self.playAgain_Button.configure(highlightbackground="#d9d9d9")
        self.playAgain_Button.configure(highlightcolor="black")
        self.playAgain_Button.configure(pady="0")
        self.playAgain_Button.configure(takefocus="0")
        self.playAgain_Button.configure(text='''play again''')

        self.close_Button = tk.Button(self.Frame1)
        self.close_Button.place(relx=0.688, rely=0.769, height=64, width=107)
        self.close_Button.configure(activebackground="#ececec")
        self.close_Button.configure(activeforeground="#000000")
        self.close_Button.configure(background="#ffffff")
        self.close_Button.configure(command=lambda: resultPage_support.on_close(False))
        self.close_Button.configure(cursor="fleur")
        self.close_Button.configure(disabledforeground="#a3a3a3")
        self.close_Button.configure(font=font14)
        self.close_Button.configure(foreground="#89c99f")
        self.close_Button.configure(highlightbackground="#d9d9d9")
        self.close_Button.configure(highlightcolor="black")
        self.close_Button.configure(pady="0")
        self.close_Button.configure(takefocus="0")
        self.close_Button.configure(text='''close''')

if __name__ == '__main__':
    vp_start_gui()





