from datetime import time
from tkinter import *
from pancakeStack import PancakeStack
import random

def sort_pancakes(n):
    if n == 1:
        return
    best = 0
    pancakes = stack.pancakes
    for i, pancake in enumerate(pancakes[:n]):
        if pancake > pancakes[best]:
            best = i
    if best == 0:
        root.after(0, lambda: stack.flip(n))
        root.after(2000, lambda: sort_pancakes(n-1))
    elif best != n-1:
        stack.flip(best+1)
        root.after(2000, lambda: stack.flip(n))
        root.after(4000, lambda: sort_pancakes(n-1))
    else:
        root.after(0, lambda: sort_pancakes(n-1))


root = Tk()
root.title("Pancake sort")
root.geometry("1600x1000")


pancakes = []
for _ in range(10):
    pancakes.append(random.randint(1,100))
stack = PancakeStack(pancakes, root, bg="white", width=1200, height=1000)
stack.pack(anchor="e", expand=True)
root.after(2000, lambda: sort_pancakes(len(pancakes)))
root.mainloop()
