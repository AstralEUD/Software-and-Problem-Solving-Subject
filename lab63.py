import tkinter
mywin = tkinter.Tk()
mywin.title("Rable Practice")
mywin.geometry("200x200")

mylabel1 = tkinter.Label(mywin, text="Hello World")
mylabel2 = tkinter.Label(mywin, text="Stay Hard", font=("궁서체",30), fg="blue")
mylabel3 = tkinter.Label(mywin, text="Study", bg="magenta", width=20, height=5, anchor=tkinter.NE)

mylabel1.pack()
mylabel2.pack()
mylabel3.pack()

mywin.mainloop()