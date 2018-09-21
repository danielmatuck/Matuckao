import math
a = float(input("Mostre o primeiro número: "))
b = float(input("Mostre o segundo número: "))
c= float(input("Mostre o terceiro número: "))
if a>b>c:
    print("O maior número é",a, "e o menor número é",c)
if b>a>c:
    print("O maior número é",b, "e o menor número é",c)
if c>a>b:
    print("O maior número é",c, "e o menor é",b)
if a>c>b:
    print("O maior número é",a,"e o menor é",c)
if b>c>a:
    print("O maior número é",b,"e o menor número é",a)
if c>b>a:
    print("O maior número é",b,"e o menor número é",a)

