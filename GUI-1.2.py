import tkinter

root = tkinter.Tk()
root.resizable(False,False)

#create canvas
myCanvas = tkinter.Canvas(root,bg="floral white",height=450,width=450)

#                             x1y1 x2 y2
face = myCanvas.create_oval(50,50,400,400,fill="gold")
eye1 = myCanvas.create_oval(150,150,175,175,fill="black")
eye2 = myCanvas.create_oval(275,150,300,175,fill="black")
mouth = myCanvas.create_rectangle(175,290,275,300,fill="black")

myCanvas.pack()
root.mainloop()