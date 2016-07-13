from Tkinter import *
win = tk ()

class EntryApp(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()

        tk.Label(self, text="This is a normal text entry box").pack()

        self.entry = tk.Entry(self, bg='white')
        self.entry.pack()

        tk.Label(self, text="This is a secret text entry box for passwords").pack()

        self.secret_entry = tk.Entry(self, show='*', bg='white')
        self.secret_entry.pack()

        tk.Button(self, text='OK', command=self.ok).pack()

    def ok(self):
        print('Text box: {}\nSecret box: {}'.format(self.entry.get(), self.secret_entry.get()))


if __name__ == '__main__':
    root = tk.Tk()

    tk.Message(
        root, text='Close this window when you are done looking at the example pop-ups.'
    ).pack(
        anchor='center', padx=100, pady=100
    )
top4 = tk.Toplevel(root)
EntryApp(top4)
root.mainloop()
