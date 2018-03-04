phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
names = []
print(phonebook)

for key, velue in phonebook.items():
    names.append(key)
    print("Phone number of %s is %d" % (key, velue))

print(names)
# testing code
if "John" in names:
    print("John is listed in the phonebook.")
if "Jill" not in names:
    print("Jill is not listed in the phonebook.")