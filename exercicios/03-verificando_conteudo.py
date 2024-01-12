import re

def check_caracter(string):
  rule = re.compile(r'[^a-zA-Z0-9]')
  string = rule.search(string)
  return not bool(string)


string = input('Digite sua frase para avaliar:\n')
print(check_caracter(string))