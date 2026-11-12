**<ins>INFORME DE LABORATORIO 12: TRATAMIENTO DE LA SEÑAL EEG, RITMOS CEREBRALES, FILTRO ICA Y EXTRACCIÓN DE CARACTERÍSTICAS</ins>**

Universidad Peruana Cayetano Heredia
Curso: Introducción a las Señales Biomédicas
Estudiante: Mariel Andrea Brachowicz Suarez
Código: 70339347
Grupo: G2
Fecha: 11/11/2026


**<ins>1. Introducción</ins>**

El electroencefalograma registra la actividad eléctrica que llega al cuero cabelludo y que se origina en los potenciales post-sinápticos de grandes grupos de neuronas corticales que se activan de forma sincronizada. Es una señal muy pequeña, de unos 20 a 100 µV, bastante menor que la del ECG, y eso hace que cualquier movimiento, parpadeo o contracción muscular pueda contaminarla con facilidad.

Para describir el EEG se suele trabajar por bandas de frecuencia: delta de 1 a 4 Hz, theta de 4 a 8 Hz, alfa de 8 a 13 Hz, beta de 13 a 30 Hz y gamma por encima de 30 Hz. Cada una se asocia a estados distintos. La alfa, por ejemplo, aparece sobre todo en reposo con los ojos cerrados y disminuye al abrirlos, mientras que la beta se relaciona con alerta y concentración. Además de los ritmos cerebrales, en el registro aparecen artefactos que no vienen del cerebro, como los parpadeos, que generan ondas lentas y grandes, la actividad muscular, que añade componentes rápidos, y la interferencia de la red eléctrica.

En este laboratorio seguimos el pipeline visto en clase: revisión de los datos, filtrado, limpieza con ICA, normalización y segmentación, extracción de características y, finalmente, clasificación de las condiciones registradas.


**<ins>2. Objetivos</ins>**

El objetivo general fue limpiar la señal EEG, analizar sus ritmos cerebrales y extraer características que permitan distinguir el estado del participante.

De forma más específica, buscamos revisar la calidad de los registros, comparar la potencia relativa de cada banda entre condiciones, aplicar una versión de ICA adaptada a un solo canal, construir una tabla de características por época y evaluar qué tan bien distintos clasificadores reconocen la condición a partir de esa tabla.


**<ins>3. Materiales y métodos</ins>**

**<ins>3.1 Adquisición</ins>**

Los registros se tomaron con un BITalino usando una derivación frontal de un solo canal: electrodo positivo en Fp1, negativo en Fp2 y referencia en O2. La frecuencia de muestreo fue de 1000 Hz, así que la frecuencia de Nyquist es 500 Hz.

El protocolo original contemplaba siete archivos, pero en nuestro caso solo contamos con cuatro: basal con ojos cerrados, ojos abiertos, música relajante y música estresante, de entre 58 y 92 segundos cada uno. No tuvimos los basales posteriores ni el registro de parpadeo y masticación, y eso limitó algunas de las comparaciones que pedía la guía.

Las cuentas del ADC se convirtieron a microvoltios con la fórmula del sensor EEG de BITalino. Con la ganancia de este sensor el rango útil es de apenas ±39.5 µV, por lo que se consideraron saturadas las muestras con valor 0 o mayor o igual a 1018.

**<ins>3.2 Procesamiento</ins>**

Todo el análisis se hizo en Python con numpy, pandas, scipy, PyWavelets y scikit-learn.

Primero se recortaron los 4 segundos iniciales de cada registro, porque el amplificador tarda un poco en estabilizarse. Luego se aplicó un filtro pasa-banda Butterworth de orden 4 entre 1 y 45 Hz, en ida y vuelta para no desfasar la señal. No se usó notch de 40 Hz, ya que con 1000 Hz de muestreo la red de 60 Hz no produce alias en 40 Hz y, además, la revisión espectral no mostró ningún pico en esa frecuencia. La opción de quitar líneas angostas quedó activada, pero el detector no encontró ninguna.

Para la limpieza se usó Wavelet-ICA. Como ICA necesita al menos tantos canales como fuentes, la señal se descompuso con una wavelet en seis sub-bandas que se trataron como canales virtuales, y sobre ellas se aplicó FastICA. Las componentes con curtosis mayor a 6 se consideraron portadoras de transitorios y se corrigieron anulando solo los coeficientes wavelet atípicamente grandes. Las componentes con más del 40 % de su potencia entre 38 y 42 Hz se habrían eliminado como interferencia de red, pero no apareció ninguna.

Después, cada registro se cortó en épocas de 2 segundos sin solapamiento y se descartó cualquier época con al menos una muestra saturada. En el análisis principal no se normalizó la señal.

De cada época se extrajeron 22 características agrupadas en cinco familias: potencia absoluta y relativa por banda, cocientes theta/beta y alfa/beta, características espectrales como la frecuencia pico y la entropía, parámetros de Hjorth y estadísticas de amplitud. La tabla final se guardó en el archivo caracteristicas_eeg.csv, con 138 épocas.

Por último, se compararon cinco clasificadores: árbol de decisión, regresión logística, random forest, KNN y SVM. Para evitar que épocas vecinas casi idénticas quedaran a la vez en entrenamiento y prueba, se agruparon en bloques de 10 segundos y se usó validación cruzada por grupos con 5 pliegues. La métrica principal fue el F1 macro, considerando que el azar para cuatro clases es 0.25.


**<ins>4. Resultados</ins>**

**<ins>4.1 Calidad de los registros</ins>**

Las cuatro grabaciones se hicieron en el orden previsto, entre las 11:59 y las 12:32, siempre con el mismo equipo y sin paquetes perdidos.

| Registro | Saturación | Desv. estándar µV | Curtosis | Estado |
|---|---|---|---|---|
| Basal | 0 % | 5.13 | 5.8 | Bueno |
| Ojos abiertos | 3.35 % | 10.72 | 5.9 | Problemático |
| Música relajante | 0 % | 4.57 | 0.4 | Bueno |
| Música estresante | 0.10 % | 8.24 | 1.7 | Revisar |

En ojos abiertos la saturación se repartía a lo largo de todo el registro, lo que sugiere movimientos oculares o parpadeos frecuentes, algo esperable en esta zona frontal. En música estresante, en cambio, fue puntual. En el espectro, ningún archivo mostró un pico de interferencia en 40 Hz.

**<ins>4.2 Ritmos cerebrales</ins>**

La potencia relativa por banda, calculada sobre la señal filtrada y sin muestras saturadas, fue la siguiente:

| Registro | Delta | Theta | Alfa | Beta | Gamma |
|---|---|---|---|---|---|
| Basal | 37.3 % | 26.3 % | 11.7 % | 16.9 % | 7.6 % |
| Ojos abiertos | 45.1 % | 26.3 % | 6.7 % | 13.3 % | 8.3 % |
| Música relajante | 26.6 % | 28.4 % | 10.3 % | 22.5 % | 11.8 % |
| Música estresante | 9.8 % | 7.5 % | 5.4 % | 39.8 % | 36.5 % |

En el basal la banda dominante fue delta y no alfa, como se esperaría con los ojos cerrados. Aun así, al abrir los ojos la alfa bajó de 11.7 % a 6.7 %, lo que es compatible con el bloqueo alfa. El cambio más grande entre esas dos condiciones fue el aumento de delta. La música estresante se separa claramente del resto, con casi el 40 % de su potencia en beta y más de un tercio en gamma.

**<ins>4.3 Limpieza con Wavelet-ICA</ins>**

| Registro | Componentes corregidas | Varianza eliminada |
|---|---|---|
| Basal | 3 | 20.7 % |
| Ojos abiertos | 6 | 76.7 % |
| Música relajante | 2 | 0.1 % |
| Música estresante | 2 | 0.0 % |

Como no teníamos el registro de parpadeo y masticación, el ejemplo paso a paso se hizo sobre el basal. Allí se corrigieron dos componentes con curtosis enormes, mayores a 20 000, y una tercera con curtosis de 6.3 que por sí sola explicaba el 81 % de la varianza de la señal.

**<ins>4.4 Épocas y características</ins>**

Tras rechazar las épocas saturadas quedaron 138 épocas válidas: 43 de basal, 14 de ojos abiertos, 44 de música relajante y 37 de música estresante. Ojos abiertos perdió casi la mitad de sus épocas.

| Característica media | Basal | Ojos abiertos | Música relajante | Música estresante |
|---|---|---|---|---|
| rel_delta | 0.404 | 0.270 | 0.384 | 0.224 |
| rel_beta | 0.209 | 0.304 | 0.225 | 0.411 |
| rel_gamma | 0.080 | 0.147 | 0.093 | 0.249 |
| theta/beta | 1.012 | 0.625 | 0.958 | 0.193 |
| Frecuencia pico Hz | 2.95 | 6.96 | 2.81 | 13.81 |
| Entropía espectral | 0.750 | 0.839 | 0.765 | 0.835 |
| Movilidad de Hjorth | 0.088 | 0.113 | 0.097 | 0.148 |
| Desv. estándar µV | 3.15 | 3.31 | 3.10 | 5.21 |

Las características que mejor parecen separar las condiciones son la potencia relativa delta y beta, la entropía espectral y la movilidad de Hjorth. Basal y música relajante tienen valores muy parecidos en casi todo, mientras que ojos abiertos y música estresante muestran una potencia más repartida y desplazada hacia frecuencias altas. La curtosis por época, en cambio, casi no varía entre condiciones.

**<ins>4.5 Clasificación de las cuatro condiciones</ins>**

| Modelo | Exactitud | F1 macro |
|---|---|---|
| Árbol de decisión | 0.550 | 0.493 |
| Regresión logística | 0.592 | 0.521 |
| Random forest | 0.598 | 0.517 |
| KNN | 0.554 | 0.494 |
| SVM | 0.563 | 0.491 |

El mejor modelo fue la regresión logística, con un F1 macro de 0.521, el doble del azar. En la matriz de confusión se ve que la música estresante se reconoce casi siempre, con 36 de 37 épocas acertadas, pero basal y música relajante se confunden mucho entre sí: 19 épocas de cada una se asignaron a la otra. Ojos abiertos fue la clase peor reconocida, con solo 2 de 14 épocas correctas. La prueba para predecir el dispositivo no se pudo hacer porque todos los registros vienen del mismo BITalino.

**<ins>4.6 Experimentos del cuestionario final</ins>**

Al comparar solo música relajante y estresante, el F1 subió a valores entre 0.967 y 1.000. La banda que más cambió fue beta, con 41.1 % en la estresante frente a 22.5 % en la relajante, seguida de gamma. La relajante tuvo más delta, theta y alfa.

En cuanto al ICA, rechazando las épocas saturadas el mejor F1 pasó de 0.514 sin ICA a 0.521 con ICA. Si no se rechazan, pasó de 0.632 a 0.645. No pudimos comparar curtosis y pico a pico en parpadeo y masticación porque ese registro no existe en nuestros datos.

Con notch de 40 Hz la gamma relativa disminuyó un poco, por ejemplo de 24.9 % a 21.7 % en música estresante. Con notch de 60 Hz o sin notch los resultados fueron prácticamente iguales, el ICA no eliminó ninguna componente de red en ningún caso y el mejor F1 se movió apenas entre 0.521 y 0.525. Desactivar el filtrado de líneas angostas no cambió nada, ya que no se había detectado ninguna.

Al normalizar la señal el mejor F1 bajó de 0.521 a 0.496. Las características que perdieron su capacidad de separar fueron las de amplitud, como la desviación estándar, la actividad de Hjorth y el pico a pico.

Finalmente, sobre la duración de la época:

| Época | Resolución | Épocas válidas | Mejor F1 | F1 promedio |
|---|---|---|---|---|
| 1 s | 1.00 Hz | 293 | 0.535 | 0.510 |
| 2 s | 0.50 Hz | 138 | 0.521 | 0.503 |
| 4 s | 0.25 Hz | 64 | 0.655 | 0.555 |


**<ins>5. Discusión</ins>**

Lo primero que nos dejó este laboratorio es que revisar los datos antes de procesarlos cambia bastante las decisiones. La guía estaba pensada para registros a 100 Hz, donde la red de 60 Hz aparece disfrazada en 40 Hz, y por eso proponía un notch en esa frecuencia. En nuestros datos, a 1000 Hz, ese problema no existe y el espectro lo confirmó. Aplicar el notch de 40 Hz por defecto solo habría recortado un poco de gamma sin quitar ninguna interferencia real.

Que el basal no tuviera alfa dominante no nos parece un error de adquisición, sino una consecuencia del montaje. La alfa de reposo se genera sobre todo en zonas occipitales y parietales, y nosotros medimos entre Fp1 y Fp2, dos puntos frontales casi simétricos cuya resta atenúa la actividad común. A eso se suma que la frente está muy expuesta a los movimientos oculares, que meten mucha energía en delta. Aun con esas limitaciones, la caída de alfa al abrir los ojos sí se observó, lo cual indica que el registro conserva algo de información fisiológica.

El registro de ojos abiertos fue claramente el más problemático. Tuvo la mayor saturación, la curtosis más alta, perdió casi la mitad de sus épocas y el ICA le quitó el 76.7 % de la varianza. Ese porcentaje es demasiado alto para pensar que solo se eliminaron artefactos; es muy probable que también se haya ido actividad cerebral. Algo parecido pasa con el basal, donde se eliminó el 20.7 % y se corrigió una componente que explicaba el 81 % de la varianza con una curtosis apenas por encima del umbral. Con un solo canal, cada componente mezcla cerebro y artefacto, así que un umbral fijo de curtosis puede resultar demasiado agresivo. En los registros de música, en cambio, el ICA solo tocó componentes de curtosis extrema y casi no modificó la señal, que es lo que esperaríamos de un método que funciona bien.

Sobre la clasificación, el F1 de 0.521 está por encima del azar, pero hay que leerlo con cuidado. La música estresante se separa sobre todo por su exceso de beta y gamma, y esas bandas en electrodos frontales están muy influenciadas por la actividad muscular de la frente y la mandíbula. Es posible que el participante haya tensado la cara al escuchar la música estresante, y que el modelo esté reconociendo eso más que un cambio cerebral. Lo mismo vale para el F1 perfecto entre las dos músicas: con una sola grabación por condición, el modelo puede estar aprendiendo rasgos propios de cada sesión, como el contacto de los electrodos o la postura, y no de la condición en sí.

Hubo dos resultados que a primera vista parecerían mejoras pero que no lo son. Al conservar las épocas saturadas el F1 subió hasta 0.645, y al usar épocas de 4 segundos llegó a 0.655. En el primer caso, la saturación es una marca muy fácil de reconocer en ojos abiertos, así que el modelo aprovecha justamente el artefacto. En el segundo, el aumento coincide con tener solo 64 épocas, lo que vuelve la estimación menos estable. Por eso preferimos quedarnos con épocas de 2 segundos y rechazo de saturadas, porque reflejan mejor la información que realmente queremos medir. Si se quisiera usar 4 segundos, habría que confirmarlo con más grabaciones.

La normalización redujo el F1, lo que indica que la amplitud ayuda a separar las condiciones. Como todas las señales se tomaron con el mismo equipo, la amplitud no refleja diferencias entre dispositivos, pero sí puede reflejar el contacto de los electrodos o la actividad muscular, así que tampoco es una información del todo limpia.


**<ins>6. Conclusiones</ins>**

La revisión inicial de los datos fue determinante. Permitió detectar la saturación en ojos abiertos y, en menor medida, en música estresante, descartar la presencia de interferencias de red y justificar que no se aplicara un notch de 40 Hz. El uso de un único BITalino eliminó el problema de confusión entre equipos.

Con el montaje frontal la alfa no domina en reposo, pero sí disminuye al abrir los ojos, de 11.7 % a 6.7 %. La música estresante mostró una potencia beta mucho mayor que la relajante.

El Wavelet-ICA permite trabajar con un solo canal y corrige transitorios bruscos, pero su efecto sobre la clasificación fue pequeño y en ojos abiertos eliminó demasiada varianza, por lo que su umbral debería ajustarse.

Se construyó una tabla de 138 épocas con 22 características. Con ella, el mejor clasificador de las cuatro condiciones fue la regresión logística, con un F1 macro de 0.521. La separación entre músicas fue casi perfecta, aunque con una sola grabación por condición no se puede asegurar que el modelo esté reconociendo diferencias fisiológicas.

Para próximas adquisiciones recomendamos completar el protocolo con todos los registros, mejorar el contacto de los electrodos, pedir al participante que relaje la frente y la mandíbula, y repetir cada condición varias veces en distintos momentos. Si es posible, sumar un electrodo en la zona occipital ayudaría mucho a observar la alfa de reposo.


**<ins>7. Referencias</ins>**

1. L. De La Cruz, Tratamiento de señal EEG, diapositivas del curso, UPCH.
2. MNE-Python, Removing muscle ICA components. https://mne.tools/stable/auto_examples/preprocessing/muscle_ica.html
3. D. Dharmaprani et al., "A comparison of independent component analysis algorithms and measures to discriminate between EEG and artifact components", IEEE EMBC, 2016, pp. 825-828.
4. A. Hyvärinen y E. Oja, "Independent component analysis: algorithms and applications", Neural Networks, vol. 13, pp. 411-430, 2000.
5. N. P. Castellanos y V. A. Makarov, "Recovering EEG brain signals: Artifact suppression with wavelet enhanced independent component analysis", J. Neurosci. Methods, vol. 158, pp. 300-312, 2006.
6. B. Hjorth, "EEG analysis based on time domain properties", Electroencephalogr. Clin. Neurophysiol., vol. 29, pp. 306-310, 1970.
7. P. D. Welch, "The use of fast Fourier transform for the estimation of power spectra", IEEE Trans. Audio Electroacoust., vol. 15, pp. 70-73, 1967.
8. J. A. Urigüen y B. Garcia-Zapirain, "EEG artifact removal: state-of-the-art and guidelines", J. Neural Eng., vol. 12, 031001, 2015.
9. PLUX Wireless Biosignals, BITalino (r)evolution: EEG Sensor Datasheet.
