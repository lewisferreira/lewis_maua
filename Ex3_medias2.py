notas = []
S = 0
while True:
	nota = float(input("Digite a nota: "))
	if nota < 0:
		break
	notas.append(nota)
for i in notas:
	S += i
if len(notas) != 0:
	print("a media eh: {0}".format(S/len(notas)))
else:
	print("nao foi digitado nenhuma nota...")
input()
