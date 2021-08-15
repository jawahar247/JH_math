def sqart(number):
  Y = 0
  z= (Y*Y)-number
  xold = 0
  while z != 0 or abs(z) < 0.001 :
    xnew = xold - (z/(2Y))
    z = (xnew*xnew)-number
  return result
