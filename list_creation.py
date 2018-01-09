###### constants
apostrophe="'"
comma=","
###############

filename='list.txt'
o_filename=filename[0:filename.find('.')]+'_1'+filename[filename.find('.'):]


fhand=open(filename)
o_fhand=open(o_filename,'w')

for line in fhand:
    line=line.strip()
    o_fhand.write(apostrophe+line+apostrophe+comma+'\n')
