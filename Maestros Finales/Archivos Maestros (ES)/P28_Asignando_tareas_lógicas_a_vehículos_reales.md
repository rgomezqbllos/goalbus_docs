---
title: Asignando tareas lógicas a vehículos reales
shortTitle: Asignación de vehículos
intro: 'Aprende a asignar las tareas de material lógicas obtenidas en el Scheduling a los vehículos reales cargados o creados previamente.'
contentType: how-tos
versions:
  - '*'
---

## Cargando o creando los vehículos reales que se utilizarán en la asignación

Una vez tengas la solución de Scheduling y de Rostering validadas y publicadas (la de rostering no sería imprescindible), se pueden crear o cargar los vehículos que se utilizarán para la asignación de las tareas lógicas calculadas en la solución de Scheduling de vehículos.

Usa esta quick start cuando ya ejecutaste el cálculo de Scheduling y Rostering y necesitas iniciar la asignación de vehículos.

Antes de empezar, asegúrate de que:
1. Ya publicaste la solución de Scheduling P16.
2. Ya validaste y consolidaste la solución de Rostering P27.

Para esta quick start, usa este caso de referencia:

> **Voy a asignar las tareas lógicas calculadas en el Scheduling de vehículos a las matrículas de los vehículos cargados o creados.**

Para cargar o crear nuevas matrículas reales:
1. Abre el módulo **Configuración** > **Vehículos** > **Vehículos Registrados**.
ref: P28_Imagen1.png | compact
2. Si quieres crear varias matrículas al mismo tiempo, la mejor opción es importarlas.
3. Selecciona el botón de importación de matrículas.
ref: P28_Imagen2.png | compact
4. Carga el fichero CSV con los nuevos vehículos siguiendo las instrucciones de la ventana.
ref: P28_Imagen3.png | compact
5. Si no hay errores, los nuevos vehículos quedarán registrados.
6. Si, por el contrario, prefieres crear uno a uno los nuevos vehículos, selecciona el botón **Nuevo vehículo**.
ref: P28_Imagen4.png | compact
7. En la ventana emergente, debes rellenar los siguientes campos:
   1. **Matrícula** del vehículo.
   2. **Depósito** al que pertenece el vehículo.
   3. **Modelo** del vehículo.
   4. **Año de Manufactura** es opcional.
   5. **Fecha de inicio de operación** a partir de la cual se podrá realizar la asignación de tareas.
ref: P28_Imagen5.png | compact
8. Guarda los cambios.
9. El registro creado aparecerá en la ventana de registros de vehículos.


Para el caso de referencia, no continúes hasta poder afirmar:
1. Todas las matrículas necesarias están cargadas o creadas.
2. Los vehículos están asociados al **modelo** que le corresponde.
3. Ya no necesitas más vehículos que los cargados y/o creados.

Cuando termines esta sección, deberías tener todas las matrículas necesarias para realizar la asignación.

Para el caso de referencia, puedes crear matrículas con el siguiente formato:

- **001-LFX**
- **002-LFX**
...
- **NNN-LFX**

## Asignando las tareas lógicas del Scheduling a vehículos reales

Una vez que todos los vehículos necesarios han sido cargados o creados en el sistema, se puede iniciar la asignación de vehículos.

Antes de empezar esta sección, asegúrate de que:
1. Ya tienes todos los vehículos cargados o creados en el sistema.
2. Ya sabes qué criterio quieres llevar en la asignación de vehículos.
3. Ya tienes una solución de rostering validada.

Para comenzar con la asignación de vehículos:
1. Abre el módulo de **Asignación de vehículos**.
ref: P28_Imagen6.png | compact
2. Puedes revisar en la barra superior las tareas sin asignar que tienes o te quedan.
ref: P28_Imagen7.png | compact
3. En el panel derecho aparecerán todas estas tareas para ser asignadas de forma manual.
ref: P28_Imagen8.png
4. Al seleccionar la opción de **asignar tarea**, el sistema te ayudará mostrándote aquellos vehículos disponibles (sin tareas asignadas o trabajando ya, pero sin solapes).
Ref: P28_Imagen9.png
5. Asigna las tareas a aquellos vehículos que correspondan.
6. Cuando hayas terminado con las asignaciones, puedes **Confirmar** para **publicar** los cambios.
ref: P28_Imagen10.png
7. Si sigues teniendo tareas sin asignar o no quieres realizar a mano toda la asignación, te puedes ayudar con el botón **Optimizar Asignación de Flota**.
ref: P28_Imagen11.png
8. Puedes repetir este proceso para todos aquellos días en los que quieras trabajar.

Para el caso de referencia, asegúrate de que:
1. Todas las tareas han sido asignadas a un vehículo.
2. Hay coherencia en las asignaciones.
3. Todos los días necesarios están cubiertos.

Cuando termines esta sección, deberías tener una solución nombrada de vehículos.
