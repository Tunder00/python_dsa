# in this file only explanation of o(log n) and o(nlog n)
# as we know every solution cannot be done in o(1) we have this o(log n)
# o(log n): is used in divide and conquer its better than o(n) but slightly slower than o(1)
# lets say we have array = [1,2,3,4,5,6,7,8] and it is sorted at any given condition
# so, I don't know where is 1, but I need to find 1.
# here usually we go to iterate full list, but it would take n operations so to cut it down
# we use divide and conquer divide the array into halves till we get the desired target
# [1,2,3,4,5,6,8] ---> [1,2,3,4] [5,6,7,8] here is my target is present at left or right array
# [1,2,3,4] [5,6,7,8] ---> [1,2] [3,4] again where is my target present
# [1,2] [3,4] ---> [1] [2] my search target is present at left
# so in above example we have finished search in 3 steps even for worst case we could finish it with 3 steps
# this we say length (8) how many times we can divide it by 2 to get 1 == 3 times
# so log 8(with base 2) == 3
# why this approach lets say we have a billion elements so the search normally should take billion operations
# but with divide and conquer we can do it in 29-30 steps approx to get a single number so
# this approach is better than o(n) but slower than o(1)

# as for o(nlog n) better than o(n^2) but slower than o(n)
# this complexity only comes for some of the sorting algorithms