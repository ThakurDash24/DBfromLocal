import mysql.connector
import sys

class DBHelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",  # ✅ Fixed here
                password="",
                database="hit-db-demo"
            )
            self.my_cursor = self.conn.cursor()
            print("✅ Connected to Database")
        except Exception as e:
            print("❌ Failed to connect to Database!")
            print("Error:", e)
            sys.exit(1)

    def register(self,name,email,pw):
        try:
            self.my_cursor.execute("""
            INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES (NULL, '{}','{}','{}');
            """.format(name,email,pw))
            self.conn.commit()
        except Exception as e :
            print(e)
        else: return 1
    
    def search(self,email,password):
        self.my_cursor.execute("""
        SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}'    """.format(email,password))
        data=self.my_cursor.fetchall()
        return data
        print(data)