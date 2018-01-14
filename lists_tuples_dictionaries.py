
l = list() #list declaration
l.append(1)
l.append(2)
l.append(3)

print l

t = (3,2,1) #tuple declaration, a tuple is immutable
print sorted(t) #function that sort a tuple
(x,y)=(10,20)
print x,y

d = {'c':20,'d':30,'a':5} #dictionary constructor
print(d)

l = list()
for k,v in d.items():
    l.append((v,k)) #put the tuple into the list, a list of tuples, in this case
                    #the value is put in the first position and the key in the second
print(sorted(l))

l.append((1,2,3)) #tuple of 3 values
print sorted(l,reverse=True) #Reverse = descending order

#list slicer
print l[:2]  #print two elements of the list


#LIST COMPREHENSION: http://www.pythonforbeginners.com/basics/list-comprehensions-in-python
#dynamic creation of the list of tuples. square brackets defines this list
#[ expression for item in list if conditional ]
print(sorted( [ (v,k) for k,v in d.items() ] ))
