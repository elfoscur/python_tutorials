import urllib

# it's like a file handler
fhand = urllib.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand:
    print(line.decode().strip()) #the line must be decoded to be converted in a string


#count world
fhand = urllib.urlopen('http://data.pr4e.org/romeo.txt')

words=dict()
for line in fhand:
    splitted_line = line.decode().split();
    for word in splitted_line:
        words[word]=words.get(word,0)+1
print words
