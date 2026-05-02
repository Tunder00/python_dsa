# O(n) constants drop why we require this
# to understand the big O we need to drop some of the constants
# like as you can see in the below program we have n inputs, but we perform n+n operations
# so here we should have O(2n) but we will drop constant and this program also has O(n) time complexity
def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
print_items(10)