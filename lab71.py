from tkinter import *
window = Tk()

button1 = Button(window, text="Button1")
button2 = Button(window, text="Button2")
button3 = Button(window, text="Button3")

button1.pack(side="left")
button2.pack(side="left")
button3.pack(side="right")

window.mainloop()