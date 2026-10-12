# Filtrado digital de una señal ECG

## Resumen 

En este laboratorio trabajamos con un notebook de Python que reunía todo el procedimiento. Durante la clase se revisó qué hacía cada bloque de código y cómo se podían interpretar las gráficas que iba generando.
Para el desarrollo usamos el archivo "basal_D1.txt", un registro propio de ECG en derivación I (D1) que obtuvimos en el laboratorio de ECG.

## 1. Lectura y visualización del ECG
Primero se importaron las librerías necesarias para leer los datos, procesar las señales y hacer las gráficas. Después se revisó la cabecera del archivo para identificar la frecuencia de muestreo, la resolución y el canal en el que estaba el ECG.
Una de las cosas que se explicó fue que nSeq no representa el tiempo, porque es un contador que se repite. Por eso, el eje temporal se construyó a partir del número de muestras y la frecuencia de muestreo. También se convirtieron los valores digitales del canal A1 a milivoltios para visualizar mejor el ECG y reconocer los complejos QRS.

## 2. Contaminación de la señal
Como el registro original estaba relativamente limpio, se le añadió ruido de manera artificial. Se usaron dos interferencias sinusoidales de 60 Hz y 120 Hz, además de ruido gaussiano. Esto permitió tener una señal original como referencia y otra contaminada para probar los métodos de filtrado.
Se compararon las gráficas en el tiempo y después se utilizó la transformada rápida de Fourier (FFT) para observar la señal en frecuencia. En este análisis se explicó que las interferencias periódicas aparecen como picos en el espectro, mientras que el ruido gaussiano se distribuye en un rango más amplio de frecuencias.

## 3. Filtros convencionales
Luego se revisaron dos formas de filtrar el ECG. La primera fue un filtro pasa-banda Butterworth de 0.5 a 40 Hz, que deja pasar principalmente las frecuencias de interés del ECG y atenúa las que están fuera de ese intervalo. También se consideró qué ocurre al reducir la frecuencia de corte superior a 15 Hz, ya que un filtro demasiado restrictivo puede modificar la forma del complejo QRS.
El segundo método fue el filtro notch, diseñado para atenuar frecuencias específicas. Se aplicó a 60 Hz y 120 Hz y se revisó el efecto del factor de calidad Q sobre el ancho de la banda que se elimina. A diferencia del pasa-banda, el notch permite actuar directamente sobre esas interferencias, pero no elimina por sí solo todo el ruido aleatorio.

## 4. Filtro adaptativo LMS
Después se explicó el funcionamiento del filtro adaptativo LMS. La principal diferencia con los filtros anteriores es que sus coeficientes se van ajustando durante el procesamiento. En el notebook se utilizaron señales de referencia relacionadas con las interferencias de 60 Hz y 120 Hz para estimarlas y restarlas del ECG contaminado.
También se revisó el parámetro MU, que controla qué tan rápido se adapta el filtro. Con valores pequeños la adaptación es más lenta y con valores grandes puede ser más rápida, aunque también existe el riesgo de que el resultado sea menos estable. Las gráficas de los coeficientes ayudaron a entender cómo el filtro va aprendiendo a cancelar la interferencia.

## 5. Transformada Wavelet
Otro método presentado fue la transformada Wavelet, que permite analizar la señal en distintos niveles de detalle. A diferencia de observar solamente el espectro con la FFT, aquí se puede estudiar cómo se distribuyen las componentes de la señal a diferentes escalas.
Se utilizó la Wavelet db4 para descomponer el ECG y se aplicó un proceso de reducción de ruido mediante umbralización. Además, el notebook incluyó comparaciones entre los modos soft y hard, y entre las familias db4 y sym8. Se comentó que este método puede ser útil para reducir ruido sin perder los eventos importantes del ECG, pero que elegir los parámetros también influye en cuánto se modifica la señal.

## 6. Comparación de resultados
Finalmente se compararon el pasa-banda, los filtros notch, el LMS, Wavelet y un método híbrido de notch más Wavelet. Para esto se utilizaron las gráficas y tres métricas: RMSE, SNR y correlación. Se explicó que el RMSE indica cuánto se aleja la señal filtrada de la original, la SNR permite evaluar la relación entre la señal y el error, y la correlación ayuda a comparar sus formas.
En los resultados registrados en el notebook, el pasa-banda obtuvo la mejor SNR, aproximadamente 20.2 dB, frente a unos 10.5 dB del notch doble. Esto fue coherente con la contaminación que se había añadido, ya que el pasa banda podía atenuar tanto las interferencias de 60 y 120 Hz como parte del ruido de alta frecuencia. Sin embargo, también se destacó que una buena métrica no garantiza que se haya conservado toda la morfología del ECG.

## Conclusión
Este laboratorio sirvió para relacionar los conceptos de filtrado digital con una señal biomédica real. Al trabajar todo desde el notebook fue posible observar cada etapa, desde la lectura del archivo y la contaminación artificial hasta la aplicación y comparación de los filtros. Lo más importante fue entender que cada método elimina un tipo de ruido de manera diferente y que no basta con obtener una señal visualmente más limpia: también hay que comprobar qué tanto cambió respecto al ECG original.
