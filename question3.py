#Password Generator function

import string
import random

#Both lower and upper case letters (A-Z and a-z)
letters = string.ascii_letters #i.e abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ


#Digits from 0-9
digits = string.digits #i.e 0123456789

#Special Symbols
special_symbols = "!@#$%^&*()|?/,<>.=-+:;~'\""

#concantenate letters,digits and sysmbols for all password characters
all_password_char = list(letters + special_symbols + digits)

#how strong  should the password be, we will use the length of the password, the longer the password the stronger
password_length = int(input("Enter the length to determine how Strong you want the password,LENGTH:"))

def password_generate(password_length):
    random.shuffle(all_password_char)
    
    #initialize empty password list to store the password generated
    password_list = []
    for i in range(password_length):
        #choose randomly any characters fron the password characters
        random_char = random.choice(all_password_char)
        password_list.append(random_char)
    
    #we can shuffle the password generated to make it more unpredictable
    random.shuffle(password_list)
    #change password list to string :)
    password = ''.join(password_list)
    
    return password

password = password_generate(password_length)

#how strong is the user's password:)
if password_length < 4:
    print(f"Password:{password}")
    print(f"The password generated is Weaker :(")
elif password_length < 8:
    print(f"Password:{password}")
    print(f"The password generated is Weak :(")
elif password_length < 12:
    print(f"Password:{password}")
    print(f"The password generated is Moderate")
elif password_length < 16:
    print(f"Password:{password}")
    print(f"The password generated is Strong :)")
else:
    print(f"Password:{password}")
    print("The password generated is Very Strong :)")


