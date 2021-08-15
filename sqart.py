def sqart(number):
  xnew = 1
  z= (xnew*xnew)-number
  xold = 0
  while z != 0 or abs(z) < 0.0001 :
    xnew = xold - (z/(2*xnew))
    z = (xnew*xnew)-number
  return z

