dict1 = {
    "value":11
}
dict2 = dict1

print("before update")

print(dict1)
print(dict2)

print(id(dict1))
print(id(dict2))

dict2['value'] = 22

print("after update")
print(dict1)
print(dict2)

print(id(dict1))
print(id(dict2))
# dictionary is mutable i.e we can change the value inside the memory