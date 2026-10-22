""""
 First project for Terra
 Simple word game
 Here we go
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import random
from PIL import Image, ImageTk  # Imported from Pillow!

lives = 5


def simple_word_game():

    with open("text.txt", "r", encoding="utf-8") as file:
        content = file.read().split()
        print(content)
    special_word = random.choice(content)

    # Tkinter
    root = tk.Tk()
    root.title("Simple Word Game")
    root.geometry("400x500")
    game_icon = tk.PhotoImage(
        file=r"C:\Users\14165\OneDrive\Desktop\Word Game!\1.Word Game\nyt-wordle.png")
    root.iconphoto(False, game_icon)
    label = ttk.Label(root, text="The Simple Word Game",
                      font=("Times New Roman", 16))
    label.pack()
    empty_gridoneO = Image.open(
        r"C:\Users\14165\OneDrive\Desktop\Word Game!\1.Word Game\Empty sprite.png")
    empty_gridoneOR = empty_gridoneO.resize((70, 70), Image.Resampling.LANCZOS)
    empty_gridoneT = ImageTk.PhotoImage(empty_gridoneOR)
    image_label = tk.Label(root, image=empty_gridoneT)
    image_label.image = empty_gridoneT
    image_label.pack()
    entry_answer = ttk.Entry(root)
    entry_answer.pack()
    status_label = ttk.Label(root, text="Start Game", font=("Arial", 12))
    status_label.pack()
    lives_label = ttk.Label(root, text=lives, font=("Arial", 12))
    lives_label.pack()

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
    funnyButton.pack()
    root.mainloop()


simple_word_game()
print(lives)
