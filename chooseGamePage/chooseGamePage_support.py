import sys
import clientBL
import json
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
    clientBL.top_scores(fe_top_scores_res)

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


def fe_top_scores_res(status_code, status_txt, top_scores_str):
    global w
    print('fe_top_scores_res')
    sys.stdout.flush()
    top_xo_scores = ""
    top_four_in_a_row_scores = ""
    print(top_scores_str)
    rows = json.loads(top_scores_str)
    for row in rows:
        if row[1] == 0:
            top_xo_scores = top_xo_scores + "\n" + row[0] + ": " + str(row[2])
        else:
            top_four_in_a_row_scores = top_four_in_a_row_scores + "\n" + row[0] + ": " + str(row[2])
    src = w.label_top_XO_scores
    src.configure(text="top xo scores:"+top_xo_scores)
    src = w.label_top_four_in_a_row_scores
    src.configure(text="top four in a row scores:"+top_four_in_a_row_scores)


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




