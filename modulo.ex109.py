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