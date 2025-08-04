# Exercício 2

numero = int(input("Escolha um número: "))
tabuada_init = int(input("Onde a tabuada deve começar: "))
tabuada_end = int(input("Até onde deve ir sua tabuada: "))

print(f"# TABUADA DO {numero}:")
for i in range(tabuada_init, tabuada_end+1):
    print(f"{numero} x {i} = {numero*i}")
