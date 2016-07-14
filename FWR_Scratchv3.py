from Tkinter import *

win1 = Tk()

#makes the main self window stay on top of all windows
win1.attributes("-topmost", True)

label1 = Label( win1, text="Enter Data A")
E1 = Entry(win1, bd =5)

label2 = Label( win1, text="Enter Data B")
E2 = Entry(win1, show='*', bd =5)


def getData():
    print E1.get()
    print E2.get()

submit = Button(win1, text ="Submit", command = getData)

label1.pack()
E1.pack()
label2.pack()
E2.pack()
submit.pack(side =BOTTOM)
win1.title("FWR Interface")
win1.mainloop()
