# pointer working for integer type data

num1=11
num2=num1

print("before update num1 and num 2")
print("num1 = ",num1)
print("num2 = ",num2)

print("num1 points to: ",id(num1))
print("num2 points to: ",id(num2))

num2 = 22

print("after update num1 and num 2")
print("num1 = ",num1)
print("num2 = ",num2)

print("num1 points to: ",id(num1))
print("num2 points to: ",id(num2))
# integers are immutable i.e., we cannot modify the value we will be pointing to a newer memory location