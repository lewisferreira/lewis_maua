notas = []
S = 0
while True:
	try:
		nota = float(raw_input("Digite a nota: "))
	except:
		print("voce nao digitou um numero")
		continue
	if nota < 0:
		break
	notas.append(nota)
for i in notas:
	S += i
if len(notas) != 0:
	print("a media eh: {0}\na maior nota foi: {1}".format(S/len(notas), max(notas) ))
else:
	print("nao foi digitado nenhuma nota...")

#Nota: 1.1
#Comentario: Valia 1.0 mas dei +0.1 pela sintese do codigo. Bonus points por usar tabs
#           no lugar de espaco
