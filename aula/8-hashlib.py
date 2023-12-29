import hashlib

#Verificar os algoritmos disponíveis
print(hashlib.algorithms_available)

#Algoritmos disponíveis de acordo com o SO
print(hashlib.algorithms_guaranteed)

#Utilizando o Sha256
algorithm = hashlib.sha256()
print(algorithm.digest())