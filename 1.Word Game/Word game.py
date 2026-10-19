# First project for Terra
# Simple word game
"""Changes



"""
import random
# Here we go
import tkinter as tk
count = 0
Win = False
with open("text.txt", "r", encoding="utf-8") as file:
    content = file.read().split()
    print(content)
special_word = random.choice(content)
root = tk.Tk()
root.title("Simple Word Game")
root.geometry("400x300")
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
