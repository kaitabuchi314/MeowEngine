from tkinter import *

class MeowEngine:
    def __init__(self):
        self.path = Tk()

        self.path.title("MeowEngine! 🐱")

        self.canvas = Canvas(self.path, width=1000, height=1000)

        self.canvas.pack()
        self.path.mainloop()

    
    def drawRect(x,y,w,h,outline,fill):
        
        self.canvas.create_rectangle(x, y, x+w, y+h,outline, fill).pack()