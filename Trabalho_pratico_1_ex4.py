def triangulo(a,b,c):
	if a+b < c:
		return False
	if c**2 == b**2 + a**2:
		return True
	else:
		return False

def dig(i):
	if i == 1:
		return int(input("Digite o tamanho do cateto: "))
	else:
		return int(input("Digite o tamanho da hipotenusa: "))

a = dig(1)
b = dig(1)
c = dig(2)

if triangulo(a,b,c):
	print("Area = {0}".format( (a+b)/2) )
else:
	print("Os catetos {0} e {1} nao formam um triangulo retangulo com hipotenusa {2}".format(a,b,c))

input()
