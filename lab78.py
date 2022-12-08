from tkinter import *

window=Tk()
window.geometry("300x400")
button1=Button(window, text="btn1")
button2=Button(window, text="btn2")
button3=Button(window, text="btn3")

button1.pack(side=RIGHT, ipadx=20, ipady=10, padx=20)
button2.pack(side=RIGHT, ipadx=20, ipady=10, padx=20)
button3.pack(side=RIGHT, ipadx=20, ipady=10, padx=20)

window.mainloop()