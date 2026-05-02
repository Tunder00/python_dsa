# in lists adding and deleting of a item also has a big o notation
# so basically
my_list = [11,23,34,5]
print(my_list)

# below will be my_list code having O(1) as complexity because we ae adding and removing at ends
my_list.append(12)
print(my_list)
my_list.pop()
print(my_list)

# below are teh codes for my_list with o(n) because reindexing is happening
my_list.pop(0)
print(my_list)
my_list.insert(0,11)
print(my_list)
my_list.insert(1,"hi")
print(my_list)
my_list.pop(1)
print(my_list)