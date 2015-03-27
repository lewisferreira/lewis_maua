def distancia(p1,p2):
	return ( ( float(p1[0]) - float(p2[0]) )**2 + ( float(p1[1]) - float(p2[1]) )**2 )**(1/2)

def dist_n_pts(pts):
	maior = 0
	for i in range(len(pts)):
		for j in range(i+1,len(pts)):
			print("p{3} = {0}\tp{4} = {1}\tDist = {2}\n\n".format( pts[i], pts[j], distancia(pts[i],pts[j]), i+1, j+1))
			if distancia(pts[i],pts[j]) > maior:
				maior = distancia(pts[i],pts[j])
				p1 = i+1
				p2 = j+1
	return [maior, p1, p2]

def dig():
	return input("Digite o ponto no seguinte formato 'x,y': ").split(',')

pts = []
for n in range(int(input("Quantos numeros deseja digitar?\t"))):
	pts.append(dig())

resultado = dist_n_pts(pts)
print("A maior distancia e {0}, entre os ponto {1} e {2}".format(resultado[0],resultado[1],resultado[2]))

input()
