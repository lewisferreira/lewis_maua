notas = []
S = 0
H = 0
while True:
	try:
		nota = float(raw_input("Digite a nota: "))
	except:
		print("voce nao digitou um numero")
		continue
	if nota < 0:
		break
	if nota > H:
		H = nota
	notas.append(nota)
for i in notas:
	S += i
if len(notas) != 0:
	print("a media eh: {0}\na maior nota foi: {1}".format(S/len(notas), H ))
else:
	print("nao foi digitado nenhuma nota...")
