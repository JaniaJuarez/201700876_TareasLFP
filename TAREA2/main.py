import json

def readJson():
    file = open('tarea2.json',)
    data = json.load(file)
    file.close()
    print("El tipo es")
    print(type(data))
    return data

dict = readJson()
for element in dict:
    print(element)

from xml.dom import minidom
doc = minidom.parse('tarea2.xml',)
personas = doc.getElementsByTagName("persona")
for persona in personas:
    atributo = persona.getAttribute("atributo")
    edad = persona.getElementsByTagName("edad")[0]
    menordeedad = persona.getElementsByTagName("menordeedad")[0]
    estatura = persona.getElementsByTagName("estatura")[0]
    print("El tipo es")
    print(type(persona))
    print("atributo:%s " % atributo)
    print("edad:%s" % edad.firstChild.data)
    print("menordeedad:%s" % menordeedad.firstChild.data)
    print("estatura:%s" % estatura.firstChild.data)


import csv

with open('tarea2.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print("El tipo es")
        print(type(row))
        print("registro: {0},edad:{1},menordeedad:{2},estatura:{3}".format(row[0],row[1],row[2],row[3]))


