import random
import string

def _Password(length):
    Uppercase=string.ascii_uppercase
    lowercase=string.ascii_lowercase
    digits=string.digits
    special_characters=string.punctuation

    all_characters=Uppercase+lowercase+digits+special_characters

    password=''.join(random.choice(all_characters)for i in range(length))
    return password
password_length=12
random_Password=_Password(password_length)

print("The Random Password is :",random_Password)
