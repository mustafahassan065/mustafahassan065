# class PasswordApplication:
#     def int(self):
#         self.passwords = {}

#     def sum_passwords(self,website,username,password):
#         if website in self.passwords:
#             print("This password is already added successfully")
#         else:
#             self.passwords[website] = {'username': username , 'password': password}
#             print(f'This password for {website} is added successfully')

#     def get_password(self , website):
#         if website in self.passwords():
#             return self.passwords[website]
#         else:
#             return None
#     def delete_password(self , website):
#         if website in self.passwords:
#             del self.passwords[website]
#             print("This password is deleted Successfully")
#         else:
#             print("f'No password found for {website}'")
#     def list_websites(self):
#         print("List of websites")
#         for website in self.passwords:
#             print(website)









# def main():
#     application = PasswordApplication()
#     print("Welcome to Password Manager Application")

#     while True:
#         print("1. Add Passwords")
#         print("2. Get Password")
#         print("3. Delete Password")
#         print("4. List the websites")
#         print("Existing the Application")

#         select = input("Select any option ")

#         if select == "1":
#             website = input("Enter the website name ")
#             username = input("Enter your username ")
#             password = input("Enter your Password ")
#             application.sum_passwords(website,username,password)

#         elif select == '2':
#             website = input("Enter the website name ")
#             application.get_password(website)

#         elif select == '3':
#             website = input("Enter the website name ")
#             application.delete_password(website)
#         elif select == '4':
#             application.list_websites()
#         elif select == '5':
#             print("Application is existing....")
  

 

# main()


class PasswordApplication:
    def int(self):
        self.passwords = {}
    def add_passwords(self , website , username,password):
        if website in self.passwords:
            print(f'The password for {website} is already present')
        else:
            self.passwords[website] = {'username' : username , 'password' : password}
            print(f'This password for {website} is added successfully')

    def get_password(self , website):
        if website in self.passwords:
            return self.passwords[website]
        else:
            return None
    def delete_passwords(self ,website):
        if website in self.passwords:
            del self.passwords[website]
            print(f"This password for {website } is deleted successfully")
        else:
            print(f"The password for {website} is not found")
            
    def list_websites(self):
        print("The list of websites is here")
        for website in self.passwords:
            print(website)








def main():

    application = PasswordApplication
    print('Welcome to Password Manager Application')

    while True:
        print("1. Add Passwords")
        print("2. Get Passwords")
        print("3. Delete Passwords")
        print("4. List the total websites")
        print("1. Existing the process")

        select = input("Select any option ")

        if select == '1':
            website = input("Enter the website name ")
            username = input("Enter your username ")
            password = input("Enter your passowrd ")
            application.add_passwords(website,username,password)
        elif select == '2':
            website = input("Enter the website name")
            application.get_password(website)
        elif select == '3' :
            website = input ("Enter the website name")
            application.delete_passwords(website)
        elif select == '4':
            application.list_websites()
        elif select == '5':
            print("The application process is existing.Goodbye!")
    

















main()