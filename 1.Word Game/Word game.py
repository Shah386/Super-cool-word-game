"""" 
 First project for Terra
 Simple word game
 Here we go
"""
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import time

count = 0
Win = False
with open("text.txt", "r", encoding="utf-8") as file:
    content = file.read().split()
    print(content)
special_word = random.choice(content)
while Win is False:
    count = 0
    print(special_word)
    guess = input("Choose a 5 letter word: ")
    for letter in guess:
        count += 1
    if int(count) > 5 or int(count) < 5:
        print("5!")
    else:
        if guess == special_word:
            print("Correct!")
            Win = True
        else:
            print("incorrect")
            continue

# Tkinter
root = tk.Tk()
root.title("Simple Word Game")
root.geometry("400x300")
label = tk.Label(root, text="The Simple Word Game", font=("Arial", 16))
label.pack()
entry_answer = tk.Entry(root)
entry_answer.pack()


def on_button_click():
    answer = entry_answer.get()
    print(answer)


status_label = tk.Label(root, text="waiting for click", font=("Arial", 12))
status_label.pack()

funnyButton = tk.Button(root, text="funy button", command=on_button_click)
funnyButton.pack()
root.mainloop()
