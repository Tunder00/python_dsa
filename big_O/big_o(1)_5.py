# in the below program we are going to learn o(1)
# this is the most optimal solution a program can have
# so here let ht input grow to a million the operation performed will be 1
# we amy ge doubt like what if we are using 2 addition operation instead on one operation will it be o(2)
# no as even then also there is a constant number of operation going to happen even when the input grows
# the complexity will remain o(1)
def add_items(n):
    return n+n
print(add_items(4))