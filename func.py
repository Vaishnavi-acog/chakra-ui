#global elements

x = "Vaishnavi"
def myfunc():
    print("My Name is" + x)
myfunc()

#local elements

x = "Vaishnavi"
def myfunc():
    x = "Python"
    print("My Name is" + x)
myfunc()

#global keyword
 
x = "I'm Global"
def myfunc():
    global x
    x = "I'm Local Now"
    print(x)
myfunc()

print(x)
