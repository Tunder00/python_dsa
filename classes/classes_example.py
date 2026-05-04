# classes are blueprint of an object it can be used and asssigned to any variable to
# create same type of object example is given below and all of DSA programs we write in classes
class Cookie:
    def __init__(self,color):
        self.color = color
    def get_color(self):
        return self.color
    def set_color(self,color):
        self.color = color
cookie_one = Cookie("green")
cookie_two = Cookie("blue")
print("cookie one is: ",cookie_one.get_color())
print("cookie two is: ",cookie_two.get_color())
cookie_one.set_color("yellow")
print("cookie one is now: ",cookie_one.get_color())
print("cookie two is still: ",cookie_two.get_color())

# for example how we can use the classes
# class linked_List:
#   def __init__(self,value):
#       self.value = value
#   def append(self,value):
#   def pop(self):
#   def prepend(self,value):
#   def insert(self,index,value):
#   def remove(self,index):
# this example shows how we can create a class and use it to create our custom object