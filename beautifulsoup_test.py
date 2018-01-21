import urllib2
import bs4

print bs4  # show informations on the module
print urllib2

url = 'https://www.crummy.com'
req = urllib2.Request(url)
resp = urllib2.urlopen(req).read()

soup = bs4.BeautifulSoup(resp, 'html.parser')

print(type(soup))

tags = soup('img')
for tag in tags:
    print(tag.get('src', None)) # like Oracle nvl
