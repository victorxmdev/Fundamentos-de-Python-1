print('Calculadora')

n1 = float(input('='))
operacao = input('Escolha a operação: + - * /')
n2 = float(input('='))

if operacao == '+':
    calculo = n1 + n2
    print(calculo)
elif operacao == '-':
    calculo = n1 + n2
    print(calculo)
elif operacao == '*':
    calculo = n1 * n2
    print(calculo)
elif operacao == '/':
    if n2 > 0:
        calculo = n1 / n2
        print(calculo)
    else: 
        print('O zero não pode dividir, inicie novamente!')
else:
    print('Operação digitada errada, inicie novamente!')