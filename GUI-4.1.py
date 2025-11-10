import tkinter as tk
from tkinter import *

screen = Tk()
screen.geometry("500x500")
screen.resizable(False, False)

class Queue:
    def __init__(self):
        self.element = []
    def enqueue (self):
        obj = Input.get(1.0, "end-1c")
        self.element.append(obj)
        Display.delete(1.0, "end-1c")
        Display.insert(tk.INSERT, "Queue:")
        for i in Q.element:
            Display.insert(tk.INSERT, f"\n{i}")
        Input.delete(1.0, "end-1c")
    def dequeue (self):
        remove = self.element[0]
        self.element.remove(remove)
        Display.delete(1.0, "end-1c")
        Display.insert(tk.INSERT, "Queue:")
        for i in Q.element:
            Display.insert(tk.INSERT, f"\n{i}")
    def pop(self):
        self.element.pop()
        Display.delete(1.0, "end-1c")
        Display.insert(tk.INSERT, "Queue:")
        for i in Q.element:
            Display.insert(tk.INSERT, f"\n{i}")

#Main Code
Q = Queue()
Display = Text(screen,width=21,height=21,font=("Arial", 14))
Display.place(x=250,y=15)
Input = Text(screen,width=19,height=1,font=("Arial", 14))
Input.place(x=15,y=15)
#BCreate = Button(screen, text = "Create Queue", command = Queue.__init__, font=("Arial", 14))
#BCreate.place(x=100, y=100)
BEnqueue = Button(screen, width=18,text="Enqueue Element",command=Q.enqueue,font=("Arial", 14))
BEnqueue.place(x=17,y=50)
BDequeue = Button(screen, width=18,text="Dequeue Element",command=Q.dequeue,font=("Arial", 14))
BDequeue.place(x=17,y=100)
BUndo = Button(screen, width=18,text="Remove Last Element",command=Q.pop,font=("Arial", 14))
BUndo.place(x=17,y=150)

Display.delete(1.0, "end-1c")
Display.insert(tk.INSERT, "Queue:")
for i in Q.element:
    Display.insert(tk.INSERT, f"\n{i}")

screen.mainloop()