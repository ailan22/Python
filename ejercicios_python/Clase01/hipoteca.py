# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca

saldo = 500000
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0
adelanto = 1000
mes = 0
while saldo > 0:
    if mes < 12:
        saldo = saldo * (1+tasa/12) - pago_mensual - adelanto
        total_pagado = total_pagado + pago_mensual + adelanto
        mes = mes + 1
      # print('Mes:', mes, 'Total pagado:', round(total_pagado,2)) sin uso de f-strings
        print(f'Mes: {mes} Total pagado: {round(total_pagado, 2)}') # uso de f-strings
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
        mes = mes + 1
      # print('Mes:', mes, 'Total pagado:', round(total_pagado,2)) sin uso de f-strings
        print(f'Mes: {mes} Total pagado: {round(total_pagado, 2)}') # uso de f-strings
