#list -- append
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)

print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

#list-- init
myStrlist = ["A","z","R"]
# prints out A,z,R
for x in myStrlist:
    print(x)

#marge (add) two list
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1,2,3] * 3)

#Problem

x = object()
y = object()

# TODO: change this code
x_list = [x]*10
y_list = [y]*10
big_list = []
big_list=x_list+y_list
print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
