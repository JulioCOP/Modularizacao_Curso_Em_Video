from exercicio109 import moeda

numero=float(input("Digite o valor da mercadoria R$: "))
taxa=int(input("Qual o índice de redução/ aumento em % ? "))
print('Para esta mercadoria:'
      f'\nAUMENTO {taxa}%:{moeda.aumentar(numero,taxa, True)}'
      f'\nDIMINUIÇÃO {taxa}%: {moeda.diminuir(numero,taxa, True)}'
      f'\nDOBRO: {moeda.dobro(numero,True)}'
      f'\nMETADE: {moeda.metade(numero, True)}')

