#string print
mystring = "Don't worry about apostrophes"
print(mystring)

# string operation
str = None
myfloat = None
myint = None

# testing code
if str == "hello":
    print("String: %s" % str)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

helloworld = "hello" + " " + "world"
print(helloworld)

lotsofhellos = "hello" * 10
print(lotsofhellos)

# This prints out "Hello, AzR!"
name = "AzR"
print("Hello, %s!" % name)

#To use two or more argument specifiers, use a tuple (parentheses)
# This prints out "AzR is 23 years old."
name = "Azr"
age = 23
print("%s is %d years old." % (name, age))

#TODO
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%.2f."

print(format_string % data)