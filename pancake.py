from tkinter import *
from turtle import width

class Pancake(Canvas):
    def __init__(self, size, width, height, *args, **kwords):
        Canvas.__init__(self, width = width,height=height, highlightthickness=0, bg="white", *args, **kwords)
        self.size = size