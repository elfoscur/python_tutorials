f_handler=open('type_function.py')
lc =0
for line in f_handler:
    lc = lc+1

print('line count: %d') % (lc)

#I have to reopen the file, otherwise it will read from the end of the file
f_handler=open('type_function.py')
file_content=f_handler.read();
print(file_content[0:20]) #print the first 20 characters
