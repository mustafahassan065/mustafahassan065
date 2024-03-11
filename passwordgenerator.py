import random
def generate_password(length = 8):
    password = ''
    select = random.randint(1,4)
    if select == '1':
        password+= chr(random.randint(65,90))
    elif select == '2':
         password+= chr(random.randint(97,122))
    elif select == '3':
        password+= chr(random.randint(48,57))
    else:
         password+= chr(random.randint(33,126))
         return password

        



def main():
    length = int(input("Enter the length of password"))
    password = generate_password(length)
    print(f'Generated password:{password}')



main()