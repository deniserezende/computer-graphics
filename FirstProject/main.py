import logging

import GeometricTransforms

option = input('MENU\n'
               'Escolha uma função:\n'
               '1. Translação\n'
               '2. Escala\n'
               '3. Rotação\n'
               '4. Cisalhamento\n'
               '5. Reflexão\n'
               '6. Rotação em relação a um ponto P\n'
               '7. Escala em relação a um ponto P\n'
               '8. Escala em relação ao centro geométrico do objeto\n')

option_int = int(option)
match option_int:
    case 1:
        Tx = int(input(f'Enter Tx= '))
        Ty = int(input(f'Enter Ty= '))
        x = int(input(f'Enter x= '))
        y = int(input(f'Enter y= '))
        new_x, new_y = GeometricTransforms.translation(x, y, Tx, Ty)
        print(f'Transladando o ponto ({x}, {y}) por (Tx={Tx}, Ty={Ty}): ({new_x}, {new_y})')

    case 2:
        Sx = int(input(f'Enter Sx= '))
        Sy = int(input(f'Enter Sy= '))
        x = int(input(f'Enter x= '))
        y = int(input(f'Enter y= '))
        new_x, new_y = GeometricTransforms.scale(x, y, Sx, Sy)
        print(f'Escalando o ponto ({x}, {y}) por (Sx={Sx}, Sy={Sy}): ({new_x}, {new_y})')

    case 3:
        x = int(input(f'Enter x= '))
        y = int(input(f'Enter y= '))
        angle = int(input(f'Enter angle= '))
        new_x, new_y = GeometricTransforms.rotation(x, y, angle)
        print(f'Rotacionando o ponto ({x}, {y}) por {angle}: ({new_x}, {new_y})')

    case 4:
        x = int(input(f'Enter x= '))
        y = int(input(f'Enter y= '))
        kx = int(input(f'Enter kx= '))
        ky = int(input(f'Enter ky= '))
        new_x, new_y = GeometricTransforms.shear(x, y, kx, ky)
        print(f'Cisalhamento do ponto ({x}, {y}) por ({kx}, {ky}): ({new_x}, {new_y})')

    case 5:
        x = int(input(f'Enter x= '))
        y = int(input(f'Enter y= '))
        type = input(f'Enter type option:\n'
                         f'x\n'
                         f'y\n'
                         f'y=x\n'
                         f'y=-x\n')
        new_x, new_y = GeometricTransforms.reflection(x, y, type)
        print(f'Reflexão do ponto ({x}, {y}) em {type}: ({new_x}, {new_y})')

    case 6:
        px = int(input(f'Enter px= '))
        py = int(input(f'Enter py= '))
        angle = int(input(f'Enter angle= '))
        x = int(input(f'Enter x= '))
        y = int(input(f'Enter y= '))

        result = GeometricTransforms.rotate_with_reference_point(x, y, math.radians(angle), px, py)
        print(f'Rotacionando o ponto ({x}, {y}) por {angle} em relação a ({px}, {py}): ({result[0].round(2)}, '
              f'{result[1].round(2)})')

    case 7:
        px = int(input(f'Enter px= '))
        py = int(input(f'Enter py= '))
        Sx = int(input(f'Enter Sx= '))
        Sy = int(input(f'Enter Sy= '))
        x = int(input(f'Enter x= '))
        y = int(input(f'Enter y= '))

        result = GeometricTransforms.scale_with_reference_point(x, y, Sx, Sy, px, py)
        print(f'Escala do ponto ({x}, {y}) em relação a ({px}, {py}) por (Sx={Sx}, Sy={Sy}): ({result[0].round(2)}, '
              f'{result[1].round(2)})')

    case 8:
        px = int(input(f'Enter px= '))
        py = int(input(f'Enter py= '))
        Sx = int(input(f'Enter Sx= '))
        Sy = int(input(f'Enter Sy= '))
        x = int(input(f'Enter x= '))
        y = int(input(f'Enter y= '))

        result = GeometricTransforms.scale_with_reference_point_as_geometric_center(x, y, Sx, Sy, px, py)
        print(
            f'Escala do ponto ({x}, {y}) em relação ao ponto geométrico ({px}, {py}) por (Sx={Sx}, Sy={Sy}): '
            f'({result[0].round(2)}, {result[1].round(2)})')
