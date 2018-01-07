astr = 'hello world'
#astr = 10
try:
    istr=int(astr)
except:
    print('error, astr is not a number')
    quit()

print istr
