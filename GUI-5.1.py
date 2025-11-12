import tkinter as tk
from tkinter import *

screen = Tk()
screen.geometry("500x500")
screen.resizable(False, False)

class Stack:
    def __init__(self):
        self.element = []
    def place (self):
        obj = Input.get(1.0, "end-1c")
        self.element.append(obj)
        Input.delete(1.0, "end-1c")
        self.display()
    def remove(self):
        self.element.pop()
        self.display()
    def display(self):
        Display1.config(state=NORMAL)
        Display2.config(state=NORMAL)
        list1 = []
        list2 = []
        size = len(self.element)
        if size < 20:
            for element in self.element:
                list1.append(element)
            length1 = 20-size
            for x in range (0, length1):
                list1.append(" ")
        else:
            for x in range (0,20):
                list1.append(self.element[x])
            for y in range (0,size-20):
                list2.append(self.element[y+20])
            length2 = 40 - len(self.element)
            for x in range(0, length2):
                list2.append(" ")
        list1.reverse()
        list2.reverse()
        Display1.delete(1.0, "end-1c")
        Display2.delete(1.0, "end-1c")
        for e in list1:
            Display1.insert(tk.INSERT, f"\n{e}")
        for e in list2:
            Display2.insert(tk.INSERT, f"\n{e}")
        Display1.config(state=DISABLED)
        Display2.config(state=DISABLED)

#Main Code
S = Stack()
Display1 = Text(screen,width=10,height=21,font=("Arial", 14))
Display1.place(x=250,y=15)
Display2 = Text(screen,width=10,height=21,font=("Arial", 14))
Display2.place(x=368,y=15)
Input = Text(screen,width=19,height=1,font=("Arial", 14))
Input.place(x=15,y=15)
BPlace = Button(screen, width=18,text="Add Element",command=S.place,font=("Arial", 14))
BPlace.place(x=17,y=50)
BRemove = Button(screen, width=18,text="Take Element",command=S.remove,font=("Arial", 14))
BRemove.place(x=17,y=150)
S.display()

screen.mainloop()
