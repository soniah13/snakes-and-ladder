import tkinter as tink
from PIL import ImageTk, Image
import random


def start_playing():
    global img_d
    global btn_p, btn_c
    # player button
    btn_p.place(x=450, y=350)
    # computer button
    btn_c.place(x=600, y=350)

    # exit button
    btn_d = tink.Button(game, text='Exit Game', height=2, width=12, fg='black', bg='maroon',
                        font=('italics', 12, 'bold'), activebackground='red', command=game.destroy)
    btn_d.place(x=530, y=10)

    # Dice
    img_d = Image.open('Simages/dice.jpg')
    img_d = img_d.resize((65, 65))
    img_d = ImageTk.PhotoImage(img_d)
    btn_d = tink.Button(game, image=img_d, height=80, width=80, bg='silver')
    btn_d.place(x=550, y=150)


def reset_coins():
    global pos_player, pos_computer
    global player_c, computer_c

    player_c.place(x=10, y=420)
    computer_c.place(x=50, y=420)
    pos_player = 0
    pos_computer = 0


def load_dice():
    global Dice
    names = ['1.roll.jpg', '2.roll.jpg', '3.roll.jpg', '4.roll.jpg', '5.roll.jpg', '6.roll.jpg']
    for name in names:
        img_dice = Image.open('Simages/' + name)
        img_dice = img_dice.resize((65, 65))
        img_dice = ImageTk.PhotoImage(img_dice)
        Dice.append(img_dice)


def ladder_pos(turns):
    global pos_player, pos_computer
    global ladder

    f = 0
    if turns == 1:
        if pos_player in ladder:
            pos_player = ladder[pos_player]
            f = 1
        else:
            if pos_computer in ladder:
                pos_computer = ladder[pos_computer]
                f = 1
    return f


def snake_pos(turns):
    global pos_player, pos_computer
    global snake

    if turns == 1:
        if pos_player in snake:
            pos_player = snake[pos_player]
    else:
        if pos_computer in snake:
            pos_computer = snake[pos_computer]


def rolling_dice():
    global Dice
    global turn
    global pos_computer, pos_player
    global btn_p, btn_c
    r = random.randint(1, 6)
    btn_d = tink.Button(game, image=Dice[r - 1], height=80, width=80, bg='silver')
    btn_d.place(x=550, y=150)

    if turn == 1:
        if (pos_player+r) <= 100:
            pos_player = pos_player + r
        lad = ladder_pos(turn)
        snake_pos(turn)
        move_coin(turn, pos_player)
        if r != 6 and lad != 1:
            turn = 2
            btn_p.configure(state='disabled')
            btn_c.configure(state='normal')
    else:
        if (pos_computer+r) <= 100:
            pos_computer = pos_computer + r
        lad = ladder_pos(turn)
        snake_pos(turn)
        move_coin(turn, pos_computer)
        if r != 6 and lad != 1:
            turn = 1
            btn_p.configure(state='normal')
            btn_c.configure(state='disabled')

    show_winner()


def show_winner():
    global pos_player, pos_computer

    if pos_player == 100:
        display = 'Congratulations player, you won!'
        lab = tink.Label(game, text=display, height=4, width=40, bg='lavender', font=('italics', 30, 'bold'))
        lab.place(x=300, y=300)
        reset_coins()
    elif pos_computer == 100:
        display = 'Congratulations computer, you won!'
        lab = tink.Label(game, text=display, height=4, width=20, bg='teal', font=('italics', 30, 'bold'))
        lab.place(x=100, y=100)
        reset_coins()


def move_coin(turns, r):
    global player_c, computer_c
    global index

    if turns == 1:
        player_c.place(x=index[r][0], y=index[r][1])
    else:
        computer_c.place(x=index[r][0], y=index[r][1])


def get_index():
    global player_c, computer_c
    num = [91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
           71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
           51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
           31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    row = 20
    i = 0
    for x in range(1, 11):
        col = 20
        for y in range(1, 11):
            index[num[i]] = (col, row)
            col = col + 40
            i = i + 1
        row = row + 40


Dice = []
index = {}
pos_player = None
pos_computer = None

ladder = {5: 32, 59: 99, 75: 97}

snake = {40: 19, 46: 25, 88: 67, 91: 54}

game = tink.Tk()
game.geometry('1000x500')
game.title('Snake and Ladder game')

frame = tink.Frame(game, width=1000, height=500, relief='raised')
frame.place(x=10, y=10)

img = ImageTk.PhotoImage(Image.open('Simages/board.jpg'))
label = tink.Label(frame, image=img)
label.place(x=0, y=0)


btn_p = tink.Button(game, text='player', height=2, width=10, fg='black', bg='violet', font=('italics', 12, 'bold'),
                    activebackground='lavender', command=rolling_dice)
btn_c = tink.Button(game, text='computer', height=2, width=10, fg='black', bg='indigo', font=('italics', 12, 'bold'),
                    activebackground='blue', command=rolling_dice)

# playing coin
player_c = tink.Canvas(game, width=20, height=20)
player_c.create_rectangle(0, 0, 20, 20, fill='violet')

# computer coin
computer_c = tink.Canvas(game, width=20, height=20)
computer_c.create_rectangle(0, 0, 20, 20, fill='indigo')

turn = 1

load_dice()

reset_coins()

get_index()

start_playing()

game.mainloop()
