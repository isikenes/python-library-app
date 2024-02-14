import tkinter as tk

class Library():
    def __init__(self):
        self.save=open("books.txt","a+")

    def __del__(self):
        self.save.close()

    def list_books(self):
        self.save.seek(0)
        books=self.save.read().splitlines()
        return books

    def add_book(self, title, author, year, pages):
        info = f"{title},{author},{year},{pages}\n"
        self.save.write(info)

    def remove_book(self, title):
        self.save.seek(0)
        books=self.save.readlines()
        self.save.seek(0)
        self.save.truncate()

        for book in books:
            book_info=book.split(",")
            if(book_info[0] == title):
                books.remove(book)
        
        for book in books:
            self.save.write(book)

class LibraryApp(tk.Tk):
    def __init__(self, library):
        super().__init__()
        self.library=library
        self.title("Library App")
        self.geometry("800x600")

        self.main_screen = tk.Frame(self)
        self.main_screen.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.main_screen, text="Library App", font=("Arial", 32),pady=20)
        self.label.pack()

        self.buton1 = tk.Button(self.main_screen, text="LIST BOOKS", command=self.list_books, font=("Arial",20))
        self.buton1.pack(pady=20)

        self.buton2 = tk.Button(self.main_screen, text="ADD BOOK", command=self.add_book, font=("Arial",20))
        self.buton2.pack(pady=20)

        self.buton3 = tk.Button(self.main_screen, text="REMOVE BOOK", command=self.remove_book, font=("Arial",20))
        self.buton3.pack(pady=20)

        self.buton4 = tk.Button(self.main_screen, text="QUIT", command=self.quit_app, font=("Arial",20))
        self.buton4.pack(pady=20)

        self.name_label = tk.Label(self.main_screen, text="by Enes Işık", font=("Arial", 12), padx=10, pady=10)
        self.name_label.pack(side=tk.BOTTOM, anchor=tk.SE)

    def list_books(self):
        for widget in self.main_screen.winfo_children():
            widget.pack_forget()

        self.listbox=tk.Listbox(self.main_screen, font=("Arial",20), justify="center")
        books=self.library.list_books()
        for book in books:
            book_info=book.split(",")
            self.listbox.insert(tk.END, f"Book Title: {book_info[0]}    |    Author: {book_info[1]}")

        self.listbox.pack(fill=tk.BOTH, expand=True,padx=20,pady=10)
        
        back_button = tk.Button(self.main_screen, text="BACK", command=self.goMainScreen, font=("Arial",14))
        back_button.pack(side=tk.BOTTOM, pady=10)

    def add_book(self):
        for widget in self.main_screen.winfo_children():
            widget.pack_forget()

        self.label1=tk.Label(self.main_screen, text="Book title:", font=("Arial", 20))
        self.label1.pack(pady=10)

        self.input1=tk.Entry(self.main_screen, font=("Arial", 20))
        self.input1.pack(pady=10)

        self.label2=tk.Label(self.main_screen, text="Book Author:", font=("Arial", 20))
        self.label2.pack(pady=10)

        self.input2=tk.Entry(self.main_screen, font=("Arial", 20))
        self.input2.pack(pady=10)

        self.label3=tk.Label(self.main_screen, text="Release year:", font=("Arial", 20))
        self.label3.pack(pady=10)

        self.input3=tk.Entry(self.main_screen, font=("Arial", 20))
        self.input3.pack(pady=10)

        self.label4=tk.Label(self.main_screen, text="Number of pages:", font=("Arial", 20))
        self.label4.pack(pady=10)

        self.input4=tk.Entry(self.main_screen, font=("Arial", 20))
        self.input4.pack(pady=10)

        back_button = tk.Button(self.main_screen, text="BACK", command=self.goMainScreen, font=("Arial",14))
        back_button.pack(side=tk.BOTTOM, pady=10)

        save_button = tk.Button(self.main_screen, text="SAVE", command=self.save_book, font=("Arial",20))
        save_button.pack(side=tk.BOTTOM, pady=20)


    def remove_book(self):
        for widget in self.main_screen.winfo_children():
            widget.pack_forget()

        self.label5=tk.Label(self.main_screen, text="Book title:", font=("Arial", 20))
        self.label5.pack(pady=50)

        self.input5=tk.Entry(self.main_screen, font=("Arial", 20))
        self.input5.pack()

        back_button = tk.Button(self.main_screen, text="BACK", command=self.goMainScreen, font=("Arial",14))
        back_button.pack(side=tk.BOTTOM, pady=10)

        remove_button = tk.Button(self.main_screen, text="REMOVE", command=self.delete_book, font=("Arial",20))
        remove_button.pack(side=tk.BOTTOM, pady=120)
        

    def quit_app(self):
        self.quit()

    def save_book(self):
        self.library.add_book(self.input1.get(), self.input2.get(), self.input3.get(), self.input4.get())
        self.goMainScreen()

    def delete_book(self):
        self.library.remove_book(self.input5.get())
        self.goMainScreen()

    def goMainScreen(self):
        for widget in self.main_screen.winfo_children():
            widget.pack_forget()

        self.label.pack()
        self.buton1.pack(pady=20)
        self.buton2.pack(pady=20)
        self.buton3.pack(pady=20)
        self.buton4.pack(pady=20)
        self.name_label.pack(side=tk.BOTTOM, anchor=tk.SE)
    

if __name__ == "__main__":
    lib=Library()
    app = LibraryApp(lib)
    app.mainloop()