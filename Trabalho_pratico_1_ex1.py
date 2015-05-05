def distancia(p1,p2):
	return ( ( float(p1[0]) - float(p2[0]) )**2 + ( float(p1[1]) - float(p2[1]) )**2 )**(1/2)

def dig():
	return input("Digite o ponto no seguinte formato 'x,y': ").split(',')

p1 = dig()
p2 = dig()

print("x1 = {0}\ty1= {1}\nx2 = {2}\ty2 = {3}\ndistancia = {4}".\
	format( p1[0], p1[1], p2[0], p2[1], distancia(p1,p2) ))

input()

# Nota: 1.0
# Great job!
