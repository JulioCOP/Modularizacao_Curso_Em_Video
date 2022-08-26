#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro()
# e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda
numero=float(input("Digite o valor da mercadoria R$: "))
print('Para esta mercadoria:'
      f'\nAUMENTO 10%: R$ {moeda.aumentar(numero)}'
      f'\nDIMINUIÇÃO 10%: R$ {moeda.diminuir(numero)}'
      f'\nDOBRO: R$ {moeda.dobro(numero)}'
      f'\nMETADE: R$ {moeda.metade(numero):.2f}')