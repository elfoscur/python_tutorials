print(ord('{')) #function ord return the ascii code of the character

x='abc'
print(type(x))
y=u'dada'           #u before the string means that it's unicode
print(type(y))
z=y.decode() #converts the unicode in str
print(type(x))
