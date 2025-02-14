print('Verificação de maioridade para entrar no show: ')

idade = int(input('Digite a sua idade'))

if idade <= 18:
    print('Usuário é maior de idade, liberado!')
else:
    print('Usuário menor de idade, só pode entrar com responsável!')