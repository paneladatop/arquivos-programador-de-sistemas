senha_correta = "lo1407"
senha_digitada = input('digite a senha: ')
while senha_digitada != senha_correta:
    print('senha errada! tente novamente.')
    senha_digitada = input("digite sua senha:")
    print('bem vindo ao sistema!')