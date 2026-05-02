# for the below function we cannot say the complexity is o(n) because here a and b are != n or even a != b
# so here we should say the complexity is o(a+b)
def print_items(a,b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)

# for the below function also we cannot say the complexity == o(n^2) because a*b != n*n
# so the complexity should be o(a*b)
def print_items1(c,d):
    for i in range(c):
        for j in range(d):
            print(i,j)
print_items(4,5)
print_items1(5,5)