import sys
_game_over = None

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

def set_results(status_code, status_txt, score, opponent_user_name, opponent_score, game_over):
    global w, _game_over
    print(opponent_user_name)
    if status_code == "15":
        w.answer_Label.configure(text="you win!!! opponent quit")
        w.answer_Label.configure(font="-family {Tw Cen MT} -size 24 -weight bold")
    else:
        w.answer_Label.configure(text=status_txt)
    w.userScore_Label.configure(text="your score: " + score)
    w.opponentScore_Label.configure(text=opponent_user_name + "'s score: " + opponent_score)
    _game_over = game_over


def on_close(play_again):
    global _game_over
    if _game_over is not None:
        _game_over(play_again)
    destroy_window()


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import resultPage
    resultPage.vp_start_gui()




