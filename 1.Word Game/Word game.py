# First project for Terra
# Simple word game
import random
# Here we go
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
count = 0
Win = False
with open("text.txt", "r", encoding="utf-8") as file:
    content = file.read().split()
    print(content)
special_word = random.choice(content)
root = tk.Tk()
root.title("Simple Word Game")
root.geometry("400x300")
label = tk.Label(root, text="Hello!", font=("Arial", 16))
label.pack()


def show_message():
    messagebox.showinfo("Success", "Funny button")


funnyButton = tk.Button(root, text="funy button", command=show_message)
funnyButton.pack()
root.mainloop()

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
