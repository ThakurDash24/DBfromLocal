import sys
from dbheiper import DBHelper
class Flipkart:
    def __init__(self):
        #connect to the database
        self.db=DBHelper()
        self.menu()
        
    def menu(self):
        user_input=input("""
              1.Enter 1 to register
              2.enter 2 to login
              3. Anything else to leave 
            """)
        if user_input=="1":
            self.register()
        elif user_input=="2":
            self.login()
        else:
            sys.exit(1000)
    
    def register(self):
        name = input("Enter the name :")
        email = input("Enter the email :")
        password = input("Enter the pw :")
        response= self.db.register(name,email,password)
        if response:
            print("Done")
        else:
            print("Nhi hua bhai")
            self.menu()
            
    def login(self):
        email=input("Enter email :")
        password=input("Enter Password :")
        data=self.db.search(email,password)
        if len(data) != 0:
            print("Hello ,",data[0][1],"!")
        else:
            print("No data found")
            self.menu()
if __name__=="__main__":
    f=Flipkart()