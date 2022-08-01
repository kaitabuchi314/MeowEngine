from tkinter import *

class MeowEngine:
    def __init__(self):

        path = Tk()

        path.title("MeowEngine! 🐱")

        canvas = Canvas(path, width=1000, height=1000, background="#333332")



        canvas.pack()
        path.mainloop()

    def __init__(self,isEnabled):
            self.enabled = isEnabled
        
    def drawRect(x,y,w,h,outline,fill):
        if self.isEnabled:
            self.canvas.create_rectangle(x, y, w, h,outline=outline, fill=fill)