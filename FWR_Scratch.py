#!/usr/bin/python
import Tkinter
#import base64



class fwrClass1_tk(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)

        self.parent = parent
        self.initialize()
# makes the main self window stay on top of all windows
        self.attributes("-topmost", True)
        bgColor = "#EDEDED"

        #gif = Tkinter.PhotoImage(data = FWgif)
        #displayGif = Tkinter.Label(self.parent, image = gif, borderwidth = 10, bg = bgColor).grid(row = 5, rowspan = 6, columnspan = 2)
    def initialize(self):
        self.grid()
# first create the widget second add it to a layout manager entry.bind pressing retrun
# show='*' to read the value of the text field and display it in the blue label, create a Tkinter variable again, so that we can do self.entryVariable.get()
        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable=self.entryVariable)
        self.entry.grid(row=1, column=0, sticky='EW')
        #self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set("Text Goes Here Ernest")
# add some buttons, command=self.OnBUttonClick- will do something when the button is clicked  relief = 'sunken',
        button = Tkinter.Button(self, text="Go away", command=self.OnButtonClick)
        button.grid(column=1, row=1)
# add a label banner, anchor="w" means that the text should be left aligned in the label
# span it across two cells (so that it appears below the text field and the button.): This is the columnspan=2 parameter
        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self, textvariable=self.labelVariable, anchor="w", fg="white", bg="red")
        label.grid(column=0, row=2,columnspan=2, sticky='EW')
        self.labelVariable.set("Hello U!")
# tell the layout manager to resize its columns and rows when the window is resized - only the first column is 0
        self.grid_columnconfigure(0,weight=1)
# prevent vertical resizing
        self.resizable(True, False)
# we fix the size of the window by setting the window size to its own size (self.geometry(self.geometry()))
# we perform an update() to make sure Tkinter has finished rendering all widgets and evaluating their size
        self.update()
        self.geometry(self.geometry())
        self.entry.focus_set()
# after entry, end the application
        self.entry.select_range(0, Tkinter.END)

    # there are different classes (called layout managers) capable of placing the widgets in containers in different ways. Some are more flexible than others. Each container (window, pane, tab, dialog...) can have its own layout manager.the grid layout manager. It's a simple grid where you put your widgets, just like you would place things in a spreadsheet (Excel, OpenOffice Calc...).For example: Put a button at column 2, row 1.  Pur a checkbox at column 5, row 3.  etc.
    # calling self.grid() will simply create the grid layout manager, and tell our window to use it
    # define the button click Event handlers are methods which will be called when something happens in the GUI
    def OnButtonClick(self):
    #print "you clicky button"
            #self.labelVariable = Tkinter.StringVar()
            #label = Tkinter.Label(self, textvariable=self.labelVariable, anchor="w", fg="white", bg="blue")
            #self.labelVariable.set("You Clicked the Button")
            #print self.labelVariable
# We first set the focus in this element focus_set()
# then select all the text selection_range()
        self.labelVariable.set( self.entryVariable.get()+" (You clicked the button)")
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)


if __name__ == "__main__":
    app = fwrClass1_tk(None)
    app.title('FWR')
    app.mainloop()
