def entra():
	return int(input("Digite o numero: "))

def checa_par(x):
	if x % 2 == 0:
		print("o numero e par!")
	else:
		print("o numero e impar!")

a = entra()
checa_par(a)
input()

# Nota: 1.0
# Comentario: Novamente bom uso de funcoes, mas input() final desnecessario
