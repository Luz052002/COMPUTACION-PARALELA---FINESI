import random
import time

def suma_ordinaria(a, b):
    c = [0] * len(a)
    for i in range(len(a)):
        c[i] = a[i] + b[i]
    for i in range(len(c)):
        print(f"c[{i}]={c[i]}")
    return c

if __name__ == "__main__":
    # Generar arrays aleatorios
    a = [random.randint(1, 100) for _ in range(5)]
    b = [random.randint(1, 100) for _ in range(5)]

    start_time = time.time()
    c_ordinaria = suma_ordinaria(a, b)
    end_time = time.time()
    tiempo_ordinaria = end_time - start_time

    print(f"Tiempo de suma ordinaria: {tiempo_ordinaria:.6f} segundos")