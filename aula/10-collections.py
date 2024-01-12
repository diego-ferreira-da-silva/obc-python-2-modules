from collections import Counter, namedtuple, deque
from operator import itemgetter

#Contar itens de uma lista
fruits = ["Maçã", "Banana","Uva", "Pêra", "Uva", "Maçã", "Laranja", "Abacaxi", "Tangerina", "Uva", "Pêra", "Banana", "Laranja", "Abacate"]
print(fruits)
print(Counter(fruits))

#Tupla nomeada
game = namedtuple('game', ['name', 'price', 'note'])
g1 = game("God of War", 200, 10.0)
print(g1)

#Ordenando dicionários
studants = {"Diego":32, "Amanda": 35, "Olivia":1}
a = sorted(studants.items(), key=itemgetter(0))
print(studants)
print(a)

#Fila com ambas extremidades
deq = deque([20, 30, 60, 120])
print(deq)
deq.appendleft(10)
print(deq)
deq.pop()
print(deq)
deq.popleft()
print(deq)