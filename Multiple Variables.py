#01 
A, B, C = "Enjoy", "Your", "Day"

print(A,B,C)
#or you can 
# print(B)
# print(C)

#02
A = B = C = "HAVE A GOOD DAY"
print(B)

#03 Unpack a Collection
Animal = ["Dog", "Cat", "Bee"]
x, y, z = Animal
print(x,y,z) 

#04 Global Variables
x = "I like apples "
def myfunc():
    print(x + " and orange")
myfunc()

# Local Variable
x = "nice to see you" # global variable
def myfunc():
    x = "of course" #local variable and use only inside the function
    print("Yes, " + x)
myfunc()
print("I am glad and " + x)

# Global Keyword
def myfunc():
    global x
    x = "there" # inside function 
myfunc()
print("Hello " + x) # can use because x is global variable
