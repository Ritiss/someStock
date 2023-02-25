import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import mysql

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="12345678",
                               database="stock")


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = mydb
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#000000', bd=10)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_open_dialog = tk.Button(toolbar, text="Add",
                                    command=self.open_dialog, bg='black', height=2, width=10, foreground='white',
                                    font=('calibri', 14),
                                    bd=0,
                                    compound=tk.TOP)
        btn_open_dialog.pack(side=tk.LEFT)
        btn_edit_dialog = tk.Button(toolbar, text="Edit",
                                    command=self.open_update_dialog, bg='black', height=2, width=10, foreground='white',
                                    font=('calibri', 14), bd=0,
                                    compound=tk.TOP)
        btn_edit_dialog.pack(side=tk.LEFT)

        btn_delete_dialog = tk.Button(toolbar, text="Delete",
                                      command=self.delete_records, bg='black', height=2, width=10, foreground='white',
                                      font=('calibri', 14),
                                      bd=0,
                                      compound=tk.TOP)
        btn_delete_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, column=("id", "title", "amount", "price"), height=10,
                                 show='headings')
        self.tree.column("id", width=50, anchor=tk.CENTER)
        self.tree.column("title", width=300, anchor=tk.CENTER)
        self.tree.column("amount", width=100, anchor=tk.CENTER)
        self.tree.column("price", width=100, anchor=tk.CENTER)

        self.tree.heading("id", text='id')
        self.tree.heading("title", text='Title')
        self.tree.heading("amount", text='Amount')
        self.tree.heading("price", text='Price')

        self.tree.pack()

    def records(self, title, amount, price):
        self.db.insert_data(title, amount, price)
        self.view_records()

    def update_records(self, title, amount, price):
        self.db.c.execute(
            '''UPDATE `box` SET `title` = %s, `amount` = %s, `price` = %s WHERE (`id` = %s);''',
            (title, amount, price, self.tree.set(
                self.tree.selection()[0], '#1')))
        self.view_records()

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM `box` WHERE (`id` = %s);''', (self.tree.set(selection_item, '#1'),))
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT * FROM box;''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def error(self):
        return messagebox.showinfo('PythonGuides', 'Thnak you for subscribing!')

    def open_dialog(self):
        Child()

    def open_update_dialog(self):
        Update()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title("Add")
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_title = tk.Label(self, text='title')
        label_title.place(x=50, y=50)
        label_amount = tk.Label(self, text='amount')
        label_amount.place(x=50, y=75)
        label_price = tk.Label(self, text='price')
        label_price.place(x=50, y=100)

        self.entry_title = ttk.Entry(self)
        self.entry_title.place(x=200, y=50)

        self.entry_amount = ttk.Entry(self)
        self.entry_amount.place(x=200, y=75)

        self.entry_price = ttk.Entry(self)
        self.entry_price.place(x=200, y=100)

        btn_cancel = ttk.Button(self, text='Cancel', command=self.destroy)
        btn_cancel.place(x=300, y=185)

        self.btn_ok = ttk.Button(self, text='Add')
        self.btn_ok.place(x=220, y=185)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_title.get(), self.entry_amount.get(),
                                                                       self.entry_price.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app
        self.db = mydb

    def init_edit(self):
        self.title('Edit')
        btn_edit = ttk.Button(self, text='Edit')
        btn_edit.place(x=220, y=185)
        btn_edit.bind('<Button-1>',
                      lambda event: self.view.update_records(self.entry_title.get(), self.entry_amount.get(),
                                                             self.entry_price.get()))

        self.grab_set()
        self.focus_set()


class DB:
    def __init__(self):
        self.db = mydb
        self.c = self.db.cursor()

    def insert_data(self, title, amount, price):
        self.c.execute(
            '''INSERT INTO `box`(`title`, `amount`, `price`) VALUES (%s, %s, %s);''',
            (title, amount, price))
        self.db.commit()


if __name__ == "__main__":
    root = tk.Tk()
    mydb = DB()
    app = Main(root)
    app.pack()
    root.title("Goods accounting")
    root.geometry('650x450+300+200')
    root.resizable(False, False)
    root.mainloop()
