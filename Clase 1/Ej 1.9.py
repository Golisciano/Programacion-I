
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0

while saldo > 0:
    mes += 1
    if mes <= 12:  
        saldo = saldo * (1 + tasa/12) - (pago_mensual + 1000)
        total_pagado += pago_mensual + 1000
    elif 61 <= mes <= 108:
        pago = pago_mensual + 1000
    else:
        saldo = saldo * (1 + tasa/12) - pago_mensual
        total_pagado += pago_mensual

print('Total pagado:', round(total_pagado, 2))
print('Meses:', mes)
