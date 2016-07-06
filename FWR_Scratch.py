#!/usr/bin/python
import Tkinter
#import base64


class fwrClass1_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
# there are different classes (called layout managers) capable of placing the widgets in containers in different ways. Some are more flexible than others. Each container (window, pane, tab, dialog...) can have its own layout manager.the grid layout manager. It's a simple grid where you put your widgets, just like you would place things in a spreadsheet (Excel, OpenOffice Calc...).For example: Put a button at column 2, row 1.  Pur a checkbox at column 5, row 3.  etc.
# calling self.grid() will simply create the grid layout manager, and tell our window to use it
# define the button click Event handlers are methods which will be called when something happens in the GUI
    def OnButtonClick(self):
        print "you clicky button"

    def OnPressEnter(self,event):
        print "You pressed the enter key"

    def initialize(self):
        self.grid()
# first create the widget second add it to a layout manager entry.bind pressing retrun
        self.entry = Tkinter.Entry(self, show='*')
        self.entry.grid(column=0, row=0, sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
# add some buttons, command=self.OnBUttonClick- will do something when the button is clicked
        button = Tkinter.Button(self, text="Go away", relief = 'sunken', command=self.OnButtonClick)
        button.grid(column=1, row=0)
# add a label banner, anchor="w" means that the text should be left aligned in the label
# span it across two cells (so that it appears below the text field and the button.): This is the columnspan=2 parameter
        label = Tkinter.Label(self, anchor="w", fg="white", bg="red")
        label.grid(column=0, row=1,columnspan=2, sticky='EW')
# tell the layout manager to resize its columns and rows when the window is resized - only the first column is 0
        self.grid_columnconfigure(0,weight=1)
# prevent vertical resizing
        self.resizable(True, False)






if __name__ == "__main__":
    app = fwrClass1_tk(None)
    app.title('FileWave Remote')
    app.mainloop()
