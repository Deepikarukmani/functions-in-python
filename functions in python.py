#definition function syntax:
def call():
    print("attend the call")
call()

#print the function using of aadd, sub, mul, div
def add():
    print("Addition:")
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print(a+b)
add()

def sub():
    print("Subtraction:")
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print(a-b)
sub()

def mul():
    print("Multiplication:")
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print(a*b)
mul()

def div():
    print("Division:")
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print(a/b)
div()

#To find odd or even fun:
def find_even_or_odd(a):
   if a%2==0:
       print("even")
   else:
       print("odd")
a= int(input("enter your num: "))
find_even_or_odd(a)

#to find pass or fail function:
def find_pass_or_fail(a):
   if a>=35:
       print("Pass")
   else:
       print("Fail")
mark= int(input("enter your mark: "))
find_pass_or_fail(mark)

# find the range to get the input from user:
def print_range(a,b):
   for i in range(a,b):
       print(i)
a= int(input("enter your num: "))
b= int(input("enter your num: "))
print_range(a,b)