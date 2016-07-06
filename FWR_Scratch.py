#!/usr/bin/python
import Tkinter

class fwrClass1_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
# there are different classes (called layout managers) capable of placing the widgets in containers in different ways. Some are more flexible than others. Each container (window, pane, tab, dialog...) can have its own layout manager.the grid layout manager. It's a simple grid where you put your widgets, just like you would place things in a spreadsheet (Excel, OpenOffice Calc...).For example: Put a button at column 2, row 1.  Pur a checkbox at column 5, row 3.  etc.
    def initialize(self):
        self.grid()

if __name__ == "__main__":
    app = fwrClass1_tk(None)
    app.title('FileWave Remote')
    app.mainloop()
