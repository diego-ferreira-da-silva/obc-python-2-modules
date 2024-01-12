import json

#Conversão de String para Dicionários
person = '{"name":"Diego", "languagens":["Python", "Javascript"]}'
person_dict = json.loads(person)
print(person_dict)
print(person_dict['languagens'])

#convertendo Dicionários para Json
person_json = json.dumps(person_dict)
print(person_json)

print(type(person_dict))
print(type(person_json))

print(json.dumps(person_dict, indent=4, sort_keys=True))

#Salvando Json em TXT
with open("person.txt", "w") as json_file:
  json.dump(person_dict, json_file)
  
#Lendo Json externo
with open("iris.json", "r") as f:
  data = json.load(f)
  print(data)