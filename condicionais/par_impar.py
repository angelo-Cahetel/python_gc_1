# Solicite ao usuário que insira um número e, em seguida, use uma estrutura `if else` para determinar se o número é par ou ímpar.


# solicitar ao usuário para inserir um número
numero = int(input('Digite um numero:'))

# usar a estrutura if e else para determinar se o número é par ou impar
if numero % 2 == 0:
    print(f'O número {numero} é par.')
else: 
    print(f'O número {numero} é ímpar.')