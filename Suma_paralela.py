import multiprocessing
import random
import time

def worker(tid, a, b, c):
    c[tid] = a[tid] + b[tid]
    print(f"c[{tid}]={c[tid]}")

def suma_paralela(a, b):
    c = multiprocessing.Array('i', len(a))  # Shared array

    processes = []
    for tid in range(len(a)):
        process = multiprocessing.Process(target=worker, args=(tid, a, b, c))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    return list(c)

if __name__ == "__main__":
    # Generar arrays aleatorios
    a = [random.randint(1, 100) for _ in range(5)]
    b = [random.randint(1, 100) for _ in range(5)]

    start_time = time.time()
    c_paralela = suma_paralela(a, b)
    end_time = time.time()
    tiempo_paralela = end_time - start_time

    print(f"Tiempo de suma paralela: {tiempo_paralela:.6f} segundos")