import random

#valores aleatórios da lista
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.choice(list1))

#intervalo de valores random
r1 = random.randint(5, 25)
print(r1)

#Seleciona caractere aleatório de String
name = "Curso Python"
r2 = random.choice(name)
print(r2)

#Seleciona mais de um aleatório
print(random.sample(list1, 3))
print(random.sample(name, 2))