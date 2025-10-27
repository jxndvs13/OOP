import tkinter

root = tkinter.Tk()
root.resizable(False, False)

myCanvas = tkinter.Canvas(root, bg="white", height=600, width=800)

shape1 = myCanvas.create_oval(20, 20, 100, 100, fill="blue")
shape1 = myCanvas.create_oval(20, 20, 100, 100, fill="red")

#initialize the constants xx, yy
bxx = 3
byy = 3 * bxx / 5
rxx = 5
ryy = 5 * rxx / 3

def move_blue():
    global bxx, byy

    #move the shape with the constant xx, yy
    myCanvas.move(shape1, bxx, byy)

    #get the current coordinates of the shape
    (x1, y1, x2, y2) = myCanvas.coords(shape1)

    #check the boundaries of the coordinates and change the constants xx, yy
    if x1 <= 0 or x2 >= 800:
        bxx = -bxx

    if y1 <= 0 or y2 >= 600:
        byy = -byy

def move_red():
    global rxx, ryy

    #move the shape with the constant xx, yy
    myCanvas.move(shape1, rxx, ryy)

    #get the current coordinates of the shape
    (x1, y1, x2, y2) = myCanvas.coords(shape1)

    #check the boundaries of the coordinates and change the constants xx, yy
    if x1 <= 0 or x2 >= 800:
        rxx = -rxx

    if y1 <= 0 or y2 >= 600:
        ryy = -ryy

#in the main program call the function move_shape()
myCanvas.after(1,move_blue())
myCanvas.after(1,move_red())

while True:
    myCanvas.after(1,move_blue())
    myCanvas.after(1,move_red())
    myCanvas.pack()
    root.mainloop()