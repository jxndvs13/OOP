#CALCULATOR
import tkinter as tk
from tkinter import *

top = Tk()
top.geometry("350x400")
top.resizable(False,False)

answer = Text(width=17,height=1,font=("Arial",25))
answer.place(x=20,y=20)

done = 0

def show(x):
    global done
    if done == 1:
        answer.delete(1.0,END)
        done = 0
    try:
        if x == "=":
            final_answer = eval(answer.get(1.0, "end-1c"))
            answer.insert(tk.INSERT,x)
            answer.insert(tk.INSERT,final_answer)
            done = 1
        else:
            answer.insert(tk.INSERT, x)
        if x =="C":
            answer.delete(1.0, END)
    except:
        answer.delete(1.0, END)

B1 = Button(top,text="1",width=8,height=4,command=lambda:show("1"))
B1.place(x=20,y=70)

B2 = Button(top,text="2",width=8,height=4,command=lambda:show("2"))
B2.place(x=100,y=70)

B3 = Button(top,text="3",width=8,height=4,command=lambda:show("3"))
B3.place(x=180,y=70)

B4 = Button(top,text="4",width=8,height=4,command=lambda:show("4"))
B4.place(x=20,y=150)

B5 = Button(top,text="5",width=8,height=4,command=lambda:show("5"))
B5.place(x=100,y=150)

B6 = Button(top,text="6",width=8,height=4,command=lambda:show("6"))
B6.place(x=180,y=150)

B7 = Button(top,text="7",width=8,height=4,command=lambda:show("7"))
B7.place(x=20,y=230)

B8 = Button(top,text="8",width=8,height=4,command=lambda:show("8"))
B8.place(x=100,y=230)

B9 = Button(top,text="9",width=8,height=4,command=lambda:show("9"))
B9.place(x=180,y=230)

B0 = Button(top,text="0",width=8,height=4,command=lambda:show("0"))
B0.place(x=20,y=310)

BPlus = Button(top,text="+",width=8,height=4,command=lambda:show("+"))
BPlus.place(x=260,y=70)

BMinus = Button(top,text="-",width=8,height=4,command=lambda:show("-"))
BMinus.place(x=260,y=150)

BMult = Button(top,text="x",width=8,height=4,command=lambda:show("*"))
BMult.place(x=260,y=230)

BDivide = Button(top,text="/",width=8,height=4,command=lambda:show("/"))
BDivide.place(x=260,y=310)

BEquals = Button(top,text="=",width=8,height=4,command=lambda:show("="))
BEquals.place(x=100,y=310)

BClear = Button(top,text="C",width=8,height=4,command=lambda:show("C"))
BClear.place(x=180,y=310)

top.mainloop()