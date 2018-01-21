import json

data = '''
        [
        {
        "name" : "Chuck",
        "phone" : { "type" : "mobile",
                    "number" : "+41 77 1991 2133"},
        "email" : { "hide": "yes"}
        },
        {
        "name" : "Steven",
        "phone" : { "type" : "mobile",
                    "number" : "+41 88 3999 0900"},
        "email" : { "hide": "yes"}
        }
        ]'''

infos = json.loads(data)
for info in infos:
    print ('Name', info["name"])
    print ('Hide', info["email"]["hide"])

print(infos)
