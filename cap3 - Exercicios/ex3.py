# Exercício do aluno
aluno = {}

aluno["nome"] = input("Digite seu nome: ")
aluno["nota"] = float(input("Digite sua nota: "))

if aluno["nota"] >= 50:
    aluno["status"] = "AP"
else:
    aluno["status"] = "RP"

print(aluno)