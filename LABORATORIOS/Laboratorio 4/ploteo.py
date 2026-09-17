import numpy as np
import matplotlib.pyplot as plt
import glob
import os

# Frecuencia de muestreo
fs = 1000

# Buscar todos los archivos .txt dentro de datos
archivos = glob.glob("datos/*.txt")

print("Archivos encontrados:")
print(archivos)

# Crear carpeta para guardar las gráficas
os.makedirs("ploteos", exist_ok=True)

# Procesar cada archivo
for archivo in archivos:

    # Cargar datos
    datos = np.loadtxt(archivo, comments="#")

    # ECG: columna A1 (sexta columna)
    ecg = datos[:, 5]

    # Crear eje de tiempo
    t = np.arange(len(ecg)) / fs

    # Obtener nombre del archivo
    nombre = os.path.basename(archivo)
    nombre_sin_extension = os.path.splitext(nombre)[0]

    # Crear gráfica
    plt.figure(figsize=(12, 5))
    plt.plot(t, ecg)

    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.title(f"Señal ECG - {nombre_sin_extension}")
    plt.grid()

    plt.tight_layout()

    # Guardar gráfica
    ruta_guardado = f"ploteos/{nombre_sin_extension}.png"
    plt.savefig(ruta_guardado, dpi=300)

    # Cerrar la figura para pasar a la siguiente
    plt.close()

    print(f"Guardado: {ruta_guardado}")

print("Todas las gráficas fueron guardadas.")