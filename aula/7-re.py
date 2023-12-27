import re

text = "OneBitCode: Transformamos pessoas em programadores sem limites"

#Índice inicial e final de palavras

match = re.search(r'pessoas em programadores', text)
print('Índice inicial ', match.start())
print('Índice final ', match.end())

#Buscando índice que possui o ponto
site = 'https://onebitcode.com'
#match = re.search(r'.', site)
match = re.search(r'\.', site)
print(match)

#buscando lista de caracteres dentro de uma frase
pattern = "[a-m]"
result = re.findall(pattern, text)
print(text)
print(result)

#verificando início de uma string
#verificar se a String começa com algum caractere
rule = r'^A'
phrases = ['A casa está suja', 'O dia está lindo', 'Vamos dar uma volta']
for f in phrases:
  if re.match(rule, f):
    print(f"Corresponde: {f}")
  else:
    print(f"Não corresponde: {f}")

#Verificar final de String
rule_end = r'!$'
phrases2 = 'O dia está lindo!'
match = re.search(rule_end, phrases2)

if match:
  print("Sim, corresponde!")
else:
  print("Não corresponde!")