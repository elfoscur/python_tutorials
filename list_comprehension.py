years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
ages = [2014 - year for year in years_of_birth]
print(ages)

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#  print only the even numbers (numeri pari) with list comprehension
elements = [el for el in a if el % 2 == 0]
print(elements)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# elements of list 1 that are presents in list 2
c = [i for i in a if i in b]
print(c)


# dictionary of tuples
# graph = {i:{k for k in range(num_nodes) if k != i} for i in range(num_nodes)}

# list comprehension with multiple loops
# generate: [0, 0, 1, 0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7, 8]
# the evaluation order is..
# for i in range(10) -> 0
#  for x in range(0) -> 0 put in the list 0
# ->1
# ->0,1
l= [x for i in range(10) for x in range(i)]
print(l)

for i in a:
    print(i)

l = [i for i in a]
print(l)
