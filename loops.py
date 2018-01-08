################# WHILE LOOPS ###############
x=5
while x > 0:
    print(x)
    x=x-1
print(str(x)+'\n'+'yeah!')

i=1
while True:
    print(i)
    i=i+1
    if i==5:
        break #exit the loop
    if i<=5:
        continue #skip to the begenning of the loop
        print('never printed')

################# FOR LOOPS ###############

print('im a for loop, i iterate a list')
for i in [1,2,3,4,5]: #this is a definitive loop
    print(i)

friends=['marco','sara','pippo']
for friend in friends:
    print('happy new year '+friend+'!')


def largest2(a,b):
    if a>b:
        return a
    else: return b

largest=None #null value
for i in [100,29,1,3,412,5,1,2]:
        largest=largest2(largest,i)

print largest
