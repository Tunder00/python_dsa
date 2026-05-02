# here the idea is as teh below program has 3 for loops
# 1st 2 for loops come to a time complexity of O(n^2) and
# 3rd for loop alone comes to o(n)
# so the total should be o(n^2 + n) right and it's correct
# but as the input size grows lets say n = 100 then n^2 becomes 10000
# as we can observe n^2 is dominant to n so we will drop n and the time complexity becomes o(n^2)
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    for k in range(n):
        print(k)
print_items(10)