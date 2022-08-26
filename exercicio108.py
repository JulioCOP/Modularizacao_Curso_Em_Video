from exercicio108 import moeda

numero=float(input("Digite o valor da mercadoria R$: "))
print('Para esta mercadoria:'
      f'\nAUMENTO 10%: R$ {moeda.moeda(moeda.aumentar(numero))}'
      f'\nDIMINUIÇÃO 10%: R$ {moeda.moeda(moeda.diminuir(numero))}'
      f'\nDOBRO: R$ {moeda.moeda(moeda.dobro(numero))}'
      f'\nMETADE: R$ {moeda.moeda(moeda.metade(numero))}')