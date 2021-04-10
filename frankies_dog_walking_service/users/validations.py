from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def validate_password(value):
    pw = value
    flag = 0
    while True:  
        if (len(pw) < 5 or len(pw) > 15):
            flag = -1
            if(len(pw < 5)):
                print("Password length too short")
            else:
                print("Password length too long")
            break
        elif not re.search("[a-z]", pw):
            flag = -1
            print("doesn't contain characters [a-z]")
            break
        elif not re.search("[A-Z]", pw):
            flag = -1
            print("doesn't contain characters [A-Z]")
            break
        elif not re.search("[0-9]", pw):
            print("doesn't contain characters [0-9]")
            flag = -1
            break
        elif not re.search("[!*$]", pw):
            flag = -1
            print("doesn't contain characters !, *, $")
            break
        elif re.search("\s", pw):
            flag = -1
            print("No spaces")
            break
        else:
            flag = 0
            print("Valid Password")
            break
  
    if flag ==-1:
        print("Not a Valid Password")
