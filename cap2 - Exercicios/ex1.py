# Exercício 1

nome_completo = input("Digite o seu nome completo: ")

print(f"Nome completo: {nome_completo.upper()} - {nome_completo.lower()}")
print(f"Número de letras: {len(nome_completo.replace(" ", ""))}")

novo_nome = nome_completo.split(" ")
novo_nome[-1] = "do Inatel"

print(f"Sobrenome substituído: {" ".join(novo_nome)}")
