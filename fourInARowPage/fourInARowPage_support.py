import sys
import clientBL
import uuid


symbol = None
color = None
board = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
         "20", "21", "22", "23", "24"]
buttons = {}
frames = {}
turn = 0
_serverGameNumber = None
_page_game_number = None
_opponent_user_name = ""
_game_over = None
abort_game = True

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
import chooseGamePage

def fe_want_to_play_res(status_code, status_txt, game_number, score, opponentUsername, opponentScore, serverGameNumber):
    global w
    print('fe_want_to_play_res')
    sys.stdout.flush()
    opponent_username_Label = w.opponent_username_Label
    opponent_score_Label= w.opponent_score_Label
    user_score_Label= w.user_score_Label
    symbol_Label=w.symbol_Label
    global symbol, turn, color
    if status_code == "08":
        opponent_username_Label.configure(text=status_txt + " (" + status_code + ")")
        symbol = "X"
        color = "red"
        enable_buttons(True)
    else:
        global _opponent_user_name
        _opponent_user_name = opponentUsername
        opponent_username_Label.configure(text="your opponent is: "+opponentUsername)
        opponent_score_Label.configure(text="opponent score: " + opponentScore)
        user_score_Label.configure(text="my score: " + score)
        if symbol is None:
            symbol = "O"
            color = "yellow"
        symbol_Label.configure(text="you are: " + color)
        w.turn_Label.configure(text="red turn")
        enable_buttons(False)
        global _serverGameNumber
        _serverGameNumber = serverGameNumber
        clientBL.set_play_cell_game_callback(fe_four_in_a_row_play_res, _serverGameNumber)


def clear_dicts():
    buttons.clear()
    frames.clear()


def set_button(cell, button):
    buttons[cell] = button
    

def set_frames(cell, frame):
    frames[cell] = frame


def enable_buttons(waiting):
    for i in range(5):
        str_i = str(i).zfill(2)
        if turn == 0 and symbol == "O" or turn == 1 and symbol == "X" or waiting is True:
            buttons[str_i].configure(state='disabled', background=color)
        else:
            buttons[str_i].configure(state='normal')


def update_cell_color(cell, turn_symbol):
    if turn_symbol == "X":
        frames[str(cell).zfill(2)].configure(background="red")
    else:
        frames[str(cell).zfill(2)].configure(background="yellow")


def fe_four_in_a_row_play_res(status_code, status_txt, opponent_move, cell, score, opponent_score):
    print("fe_four_in_a_row_play_res opponent_move:" + str(opponent_move) + " cell:"+str(cell))
    global w
    # this is the opponent move
    if opponent_move == 1:
        if symbol == "X":
            board[cell] = "O"
            update_cell_color(cell, "O")
        else:
            board[cell] = "X"
            update_cell_color(cell, "X")

    if status_code == "00":
        global turn
        if turn == 0:
            turn = 1
            w.turn_Label.configure(text="yellow turn")
        else:
            turn = 0
            w.turn_Label.configure(text="red turn")
        waiting = False
        enable_buttons(waiting)
    elif status_code == "12" or status_code == "13" or status_code == "14" or status_code == "15":
        global abort_game
        abort_game = False
        startResultPage(status_code, status_txt, score, opponent_score)
    else:
        opponent_username_Label = w.opponent_username_Label
        opponent_username_Label.configure(text=status_txt)


def set_close_callback(abort_game):
    global _game_over
    _game_over = abort_game


def startResultPage(status_code, status_txt, score, opponent_score):
    sys.stdout.flush()
    sys.path.append('..\\resultPage')
    import resultPage
    import resultPage_support
    resultPage.create_Toplevel1(root, 'Hello', top_level)
    global _opponent_user_name
    print("startResultPage _opponent_user_name:"+_opponent_user_name)
    resultPage_support.set_results(status_code, status_txt, score, _opponent_user_name, opponent_score, game_over)


def button_click(col):
    print("fourInARowPage_support button_click:" + str(col))
    global symbol, w, _serverGameNumber
    finish = False
    row = 0
    cell = 0
    while not finish and row < 5:
        cell = 5*row + col
        if board[cell] == str(cell).zfill(2):
            finish = True
        else:
            row = row+1
    if finish is False:
        opponentName_Label = w.opponentName_Label
        opponentName_Label.configure(text="this row is full")
    else:
        board[cell] = symbol
        update_cell_color(cell, symbol)
    print("fourInARowPage_support click cell:" + str(cell))
    waiting = True
    enable_buttons(waiting)
    clientBL.play_cell_game(fe_four_in_a_row_play_res, _serverGameNumber, cell)


def on_close():
    print("fourInARowPage_support on_close")
    global _game_over, _serverGameNumber, _page_game_number, abort_game
    if _game_over is not None:
        if _serverGameNumber == None:
            _game_over("01", _page_game_number, abort_game, False)
        else:
            _game_over("01", _serverGameNumber, abort_game, False)


def game_over(play_again):
    destroy_window()
    global _game_over, _serverGameNumber, abort_game
    if _game_over is not None:
        _game_over("01", _serverGameNumber, abort_game, play_again)


def init(top, gui, *args, **kwargs):
    global w, top_level, root, symbol, color, board, turn, _serverGameNumber,_page_game_number,_opponent_user_name, abort_game
    w = gui
    top_level = top
    root = top
    symbol = None
    color = None
    board = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
             "18", "19",
             "20", "21", "22", "23", "24"]
    turn = 0
    _serverGameNumber = None
    _page_game_number = None
    _opponent_user_name = ""
    abort_game = True
    start_game()

def start_game():
    global _page_game_number
    _page_game_number = str(uuid.uuid4())
    clientBL.want_to_play(fe_want_to_play_res, "01", _page_game_number)


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import fourInARowPage
    fourInARowPage.vp_start_gui()




