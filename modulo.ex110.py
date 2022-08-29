def aumentar(n=0,indice=0, formato=False):
    a= n + ((n*indice)/100)
    return a if formato is False else moeda(a)


def diminuir(n=0, indice=0, formato= False):
    d=n - ((n*indice)/100)
    return d if formato is False else moeda(d)

def dobro(n=0, formato=False):
    db= n*2
    return db if formato is False else moeda(db)

def metade(n=0, formato=False):
    m= n/2
    return m if formato is False else moeda(m)

def moeda(n=0,moeda='R$'):
    return f' {moeda} {n:.2f}'.replace(',','.')

def resumo (n=0,indice=0):
    print("#"*40)
    print("ANALISE DE PREÇO DA MERCADORIA".center(35))
    print("#"*40)
    print("-"*40)
    print(f'Preço da mercadoria: R$ \t{n:.2f}')
    print(f'Taxa a ser calculada: \t{indice} %')
    print(f"DOBRO DO PREÇO: \t{dobro(n,True)}")
    print(f'METADE DO PREÇO: \t{metade(n,True)}')
    print(f'AUMENTO DE {indice}%: \t{aumentar(n,indice,True)}')
    print(f'DIMINUIR {indice}%: \t{diminuir(n, indice,True)}')
    print("-"*40)


