i = 0
S = 0
while True:
	nota = float(input("Digite a nota: "))
	if nota < 0:
		break
	S += nota
	i += 1
if i != 0:
	print("a media eh: {0}".format(S/i))
else:
	print("nao foi digitado nenhuma nota...")
input()

# Nota: 1.0
# Comentario: Excelente otimizacao
