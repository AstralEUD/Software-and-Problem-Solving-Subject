import tkinter
frameList = ["canada0.gif","canada1.gif","canada2.gif","canada3.gif","canada4.gif","canada5.gif","canada6.gif"]
photoNum = 0

def clickNext():
    global photoNum
    photoNum += 1
    if photoNum > 6:
        photoNum = 0
    photo = tkinter.PhotoImage(file="gif/"+frameList[photoNum])
    pLabel.config(image=photo)
    pLabel.image = photo

def clickPrev():
    global photoNum
    photoNum -= 1
    if photoNum < 0:
        photoNum = 6
    photo = tkinter.PhotoImage(file="gif/"+frameList[photoNum])
    pLabel.config(image=photo)
    pLabel.image = photo
window=tkinter.Tk()
window.geometry("730x950")
window.title("Canada")

btnPrev = tkinter.Button(window, text="Prev", command=clickPrev)
btnNext = tkinter.Button(window, text="Next", command=clickNext)

photo = tkinter.PhotoImage(file="gif/"+frameList[0])
pLabel = tkinter.Label(window, image=photo)

btnPrev.place(x=250, y=10)
btnNext.place(x=400, y=10)
pLabel.place(x=15, y=50)

window.mainloop()

