import random
import statistics
import csv

def medir_temp(n):
    temps = [random.normalvariate(37, 0.2) for _ in range(n)]
    with open('temperaturas.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['temperaturas'])
        for t in temps:
            writer.writerow([round(t, 2)])
    return temps

def resumen_temp(n):
    temps = medir_temp(n)
    t_max = max(temps)
    t_min = min(temps)
    t_prom = sum(temps) / n
    t_mediana = statistics.median(temps)
    return (t_max, t_min, t_prom, t_mediana)

if __name__ == "__main__":
    n = 999
    resumen = resumen_temp(n)
    print(f"Máxima: {resumen[0]:.2f}")
    print(f"Mínima: {resumen[1]:.2f}")
    print(f"Promedio: {resumen[2]:.2f}")
    print(f"Mediana: {resumen[3]:.2f}")
