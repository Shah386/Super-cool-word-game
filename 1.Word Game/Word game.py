""""
 First project for Terra
 Simple word game
 Here we go
"""
import os
import tkinter as tk
import random
from tkinter import font as tkfont
import pyglet
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *


from PIL import Image, ImageTk  # Imported from Pillow!


lives = 5
rows = 5
coloumns = 5


def simple_word_game():

    with open("text.txt", "r", encoding="utf-8") as file:
        content = file.read().split()
        print(content)
    special_word = random.choice(content)
    global rows
    # Tkinter
    root = tk.Tk()
    root.title("Simple Word Game")
    root.geometry("800x1000")
    root.resizable(False, False)
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
    # Title
    label = ttk.Label(root, text="The Simple Word Game",
                      font=("Times New Roman", 16))
    label.place(x=400, y=50, anchor="center")
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
            image_label = tk.Label(grid_frame, image=empty_gridoneT)
            image_label.grid(
                row=row_amount, column=column_amount)
    # The words to go in the grid
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_label = tk.Label(root, font="augiepixel", text="Placeholder")
    key_label.place(x=400, y=900)

    def key_press(event):
        key_label.config(text=event.char)
    for letter in letters:
        root.bind(letter, key_press)
    # Placeholder labels
    entry_answer = ttk.Entry(root)
    entry_answer.place(x=400, y=100, anchor="center")
    status_label = ttk.Label(root, text="Start Game", font=("comicsans", 12))
    status_label.place(x=400, y=120, anchor="center")
    lives_label = ttk.Label(root, text=lives, font=("augiepixel", 20))
    lives_label.place(x=400, y=140, anchor="center")

    def on_button_click():
        global lives
        answer = entry_answer.get()
        answer = answer.upper()
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
                    status_label.config(text="Correct!")
                    Win = True
                else:
                    status_label.config(text="Incorrect!")
                    lives -= 1
                    lives_label.config(text=lives)
        else:
            print("You ran out of lives!")
    funnyButton = ttk.Button(root, text="funy button", command=on_button_click)
    funnyButton.place(x=400, y=250, anchor="center")
    root.mainloop()


simple_word_game()
print(lives)
