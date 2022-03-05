row = 8
cols = 4

m = []
for i in range(row):
    r = []
    for j in range(cols):
        r.append(i*cols+j)
    m.append(r)
print(m)

m2 = [[i*cols+j for j in range(cols)] for i in range(row)]
print(m2)

def get_maximo(lst):
    return max(lst)

elem_maximos = list(map(get_maximo, m))
print('Los elementos mayores son: ', elem_maximos)
