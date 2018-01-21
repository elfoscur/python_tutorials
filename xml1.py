import xml.etree.ElementTree as ET

data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
        +41 77 1239 93219
    </phone>
    <email hide = "yes" />
    </person>'''

tree = ET.fromstring(data)

print("Name: ", tree.find('name').text)
print("Attr: ", tree.find('email').get('hide'))


stuff_data = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuch</name>
        </user>
        <user x="7">
            <id>002</id>
            <name>Steven</name>
        </user>
        </users>
        </stuff>'''

stuff = ET.fromstring(stuff_data)

lst = stuff.findall('users/user')  # with stuff it doesn't work!
print('User count: ', len(lst))

for item in lst:
    print('Name:', item.find('name').text)
    print('Id:', item.find('id').text)
    print('Attribute: ', item.get('x'))
