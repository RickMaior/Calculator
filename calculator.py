from tkinter import *


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.label_text = StringVar()
        self.label_text.set("Total")

        self.master = master
        self.total = 0
        self.partial = 0
        self.operation = 0

        self.init_window()

    def init_window(self):
        self.master.title("Calculator")

        l1 = Label(textvariable=self.label_text, fg="black", bg="white").pack(anchor="nw", side=TOP)

        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)

        edit = Menu(menu)
        edit.add_command(label="Reset", command=self.client_reset)
        menu.add_cascade(label="Edit", menu=edit)

        # creating buttons
        b1 = Button(self, text="1", command=lambda: self.button_function(1))
        b2 = Button(self, text="2", command=lambda: self.button_function(2))
        b3 = Button(self, text="3", command=lambda: self.button_function(3))

        b4 = Button(self, text="4", command=lambda: self.button_function(4))
        b5 = Button(self, text="5", command=lambda: self.button_function(5))
        b6 = Button(self, text="6", command=lambda: self.button_function(6))

        b7 = Button(self, text="7", command=lambda: self.button_function(7))
        b8 = Button(self, text="8", command=lambda: self.button_function(9))
        b9 = Button(self, text="9", command=lambda: self.button_function(9))

        b0 = Button(self, text="0", command=lambda: self.button_function(0))

        addButton = Button(self, text="Add", command=lambda: self.button_function("add"))
        subbButton = Button(self, text="Subb", command=lambda: self.button_function("subb"))
        equalButton = Button(self, text="=", command=lambda: self.button_function("="))

        # align of buttons

        # l1.grid(row=0, column=0)
        b1.grid(row=1, column=0)
        b2.grid(row=1, column=1)
        b3.grid(row=1, column=2)

        b4.grid(row=2, column=0)
        b5.grid(row=2, column=1)
        b6.grid(row=2, column=2)

        b7.grid(row=3, column=0)
        b8.grid(row=3, column=1)
        b9.grid(row=3, column=2)

        b0.grid(row=4, column=1)

        addButton.grid(row=1, column=3)
        subbButton.grid(row=2, column=3)
        equalButton.grid(row=3, column=3)

    def client_exit(self):
        exit()

    def client_reset(self):
        print("Reseting values")

    def button_function(self, button):

        if button == "add":
            self.operation = "+"
            self.total = self.partial
            self.partial = 0
            print("Adding")
        elif button == "subb":
            self.operation = "-"
            self.total = self.partial
            self.partial = 0
            print("Subtracting")
        elif button == "=":
            if self.operation == "+":
                # print(f"Going to {self.total}+{self.partial}")
                self.total = self.total + self.partial
                self.partial = self.total
                self.operation = 0
                self.label_text.set(f"Total= {self.total}")
                print(f"Total = {self.total} ")
            elif self.operation == "-":
                # print(f"Going to {self.total}-{self.partial}")
                self.total = self.total - self.partial
                self.partial = self.total
                self.operation = 0
                self.label_text.set(f"Total= {self.total}")
                print(f"Total = {self.total} ")
            else:
                self.label_text.set(f"Total= {self.total}")
                print(self.total)

        else:
            self.partial = self.partial * 10 + button
            self.label_text.set(f"Sub total= {self.partial}")
            print(self.partial)


root = Tk()
root.geometry("400x300")

app = Window(root)

root.mainloop()
