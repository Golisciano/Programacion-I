saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0

print(f"{'Mes':<5}{'Total pagado':<20}{'Saldo restante':<20}")

while saldo > 0:
    mes += 1

    if mes <= 12:
        pago = pago_mensual + 1000
    elif 61 <= mes <= 108:
        pago = pago_mensual + 1000
    else:
        pago = pago_mensual

    if saldo * (1 + tasa/12) < pago:
        pago = saldo * (1 + tasa/12)

    saldo = saldo * (1 + tasa/12) - pago
    total_pagado += pago

    print(f"{mes:<5}{round(total_pagado, 2):<20}{round(saldo, 2):<20}")
