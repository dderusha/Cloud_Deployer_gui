from Tkinter import *

def newWin () :
    global de1, de2
    win1 = Tk()
# makes the main self window stay on top of all windows
    win1.attributes("-topmost", True)
# Framing in the widgets

    myframe1 = Frame(win1)
    myframe1.pack()

# label the widget entry box

    Label(myframe1, text="Enter in AWS Access Code").grid(row=1, column=10, sticky=W)
    de1 = StringVar()
    name = Entry(myframe1, textvariable=de1)
    name.grid(row=2, column=10, sticky=W)


    myframe2 = Frame(win1)
    myframe2.pack()

# label frame 2
    Label(myframe2, text="Enter in AWS Secret Code").grid(row=1, column=10, sticky=W)
    de2 = StringVar()
    name2 = Entry(myframe2, textvariable=de2)
    name2.grid(row=2, column=10, sticky=W)

# button in frame 3
    myframe3 = Frame(win1)
    myframe3.pack()

    b1 = Button(myframe3, text="Submit")
    b1.pack(side=RIGHT, padx=90)

    return win1

#def but1() : print "Data Submitted" # action for button click

win1 = newWin()
win1.mainloop()
