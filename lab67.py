import tkinter

mywin = tkinter.Tk()
mywin.title("Rable Practice")
mywin.geometry("200x200")
counter = 0

mylabel = tkinter.Label(mywin, text=str(counter))
mylabel.pack()

def myfunc():
    global counter
    counter += 1
    mylabel.config(text=str(counter))

mybtn1 = tkinter.Button(mywin, text="Click Me", command=myfunc)
mybtn1.pack()

mywin.mainloop()