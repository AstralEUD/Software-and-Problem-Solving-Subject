import tkinter

mywin = tkinter.Tk()
mywin.title("Rable Practice")
mywin.geometry("200x200")

def myfunc():
    mylabel1=tkinter.Label(mywin, text="Hello World")
    mylabel1.pack()

mybtn1 = tkinter.Button(mywin, text="Click Me", command=myfunc)
mybtn1.pack()

mywin.mainloop()