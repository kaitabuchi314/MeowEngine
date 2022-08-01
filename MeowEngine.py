from tkinter import *

class MeowEngine:
    def __init__(self):
        self.path = Tk()

        self.path.title("MeowEngine! 🐱")

        self.canvas = Canvas(self.path, width=1000, height=1000, background="#333332")

        self.canvas.pack()
        self.path.mainloop()

    
    def drawRect(x,y,w,h,outline,fill):
        
        self.canvas.create_rectangle(x, y, w, h,outline, fill)