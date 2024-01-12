import hashlib

#Verificar os algoritmos disponíveis
print(hashlib.algorithms_available)

#Algoritmos disponíveis de acordo com o SO
print(hashlib.algorithms_guaranteed)

#Utilizando o Sha256
algorithm = hashlib.sha256()
print(algorithm.digest())
message = "A melhor forma de prever o futuro é criá-lo".encode()
algorithm.update(message)
print(algorithm.hexdigest())


#Utilizando md5
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())