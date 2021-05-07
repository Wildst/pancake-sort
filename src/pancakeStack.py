from pancake import Pancake
from tkinter import *
import math

class PancakeStack(Canvas):
    def __init__(self, pancakes, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs, highlightthickness=0)
        self.pancakes = pancakes
        self.width = kwargs["width"] if "width" in kwargs else 250
        self.height = (kwargs["height"] if "height" in kwargs else 250)/len(pancakes)*0.4
        self.top_offset = (kwargs["height"] if "height" in kwargs else 250)*0.6
        self.amount = 0
        self.progress = 0
        self.draw_pancakes()

    def draw_pancakes(self):
        self.delete("all")

        angle = math.pi*self.progress/100
        ox, oy = self.width / 2, self.top_offset + self.height*self.amount/2

        for i, pancake in enumerate(self.pancakes):
            size=pancake/max(self.pancakes)

            x0 = x1 = self.width/2 - size*self.width*0.35
            y0 = y3 = self.height*.05+self.height*i + self.top_offset
            x2 = x3 = self.width/2 + size*self.width*0.35
            y1 = y2 = self.height*.95+self.height*i + self.top_offset

            if i < self.amount:
                # rotate stack
                x0, y0 = rotate(x0, y0, ox, oy, angle)
                x1, y1 = rotate(x1, y1, ox, oy, angle)
                x2, y2 = rotate(x2, y2, ox, oy, angle)
                x3, y3 = rotate(x3, y3, ox, oy, angle)
                
                # throw a stack
                y0 -= self.top_offset*math.sin(angle)*.6
                y1 -= self.top_offset*math.sin(angle)*.6
                y2 -= self.top_offset*math.sin(angle)*.6
                y3 -= self.top_offset*math.sin(angle)*.6

            self.create_polygon(
                x0, y0, x1, y1, x2, y2, x3, y3,
                fill="brown")
            self.create_oval(
                (x1+x0)/2-self.height*.45, (y0+y1)/2-self.height*.45,
                (x1+x0)/2+self.height*.45, (y0+y1)/2+self.height*.45,
                fill="brown", width=0
            )
            self.create_oval(
                (x2+x3)/2-self.height*.45, (y2+y3)/2-self.height*.45,
                (x2+x3)/2+self.height*.45, (y2+y3)/2+self.height*.45,
                fill="brown", width=0
            )
            
    def flip(self, amount):
        self.amount = amount
        self.progress = 0
        self.pancakes = self.pancakes[::-1][-amount:] + self.pancakes[amount:]
        self.run_animation()

    def run_animation(self):
        self.draw_pancakes()
        self.update()
        if self.progress < 100:
            self.after(12, self.run_animation)
        self.progress += 2
        

def rotate(x0, y0, x1, y1, angle):
    """
    p'x = cos(theta) * (px-ox) - sin(theta) * (py-oy) + ox

    p'y = sin(theta) * (px-ox) + cos(theta) * (py-oy) + oy
    """
    x2 = math.cos(angle) * (x0-x1) - math.sin(angle)*(y0-y1) + x1
    y2 = - math.sin(angle) * (x0-x1) - math.cos(angle)*(y0-y1) + y1

    return x2, y2