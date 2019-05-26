import json
import urllib.request

# download raw json object
url = "https://raw.githubusercontent.com/jdolan/quetoo/master/src/cgame/default/ui/settings/SystemViewController.json"
data = urllib.request.urlopen(url).read().decode()

# parse json object and place into dictionary
obj = json.loads(data)

# output some object attributes
var = input("Please enter something: "'\n')

if var[0] == '.':
    var = var[1:]
elif var[0] =='#':
    var = var[1:]

def getvalues(obj, key):
    arr = []

    def extract(obj, arr, key):

        #checks if the JSON obj is a dictionary
        if isinstance(obj, dict):
            for k, v in obj.items():
                
                #Since classNames always returns a list we can append it to the array immediately
                if k == 'classNames':
                    arr.append(v)

                #for classes and identifiers we must recursively call the function in order to get the key we want inside the nested child views
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results


count = 0

#finding classes
classobj = getvalues(obj, 'class')

for i in classobj:
    if i == var:
        count = count + 1
        print('"class": "' + var +'"')


#finding classNames
classNamesobj = getvalues(obj, 'classNames')
for i in classNamesobj:
    for i2 in i:
        if i2 == var:
            count = count + 1
            print('"classNames": ',i)

#finding identifiers
identifierobj = getvalues(obj, 'identifier')

for i in identifierobj:
    if i == var:
        count = count + 1
        print('"identifier": "' + var +'"')

print('\n'"The amount of times this selector appears:", count)