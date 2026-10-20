"""" 
 First project for Terra
 Simple word game
 Here we go
"""
from tkinter import *
import tkinter as tk
import random


lives = 5


def simple_word_game():

    with open("text.txt", "r", encoding="utf-8") as file:
        content = file.read().split()
        print(content)
    special_word = random.choice(content)

    # Tkinter
    root = tk.Tk()
    root.title("Simple Word Game")
    root.geometry("400x300")
    label = tk.Label(root, text="The Simple Word Game", font=("Arial", 16))
    label.pack()
    entry_answer = tk.Entry(root)
    entry_answer.pack()
    status_label = tk.Label(root, text="Start Game", font=("Arial", 12))
    status_label.pack()
    lives_label = tk.Label(root, text=lives, font=("Arial", 12))
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
    funnyButton = tk.Button(root, text="funy button", command=on_button_click)
    funnyButton.pack()
    root.mainloop()


simple_word_game()
print(lives)
