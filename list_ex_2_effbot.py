from Tkinter import *

master = Tk()

listbox = Listbox(master)
listbox.pack()

listbox.insert(END, "Here is my list entry")

lb = Listbox(master)
# b1 = Button.bind(master, "<Double-Button-1", listbox.OnDouble)

#I'd like to populate this list box with the AWS package directory listing read from
# either a file on GIT or somehow listing the contents.

for item in ["file1.pkg", "file2.pkg", "file3.pkg", "file4.pkg"]:
    listbox.insert(END, item)

mainloop()
