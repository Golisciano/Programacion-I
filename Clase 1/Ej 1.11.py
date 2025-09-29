saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0

# Encabezado de la tabla
print(f"{'Mes':<5}{'Total pagado':<20}{'Saldo restante':<20}")

while saldo > 0:
    mes += 1
    
    # Determinar pago del mes según los extras
    if mes <= 12:
        pago = pago_mensual + 1000
    elif 61 <= mes <= 108:
        pago = pago_mensual + 1000
    else:
        pago = pago_mensual
    
    # Calcular saldo con interés antes de aplicar el pago
    saldo_con_interes = saldo * (1 + tasa/12)
    
    # Ajustar último pago si supera lo adeudado
    if pago > saldo_con_interes:
        pago = saldo_con_interes
    
    # Actualizar saldo y total pagado
    saldo = saldo_con_interes - pago
    total_pagado += pago
    
    # Imprimir fila
    print(f"{mes:<5}{round(total_pagado, 2):<20}{round(saldo, 2):<20}")
