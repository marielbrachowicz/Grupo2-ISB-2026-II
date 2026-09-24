# Sistema de biofeedback basado en electrooculografía (EOG) para entrenamiento del reflejo vestíbulo-ocular (VOR)

## 1. Planteamiento del problema
El reflejo vestíbulo-ocular (VOR) estabiliza la mirada durante los movimientos de la cabeza. Cuando la cabeza gira hacia un lado, los ojos rotan en sentido contrario para mantener la fijación sobre un objetivo [1]. De essta forma, la imagen permanece estable en la retina, lo que hace posible actividades cotidianas como caminar o leer.

Cuando este mecanismo no presenta una respuesta suficiente, la estabilidad visual durante el movimiento se ve perjudicada. Ya que, pueden aparecer problemas como mareos, desequilibrios e inestabilidad en la mirada [2].

Los ejercicios de estabilización visual forman parte de los programas de rehabilitación vestibular y combinan la fijación de un objetivo con el movimiento de cabeza. La guía de 2016 no recomienda usar movimientos sacádicos o de seguimiento voluntarios, sin movimiento de cabeza, como ejercicios específicos de estabilidad de mirada [3].

Gran parte de estos ejercicios se realizan fuera de la consulta, y a los terapeutas les resulta dificil obtener información sobre el cumplimiento y la calidad de ejecución [4]. Durante las consultas médicas, la evaluación del cumplimiento de la mirada puede variar según la experiencia del clínico y no hay métodos objetivos sencillos para registrar el desempeño de los ejercicios [5].

## 2. Propuesta de solución
Sistema accesible de biofeedback basado en EOG que permite cuantificar la estabilidad ocular durante ejercicios asociados al VOR y proporcionar retroalimentación objetiva para entrenamiento y seguimiento del progreso sin realizar un diagnóstico clínico.

### 2.1 Adquisición de la señal
Se plantea utilizar EOG como señal biomédica principal. El voltaje medido en electrodos superficiales alrededor del ojo varía con la rotación ocular [1].

El sistema permitirá registrar movimientos oculares horizontales y verticales mediante una configuración adecuada de electrodos superficiales. Se contempla utilizar una plataforma de adquisición como BITalino.

El usuario realizará los ejercicios guiados mientras el sistema registra principalmente la respuesta ocular. El movimiento de cabeza forma parte del protocolo del ejercicio y no se mide con hardware adicional.

### 2.2 Interfaz
La interfaz mostrará retroalimentación sobre su desempeño. Incluyendo, indicador de estabilidad visual expresado en porcentaje, tiempo mantiendo la mirada y progreso entre sesiones.
Estos indicadores son métricas propias del proyecto, calculadas a partir de la señal EOG. No constituyen parámetros clínicos.

## 3. Paper de referencia
J. R. Nezvadovitz and H. M. Rao, "Using natural head movements to continually calibrate EOG signals," J. Eye Mov. Res., vol. 15, no. 5, pp. 1–13, 2022, doi: 10.16910/jemr.15.5.6. [1] 

El estudio propone calibrar automáticamente la relación entre el voltaje EOG y la dirección de la mirada, sin cámaras ni monitores externos. Esa relación cambia con el tiempo por la impedancia piel-electrodo y la adaptación retiniana, lo que obliga a recalibrar con frecuencia.

Combina EOG con giroscopio de tres ejes en la cabeza. La mirada se modela como una contrarrotación del movimiento cefálico y usa un filtro de Kalman extendido para estimar de forma continua la dirección de la mirada y coeficientes de calibración. Fue validado con cuatro sujetos, comparando lo resultados contra un seguidor ocular por video.

La discrepancia promedio obtenida respecto al seguidor por video fue de 3.54° ± 0.71° [1].

Este estudio respalda que la señal EOG puede utilizarse para estudiar movimientos oculares relacionados con el VOR, evidenciando que la relación entre la actividad ocular y los movimientos cefálicos puede ser cuantificada.

Este proyecto no busca replicar la metodología propuesta en el artículo, sino adaptar el uso de la señal EOG hacia una aplicación de biofeedback más accesible, orientada al entrenamiento y monitoreo de la estabilidad de la mirada durante ejercicios asociados al VOR.
### Presentación del proyecto
[Ver presentación en Google Drive](https://drive.google.com/file/d/1pHOiaigWpSwrBcDilsLz5GzxhA7_OwCG/view?usp=sharing)
## REFERENCIAS
[1] J. R. Nezvadovitz and H. M. Rao, "Using natural head movements to continually calibrate EOG signals," J. Eye Mov. Res., vol. 15, no. 5, pp. 1–13, 2022, doi: 10.16910/jemr.15.5.6.

[2] C. D. Hall et al., "Vestibular rehabilitation for peripheral vestibular hypofunction: An updated clinical practice guideline from the Academy of Neurologic Physical Therapy of the American Physical Therapy Association," J. Neurol. Phys. Ther., vol. 46, no. 2, pp. 118–177, Apr. 2022.

[3] C. D. Hall et al., "Vestibular rehabilitation for peripheral vestibular hypofunction: An evidence-based clinical practice guideline," J. Neurol. Phys. Ther., vol. 40, no. 2, pp. 124–155, Apr. 2016, doi: 10.1097/NPT.0000000000000120.

[4] K. Huang, P. J. Sparto, S. Kiesler, D. P. Siewiorek, and A. Smailagic, "iPod-based in-home system for monitoring gaze-stabilization exercise compliance of individuals with vestibular hypofunction," J. NeuroEng. Rehabil., vol. 11, art. no. 69, 2014.

[5] B. N. Klatt et al., "A tablet-based technology for objective exercise monitoring in vestibular rehabilitation: Mixed methods study," JMIR Rehabil. Assist. Technol., vol. 12, art. no. e58713, 2025, doi: 10.2196/58713.