import tkinter

mywin = tkinter.Tk()
mywin.title("Rable Practice")
mywin.geometry("200x200")

def myfunc():
    messagebox.showinfo("Message", "Hello World")

myphoto=tkinter.PhotoImage(file="picture\dog.gif")
mybtn1 = tkinter.Button(mywin, image=myphoto, command=myfunc)
mybtn1.pack()

mywin.mainloop()