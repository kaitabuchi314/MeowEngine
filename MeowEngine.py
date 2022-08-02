from tkinter import *

class MeowEngine:
    def __init__(self):
        self.path = Tk()

        self.path.title("MeowEngine! 🐱")

        self.canvas = Canvas(self.path, width=1000, height=1000)

        self.canvas.pack()
        self.path.mainloop()

    def drawLine(self, x1,y1,x2,y2):
        self.canvas.create_line(x1, y1, x2, y2)
    def drawRect(self, x,y,w,h,outline,fill):
        self.canvas.create_rectangle(x, y, x+w, y+h,outline=outline, fill=fill)