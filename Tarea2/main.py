import json

def readJson():
    file = open('tarea.json')
    data = json.load(file)
    file.close()
    print(data)
    return data

dict = readJson()
for element in dict:
    print(element)
