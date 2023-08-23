from tkinter import Tk, Frame, Label, LabelFrame, Button, Entry, messagebox, Checkbutton, IntVar, Canvas, END
from tkinter import ttk 
from database import Database

# Work on ID, delete and update function 
# Work on Vertical Scrollbar for the self.main window / Fix the Tree window size issue (expand)


class main_window():

    def __init__(self, main, db):
        self.main = main # Tk() 
        self.db = db 

        self.website = ""
        self.email = ""
        self.username = ""
        self.password = ""
        self.security_question = ""
        self.security_answer = ""
        self.notes = ""

        self.upper_case_letters = IntVar()
        self.lower_case_letters = IntVar()
        self.special_char = IntVar()
        self.numbers = IntVar()
        
        self.main.title("Password Manager")
        self.main.geometry("1230x780+150+0") # widthxheight+x_position+y_position
        self.main.configure(bg="#000000")
        self.main.resizable(width=False, height=True)
        # self.main = ttk.Frame(self.main)
        # self.main.pack(fill="both", expand=True, padx=20, pady=5)

        self.head_title = Label(self.main, text="Password Manager", width=75, bg="#4B4A54", fg="#FFFFFF", font=("Courier", 20, "bold"), highlightbackground="#FFFFFF", highlightthickness=3,
                           padx=10, pady=10, justify="center", anchor="center").grid(columnspan=4, pady=15, sticky="nsew") 

        # self.crud_frame = Frame(self.main, bg="#7C7B86", highlightbackground="#FFFFFF", highlightthickness=3, padx=10, pady=20)
        self.crud_frame = LabelFrame(self.main, text="Account Password Entry", bg="#7C7B86", highlightbackground="#FFFFFF", highlightthickness=3, font=("Courier", 12, "bold"), relief="flat", padx=10, pady=10) # relief="flat" - Text with no border 
        self.crud_frame.grid(row=1, column=0, rowspan=3, padx=20, pady=10, sticky="w") 

        self.search_frame = LabelFrame(self.main, text="Search Account", bg="#7C7B86", highlightbackground="#FFFFFF", highlightthickness=3, font=("Courier", 12, "bold"), relief="flat", padx=10, pady=10)
        self.search_frame.grid(row=1, column=1, padx=20, pady=10, sticky="n")

        self.pw_strength_frame = LabelFrame(self.main, text="Password Strength Meter", bg="#7C7B86", highlightbackground="#FFFFFF", highlightthickness=3, font=("Courier", 12, "bold"), relief="flat", padx=10, pady=10)
        self.pw_strength_frame.grid(row=2, column=1, padx=20, pady=10, sticky="n")

        self.pw_generator_frame = LabelFrame(self.main, text="Password Generator", bg="#7C7B86", highlightbackground="#FFFFFF", highlightthickness=3, font=("Courier", 12, "bold"), relief="flat", padx=10, pady=10)
        self.pw_generator_frame.grid(row=3, column=1, padx=20, pady=10, sticky="n")

        self.create_entry_labels()
        self.create_entry_boxes()
        self.create_crud_buttons()
        self.create_buttons()
        self.create_checkboxes()
        self.create_accounts_tree()    

    def create_entry_labels(self):
        self.row_no = self.col_no = 0

        Label(self.pw_strength_frame, text="Enter Password", bg="#7C7B86", fg="#FFFFFF", font=("Courier", 12, "bold"), padx=5, pady=1).grid(row=self.row_no, column=self.col_no, padx=5, pady=1, sticky="w")
        
        Label(self.pw_generator_frame, text="Password Length", bg="#7C7B86", fg="#FFFFFF", font=("Courier", 12, "bold"), padx=5, pady=1).grid(row=self.row_no, column=self.col_no, padx=5, pady=1, sticky="w")

        labels_info = ("ID", "Website*", "Email*", "Username*", "Password*", "Security Question", "Security Answer", "Notes")
        for label_info in labels_info:
            # Make Label Width Smaller 
            Label(self.crud_frame, text=label_info, bg="#7C7B86", fg="#FFFFFF", font=("Courier", 12, "bold"), padx=5, pady=1).grid(row=self.row_no, column=self.col_no, padx=5, pady=1, sticky="w")
            self.row_no += 1

    def create_entry_boxes(self):
        self.entry_boxes = []
        
        self.row_no = self.col_no = 0

        # Password Strenght Entry Box 
        self.password_strength = Entry(self.pw_strength_frame, width=19, bg="#FFFFFF", highlightcolor="#FFFFFF", highlightbackground="#000000", highlightthickness=2, font=("Courier", 12), relief="flat")
        self.password_strength.grid(row=self.row_no, column=self.col_no+1, sticky="w")

        # Generate Password Entry Box 
        self.generate_password = Entry(self.pw_generator_frame, width=13, bg="#FFFFFF", highlightcolor="#FFFFFF", highlightbackground="#000000", highlightthickness=2, font=("Courier", 12), relief="flat")
        self.generate_password.grid(row=self.row_no, column=self.col_no+1, sticky="w")

        # Search Account Entry Box 
        self.search_account = Entry(self.search_frame, width=36, bg="#FFFFFF", highlightcolor="#FFFFFF", highlightbackground="#000000", highlightthickness=2, font=("Courier", 12), relief="flat")
        self.search_account.grid(row=self.row_no, column=self.col_no)
        
        self.col_no += 1
        self.row_no = 0
       
       # id Entry Box 
        id_entry = Entry(self.crud_frame, width=25, bg="#000000", fg="#FFFFFF", highlightcolor="#FFFFFF", highlightbackground="#FFFFFF", highlightthickness=2, font=("Courier", 12), relief="flat")
        id_entry.grid(row=self.row_no, column=self.col_no, padx=20, pady=10, sticky="w")
        self.entry_boxes.append(id_entry)

        self.row_no += 1

        for i in range(7):
            show = ""
            if i == 3:
                show = "*"
                entry_box = Entry(self.crud_frame, width=18, bg="#FFFFFF", highlightcolor="#FFFFFF", highlightbackground="#000000", highlightthickness=2, font=("Courier", 12), relief="flat", show=show)
                entry_box.grid(row=self.row_no, column=1, columnspan=1, padx=20, pady=10, sticky="w") ### Change columnspan 
            else:
                entry_box = Entry(self.crud_frame, width=25, bg="#FFFFFF", highlightcolor="#FFFFFF", highlightbackground="#000000", highlightthickness=2, font=("Courier", 12), relief="flat", show=show)
                entry_box.grid(row=self.row_no, column=self.col_no, columnspan=2, padx=20, pady=10, sticky="w") ### Change columnspan 
            self.row_no += 1 
            self.entry_boxes.append(entry_box)

    def create_checkboxes(self):
        self.row_no = 1
        self.col_no = 0 

        self.upper_checkbox = Checkbutton(self.pw_generator_frame, text="Uppercase Letters", variable=self.upper_case_letters, onvalue=1, offvalue=0, font=("Courier", 11, "bold"), bg="#7C7B86", activebackground="#7C7B86", relief="flat", padx=10, pady=10)
        self.upper_checkbox.grid(row=self.row_no, column=self.col_no)
        self.lower_checkbox = Checkbutton(self.pw_generator_frame, text="Lowercase Letters", variable=self.lower_case_letters, onvalue=1, offvalue=0, font=("Courier", 11, "bold"), bg="#7C7B86", activebackground="#7C7B86", relief="flat", padx=10, pady=10)
        self.lower_checkbox.grid(row=self.row_no+1, column=self.col_no)
        self.special_char_checkbox = Checkbutton(self.pw_generator_frame, text="Special Characters", variable=self.special_char, onvalue=1, offvalue=0, font=("Courier", 11, "bold"), bg="#7C7B86", activebackground="#7C7B86", relief="flat", padx=10, pady=10)
        self.special_char_checkbox.grid(row=self.row_no, column=self.col_no+1, columnspan=2)
        self.numbers_checkbox = Checkbutton(self.pw_generator_frame, text="Numbers", variable=self.numbers, onvalue=1, offvalue=0, font=("Courier", 11, "bold"), bg="#7C7B86", activebackground="#7C7B86", relief="flat", padx=10, pady=10)
        self.numbers_checkbox.grid(row=self.row_no+1, column=self.col_no+1, columnspan=2, sticky="nswe")

    def create_buttons(self):
        self.row_no = self.col_no = 0

        # Copy Password Button 
        Button(self.crud_frame, command=self.copy_password, width=5, text="Copy", bg="#000000", fg="#FFFFFF", font=("Courier", 12), padx=3, pady=0).grid(row=self.row_no+4, column=self.col_no+1, padx=5, pady=2, sticky="e")
        
        # Search Button 
        Button(self.search_frame, width=10, text="Search", bg="#000000", fg="#FFFFFF", font=("Courier", 12), padx=3, pady=0).grid(row=self.row_no, column=self.col_no+1, padx=5, pady=2)

        # Check Password Strength Button 
        Button(self.pw_strength_frame, width=10, text="Check PW", bg="#000000", fg="#FFFFFF", font=("Courier", 12), padx=3, pady=0).grid(row=self.row_no, column=self.col_no+2, padx=5, pady=2)
        
        # Generate Password Button 
        Button(self.pw_generator_frame, width=12, text="Generate PW", bg="#000000", fg="#FFFFFF", font=("Courier", 12), padx=3, pady=0).grid(row=self.row_no, column=self.col_no+2, padx=5, pady=2, sticky="e")

    def create_crud_buttons(self):
        buttons_info = (("Save", "#59B400", self.save_account_info), ("Update", "#00AAFF", self.update_account_info), ("Delete", "#FF5383", self.delete_account_info), ("Show Account Info", "#E996FA", self.show_accounts_info)) # ("Copy Password", "#E996FA", self.copy_password)
        
        # Top Row Buttons 
        self.row_no += 1
        self.col_no = 0 

        # Create Top Row Bottons 
        for button_info in buttons_info[:2]:
            Button(self.crud_frame, width=15, text=button_info[0], bg=button_info[1], fg="#000000", font=("Courier", 12), padx=3, pady=0, command=button_info[2]).grid(row=self.row_no, column=self.col_no, padx=5, pady=2, sticky="ew")
            self.crud_frame.grid_columnconfigure(self.col_no, uniform="buttons")  # Uniform width for buttons
            self.col_no += 1

        # Reset Column Number for the Bottom Bottons 
        self.col_no = 0
        self.row_no += 1

        # Create Bottom Row Bottons
        for button_info in buttons_info[2:]:
            Button(self.crud_frame, width=15, text=button_info[0], bg=button_info[1], fg="#000000", font=("Courier", 12), padx=3, pady=0, command=button_info[2]).grid(row=self.row_no, column=self.col_no, padx=5, pady=10, sticky="ew")
            self.crud_frame.grid_columnconfigure(self.col_no, uniform="buttons") 
            self.col_no += 1

    def save_account_info(self):
        # self.id = self.entry_boxes[0].get()
        self.website = self.entry_boxes[1].get()
        self.email = self.entry_boxes[2].get() 
        self.username = self.entry_boxes[3].get() 
        self.password = self.entry_boxes[4].get() 
        self.security_question = self.entry_boxes[5].get() 
        self.security_answer = self.entry_boxes[6].get() 
        self.notes = self.entry_boxes[7].get() 

        required_fields = [1, 2, 3, 4]

        if any(not self.entry_boxes[index].get() for index in required_fields):
            messagebox.showerror("Error", "Please fill in the required fields!")

        for index in required_fields:
            if not self.entry_boxes[index].get():
                self.entry_boxes[index].config(highlightbackground="#FF0000", highlightthickness=2, relief="flat")
            else:
                self.entry_boxes[index].config(highlightbackground="#FFFFFF", highlightthickness=2, relief="flat")
                self.entry_boxes[index].delete(0, END)

        data = {"website": self.website, "email": self.email, "username": self.username, "password": self.password, "security_question": self.security_question, "security_answer": self.security_answer, "notes": self.notes}
        
        self.db.create_account_info(data)
        self.show_accounts_info()

    def update_account_info(self):
        self.id = self.entry_boxes[0].get()
        self.website = self.entry_boxes[1].get()
        self.email = self.entry_boxes[2].get() 
        self.username = self.entry_boxes[3].get() 
        self.password = self.entry_boxes[4].get() 
        self.security_question = self.entry_boxes[5].get() 
        self.security_answer = self.entry_boxes[6].get() 
        self.notes = self.entry_boxes[7].get() 
    
        data = {"id": self.id, "website": self.website, "email": self.email, "username": self.username, "password": self.password, "security_question": self.security_question, "security_answer": self.security_answer, "notes": self.notes}
        self.db.update_account_info(data)
        for entry_box in self.entry_boxes:
            entry_box.delete(0, END)
        self.show_accounts_info()

    def delete_account_info(self):
        self.id = self.entry_boxes[0].get()
        self.db.delete_account_info(self.id)
        for entry_box in self.entry_boxes:
            entry_box.delete(0, END)
        self.show_accounts_info()

    def copy_password(self):
        password = self.entry_boxes[4].get()
        if password != "":
            self.main.clipboard_clear() # Clear the clipboard 
            self.main.clipboard_append(password) # Copy the password to the clipboard 
            messagebox.showinfo("Copy", "Password Copied") 
        else:
            messagebox.showerror("Failed", "No Password")
        
        for entry_box in self.entry_boxes:
            entry_box.delete(0, END)

    def show_accounts_info(self):
        for account in self.accounts_tree.get_children():
            self.accounts_tree.delete(account)
        accounts_list = self.db.show_accounts() 
        for account in accounts_list:
            self.accounts_tree.insert("", END, values=(account[0], account[1], account[2], account[3], account[5], account[6], account[7]))
            # self.accounts_tree.insert("", END, values=(account[0], account[1], account[2], account[3], account[4], account[5], account[6], account[7]))
            # print(account) 

    def create_accounts_tree(self):
        # columns = ("ID", "Website", "Email", "Username", "Password", "Security Q", "Security A", "Notes")
        # columns_widths= (40, 110, 200, 120, 150, 220, 100, 220)

        self.id = self.entry_boxes[0].get()

        columns = ("ID", "Website", "Email", "Username", "Security Q", "Security A", "Notes")
        columns_widths= (40, 110, 200, 120, 220, 220, 220)

        tree_frame = Frame(self.main, highlightbackground="#FFFFFF", highlightthickness=3, relief="flat")
        tree_frame.grid(row=5, column=0, columnspan=4, padx=20, pady=5, sticky="w")

        self.accounts_tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=5)
        # self.accounts_tree.heading("ID", text="ID")
        # self.accounts_tree.heading("Website", text="Website")
        # self.accounts_tree.heading("Email", text="Email")
        # self.accounts_tree.heading("Username", text="Username")
        # self.accounts_tree.heading("Security Q", text="Security Q")
        # self.accounts_tree.heading("Security A", text="Security A")
        # self.accounts_tree.heading("Notes", text="Notes")


        # self.accounts_tree["displaycolumns"] = ("ID", "Website", "Email", "Username", "Security Q", "Security A", "Notes")

        for column, width in zip(columns, columns_widths):
            self.accounts_tree.column(column, width=width)
            self.accounts_tree.heading(column, text=column)

        # self.accounts_tree.config(displaycolumns=("ID", "Website", "Email", "Username", "Security Q", "Security A", "Notes"))

        self.accounts_tree.grid(row=5, column=0, sticky="w") # padx=20, pady=10, 

        # Create a Vertical Scrollbar on the right side and Link to the Treeview 
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.accounts_tree.yview)
        scrollbar.grid(row=5, column=1, sticky="ns")
        self.accounts_tree.configure(yscrollcommand=scrollbar.set)

        # Allow the Treeview widget to expand within the tree_frame
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)

        def selected_account(event):
            for selected_ac in self.accounts_tree.selection():
                account = self.accounts_tree.item(selected_ac)
                record = account["values"]
                for entry_box, account in zip(self.entry_boxes, record):
                    entry_box.delete(0, END) # Delete whatever is in the entry boxes
                    entry_box.insert(0, account) # Insert selected account info into the entry boxes 
        self.accounts_tree.bind("<<TreeviewSelect>>", selected_account)


if __name__ == "__main__":
    # Database Table(s)
    db_class = Database()
    db_class.create_table()

    # Tkinter Window 
    main = Tk() 
    main_class = main_window(main, db_class)
    main.mainloop()