def soma(a,b): 
	return a+b

def entra():
	return int(input("Digite a nota: "))

a = entra()
b = entra()
c = entra()

print(soma(soma(a, b), c)/3)	#reaproveitando a funcao de soma criada antes
input()

# Nota: 0.9
# Comentario: Bom uso de funcoes, entretanto input desnecessario no final
