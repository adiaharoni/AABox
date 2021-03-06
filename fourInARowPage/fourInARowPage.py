#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Apr 28, 2020 07:03:50 PM +0300  platform: Windows NT

import sys
from tkinter import messagebox

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

import fourInARowPage_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", on_close)
    top = Toplevel1 (root)
    fourInARowPage_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    fourInARowPage_support.init(w, top, *args, **kwargs)
    w.protocol("WM_DELETE_WINDOW", on_close)
    return (w, top)

def set_close_callback(abort_game):
    fourInARowPage_support.set_close_callback(abort_game)

def on_close():
    print ("4 in a row closing")
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        fourInARowPage_support.on_close()
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
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=[('selected', _compcolor), ('active',_ana2color)])
        fourInARowPage_support.clear_dicts()

        top.geometry("600x450+454+177")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(0, 0)
        top.title("Four In A Row")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.067, rely=0.044, relheight=0.896
                , relwidth=0.872)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#3c8867")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.for_in_a_row_Label = tk.Label(self.Frame1)
        self.for_in_a_row_Label.place(relx=0.172, rely=0.02, height=71
                , width=404)
        self.for_in_a_row_Label.configure(activebackground="#f9f9f9")
        self.for_in_a_row_Label.configure(activeforeground="#ffffff")
        self.for_in_a_row_Label.configure(background="#3c8867")
        self.for_in_a_row_Label.configure(disabledforeground="#a3a3a3")
        self.for_in_a_row_Label.configure(font="-family {Tw Cen MT} -size 36 -weight bold")
        self.for_in_a_row_Label.configure(foreground="#ffffff")
        self.for_in_a_row_Label.configure(highlightbackground="#d9d9d9")
        self.for_in_a_row_Label.configure(highlightcolor="black")
        self.for_in_a_row_Label.configure(text='''Four In A Row play!''')

        self.TSeparator1_1 = ttk.Separator(self.Frame1)
        self.TSeparator1_1.place(relx=0.966, rely=0.273, relheight=0.67)
        self.TSeparator1_1.configure(orient="vertical")

        self.TSeparator1_2 = ttk.Separator(self.Frame1)
        self.TSeparator1_2.place(relx=0.847, rely=0.273, relheight=0.67)
        self.TSeparator1_2.configure(orient="vertical")

        self.TSeparator1_3 = ttk.Separator(self.Frame1)
        self.TSeparator1_3.place(relx=0.732, rely=0.273, relheight=0.67)
        self.TSeparator1_3.configure(orient="vertical")

        self.TSeparator1_4 = ttk.Separator(self.Frame1)
        self.TSeparator1_4.place(relx=0.618, rely=0.273, relheight=0.67)
        self.TSeparator1_4.configure(orient="vertical")

        self.TSeparator1_5 = ttk.Separator(self.Frame1)
        self.TSeparator1_5.place(relx=0.503, rely=0.273, relheight=0.67)
        self.TSeparator1_5.configure(orient="vertical")

        self.TSeparator1_6 = ttk.Separator(self.Frame1)
        self.TSeparator1_6.place(relx=0.382, rely=0.273, relheight=0.67)
        self.TSeparator1_6.configure(orient="vertical")

        self.TSeparator7 = ttk.Separator(self.Frame1)
        self.TSeparator7.place(relx=0.38, rely=0.94, relwidth=0.593)

        self.turn_Label = tk.Label(self.Frame1)
        self.turn_Label.place(relx=0.057, rely=0.673, height=51, width=154)
        self.turn_Label.configure(activebackground="#f9f9f9")
        self.turn_Label.configure(activeforeground="black")
        self.turn_Label.configure(anchor='w')
        self.turn_Label.configure(background="#3c8867")
        self.turn_Label.configure(disabledforeground="#a3a3a3")
        self.turn_Label.configure(font="-family {Tw Cen MT} -size 9 -weight bold")
        self.turn_Label.configure(foreground="#000000")
        self.turn_Label.configure(highlightbackground="#d9d9d9")
        self.turn_Label.configure(highlightcolor="black")
        self.turn_Label.configure(justify='left')

        self.symbol_Label = tk.Label(self.Frame1)
        self.symbol_Label.place(relx=0.057, rely=0.273, height=51, width=154)
        self.symbol_Label.configure(activebackground="#f9f9f9")
        self.symbol_Label.configure(activeforeground="black")
        self.symbol_Label.configure(anchor='w')
        self.symbol_Label.configure(background="#3c8867")
        self.symbol_Label.configure(disabledforeground="#a3a3a3")
        self.symbol_Label.configure(font="-family {Tw Cen MT} -size 9 -weight bold")
        self.symbol_Label.configure(foreground="#000000")
        self.symbol_Label.configure(highlightbackground="#d9d9d9")
        self.symbol_Label.configure(highlightcolor="black")
        self.symbol_Label.configure(justify='left')

        self.opponent_username_Label = tk.Label(self.Frame1)
        self.opponent_username_Label.place(relx=0.057, rely=0.473, height=51, width=154)
        self.opponent_username_Label.configure(activebackground="#f9f9f9")
        self.opponent_username_Label.configure(activeforeground="black")
        self.opponent_username_Label.configure(anchor='w')
        self.opponent_username_Label.configure(background="#3c8867")
        self.opponent_username_Label.configure(disabledforeground="#a3a3a3")
        self.opponent_username_Label.configure(font="-family {Tw Cen MT} -size 9 -weight bold")
        self.opponent_username_Label.configure(foreground="#000000")
        self.opponent_username_Label.configure(highlightbackground="#d9d9d9")
        self.opponent_username_Label.configure(highlightcolor="black")
        self.opponent_username_Label.configure(justify='left')

        self.opponent_score_Label = tk.Label(self.Frame1)
        self.opponent_score_Label.place(relx=0.057, rely=0.573, height=51
                , width=154)
        self.opponent_score_Label.configure(activebackground="#f9f9f9")
        self.opponent_score_Label.configure(activeforeground="black")
        self.opponent_score_Label.configure(anchor='w')
        self.opponent_score_Label.configure(background="#3c8867")
        self.opponent_score_Label.configure(disabledforeground="#a3a3a3")
        self.opponent_score_Label.configure(font="-family {Tw Cen MT} -size 9 -weight bold")
        self.opponent_score_Label.configure(foreground="#000000")
        self.opponent_score_Label.configure(highlightbackground="#d9d9d9")
        self.opponent_score_Label.configure(highlightcolor="black")
        self.opponent_score_Label.configure(justify='left')

        self.user_score_Label = tk.Label(self.Frame1)
        self.user_score_Label.place(relx=0.057, rely=0.373, height=51, width=154)
        self.user_score_Label.configure(activebackground="#f9f9f9")
        self.user_score_Label.configure(activeforeground="black")
        self.user_score_Label.configure(anchor='w')
        self.user_score_Label.configure(background="#3c8867")
        self.user_score_Label.configure(disabledforeground="#a3a3a3")
        self.user_score_Label.configure(font="-family {Tw Cen MT} -size 11 -weight bold")
        self.user_score_Label.configure(foreground="#000000")
        self.user_score_Label.configure(highlightbackground="#d9d9d9")
        self.user_score_Label.configure(highlightcolor="black")
        self.user_score_Label.configure(justify='left')

        self.Frame2_000 = tk.Frame(self.Frame1)
        self.Frame2_000.place(relx=0.402, rely=0.819, relheight=0.112
                , relwidth=0.086)
        self.Frame2_000.configure(relief='groove')
        self.Frame2_000.configure(borderwidth="2")
        self.Frame2_000.configure(relief="groove")
        self.Frame2_000.configure(background="#3c8867")
        fourInARowPage_support.set_frames("00", self.Frame2_000)

        self.Frame2_001 = tk.Frame(self.Frame1)
        self.Frame2_001.place(relx=0.516, rely=0.819, relheight=0.112
                              , relwidth=0.086)
        self.Frame2_001.configure(relief='groove')
        self.Frame2_001.configure(borderwidth="2")
        self.Frame2_001.configure(relief="groove")
        self.Frame2_001.configure(background="#3c8867")
        self.Frame2_001.configure(highlightbackground="#d9d9d9")
        self.Frame2_001.configure(highlightcolor="black")
        fourInARowPage_support.set_frames("01", self.Frame2_001)

        self.Frame2_002 = tk.Frame(self.Frame1)
        self.Frame2_002.place(relx=0.631, rely=0.819, relheight=0.112
                              , relwidth=0.086)
        self.Frame2_002.configure(relief='groove')
        self.Frame2_002.configure(borderwidth="2")
        self.Frame2_002.configure(relief="groove")
        self.Frame2_002.configure(background="#3c8867")
        self.Frame2_002.configure(highlightbackground="#d9d9d9")
        self.Frame2_002.configure(highlightcolor="black")
        fourInARowPage_support.set_frames("02", self.Frame2_002)

        self.Frame2_003 = tk.Frame(self.Frame1)
        self.Frame2_003.place(relx=0.746, rely=0.819, relheight=0.112
                , relwidth=0.086)
        self.Frame2_003.configure(relief='groove')
        self.Frame2_003.configure(borderwidth="2")
        self.Frame2_003.configure(relief="groove")
        self.Frame2_003.configure(background="#3c8867")
        self.Frame2_003.configure(highlightbackground="#d9d9d9")
        self.Frame2_003.configure(highlightcolor="black")
        fourInARowPage_support.set_frames("03", self.Frame2_003)

        self.Frame2_004 = tk.Frame(self.Frame1)
        self.Frame2_004.place(relx=0.86, rely=0.819, relheight=0.112
                , relwidth=0.086)
        self.Frame2_004.configure(relief='groove')
        self.Frame2_004.configure(borderwidth="2")
        self.Frame2_004.configure(relief="groove")
        self.Frame2_004.configure(background="#3c8867")
        self.Frame2_004.configure(highlightbackground="#d9d9d9")
        self.Frame2_004.configure(highlightcolor="black")
        fourInARowPage_support.set_frames("04", self.Frame2_004)

        self.Frame2_005 = tk.Frame(self.Frame1)
        self.Frame2_005.place(relx=0.402, rely=0.695, relheight=0.112
                , relwidth=0.086)
        self.Frame2_005.configure(relief='groove')
        self.Frame2_005.configure(borderwidth="2")
        self.Frame2_005.configure(relief="groove")
        self.Frame2_005.configure(background="#3c8867")
        self.Frame2_005.configure(highlightbackground="#d9d9d9")
        self.Frame2_005.configure(highlightcolor="black")
        fourInARowPage_support.set_frames("05", self.Frame2_005)

        self.Frame2_006 = tk.Frame(self.Frame1)
        self.Frame2_006.place(relx=0.516, rely=0.695, relheight=0.112
                              , relwidth=0.086)
        self.Frame2_006.configure(relief='groove')
        self.Frame2_006.configure(borderwidth="2")
        self.Frame2_006.configure(relief="groove")
        self.Frame2_006.configure(background="#3c8867")
        self.Frame2_006.configure(highlightbackground="#d9d9d9")
        self.Frame2_006.configure(highlightcolor="black")
        fourInARowPage_support.set_frames("06", self.Frame2_006)

        self.Frame2_007 = tk.Frame(self.Frame1)
        self.Frame2_007.place(relx=0.631, rely=0.695, relheight=0.112
                , relwidth=0.086)
        self.Frame2_007.configure(relief='groove')
        self.Frame2_007.configure(borderwidth="2")
        self.Frame2_007.configure(relief="groove")
        self.Frame2_007.configure(background="#3c8867")
        self.Frame2_007.configure(highlightbackground="#d9d9d9")
        self.Frame2_007.configure(highlightcolor="black")
        fourInARowPage_support.set_frames("07", self.Frame2_007)

        self.Frame2_008 = tk.Frame(self.Frame1)
        self.Frame2_008.place(relx=0.746, rely=0.695, relheight=0.112
                , relwidth=0.086)
        self.Frame2_008.configure(relief='groove')
        self.Frame2_008.configure(borderwidth="2")
        self.Frame2_008.configure(relief="groove")
        self.Frame2_008.configure(background="#3c8867")
        self.Frame2_008.configure(highlightbackground="#d9d9d9")
        self.Frame2_008.configure(highlightcolor="black")
        fourInARowPage_support.set_frames("08", self.Frame2_008)

        self.Frame2_009 = tk.Frame(self.Frame1)
        self.Frame2_009.place(relx=0.86, rely=0.695, relheight=0.112
                , relwidth=0.086)
        self.Frame2_009.configure(relief='groove')
        self.Frame2_009.configure(borderwidth="2")
        self.Frame2_009.configure(relief="groove")
        self.Frame2_009.configure(background="#3c8867")
        self.Frame2_009.configure(highlightbackground="#d9d9d9")
        self.Frame2_009.configure(highlightcolor="black")
        fourInARowPage_support.set_frames("09", self.Frame2_009)

        self.Frame2_010 = tk.Frame(self.Frame1)
        self.Frame2_010.place(relx=0.402, rely=0.571, relheight=0.112
                , relwidth=0.086)
        self.Frame2_010.configure(relief='groove')
        self.Frame2_010.configure(borderwidth="2")
        self.Frame2_010.configure(relief="groove")
        self.Frame2_010.configure(background="#3c8867")
        self.Frame2_010.configure(highlightbackground="#d9d9d9")
        self.Frame2_010.configure(highlightcolor="black")
        fourInARowPage_support.set_frames("10", self.Frame2_010)

        self.Frame2_011 = tk.Frame(self.Frame1)
        self.Frame2_011.place(relx=0.516, rely=0.571, relheight=0.112
                              , relwidth=0.086)
        self.Frame2_011.configure(relief='groove')
        self.Frame2_011.configure(borderwidth="2")
        self.Frame2_011.configure(relief="groove")
        self.Frame2_011.configure(background="#3c8867")
        self.Frame2_011.configure(highlightbackground="#d9d9d9")
        self.Frame2_011.configure(highlightcolor="black")
        fourInARowPage_support.set_frames("11", self.Frame2_011)

        self.Frame2_012 = tk.Frame(self.Frame1)
        self.Frame2_012.place(relx=0.631, rely=0.571, relheight=0.112
                              , relwidth=0.086)
        self.Frame2_012.configure(relief='groove')
        self.Frame2_012.configure(borderwidth="2")
        self.Frame2_012.configure(relief="groove")
        self.Frame2_012.configure(background="#3c8867")
        self.Frame2_012.configure(highlightbackground="#d9d9d9")
        self.Frame2_012.configure(highlightcolor="black")
        fourInARowPage_support.set_frames("12", self.Frame2_012)

        self.Frame2_013 = tk.Frame(self.Frame1)
        self.Frame2_013.place(relx=0.746, rely=0.571, relheight=0.112
                , relwidth=0.086)
        self.Frame2_013.configure(relief='groove')
        self.Frame2_013.configure(borderwidth="2")
        self.Frame2_013.configure(relief="groove")
        self.Frame2_013.configure(background="#3c8867")
        self.Frame2_013.configure(highlightbackground="#d9d9d9")
        self.Frame2_013.configure(highlightcolor="black")
        fourInARowPage_support.set_frames("13", self.Frame2_013)

        self.Frame2_014 = tk.Frame(self.Frame1)
        self.Frame2_014.place(relx=0.86, rely=0.571, relheight=0.112
                , relwidth=0.086)
        self.Frame2_014.configure(relief='groove')
        self.Frame2_014.configure(borderwidth="2")
        self.Frame2_014.configure(relief="groove")
        self.Frame2_014.configure(background="#3c8867")
        self.Frame2_014.configure(highlightbackground="#d9d9d9")
        self.Frame2_014.configure(highlightcolor="black")
        fourInARowPage_support.set_frames("14", self.Frame2_014)

        self.Frame2_015 = tk.Frame(self.Frame1)
        self.Frame2_015.place(relx=0.402, rely=0.447, relheight=0.112
                , relwidth=0.086)
        self.Frame2_015.configure(relief='groove')
        self.Frame2_015.configure(borderwidth="2")
        self.Frame2_015.configure(relief="groove")
        self.Frame2_015.configure(background="#3c8867")
        self.Frame2_015.configure(highlightbackground="#d9d9d9")
        self.Frame2_015.configure(highlightcolor="black")
        fourInARowPage_support.set_frames("15", self.Frame2_015)

        self.Frame2_016 = tk.Frame(self.Frame1)
        self.Frame2_016.place(relx=0.516, rely=0.447, relheight=0.112
                              , relwidth=0.086)
        self.Frame2_016.configure(relief='groove')
        self.Frame2_016.configure(borderwidth="2")
        self.Frame2_016.configure(relief="groove")
        self.Frame2_016.configure(background="#3c8867")
        self.Frame2_016.configure(highlightbackground="#d9d9d9")
        self.Frame2_016.configure(highlightcolor="black")
        fourInARowPage_support.set_frames("16", self.Frame2_016)

        self.Frame2_017 = tk.Frame(self.Frame1)
        self.Frame2_017.place(relx=0.631, rely=0.447, relheight=0.112
                              , relwidth=0.086)
        self.Frame2_017.configure(relief='groove')
        self.Frame2_017.configure(borderwidth="2")
        self.Frame2_017.configure(relief="groove")
        self.Frame2_017.configure(background="#3c8867")
        self.Frame2_017.configure(highlightbackground="#d9d9d9")
        self.Frame2_017.configure(highlightcolor="black")
        fourInARowPage_support.set_frames("17", self.Frame2_017)

        self.Frame2_018 = tk.Frame(self.Frame1)
        self.Frame2_018.place(relx=0.746, rely=0.447, relheight=0.112
                , relwidth=0.086)
        self.Frame2_018.configure(relief='groove')
        self.Frame2_018.configure(borderwidth="2")
        self.Frame2_018.configure(relief="groove")
        self.Frame2_018.configure(background="#3c8867")
        self.Frame2_018.configure(highlightbackground="#d9d9d9")
        self.Frame2_018.configure(highlightcolor="black")
        fourInARowPage_support.set_frames("18", self.Frame2_018)

        self.Frame2_019 = tk.Frame(self.Frame1)
        self.Frame2_019.place(relx=0.86, rely=0.447, relheight=0.112
                              , relwidth=0.086)
        self.Frame2_019.configure(relief='groove')
        self.Frame2_019.configure(borderwidth="2")
        self.Frame2_019.configure(relief="groove")
        self.Frame2_019.configure(background="#3c8867")
        self.Frame2_019.configure(highlightbackground="#d9d9d9")
        self.Frame2_019.configure(highlightcolor="black")
        fourInARowPage_support.set_frames("19", self.Frame2_019)

        self.Frame2_020 = tk.Frame(self.Frame1)
        self.Frame2_020.place(relx=0.402, rely=0.323, relheight=0.112
                , relwidth=0.086)
        self.Frame2_020.configure(relief='groove')
        self.Frame2_020.configure(borderwidth="2")
        self.Frame2_020.configure(relief="groove")
        self.Frame2_020.configure(background="#3c8867")
        self.Frame2_020.configure(highlightbackground="#d9d9d9")
        self.Frame2_020.configure(highlightcolor="black")
        fourInARowPage_support.set_frames("20", self.Frame2_020)

        self.Frame2_021 = tk.Frame(self.Frame1)
        self.Frame2_021.place(relx=0.516, rely=0.323, relheight=0.112
                , relwidth=0.086)
        self.Frame2_021.configure(relief='groove')
        self.Frame2_021.configure(borderwidth="2")
        self.Frame2_021.configure(relief="groove")
        self.Frame2_021.configure(background="#3c8867")
        self.Frame2_021.configure(highlightbackground="#d9d9d9")
        self.Frame2_021.configure(highlightcolor="black")
        fourInARowPage_support.set_frames("21", self.Frame2_021)

        self.Frame2_022 = tk.Frame(self.Frame1)
        self.Frame2_022.place(relx=0.631, rely=0.323, relheight=0.112
                , relwidth=0.086)
        self.Frame2_022.configure(relief='groove')
        self.Frame2_022.configure(borderwidth="2")
        self.Frame2_022.configure(relief="groove")
        self.Frame2_022.configure(background="#3c8867")
        self.Frame2_022.configure(highlightbackground="#d9d9d9")
        self.Frame2_022.configure(highlightcolor="black")
        fourInARowPage_support.set_frames("22", self.Frame2_022)

        self.Frame2_023 = tk.Frame(self.Frame1)
        self.Frame2_023.place(relx=0.746, rely=0.323, relheight=0.112
                , relwidth=0.086)
        self.Frame2_023.configure(relief='groove')
        self.Frame2_023.configure(borderwidth="2")
        self.Frame2_023.configure(relief="groove")
        self.Frame2_023.configure(background="#3c8867")
        self.Frame2_023.configure(highlightbackground="#d9d9d9")
        self.Frame2_023.configure(highlightcolor="black")
        fourInARowPage_support.set_frames("23", self.Frame2_023)

        self.Frame2_024 = tk.Frame(self.Frame1)
        self.Frame2_024.place(relx=0.86, rely=0.323, relheight=0.112
                , relwidth=0.086)
        self.Frame2_024.configure(relief='groove')
        self.Frame2_024.configure(borderwidth="2")
        self.Frame2_024.configure(relief="groove")
        self.Frame2_024.configure(background="#3c8867")
        self.Frame2_024.configure(highlightbackground="#d9d9d9")
        self.Frame2_024.configure(highlightcolor="black")
        fourInARowPage_support.set_frames("24", self.Frame2_024)

        self.Button0 = tk.Button(self.Frame1)
        self.Button0.place(relx=0.412, rely=0.199, height=30, width=30)
        self.Button0.configure(activebackground="#3c8867")
        self.Button0.configure(activeforeground="white")
        self.Button0.configure(activeforeground="#3c8867")
        self.Button0.configure(command=lambda: fourInARowPage_support.button_click(0))
        self.Button0.configure(background="#eb0214")
        self.Button0.configure(text="V")
        self.Button0.configure(font="-family {Tw Cen MT} -size 14 -weight bold")
        self.Button0.configure(disabledforeground="#a3a3a3")
        self.Button0.configure(foreground="#000000")
        self.Button0.configure(highlightbackground="#d9d9d9")
        self.Button0.configure(highlightcolor="black")
        self.Button0.configure(pady="0")
        fourInARowPage_support.set_button("00", self.Button0)

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.526, rely=0.199, height=30, width=30)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(command=lambda: fourInARowPage_support.button_click(1))
        self.Button1.configure(background="#eb0214")
        self.Button1.configure(text="V")
        self.Button1.configure(font="-family {Tw Cen MT} -size 14 -weight bold")
        self.Button1.configure(cursor="fleur")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        fourInARowPage_support.set_button("01", self.Button1)

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.641, rely=0.199, height=30, width=30)
        self.Button2.configure(activebackground="#f9f9f9")
        self.Button2.configure(activeforeground="black")
        self.Button2.configure(command=lambda: fourInARowPage_support.button_click(2))
        self.Button2.configure(background="#eb0214")
        self.Button2.configure(text="V")
        self.Button2.configure(font="-family {Tw Cen MT} -size 14 -weight bold")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        fourInARowPage_support.set_button("02", self.Button2)

        self.Button3 = tk.Button(self.Frame1)
        self.Button3.place(relx=0.756, rely=0.199, height=30, width=30)
        self.Button3.configure(activebackground="#f9f9f9")
        self.Button3.configure(activeforeground="black")
        self.Button3.configure(command=lambda: fourInARowPage_support.button_click(3))
        self.Button3.configure(background="#eb0214")
        self.Button3.configure(text="V")
        self.Button3.configure(font="-family {Tw Cen MT} -size 14 -weight bold")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        fourInARowPage_support.set_button("03", self.Button3)

        self.Button4 = tk.Button(self.Frame1)
        self.Button4.place(relx=0.87, rely=0.199, height=30, width=30)
        self.Button4.configure(activebackground="#f9f9f9")
        self.Button4.configure(activeforeground="black")
        self.Button4.configure(command=lambda: fourInARowPage_support.button_click(4))
        self.Button4.configure(background="#eb0214")
        self.Button4.configure(text="V")
        self.Button4.configure(font="-family {Tw Cen MT} -size 14 -weight bold")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        fourInARowPage_support.set_button("04", self.Button4)

if __name__ == '__main__':
    vp_start_gui()





