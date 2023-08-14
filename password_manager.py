from tkinter import Tk, Frame, Label, LabelFrame, Button, Entry, messagebox, StringVar, Canvas, END
from tkinter import ttk 
from database import Database

# Work on ID, delete and update function 
# Work on Vertical Scrollbar for the self.main window / Fix the Tree window size issue (expand)


class main_window():

    def __init__(self, main, db):
        self.main = main # Tk() 
        self.db = db 

        # self.last_inserted_id = self.db.retrieve_last_inserted_id()
        self.id_count = 0
        self.id_var = StringVar()

        self.website = ""
        self.email = ""
        self.username = ""
        self.password = ""
        self.security_question = ""
        self.security_answer = ""
        self.notes = ""
        
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
        self.crud_frame.grid(row=1, column=0, padx=20, pady=10, sticky="w") 

        self.search_frame = LabelFrame(self.main, text="Search Account", bg="#7C7B86", highlightbackground="#FFFFFF", highlightthickness=3, font=("Courier", 12, "bold"), relief="flat", padx=10, pady=10)
        self.search_frame.grid(row=1, column=1, padx=10, pady=10, sticky="n")

        self.search_account()
        self.create_entry_labels()
        self.create_entry_boxes()
        self.create_crud_buttons()
        self.create_accounts_tree()

    def increment_id(self):
        last_inserted_id = self.db.retrieve_last_inserted_id()
        print(last_inserted_id)
        self.id_count = last_inserted_id + 1 
        self.id_var.set(str(self.id_count))

    def search_account(self):
        self.row_no = self.col_no = 0
        self.search_account = Entry(self.search_frame, width=36, bg="#FFFFFF", highlightcolor="#FFFFFF", highlightbackground="#000000", highlightthickness=2, font=("Courier", 12), relief="flat")
        self.search_account.grid(row=self.row_no, column=self.col_no)
        
        Button(self.search_frame, width=10, text="Search", bg="#000000", fg="#FFFFFF", font=("Courier", 12), padx=3, pady=0).grid(row=self.row_no, column=self.col_no+1, padx=5, pady=2)

    def create_entry_labels(self):
        labels_info = ("ID", "Website*", "Email*", "Username*", "Password*", "Security Question", "Security Answer", "Notes")
        for label_info in labels_info:
            Label(self.crud_frame, text=label_info, bg="#7C7B86", fg="#FFFFFF", font=("Courier", 12, "bold"), padx=5, pady=1).grid(row=self.row_no, column=self.col_no, padx=5, pady=1, sticky="w")
            self.row_no += 1

    def create_entry_boxes(self):
        self.entry_boxes = []
        self.col_no += 1
        self.row_no = 0

        id_entry = Label(self.crud_frame, textvariable=self.id_var, width=25, bg="#000000", fg="#FFFFFF", state="disabled", font=("Courier", 13, "bold"), relief="flat") # textvariable=self.id_var
        id_entry.grid(row=self.row_no, column=self.col_no, padx=20, pady=10, sticky="w")

        # self.increment_id()

        self.row_no += 1

        for i in range(7):
            show = ""
            if i == 3:
                show = "*"
            entry_box = Entry(self.crud_frame, width=25, bg="#FFFFFF", highlightcolor="#FFFFFF", highlightbackground="#000000", highlightthickness=2, font=("Courier", 12), relief="flat", show=show)
            entry_box.grid(row=self.row_no, column=self.col_no, padx=20, pady=10, sticky="w")
            self.row_no += 1 
            self.entry_boxes.append(entry_box)

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
        self.website = self.entry_boxes[0].get()
        self.email = self.entry_boxes[1].get() 
        self.username = self.entry_boxes[2].get() 
        self.password = self.entry_boxes[3].get() 
        self.security_question = self.entry_boxes[4].get() 
        self.security_answer = self.entry_boxes[5].get() 
        self.notes = self.entry_boxes[6].get() 

        required_fields = [0, 1, 2, 3]

        if any(not self.entry_boxes[index].get() for index in required_fields):
            messagebox.showerror("Error", "Please fill in the required fields!")

        for index in required_fields:
            if not self.entry_boxes[index].get():
                self.entry_boxes[index].config(highlightbackground="#FF0000", highlightthickness=2, relief="flat")
            else:
                self.entry_boxes[index].config(highlightbackground="#FFFFFF", highlightthickness=2, relief="flat")
                self.increment_id()

        data = {"website": self.website, "email": self.email, "username": self.username, "password": self.password, "security_question": self.security_question, "security_answer": self.security_answer, "notes": self.notes}
        
        self.db.create_account_info(data)

    def update_account_info(self):
        # self.website = self.entry_boxes[0].get()
        # self.email = self.entry_boxes[1].get() 
        # self.username = self.entry_boxes[2].get() 
        # self.password = self.entry_boxes[3].get() 
        # self.security_question = self.entry_boxes[4].get() 
        # self.security_answer = self.entry_boxes[5].get() 
        # self.notes = self.entry_boxes[6].get() 
    
        data = {"website": self.website, "email": self.email, "username": self.username, "password": self.password, "security_question": self.security_question, "security_answer": self.security_answer, "notes": self.notes}
        self.db.update_account_info(data)

    def delete_account_info(self, id):
        # id = self.entry_boxes[0].get() 
        # self.db.delete_account_info(id)
        pass

    def copy_password(self):
        pass

    def show_accounts_info(self):
        accounts_list = self.db.show_accounts() 
        for account in accounts_list:
            self.accounts_tree.insert("", END, values=(account[0], account[1], account[2], account[3], account[4], account[5], account[6], account[7]))
            # print(account) 

    def create_accounts_tree(self):
        columns = ("ID", "Website", "Email", "Username", "Password", "Security Q", "Security A", "Notes")
        columns_widths= (40, 110, 200, 120, 150, 220, 100, 220)

        tree_frame = Frame(self.main, highlightbackground="#FFFFFF", highlightthickness=3, relief="flat")
        tree_frame.grid(row=3, column=0, columnspan=4, padx=20, pady=5, sticky="w")

        self.accounts_tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
        
        for column, width in zip(columns, columns_widths):
            self.accounts_tree.column(column, width=width)
            self.accounts_tree.heading(column, text=column)

        self.accounts_tree.grid(row=3, column=0, sticky="w") # padx=20, pady=10, 

        # Create a Vertical Scrollbar on the right side and Link to the Treeview 
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.accounts_tree.yview)
        scrollbar.grid(row=3, column=1, sticky="ns")
        self.accounts_tree.configure(yscrollcommand=scrollbar.set)

        # Allow the Treeview widget to expand within the tree_frame
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)


if __name__ == "__main__":
    # Database Table(s)
    db_class = Database()
    db_class.create_table()

    # Tkinter Window 
    main = Tk() 
    main_class = main_window(main, db_class)
    main.mainloop()