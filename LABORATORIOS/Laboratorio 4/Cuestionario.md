# Informe 4 de laboratorio

## Introducción

En el presente laboratorio se realizó la adquisición y análisis de señales de electrocardiografía (ECG) utilizando el sistema BITalino y el sensor de ECG. El objetivo fue observar cómo las señales eléctricas producidas por la actividad cardíaca pueden ser registradas desde la superficie de la piel y cómo sus características pueden variar según la derivación utilizada y las condiciones fisiológicas del sujeto.

De acuerdo con la guía de BITalino, el ECG permite registrar las variaciones eléctricas asociadas con la actividad del corazón. La señal obtenida está relacionada con las diferentes etapas del ciclo cardíaco, incluyendo las ondas P, el complejo QRS y la onda T. Además, la guía señala que la dirección y amplitud de los componentes de la señal dependen de la orientación del dipolo cardíaco respecto a los electrodos.

Para la adquisición se utilizaron tres electrodos, correspondientes a las dos entradas de medición y al electrodo de referencia del sensor ECG. 

En este experimento se empleó la configuración de los electrodos sobre las clavículas y la cadera, específicamente sobre la cresta ilíaca. Esta disposición permite obtener las tres derivaciones bipolares de Einthoven: I, II y III, modificando la conexión de los electrodos.

Las tres derivaciones de Einthoven permiten observar la actividad eléctrica cardíaca desde diferentes direcciones. La derivación I corresponde a la diferencia de potencial entre el brazo derecho (RA) y el brazo izquierdo (LA), la derivación II entre el brazo derecho y la pierna izquierda (LL), y la derivación III entre el brazo izquierdo y la pierna izquierda.

## Metodología

El experimento consistió en realizar adquisiciones de la señal ECG bajo diferentes condiciones fisiológicas y utilizando las tres derivaciones de Einthoven. Para todas las mediciones se mantuvo la configuración de los electrodos sobre las clavículas y la cresta ilíaca, realizando los cambios correspondientes en las conexiones para obtener cada una de las derivaciones.

La adquisición se realizó mediante el sistema BITalino y el software OpenSignals. La guía recomienda utilizar tres electrodos Ag/AgCl para el sensor ECG y limpiar previamente la zona de colocación para mejorar la conductividad de la piel. También se recomienda colocar los electrodos en zonas con poca actividad muscular para reducir el ruido producido por las activaciones musculares y los artefactos de movimiento. 

El experimento se dividió en cuatro condiciones principales, realizando las adquisiciones correspondientes para los tres meridianos o derivaciones:

1. **Estado basal:** se realizó una primera adquisición de la señal ECG en condiciones de reposo.
2. **Hiperventilación:** se realizó una adquisición durante una condición de respiración acelerada.
3. **Hipoventilación:** se realizó una adquisición durante una condición de respiración reducida.
4. **Actividad:** se realizó una adquisición después de realizar actividad física.


## Procesamiento de las señales

Las señales obtenidas durante el laboratorio fueron exportadas desde OpenSignals en formato `.txt` y posteriormente procesadas mediante Python. Para cada archivo se identificó la columna correspondiente al canal ECG y se construyó un eje temporal a partir de la frecuencia de muestreo utilizada durante la adquisición.

Se realizaron gráficos de las señales ECG para visualizar su comportamiento en cada condición experimental y en cada derivación. La representación temporal permite observar los ciclos cardíacos y comparar características como la amplitud, la periodicidad, la presencia de ruido y la forma de los complejos cardíacos.

La guía señala que, a partir de los picos R, es posible calcular la frecuencia cardíaca en latidos por minuto (bpm) y analizar la variabilidad de la frecuencia cardíaca mediante los intervalos entre dichos picos.

## Resultados

Las señales obtenidas fueron graficadas en Python para cada una de las condiciones experimentales. Los gráficos permiten visualizar las diferencias entre las señales registradas en estado basal, durante hiperventilación, hipoventilación y después de realizar actividad física.

### Estado basal

En esta condición se obtuvo la señal ECG correspondiente al estado de reposo para cada una de las tres derivaciones.

### Estado basal

#### Derivación I

![ECG basal - Derivación I](ploteos/basal_D1.png)

#### Derivación II

![ECG basal - Derivación II](ploteos/basal_D2.png)

#### Derivación III

![ECG basal - Derivación III](ploteos/basal_D3.png)

### Hiperventilación

En esta condición se registró la señal ECG mientras se realizaba una respiración más rápida. Esta adquisición permite evaluar si los cambios en la respiración producen modificaciones observables en la señal ECG.

**[INSERTAR AQUÍ LAS GRÁFICAS DE HIPERVENTILACIÓN I, II Y III]**

### Hipoventilación

En esta condición se registró la señal ECG durante una respiración reducida. La comparación con el estado basal y con la hiperventilación permite observar posibles modificaciones relacionadas con las condiciones respiratorias.

**[INSERTAR AQUÍ LAS GRÁFICAS DE HIPOVENTILACIÓN I, II Y III]**

### Actividad

Finalmente, se registró la señal ECG asociada a la condición de actividad física. Esta adquisición permite comparar el comportamiento de la señal respecto al estado basal y observar los cambios relacionados con la frecuencia cardíaca y la morfología de los ciclos.

**[INSERTAR AQUÍ LAS GRÁFICAS DE ACTIVIDAD I, II Y III]**

## Análisis

En esta sección se analizarán las señales obtenidas considerando dos aspectos principales: **la condición fisiológica** y **la derivación utilizada**.

Para comparar las diferentes condiciones, se deberá observar principalmente la frecuencia cardíaca, identificando los picos R y calculando los intervalos entre ellos. A partir de estos intervalos se puede estimar la frecuencia cardíaca en bpm. También se puede comparar la regularidad de los intervalos entre los diferentes ciclos cardíacos. La guía indica que los intervalos entre picos R permiten analizar la variabilidad de la frecuencia cardíaca. :contentReference[oaicite:8]{index=8}

También se analizarán las diferencias de amplitud y morfología de la señal entre las derivaciones I, II y III. Debido a que cada derivación mide la actividad eléctrica cardíaca desde una dirección diferente, es esperable que los componentes de la señal no presenten exactamente la misma amplitud o polaridad. La guía explica que la amplitud depende del ángulo entre la dirección del dipolo cardíaco y la dirección de medición, mientras que la dirección de la amplitud depende de la orientación del dipolo respecto a los electrodos. :contentReference[oaicite:9]{index=9}

Finalmente, se evaluará la presencia de ruido y artefactos en cada adquisición. Estos pueden estar relacionados con el movimiento, la actividad muscular o la respiración. La guía destaca que el movimiento puede introducir artefactos en el ECG y que la respiración también puede influir en las características observadas en la señal. :contentReference[oaicite:10]{index=10} :contentReference[oaicite:11]{index=11}

**[ESPACIO PARA DESARROLLAR EL ANÁLISIS DE LAS 12 SEÑALES]**

En esta parte se compararán específicamente:

- Basal vs. hiperventilación.
- Basal vs. hipoventilación.
- Basal vs. actividad.
- Derivación I vs. derivación II vs. derivación III.
- Frecuencia cardíaca en cada condición.
- Amplitud y morfología de los complejos ECG.
- Presencia de ruido o artefactos.
- Regularidad de los intervalos entre los picos R.

## Conclusiones

**[ESPACIO PARA COLOCAR LAS CONCLUSIONES DEL EXPERIMENTO]**