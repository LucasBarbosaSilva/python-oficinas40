xa, ya = [float(x) for x in input("Digite os valores da primeira coordenada: ").split()]
xb, yb = [float(x) for x in input("Digite os valores da segunda coordenada: ").split()]

import math

resultado = math.sqrt(((xb - xa)**2 + (yb - ya)**2))

print ("A distância é de ", resultado)
if(xa == ya and xb == yb):
  print("Tudo igual")