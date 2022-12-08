import tkinter
mywin = tkinter.Tk()
mywin.title("Rable Practice")

myphoto=tkinter.PhotoImage(file="picture\dog.gif")
mylabel1=tkinter.Label(mywin, image=myphoto)
mylabel1.pack()

mywin.mainloop()