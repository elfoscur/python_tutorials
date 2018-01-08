a='this is a string' #string is like an array from 0 to len(string)

print(len(a)) #string length
for letter in a:
    print(letter)

print(a[0:len(a)]) #square brackets specify a substring, in this case 0 to len(a) is the whole substring
print(a[0:4]) #this
print(a[5:]) #is a string (from 5 to end of the string)
print(a[:]) #this is a string

#existence of a string inside a substring
print('is' in a) #True
if 'is' in a:
    print('is is present')

#string as an object, has methods
print(type(a)) #type 'str'
print(dir(a)) #list of methods

print(a.upper()) #don't forget the () after the method!
print('LOWER'.lower())
print('hello pippo!'.replace('pippo','pluto'))#replace the string 'pippo' with 'pluto'
print(a.find('is')) #return the position of the first 'is'
email='test@email.com is my email'
atpos=email.find('@')
domain=email[atpos+1:email.find(' ',atpos)]
print(domain)


print('   this trim your string on both sides'.strip()) #whitespace is the default

print('www.example.com'.lstrip('w.')) #removes 'w' and '.' starting from the left
