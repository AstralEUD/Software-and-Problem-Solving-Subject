from tkinter import *

window=Tk()
window.geometry("300x400")
button1=Button(window, text="btn1")
button2=Button(window, text="btn2")
button3=Button(window, text="btn3")
button4=Button(window, text="btn4")

button1.pack(side=LEFT, fill=X)
button2.pack(side=RIGHT, fill=X)
button3.pack(side=TOP, fill=X)
button4.pack(side=BOTTOM, fill=X)

window.mainloop()