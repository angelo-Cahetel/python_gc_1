# Solicite um nome de usuário e uma senha e use uma estrutura `if else` para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

# valores esperados para o acesso
nome_esperado = 'usuario'
senha_esperada = '250803an'

# Solicitar ao usuário que insira o nome de usuário e a senha
nome_usuario = input('Por favor, digite seu nome de usuário: ')
senha_usuario = input('Por favor, digite sua senha de usuário')

# Verifica se o nome de usuário e a senha fornecida correspondem aos valores esperados
if nome_usuario == nome_esperado and senha_usuario == senha_esperada:
    print('Acesso concedido com sucesso!')
else: 
    print('Nome de usuário ou senha incorretos')