row = 8
cols = 4

m = [[i*cols+j for j in range(cols)] for i in range(row)]
print(m)

def get_maximo(lst):
    return max(lst)

elem_maximos = list(map(get_maximo, m))
print('Los elementos mayores son: ', elem_maximos)
