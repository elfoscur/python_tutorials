years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
ages = [2014 - year for year in years_of_birth]
print(ages)

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#  print only the even numbers (numeri pari) with list comprehension
elements = [el for el in a if el % 2 == 0]
print elements


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# elements of list 1 that are presents in list 2
c = [i for i in a if i in b]
print c
