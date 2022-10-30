import random
import string

decimal = string.digits
capital_letters = string.ascii_lowercase
small_letters = string.ascii_uppercase
special_characters = string.punctuation

combine_all = list(decimal+small_letters+capital_letters+special_characters)
password_length = int(input('\n Enter length of password you want?:'))
getpassword = random.sample(combine_all, k=password_length)
newpassword = ''

for password in getpassword:
    newpassword= newpassword+password


print('\n Password in list: ',getpassword)
print('Clean Password:',newpassword)