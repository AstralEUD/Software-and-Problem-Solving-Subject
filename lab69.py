import tkinter
from tkinter import messagebox

mywin = tkinter.Tk()
mywin.title("체크버튼 연습")


def myfunc():
    if var.get()==1:
        messagebox.showinfo("", "파이썬이 선택되었어요")
    elif var.get()==2:
        messagebox.showinfo("", "랩터가 선택되었어요")
    elif var.get()==3:
        messagebox.showinfo("", "자바가 선택되었어요")
    elif var.get()==4:
        messagebox.showinfo("", "C++이 선택되었어요")

var = tkinter.IntVar()
myRdbtn1 = tkinter.Radiobutton(mywin, text="파이썬", variable=var, value=1, command=myfunc)
myRdbtn1.pack()
myRdbtn2 = tkinter.Radiobutton(mywin, text="랩터", variable=var, value=2, command=myfunc)
myRdbtn2.pack()
myRdbtn3 = tkinter.Radiobutton(mywin, text="자바", variable=var, value=3, command=myfunc)
myRdbtn3.pack()
myRdbtn4 = tkinter.Radiobutton(mywin, text="C++", variable=var, value=4, command=myfunc)
myRdbtn4.pack()
mywin.mainloop()