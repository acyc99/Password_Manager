import sqlite3

class Database:
        
    def __init__(self):
        self.db_name = "password_records.db"
        self.db_connect = None 

    def connect_to_db(self):
        self.db_connect = sqlite3.connect(self.db_name)
    
    def close_db(self):
        if self.db_connect:
            self.db_connect.close() 



    def create_table(self, table_name="password_info"):
        create_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            website TEXT NOT NULL,
            email VARCHAR(200) NOT NULL,
            username VARCHAR(100) NOT NULL, 
            password VARCHAR(50) NOT NULL, 
            security_question TEXT DEFAULT NULL, 
            security_answer TEXT DEFAULT NULL,
            notes TEXT DEFAULT NULL,
            created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        try:
            self.connect_to_db() 
            cursor = self.db_connect.cursor()
            cursor.execute(create_query)
            print("Table successfully created")
            self.db_connect.commit() 
        except sqlite3.Error as e: 
            print("Error creating table:", e)
        finally:
            self.close_db() 



    def create_account_info(self, data, table_name="password_info"):
        # id = data["id"]
        website = data["website"]
        email = data["email"]
        username = data["username"]
        password = data["password"]
        security_question = data["security_question"]
        security_answer = data["security_answer"]
        notes = data["notes"]

        insert_query = f"""
        INSERT INTO {table_name} ("website", "email", "username", "password", "security_question", "security_answer", "notes") VALUES 
        (?, ?, ?, ?, ?, ?, ?);
        """
        
        try:
            self.connect_to_db() 
            cursor = self.db_connect.cursor()
            if website == "" or email == "" or username == "" or password == "":
                print("Please fill in the required fields") 
            else: 
                cursor.execute(insert_query, (website, email, username, password, security_question, security_answer, notes))
                print("Account info successfully inserted", (website, email, username, password, security_question, security_answer, notes))
                self.db_connect.commit() 
                # cursor.close()
        except sqlite3.Error as e: 
            print("Error inserting account info:", e)
        finally:
            self.close_db() 



    def show_accounts(self, table_name="password_info"):
        select_query = f"""
        SELECT * FROM {table_name};
        """

        self.connect_to_db() 
        cursor = self.db_connect.cursor()
        accounts_list = cursor.execute(select_query)
        return accounts_list



    def search_accounts(self, keyword, table_name="password_info"):
        search_query = f"""
        SELECT * from {table_name}
        WHERE LOWER(website) LIKE ?;
        """

        try: 
            self.connect_to_db()
            cursor = self.db_connect.cursor() 
            keyword = keyword.lower()
            cursor.execute(search_query, [f"%{keyword}%"])
            search_results = cursor.fetchall()

            return search_results
        
        except sqlite3.Error as e:
            print("Error searching records:", e)
            return None
        finally:
            self.close_db()



    def update_account_info(self, data, table_name="password_info"):
        id = data["id"]
        website = data["website"]
        email = data["email"]
        username = data["username"]
        password = data["password"]
        security_question = data["security_question"]
        security_answer = data["security_answer"]
        notes = data["notes"]

        update_query = f"""
        UPDATE {table_name} SET 
        website = ?, email = ?, username = ?, password = ?, security_question = ?, security_answer = ?, notes = ?
        WHERE id = ?;
        """

        try:
            self.connect_to_db() 
            cursor = self.db_connect.cursor()
            print("Update Query:", update_query)
            print("Data to Update:", (id, website, email, username, password, security_question, security_answer, notes))
            cursor.execute(update_query, (website, email, username, password, security_question, security_answer, notes, id))
            self.db_connect.commit()
        except sqlite3.Error as e: 
            print("Error updating account info:", e)
        finally:
            self.close_db() 



    def delete_account_info(self, id, table_name="password_info"):

        delete_query = f"""
        DELETE FROM {table_name} WHERE id = ?;
        """

        try:
            self.connect_to_db() 
            cursor = self.db_connect.cursor()
            cursor.execute(delete_query, (id,))
            print("Account info successfully deleted")
            self.db_connect.commit()
        except sqlite3.Error as e: 
            print("Error deleting account info:", e)
        finally:
            self.close_db() 


    def retrieve_ac_pw(self, id, table_name="password_info"):

        retrieve_pw_query = f"""
        SELECT password FROM {table_name} WHERE id = ?; 
        """

        try:
            self.connect_to_db()
            cursor = self.db_connect.cursor()
            cursor.execute(retrieve_pw_query, (id,))
            result = cursor.fetchone()
            if result:
                password = result[0]
                print("Account password successfully retrieved")
                return password  # Return the retrieved password
            else:
                print("No matching record found.")
                return None  # Return None if no matching record is found
        except sqlite3.Error as e: 
            print("Error retrieving password:", e)
        finally:
            self.close_db() 