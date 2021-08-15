def sqart(number):
  xnew = 1
  z= (xnew*xnew)-number
  xold = 0
  while z != 0 or abs(z) < 0.0001 :
    xnew = xold - (z/(2*xnew))
    z = (xnew*xnew)-number
  return z
def cuberoot(number):
  Y = 1
  Z = (Y*Y*Y) - number 
  x_old = 0
  while Z !=0 and abs(Z) < 0.0001:
   Y = x_old - (Z/3*Y*Y)
    Z = (Y*Y*Y) - number
    reurn Z
