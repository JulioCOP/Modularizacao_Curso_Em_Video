from exercicio112.utilidadesCeV import moeda
from exercicio112.utilidadesCeV import dados
numero= dados.leiaDinheiro("Informe o valor da mercadoria: R$ ")
taxa=int(input("Qual o índice de redução/ aumento em % ? "))
moeda.resumo(numero,taxa)

