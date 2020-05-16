import sys
import clientBL

_abort_user = None

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

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def startXOPage():
    sys.stdout.flush()
    sys.path.append('..\\XOPage')
    global w
    w.button_XO.configure(state='disabled')
    import XOPage
    XOPage.create_Toplevel1(root, 'Hello', top_level)
    XOPage.set_close_callback(game_over)

def startFourInARowPage():
    sys.stdout.flush()
    sys.path.append('..\\fourInARowPage')
    global w
    w.button_4InARow.configure(state='disabled')
    import fourInARowPage
    fourInARowPage.create_Toplevel1(root, 'Hello', top_level)
    fourInARowPage.set_close_callback(game_over)


def game_over(gameid, game_number, abort_game, play_again):
    print("chooseGamePage game_over game_id:" + gameid + " game_number:" + game_number)
    global w
    if gameid == "00":
        w.button_XO.configure(state='normal')
    else:
        w.button_4InARow.configure(state='normal')

    if abort_game is True:
        clientBL.abort_game(gameid, game_number)

    if play_again:
        if gameid == "00":
            startXOPage()
        else:
            startFourInARowPage()


def set_close_callback(abort_user):
    global _abort_user
    _abort_user = abort_user

def on_close():
    global _abort_user
    if _abort_user is not None:
        _abort_user()


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import unknown
    unknown.vp_start_gui()




