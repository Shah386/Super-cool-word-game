""""
 First project for Terra
 Simple word game
 Here we go
"""
# Tomorrow, Try to fix the letter system
import os
import tkinter as tk
import random
import sys
from tkinter import font as tkfont
import pyglet
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *


from PIL import Image, ImageTk  # Imported from Pillow!


lives = 5
rows = 5
coloumns = 5
player_row = 0
player_col = 0
grid_position = {}
xpos = 130
ypos = 190
start = 0
end = start + 5
player_rows = 1


def simple_word_game():
    global coloumns, player_rows, xpos, ypos, lives
    with open("text.txt", "r", encoding="utf-8") as file:
        content = file.read().split()
        print(content)
    special_word = random.choice(content)

    # Tkinter
    root = tk.Tk()
    root.title("Simple Word Game")
    root.geometry("800x1000")
    root.resizable(False, False)

    def restart_program():
        root.destroy()
        os.execl(sys.executable, sys.executable, *sys.argv)
    # Game Icon
    game_icon = tk.PhotoImage(
        file=r"C:\Users\14165\OneDrive\Desktop\Word Game!\1.Word Game\nyt-wordle.png")
    root.iconphoto(False, game_icon)
    # Custom Font
    font_path = os.path.abspath(
        r"C:\Users\14165\OneDrive\Desktop\Word Game!\1.Word Game\augiepixel.ttf")
    pyglet.options["win32_gdi_font"] = True
    pyglet.font.add_file(font_path)
    game_font = tkfont.Font(family="augiepixel", size=15, weight="bold")
    # colorings
    root.config(bg="lightblue")
    # watermark
    intro_watermark = tk.Label(
        root, text="made by \n Shah", anchor="center", bg="#ADD8E6", fg="#FFAC1C", font="augiepixel")
    intro_watermark.place(x=360, y=900)
    # Widgets
    top_label = tk.Label(root, text="The Simple Word Game",
                         font=("augiepixel", 30), bg="#ADD8E6",  fg="#FFAC1C", anchor="center")
    top_label.place(x=230, y=10)
    entry_answer = tk.Entry(root)
    entry_answer.place(x=400, y=100, anchor="center")
    status_label = tk.Label(root, text="Start Game",
                            font=("augiepixel", 30), bg="#ADD8E6",  fg="#FFAC1C")
    status_label.place(x=400, y=70, anchor="center")
    lives_label = tk.Label(root, text=f"Lives: {lives}", font=(
        "augiepixel", 30), bg="#ADD8E6", fg="#FFAC1C")
    lives_label.place(x=400, y=140, anchor="center")
    hint_label = tk.Label(root, text="_____________",
                          font=("augiepixel", 30), bg="#ADD8E6",  fg="#FFAC1C", anchor="center")
    hint_label.place(x=300, y=800)
    word_label = tk.Label(root, text=content, font=(
        "augiepixel", 10), bg="#ADD8E6",  fg="#FFAC1C", wraplength=350, anchor="center")
    word_label.place(x=220, y=930)
    # The Empty Grid
    grid_frame = tk.Frame(root)
    grid_frame.pack(expand=True, side="top", pady=150, anchor="n")
    empty_gridoneO = Image.open(
        r"C:\Users\14165\OneDrive\Desktop\Word Game!\1.Word Game\Empty sprite.png")
    empty_gridoneOR = empty_gridoneO.resize(
        (125, 125), Image.Resampling.LANCZOS)
    empty_gridoneT = ImageTk.PhotoImage(empty_gridoneOR)
    for row_amount in range(rows):
        for column_amount in range(coloumns):
            image_label = tk.Label(
                grid_frame, image=empty_gridoneT, bg="#ADD8E6")
            image_label.grid(
                row=row_amount, column=column_amount)
            grid_position[f"{column_amount},{row_amount}"] = image_label.grid_info()
    # The words to go in the grid
    grid_labels = [tk.Label(root, text=str(i), font=(
        "augiepixel", 30), anchor="center") for i in range(1, 27)]

    def makeletters(word):
        global xpos, ypos, player_rows
        player_rows
        xpos = 130
        if player_rows == 1:
            ypos = 190
            for elabel, letters in zip(grid_labels[0:5], word):
                elabel.place(x=xpos, y=ypos)
                elabel.config(text=letters, bg="#ADD8E6", fg="#FFAC1C")
                xpos += 130
                print(xpos)

        if player_rows == 2:
            ypos = 320
            for elabel, letters in zip(grid_labels[6:11], word):
                elabel.place(x=xpos, y=ypos)
                elabel.config(text=letters, bg="#ADD8E6", fg="#FFAC1C")
                xpos += 130

        if player_rows == 3:
            ypos = 450
            for elabel, letters in zip(grid_labels[11:16], word):
                elabel.place(x=xpos, y=ypos)
                elabel.config(text=letters, bg="#ADD8E6", fg="#FFAC1C")
                xpos += 130
            print(xpos)

        if player_rows == 4:
            ypos = 580
            for elabel, letters in zip(grid_labels[16:21], word):
                elabel.place(x=xpos, y=ypos)
                xpos += 130
                elabel.config(text=letters, bg="#ADD8E6", fg="#FFAC1C")
            print(xpos)
        if player_rows == 5:
            ypos = 710
            for elabel, letters in zip(grid_labels[21:], word):
                elabel.place(x=xpos, y=ypos)
                elabel.config(text=letters, bg="#ADD8E6", fg="#FFAC1C")
                xpos += 130
            print(xpos)
        if xpos >= 780:
            xpos = 130
            player_rows += 1

    def on_button_click():
        global lives
        ansletters = list(special_word)
        answer = entry_answer.get()
        answer = answer.upper()
        makeletters(answer)
        print(answer)
        count = 0
        print(special_word)
        if lives > 0:
            for letter in answer:
                count += 1
            if int(count) > 5 or int(count) < 5:
                print("5!")
            else:
                if answer == special_word:
                    status_label.config(
                        text="Correct!", bg="#ADD8E6", fg="#00F700")
                    restart_button = tk.Button(root, text="Exit", command=restart_program,
                                               bg="#ADD8E6", fg="#FFAC1C", anchor="center", font="augiepixel")
                    restart_button.place(x=400, y=900)
                else:
                    status_label.config(text="Incorrect!",
                                        bg="#ADD8E6", fg="#EE4B2B")
                    lives -= 1
                    lives_label.config(text=lives)
                    count = 0
                    hint = random.choice(ansletters)
                    hint_label.config(text=f"Word Contains {hint}")
        else:
            status_label.config(text=f"The answer was{special_word}")
            restart_button = tk.Button(
                root, text="Exit", command=restart_program, bg="#ADD8E6", fg="#FFAC1C", anchor="center", font="augiepixel")
            restart_button.place(x=400, y=900)

    funnyButton = ttk.Button(root, text="Answer", command=on_button_click)
    funnyButton.place(x=400, y=250, anchor="center")

    root.mainloop()


simple_word_game()
print(lives)
