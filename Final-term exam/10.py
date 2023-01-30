import tkinter

def transfer():
    dollar = float(mytext2.get())
    won = int(dollar*1308.50)
    mytext3 = tkinter.Label(mywin, text=f'원 : {won}')
    mytext3.place(x=75, y=150)

mywin = tkinter.Tk()
mywin.title("환율 계산기")
mywin.geometry("300x300")

mytext1 = tkinter.Label(mywin, text="달러: ", padx=0, pady=0)
mytext2 = tkinter.Entry(mywin)
mybutton = tkinter.Button(mywin, text="환율 계산", command=transfer)


mytext1.place(x=75, y=50)
mytext2.place(x=125, y=50)
mybutton.place(x=125, y=100)
'''mytext1.pack()
mytext2.pack()'''
#mybutton.pack()

mywin.mainloop()
