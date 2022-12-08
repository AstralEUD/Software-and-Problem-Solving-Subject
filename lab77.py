from tkinter import *

window=Tk()
window.geometry("300x400")
button1=Button(window, text="btn1")
button2=Button(window, text="btn2")
button3=Button(window, text="btn3")

button1.pack(side=TOP, ipadx=10, ipady=10)
button2.pack(side=TOP, ipadx=20, ipady=20)
button3.pack(side=TOP, ipadx=30, ipady=30)
window.mainloop()