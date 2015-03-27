import math

def pol(p):
	p[0] = float(p[0])
	p[1] = float(p[1])
	r = ( p[0]**2 + p[1]**2 )**(1/2)
	ang = math.atan2(p[0],p[1])
	ang = 180*ang/math.pi
	print("{0} /{1}º".format(r, ang))

def dig():
	return input("Digite o ponto no seguinte formato 'x,y': ").split(',')

p1 = dig()
p2 = dig()
pol(p1)
pol(p2)

input()
