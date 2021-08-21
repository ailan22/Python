
precios_dic = open('../Data/precios.csv', 'rt')
row = precios_dic.readline(precios_dic)
camion_lista = open('../Data/camion.csv')
print(precios_dic)

#precios_venta= 0.00
#for row in camion:
#    if row[0] in precios_dic:
#        precios_venta += (precios['camion[row[0]]'] * row[1])