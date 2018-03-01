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