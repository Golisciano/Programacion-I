# costo_camion.py
import sys
import informe_final  # importa funciones de informe_final

def costo_camion(nombre_archivo):
    camion = informe_final.leer_camion(nombre_archivo)
    total = 0.0
    for lote in camion:
        total += lote['cajones'] * lote['precio']
    return total

def f_principal(args):
    if len(args) != 2:
        print('Uso: costo_camion.py archivo_camion')
        return
    archivo = args[1]
    costo = costo_camion(archivo)
    print(f'Costo total: {costo:.2f}')

if __name__ == '__main__':
    f_principal(sys.argv)
