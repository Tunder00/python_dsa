# O(n^2) here we will have n inputs, and we will perform n*n operations
#  as in the below given program we if the input is 10 then the no. of operations performed will be
# n*n i.e., 10*10 = 100 operations, in most of the time DSA programs are written to come out of this time complexity
# because we need too much time as the input grows.
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
print_items(10)