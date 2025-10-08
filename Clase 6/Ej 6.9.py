import csv
import matplotlib.pyplot as plt

def plotear_temperaturas():
    temperaturas = []

    with open('temperaturas.csv', 'r', encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector) 
        for fila in lector:
            try:
                temperaturas.append(float(fila[0]))
            except ValueError:
                continue 
            
    plt.hist(temperaturas, bins=30, color='skyblue', edgecolor='black')
    plt.title('Histograma de Temperaturas Simuladas')
    plt.xlabel('Temperatura corporal (°C)')
    plt.ylabel('Frecuencia')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

if __name__ == "__main__":
    plotear_temperaturas()
