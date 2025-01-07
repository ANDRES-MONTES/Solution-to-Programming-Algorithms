def solution(inputArray, k):
    import numpy as np
    lista = np.array(inputArray)
    sums = np.convolve(lista, np.ones(k, int), 'valid')
    return np.max(sums)

            
            

if __name__ == '__main__':
    data =   [2, 3, 5, 1, 6]
    k = 2
    result = solution(data, k)
    print(result)
    import numpy as np
import time

def metodo_manual(data, tamaño_ventana):
    return [sum(data[i:i+tamaño_ventana]) for i in range(len(data) - tamaño_ventana + 1)]

def metodo_numpy(data, tamaño_ventana):
    return np.convolve(data, np.ones(tamaño_ventana, dtype=int), 'valid')

# Crear datos de prueba
datos = np.random.randint(0, 100, 1000000)
tamaño_ventana = 100

# Medir tiempo para el método manual
inicio = time.time()
resultado_manual = metodo_manual(datos, tamaño_ventana)
fin = time.time()
tiempo_manual = fin - inicio

# Medir tiempo para el método NumPy
inicio = time.time()
resultado_numpy = metodo_numpy(datos, tamaño_ventana)
fin = time.time()
tiempo_numpy = fin - inicio

print(f"Tiempo método manual: {tiempo_manual:.4f} segundos")
print(f"Tiempo método NumPy: {tiempo_numpy:.4f} segundos")
print(f"NumPy es {tiempo_manual / tiempo_numpy:.2f} veces más rápido")