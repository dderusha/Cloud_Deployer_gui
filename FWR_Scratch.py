#!/usr/bin/python
import Tkinter

class fwrClass1_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self(grid)

if __name__ == "__main__":
    app = fwrClass1_tk(None)
    app.title('FileWave Remote')
    app.mainloop()
