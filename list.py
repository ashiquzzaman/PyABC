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