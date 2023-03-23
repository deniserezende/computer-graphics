import math
import GeometricTransforms

# Exemplo de TRANSLAÇÃO
print(f'------------ TESTANDO TRANSLAÇÃO ------------')
Tx = 3
Ty = -4
x = 4
y = 5
new_x, new_y = GeometricTransforms.translation(x, y, Tx, Ty)
print(f'Transladando o ponto ({x}, {y}) por (Tx={Tx}, Ty={Ty}): ({new_x}, {new_y})')
x = 8
y = 5
new_x, new_y = GeometricTransforms.translation(x, y, Tx, Ty)
print(f'Transladando o ponto ({x}, {y}) por (Tx={Tx}, Ty={Ty}): ({new_x}, {new_y})')
x = 8
y = 8
new_x, new_y = GeometricTransforms.translation(x, y, Tx, Ty)
print(f'Transladando o ponto ({x}, {y}) por (Tx={Tx}, Ty={Ty}): ({new_x}, {new_y})')
x = 6
y = 10
new_x, new_y = GeometricTransforms.translation(x, y, Tx, Ty)
print(f'Transladando o ponto ({x}, {y}) por (Tx={Tx}, Ty={Ty}): ({new_x}, {new_y})')
x = 4
y = 8
new_x, new_y = GeometricTransforms.translation(x, y, Tx, Ty)
print(f'Transladando o ponto ({x}, {y}) por (Tx={Tx}, Ty={Ty}): ({new_x}, {new_y})')


# Exemplo de ESCALA
print(f'------------ TESTANDO ESCALA ------------')
Sx = 1/2
Sy = 1/2
x = 4
y = 5
new_x, new_y = GeometricTransforms.scale(x, y, Sx, Sy)
print(f'Escalando o ponto ({x}, {y}) por (Sx={Sx}, Sy={Sy}): ({new_x}, {new_y})')
x = 8
y = 5
new_x, new_y = GeometricTransforms.scale(x, y, Sx, Sy)
print(f'Escalando o ponto ({x}, {y}) por (Sx={Sx}, Sy={Sy}): ({new_x}, {new_y})')
x = 8
y = 8
new_x, new_y = GeometricTransforms.scale(x, y, Sx, Sy)
print(f'Escalando o ponto ({x}, {y}) por (Sx={Sx}, Sy={Sy}): ({new_x}, {new_y})')
x = 6
y = 10
new_x, new_y = GeometricTransforms.scale(x, y, Sx, Sy)
print(f'Escalando o ponto ({x}, {y}) por (Sx={Sx}, Sy={Sy}): ({new_x}, {new_y})')
x = 4
y = 8
new_x, new_y = GeometricTransforms.scale(x, y, Sx, Sy)
print(f'Escalando o ponto ({x}, {y}) por (Sx={Sx}, Sy={Sy}): ({new_x}, {new_y})')


# Exemplo de ROTAÇÃO EM RELAÇÃO A UM PONTO P
print(f'------------ TESTANDO ROTAÇÃO EM RELAÇÃO A UM PONTO P ------------')
px = 4
py = 5
angle = 45

x = 6
y = 10
result = GeometricTransforms.rotate_with_reference_point(x, y, math.radians(angle), px, py)
print(f'Rotacionando o ponto ({x}, {y}) por {angle} em relação a ({px}, {py}): ({result[0].round(2)}, '
      f'{result[1].round(2)})')

x = 8
y = 8
result = GeometricTransforms.rotate_with_reference_point(x, y, math.radians(angle), px, py)
print(f'Rotacionando o ponto ({x}, {y}) por {angle} em relação a ({px}, {py}): ({result[0].round(2)}, '
      f'{result[1].round(2)})')

x = 8
y = 5
result = GeometricTransforms.rotate_with_reference_point(x, y, math.radians(angle), px, py)
print(f'Rotacionando o ponto ({x}, {y}) por {angle} em relação a ({px}, {py}): ({result[0].round(2)}, '
      f'{result[1].round(2)})')

x = 4
y = 5
result = GeometricTransforms.rotate_with_reference_point(x, y, math.radians(angle), px, py)
print(f'Rotacionando o ponto ({x}, {y}) por {angle} em relação a ({px}, {py}): ({result[0].round(2)}, '
      f'{result[1].round(2)})')

x = 4
y = 8
result = GeometricTransforms.rotate_with_reference_point(x, y, math.radians(angle), px, py)
print(f'Rotacionando o ponto ({x}, {y}) por {angle} em relação a ({px}, {py}): ({result[0].round(2)}, '
      f'{result[1].round(2)})')


# Exemplo de ESCALA EM RELAÇÃO A UM PONTO P
print(f'------------ TESTANDO ESCALA EM RELAÇÃO A UM PONTO P ------------')
px = 4
py = 5
Sx = 1/2
Sy = 1/2

x = 6
y = 10
result = GeometricTransforms.scale_with_reference_point(x, y, Sx, Sy, px, py)
print(f'Escala do ponto ({x}, {y}) em relação a ({px}, {py}) por (Sx={Sx}, Sy={Sy}): ({result[0].round(2)}, '
      f'{result[1].round(2)})')

x = 8
y = 8
result = GeometricTransforms.scale_with_reference_point(x, y, Sx, Sy, px, py)
print(f'Escala do ponto ({x}, {y}) em relação a ({px}, {py}) por (Sx={Sx}, Sy={Sy}): ({result[0].round(2)}, '
      f'{result[1].round(2)})')

x = 8
y = 5
result = GeometricTransforms.scale_with_reference_point(x, y, Sx, Sy, px, py)
print(f'Escala do ponto ({x}, {y}) em relação a ({px}, {py}) por (Sx={Sx}, Sy={Sy}): ({result[0].round(2)}, '
      f'{result[1].round(2)})')

x = 4
y = 5
result = GeometricTransforms.scale_with_reference_point(x, y, Sx, Sy, px, py)
print(f'Escala do ponto ({x}, {y}) em relação a ({px}, {py}) por (Sx={Sx}, Sy={Sy}): ({result[0].round(2)}, '
      f'{result[1].round(2)})')

x = 4
y = 8
result = GeometricTransforms.scale_with_reference_point(x, y, Sx, Sy, px, py)
print(f'Escala do ponto ({x}, {y}) em relação a ({px}, {py}) por (Sx={Sx}, Sy={Sy}): ({result[0].round(2)}, '
      f'{result[1].round(2)})')


# Exemplo de ESCALA EM RELAÇÃO AO CENTRO GEOMÉTRICO
print(f'------------ TESTANDO ESCALA EM RELAÇÃO AO CENTRO GEOMÉTRICO ------------')
px = 6
py = 7.2
Sx = 2
Sy = 2

x = 6
y = 10
result = GeometricTransforms.scale_with_reference_point_as_geometric_center(x, y, Sx, Sy, px, py)
print(f'Escala do ponto ({x}, {y}) em relação ao ponto geométrico ({px}, {py}) por (Sx={Sx}, Sy={Sy}): ({result[0].round(2)}, '
      f'{result[1].round(2)})')

x = 8
y = 8
result = GeometricTransforms.scale_with_reference_point_as_geometric_center(x, y, Sx, Sy, px, py)
print(f'Escala do ponto ({x}, {y}) em relação ao ponto geométrico ({px}, {py}) por (Sx={Sx}, Sy={Sy}): ({result[0].round(2)}, '
      f'{result[1].round(2)})')

x = 8
y = 5
result = GeometricTransforms.scale_with_reference_point_as_geometric_center(x, y, Sx, Sy, px, py)
print(f'Escala do ponto ({x}, {y}) em relação ao ponto geométrico ({px}, {py}) por (Sx={Sx}, Sy={Sy}): ({result[0].round(2)}, '
      f'{result[1].round(2)})')

x = 4
y = 5
result = GeometricTransforms.scale_with_reference_point_as_geometric_center(x, y, Sx, Sy, px, py)
print(f'Escala do ponto ({x}, {y}) em relação ao ponto geométrico ({px}, {py}) por (Sx={Sx}, Sy={Sy}): ({result[0].round(2)}, '
      f'{result[1].round(2)})')

x = 4
y = 8
result = GeometricTransforms.scale_with_reference_point_as_geometric_center(x, y, Sx, Sy, px, py)
print(f'Escala do ponto ({x}, {y}) em relação ao ponto geométrico ({px}, {py}) por (Sx={Sx}, Sy={Sy}): ({result[0].round(2)}, '
      f'{result[1].round(2)})')