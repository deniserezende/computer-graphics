# Implemente em sua linguagem de preferência os seguintes algoritmos:

# - Algoritmo DDA para traçado de retas
# dda(x1, y1, x2, y2)
# *x1 e y1 são os pontos iniciais da reta, e x2 e y2 são os pontos finais da reta.
# *este não é necessáro generalizar para quaisquer tipos de retas. Implemente apenas o algoritmo padrão
# presente no material.

# - Algoritmo de Bresenhan (ponto médio) para traçado de retas
# bresenhan_retas(x1, y1, x2, y2)
# *x1 e y1 são os pontos iniciais da reta, e x2 e y2 são os pontos finais da reta.
# *generalize os algoritmos para traçar qualquer tipo de reta, independente da direção e intensidade da inclinação.

# - Algoritmo de Bresenhan (ponto médio) para traçado de circunferências
# bresenhan_circunferencia(xc, yc, r)
# *xc e yc representam o centro da circunferência e r é o raio.
# *no traçado de circunferências, generalize para desenhar uma circunferência centrada em qualquer ponto.
#
# Para exibir o resultado do traçado, você pode utilizar:
# - Plot do tipo scatter (matplotlib/pyplot) para plota apenas os pontos calculados no plano cartesiano
# (não é ideal, mas já conseguimos ter uma visualição simples e rápida)
# - Biblioteca pygame em python (segue anexo um código de exemplo)
# - Biblioteca graphics.py em python
# - Biblioteca PIL em python
# - Biblioteca graphics.h em C
# - Ou qualquer outra forma de sua preferência!
#
# *Podem utilizar a forma de exibição mais simples sem problemas, pois o importante neste momento são os cálculos
# estarem corretos. Mais a diante vamos estudar o OpenGL mais a fundo para síntese e exibição gráfica.


import logging

import MatrixTransformations

option = input('MENU\n'
               'ESCOLHA UMA FUNÇÃO:\n'
               '1. DDA\n'
               '2. ALGORITMO DE BRESENHAM PARA RETAS\n'
               '3. ALGORITMO DE BRESENHAM PARA CIRCUNFERÊNCIAS\n')

option_int = int(option)
match option_int:
    case 1:
        x_initial = int(input(f'Enter x initial = '))
        y_initial = int(input(f'Enter y initial = '))
        x_final = int(input(f'Enter x final = '))
        y_final = int(input(f'Enter y final = '))
        MatrixTransformations.dda(x_initial, y_initial, x_final, y_final)

    case 2:
        x_initial = int(input(f'Enter x initial = '))
        y_initial = int(input(f'Enter y initial = '))
        x_final = int(input(f'Enter x final = '))
        y_final = int(input(f'Enter y final = '))
        MatrixTransformations.bresenhams_line_algorithm(x_initial, y_initial, x_final, y_final)

    case 3:
        radius = int(input("Enter the radius of the circle: "))
        MatrixTransformations.bresenhams_circle_algorithm(radius)

    case other:
        logging.error('Not a option.')
        exit()
