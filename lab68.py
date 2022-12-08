import tkinter
from tkinter import messagebox

mywin = tkinter.Tk()
mywin.title("체크버튼 연습")

def myfunc():
    if chk.get()==1:
        messagebox.showinfo("Message", "체크버튼이 선택되었습니다.")
    elif chk.get()==0:
        messagebox.showinfo("Message", "체크버튼이 선택되지 않았습니다.")

chk = tkinter.IntVar()
mychk = tkinter.Checkbutton(mywin, text="체크버튼", variable=chk, command=myfunc)
mychk.pack()

mywin.mainloop()