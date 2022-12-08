import tkinter

mywin = tkinter.Tk()
mywin.title("entry Practice")
mywin.geometry("300x300")
counter=0

mylabel = tkinter.Label(mywin, text="이름을 넣으세요: ")
mylabel.pack()
myentry=tkinter.Entry(mywin)
myentry.pack()

def myfunc():
    mylabel.config(text=myentry.get() + "씨 안녕하세요")

mybtn1 = tkinter.Button(mywin, text="Click Me", command=myfunc)
mybtn1.pack()

mywin.mainloop()