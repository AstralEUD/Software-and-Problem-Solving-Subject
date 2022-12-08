from tkinter import *

window=Tk()
window.geometry("300x400")
button1=Button(window, text="btn1")
button2=Button(window, text="btn2")
button3=Button(window, text="btn3")

button1.pack(side=TOP, fill=X, padx=30, pady=30)
button2.pack(side=TOP, fill=X, padx=30, pady=30)
button3.pack(side=TOP, fill=X, padx=30, pady=30)
window.mainloop()