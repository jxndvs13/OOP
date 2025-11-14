import tkinter as tk
from tkinter import *

screen = Tk()
screen.geometry("720x500")
screen.resizable(False, False)

class Queue:
    def __init__(self, name):
        self.name = name
        self.element = []
    def enqueue(self):
        obj = QInput.get(1.0, "end-1c")
        self.element.append(obj)
        self.display()
        QInput.delete(1.0, "end-1c")
    def dequeue(self):
        remove = self.element[0]
        self.element.remove(remove)
        self.display()
    def display(self):
        QDisplay.config(state=NORMAL)
        QDisplay.delete(1.0, "end-1c")
        QDisplay.insert(tk.INSERT, f"{self.name}:")
        for i in self.element:
            QDisplay.insert(tk.INSERT, f"\n{i}")
        QDisplay.config(state=DISABLED)

class Stack:
    def __init__(self, name):
        self.name = name
        self.element = []

    def place(self):
        obj = SInput.get(1.0, "end-1c")
        self.element.append(obj)
        SInput.delete(1.0, "end-1c")
        self.display()
    def remove(self):
        self.element.pop()
        self.display()
    def display(self):
        SDisplay.config(state=NORMAL)
        list1 = []
        size = len(self.element)
        for element in self.element:
            list1.append(element)
        length1 = 20 - size
        for x in range(0, length1):
            list1.append(" ")
        list1.reverse()
        SDisplay.delete(1.0, "end-1c")
        SDisplay.insert(tk.INSERT, f"{self.name}:")
        for e in list1:
            SDisplay.insert(tk.INSERT, f"\n{e}")
        SDisplay.config(state=DISABLED)

Q1 = Queue("Queue 1")
Q2 = Queue("Queue 2")
Q3 = Queue("Queue 3")
S1 = Stack("Stack 1")
S2 = Stack("Stack 2")
S3 = Stack("Stack 3")

QDisplay = Text(screen,width=8,height=21,font=("Arial", 14))
QDisplay.place(x=250,y=15)
QInput = Text(screen,width=19,height=1,font=("Arial", 14))
QInput.place(x=15,y=15)
Q1L = Label(screen,text="Q1",font=("Arial", 14))
Q1L.place(x=30,y=50)
EnQ1 = Button(screen, width=5,text="Add",command=Q1.enqueue,font=("Arial", 14))
EnQ1.place(x=15,y=90)
DeQ1 = Button(screen, width=5,text="Take",command=Q1.dequeue,font=("Arial", 14))
DeQ1.place(x=15,y=135)
ShowQ1 = Button(screen, width=5,text="Show",command=Q1.display,font=("Arial", 14))
ShowQ1.place(x=15,y=180)
Q2L = Label(screen,text="Q2",font=("Arial", 14))
Q2L.place(x=105,y=50)
EnQ2 = Button(screen, width=5,text="Add",command=Q2.enqueue,font=("Arial", 14))
EnQ2.place(x=90,y=90)
DeQ2 = Button(screen, width=5,text="Take",command=Q2.dequeue,font=("Arial", 14))
DeQ2.place(x=90,y=135)
ShowQ2 = Button(screen, width=5,text="Show",command=Q2.display,font=("Arial", 14))
ShowQ2.place(x=90,y=180)
Q3L = Label(screen,text="Q3",font=("Arial", 14))
Q3L.place(x=180,y=50)
EnQ3 = Button(screen, width=5,text="Add",command=Q3.enqueue,font=("Arial", 14))
EnQ3.place(x=165,y=90)
DeQ3 = Button(screen, width=5,text="Take",command=Q3.dequeue,font=("Arial", 14))
DeQ3.place(x=165,y=135)
ShowQ3 = Button(screen, width=5,text="Show",command=Q3.display,font=("Arial", 14))
ShowQ3.place(x=165,y=180)
SDisplay = Text(screen,width=8,height=21,font=("Arial", 14))
SDisplay.place(x=610,y=15)
SInput = Text(screen,width=19,height=1,font=("Arial", 14))
SInput.place(x=375,y=15)
S1L = Label(screen,text="S1",font=("Arial", 14))
S1L.place(x=390,y=50)
EnS1 = Button(screen, width=5,text="Add",command=S1.place,font=("Arial", 14))
EnS1.place(x=375,y=90)
DeS1 = Button(screen, width=5,text="Take",command=S1.remove,font=("Arial", 14))
DeS1.place(x=375,y=135)
ShowS1 = Button(screen, width=5,text="Show",command=S1.display,font=("Arial", 14))
ShowS1.place(x=375,y=180)
S2L = Label(screen,text="S2",font=("Arial", 14))
S2L.place(x=465,y=50)
EnS2 = Button(screen, width=5,text="Add",command=S2.place,font=("Arial", 14))
EnS2.place(x=450,y=90)
DeS2 = Button(screen, width=5,text="Take",command=S2.remove,font=("Arial", 14))
DeS2.place(x=450,y=135)
ShowS2 = Button(screen, width=5,text="Show",command=S2.display,font=("Arial", 14))
ShowS2.place(x=450,y=180)
S3L = Label(screen,text="S3",font=("Arial", 14))
S3L.place(x=540,y=50)
EnS3 = Button(screen, width=5,text="Add",command=S3.place,font=("Arial", 14))
EnS3.place(x=525,y=90)
DeS3 = Button(screen, width=5,text="Take",command=S3.remove,font=("Arial", 14))
DeS3.place(x=525,y=135)
ShowS3 = Button(screen, width=5,text="Show",command=S3.display,font=("Arial", 14))
ShowS3.place(x=525,y=180)

Q1.display()
S1.display()

screen.mainloop()