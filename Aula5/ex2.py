print('Digite os 3 comprimentos de um triângulo: ')

a = int(input('Digite o primeiro lado: '))
b = int(input('Digite o segundo lado: '))
c = int(input('Digite o terceiro lado: '))

if a == b == c:
    print('O triângulo é equilátero')
elif a == b or a == c or b == c:
    print('O triângulo é isósceles')
else:
    print('O triângulo é escaleno')
