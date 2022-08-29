def leiaDinheiro(msg):
    valido=False
#variavel (flag)False, pois o valor ainda não é valido
    while not valido:
        entrada=str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada=='':
            print(f'\033[31mERRO: \"{entrada} é um preço inválido!\033[m')
        else:
            valido=True
            return float(entrada)
#para esse código, força o programa a solicitar entrada de dados que sejam números
#em caso de digitar uma string por exemplo, ele retorna mensagem de erro
#ao usuário digitar um valor com "," o programa retorna também os valores
#e em caso do usuário dar um enter, o programa ainda solicita que o mesmo informe um valor



