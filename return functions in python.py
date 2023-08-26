# set_username = "Titikkasha" , set_password =  "1502". get input for username and password.create a function called validate.
#if username and password matches the function should true else false:

set_username = "Titikkasha"
set_password =  "1502"

user_name = input("enter your username")
password  = int(input("enter your password"))

def validate():
    if set_username == user_name and set_password == password:
        return True
    else:
        return False

print(validate())


# (a+b)*c Get input for a and b and function called add() which should return the sum of a and b. and multiply that sum with c:

a = int(input("enter your num a: "))
b  = int(input("enter your num b: "))
c  = int(input("enter your num c: "))

def add(a,b):
    return a+b

added = add(a,b)
output = added*c
print(output)