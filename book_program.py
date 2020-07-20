from tkinter import *
from book_functions import Database

datab = Database('book.db')

class Interface:

    def __init__(self, interface):
        self.interface = interface
        self.interface.title('Laura Gnc - Bookstore App')

        # Labels are the text explaining what field is what (Title, Year, ISBN, Author)
        l1 = Label(interface, text='Title')
        l1.grid(row=0, column=0)

        l2 = Label(interface, text='Author')
        l2.grid(row=0, column=2)

        l3 = Label(interface, text='Year')
        l3.grid(row=1, column=0)

        l4 = Label(interface, text='ISBN')
        l4.grid(row=1, column=2)

        # Entries are the blank fields used to type input in it for the Title, Author, Year, ISBN
        self.title_text = StringVar()
        self.e1 = Entry(interface, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)

        self.author_text = StringVar()
        self.e2 = Entry(interface, textvariable=self.author_text)
        self.e2.grid(row=0, column=3)

        self.year_text = StringVar()
        self.e3 = Entry(interface, textvariable=self.year_text)
        self.e3.grid(row=1, column=1)

        self.isbn_text = StringVar()
        self.e4 = Entry(interface, textvariable=self.isbn_text)
        self.e4.grid(row=1, column=3)

        # Listbox
        self.list1 = Listbox(interface, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        # Scrollbar
        sb1 = Scrollbar(interface)
        sb1.grid(row=2, column=2, rowspan=6)

        # Link the Listbox with the Scrollbar
        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview())

        # Bind feature:
        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        # Buttons - click on them to perform an action/function
        b1 = Button(interface, text='View All', width=10, command=self.view_command)
        b1.grid(row=2, column=3)

        b1 = Button(interface, text='Search Entry', width=10, command=self.search_command)
        b1.grid(row=3, column=3)

        b1 = Button(interface, text='Add Entry', width=10, command=self.add_command)
        b1.grid(row=4, column=3)

        b1 = Button(interface, text='Update', width=10, command=self.update_command)
        b1.grid(row=5, column=3)

        b1 = Button(interface, text='Delete', width=10, command=self.delete_command)
        b1.grid(row=6, column=3)

        b1 = Button(interface, text='Quit', width=10, command=interface.destroy)
        b1.grid(row=7, column=3)

    def get_selected_row(self, event):
        try:
            global selected_tuple
            index = self.list1.curselection()[0]
            selected_tuple = self.list1.get(index)

            # To make the item appears in the fields
            self.e1.delete(0, END)
            self.e1.insert(END, selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(END, selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(END, selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END, selected_tuple[4])
        except IndexError:
            pass

    def view_command(self):
        self.list1.delete(0, END)
        for i in datab.view():
            self.list1.insert(END, i)

    def search_command(self):
        self.list1.delete(0, END)
        for i in datab.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.list1.insert(END, i)

    def add_command(self):
        datab.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))

    def delete_command(self):
        datab.delete(selected_tuple[0])
        # The next line is showing the user the change by calling the view function.
        self.view_command()

    def update_command(self):
        datab.update(selected_tuple[0], self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        print(selected_tuple[0], selected_tuple[1], selected_tuple[2], selected_tuple[3], selected_tuple[4])


interface = Tk()
inter = Interface(interface)
interface.mainloop()