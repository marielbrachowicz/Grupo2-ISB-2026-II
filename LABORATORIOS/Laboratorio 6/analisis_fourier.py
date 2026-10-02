import json
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from scipy import signal

#CONFIGURACIÓN

GAIN = 40000
VCC = 3.3
NBITS = 10

BANDAS = {"Delta": (0.5, 4), "Theta": (4, 8), "Alfa":  (8, 12), "Beta":  (12, 25), "Gamma": (25, 45)}

#Buscar archivos
archivos = list(Path(".").glob("*.txt"))


#LEER ARCHIVO

def cargar_eeg(archivo):

    #Leer encabezado
    with open(archivo, "r") as f:
        for linea in f:
            if linea.startswith("# {"):
                meta = list(json.loads(linea[1:]).values())[0]

    #Leer datos
    datos = np.loadtxt(archivo, comments="#")
    columnas = meta["column"]
    A1 = datos[:, columnas.index("A1")]
    A2 = datos[:, columnas.index("A2")]
    fs = meta["sampling rate"]
    adc = np.column_stack((A1, A2))
    #Conversión ADC -> microvoltios
    eeg = ((adc / 2**NBITS - 0.5) * VCC / GAIN) * 1e6
    
    return eeg, adc, fs


#SEPARAR BANDAS CON FOURIER

def separar_bandas(x, fs):

    x = x - np.mean(x)
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1/fs)

    resultado = {}

    for nombre, (f1, f2) in BANDAS.items():
        mascara = (f >= f1) & (f < f2)
        X_banda = X * mascara
        resultado[nombre] = np.fft.irfft(X_banda, n=len(x))
    return resultado


#ANALIZAR CADA ARCHIVO

for archivo in archivos:

    eeg, adc, fs = cargar_eeg(archivo)

    print("\n========================================")
    print("Analizando:", archivo.stem)
    print("========================================")
    print("Frecuencia de muestreo:", fs, "Hz")
    print("Duración:", round(len(eeg)/fs, 2), "s")

    #Porcentaje de saturación
    saturacion = np.mean(
        (adc <= 0) | (adc >= 2**NBITS - 1),
        axis=0
    ) * 100

    print("Saturación A1:", round(saturacion[0], 2), "%")
    print("Saturación A2:", round(saturacion[1], 2), "%")


    #SEÑAL EEG EN EL TIEMPO

    tiempo = np.arange(len(eeg)) / fs
    plt.figure(figsize=(12,4))
    plt.plot(tiempo, eeg[:,0] - np.mean(eeg[:,0]), label="A1", linewidth=0.7)
    plt.plot(tiempo, eeg[:,1] - np.mean(eeg[:,1]), label="A2", linewidth=0.7)
    plt.xlabel("Tiempo [s]")
    plt.ylabel("EEG [µV]")
    plt.title("Señal EEG - " + archivo.stem)
    plt.legend()
    plt.grid()
    plt.show()

    #FFT

    plt.figure(figsize=(10,4))

    for canal in range(2):

        x = eeg[:,canal] - np.mean(eeg[:,canal])

        #Ventana Hann (de DSP lol)
        ventana = np.hanning(len(x))
        X = np.fft.rfft(x * ventana)
        f = np.fft.rfftfreq(len(x), 1/fs)
        amplitud = 2*np.abs(X) / np.sum(ventana)

        #Mostrar solamente 0.5-50 Hz
        m = (f >= 0.5) & (f <= 50)
        plt.plot(f[m], amplitud[m], label="A" + str(canal+1))

    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("Amplitud [µV]")
    plt.title("Espectro FFT - " + archivo.stem)
    plt.legend()
    plt.grid()
    plt.show()


    #SEPARACIÓN EN BANDAS

    #Usamos A1
    x = eeg[:,0]
    bandas = separar_bandas(x, fs)
    #10s
    inicio = 5
    duracion = 10
    m = (tiempo >= inicio) & (tiempo < inicio + duracion)
    plt.figure(figsize=(12,8))

    i = 1
    for nombre, señal in bandas.items():

        plt.subplot(5,1,i)
        plt.plot(tiempo[m], señal[m])
        plt.ylabel(nombre)
        plt.grid()

        i += 1

    plt.xlabel("Tiempo [s]")
    plt.suptitle("Bandas EEG - " + archivo.stem + " - A1")
    plt.tight_layout()
    plt.show()

    #POTENCIA DE CADA BANDA

    potencias = {}

    for nombre, señal in bandas.items():
        potencias[nombre] = np.mean(señal**2)
        
    total = sum(potencias.values())

    print("\nPotencia relativa A1:")
    relativas = []

    for nombre in BANDAS:

        relativa = potencias[nombre] / total
        relativas.append(relativa)
        print(nombre, "=", round(relativa*100, 2), "%")

    #Gráfico de potencia relativa
    plt.figure(figsize=(8,4))
    plt.bar(BANDAS.keys(), np.array(relativas)*100)
    plt.ylabel("Potencia relativa [%]")
    plt.title("Potencia por banda - " + archivo.stem)
    plt.grid(axis="y")
    plt.show()


    #ESPECTROGRAMA
    x = eeg[:,0] - np.mean(eeg[:,0])
    f, t, S = signal.spectrogram(x, fs, nperseg=int(2*fs), noverlap=int(fs))

    m = f <= 50
    plt.figure(figsize=(10,4))
    plt.pcolormesh(t, f[m], 10*np.log10(S[m] + 1e-12), shading="auto")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Frecuencia [Hz]")
    plt.title("Espectrograma - " + archivo.stem + " - A1")
    plt.colorbar(label="Potencia [dB]")
    plt.show()
