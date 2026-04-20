---
title: Gestionando ausencias, inactividades y disponibilidad de personal
shortTitle: Disponibilidad personal
intro: 'Aprende a registrar ausencias, inactividades y restricciones de disponibilidad para que Rostering asigne solo a personas realmente elegibles y no intente cubrir trabajo con conductores no disponibles.'
contentType: how-tos
versions:
  - '*'
---

## Entendiendo la diferencia entre ausencia, inactividad y disponibilidad

Antes de calcular Rostering, necesitas controlar qué personas están realmente disponibles para trabajar. En esta capa ya no basta con que el conductor exista, esté adscrito al contexto correcto y tenga reglas aplicables. También necesitas decirle al sistema si esa persona:
1. está disponible,
2. está ausente,
3. está inactiva,
4. o tiene una disponibilidad parcial o restringida.

Usa esta quick start cuando ya tengas cargados los conductores, revisada su adscripción operativa y preparada la base de reglas de Rostering, y necesites impedir que el cálculo intente asignar trabajo a personas no elegibles.

Antes de empezar, asegúrate de que:
1. Ya cargaste y revisaste conductores en P20.
2. Ya validaste su adscripción operativa en P21.
3. Ya definiste la base de reglas de Rostering en P22.
4. Tienes claro qué colectivo de personal participará en el cálculo.
5. Ya sabes si en tu operación necesitas registrar vacaciones, bajas, permisos, indisponibilidades parciales o estados no operativos.

Para esta quick start, usa este caso de referencia:

> **Voy a registrar ausencias, inactividades y restricciones de disponibilidad sobre los conductores que cubrirán la línea L1 para asegurarme de que Rostering solo asigne trabajo a personas realmente elegibles.**

Para entender correctamente estos conceptos:
1. Usa una **ausencia** cuando la persona existe y pertenece al colectivo, pero no está disponible durante un período concreto.
2. Usa una **inactividad** cuando la persona debe quedar fuera de la operativa durante un período más estructural o no debe participar en el cálculo.
3. Usa una **restricción de disponibilidad** cuando la persona sí puede trabajar, pero no en todo momento o no bajo todas las condiciones.
4. No mezcles estos conceptos como si fueran lo mismo.
5. Usa esta regla de lectura:
   1. **ausencia** = no puede trabajar durante un período concreto,
   2. **inactividad** = no debe tratarse como recurso operativo en ese contexto o período,
   3. **disponibilidad restringida** = puede trabajar, pero con límites.

Para registrar los tipos de ausencias, inactividades o indisponibilidades:
1. En GoalBus, debes abrir **Configuración** > **Personal** > **Configuración de Ausencias**.
ref: P23_Imagen1.png | compact
2. Revisa si todos los tipos de ausencia que necesitas están creados. 
3. Si no existe ningún tipo de ausencia o necesitas crear alguno nuevo, pulsa en el botón **Crear Nueva Ausencia**.
ref: P23_Imagen2.png | compact
4. Para crear un nuevo tipo de ausencia se deben rellenar los siguientes campos:
   1. **Nombre de Ausencia**: nombre del tipo de ausencia que se va a crear.
   2. **Nombre corto**: para vistas compactas.
   3. **GoalDriver ID**: código interno si se trabaja con integraciones.
   4. **Categoría de ausencia**: puede ser de **Pura**, **Libre** o de **Trabajo**. En función de lo que se elija, se deberá asignar una duración (**Horaria** o de **Jornada completa**), una duración de **Tiempo de trabajo** o de **Máximo de días**.
   5. **Elegibilidad para Asignar Trabajo**: si se podrá elegir al conductor para asignarle trabajo o no, a pesar de su ausencia.
   6. Selecciona si este tipo de ausencia será **Solicitable por el conductor**.
5. Guarda el nuevo tipo de ausencia.
ref: P23_Imagen3.png | compact
6. Sigue registrando todos aquellos tipos de ausencia necesarios.
7. Confirma que tienes todos los tipos de ausencia que se precisan para tu planificación.

Cuando termines esta sección, deberías tener una visión clara de qué tipo de ausencias vas a poder utilizar en tu planificación de rostering y que vas a poder asignar a los diferentes conductores. fileciteturn22file3L1-L20 fileciteturn22file2L1-L18

## Registrando ausencias planificadas del conductor

Las ausencias planificadas son uno de los primeros elementos que debes cargar antes del cálculo de Rostering. Aquí entran vacaciones, permisos, incapacidades, licencias o cualquier otro período en el que una persona no deba recibir trabajo.

Antes de empezar esta sección, asegúrate de que:
1. Ya sabes qué conductores tendrán ausencias dentro del horizonte de cálculo.
2. Ya conoces las fechas exactas o aproximadas de esas ausencias.
3. Quieres dejar al sistema sin ambigüedad sobre qué días la persona no puede ser usada.
4. Ya has creado todos los tipos de ausencia necesarios.

Para registrar ausencias en el perfil del conductor:
1. En GoalBus, debes abrir **Configuración** > **Personal** > **Gestión de conductores**.
ref: P23_Imagen4.png | compact
2. Pulsa en el botón de la barra superior para cargar los datos de ausencias.
ref: P23_Imagen5.png | compact
3. Selecciona la acción **Cargar ausencias de personal**.
ref: P23_Imagen6.png | compact
4. Carga el fichero de ausencias de personal en la ventana emergente. En dicha ventana puedes revisar el formato del fichero de ausencias, ya sea leyendo las instrucciones o descargando una plantilla de ejemplo.
ref: P23_Imagen7.png | full
5. Confirma la carga del fichero.
6. Guarda el registro.
7. Ahora podrás revisar las ausencias cargadas en el perfil de cada conductor.

Para el caso de referencia, una lógica mínima podría ser:
1. Conductor A: vacaciones del 10 al 20
2. Conductor B: permiso el día 14
3. Conductor C: incapacidad durante una semana concreta

Cuando termines esta sección, deberías tener registradas las ausencias principales que afectan al cálculo de Rostering.

## Comprobando que Rostering ya ve correctamente la elegibilidad real

El último paso es validar que la combinación entre conductores, adscripción, reglas y disponibilidad ya refleja la realidad del cálculo. Aquí el objetivo es asegurarte de que Rostering no intentará asignar trabajo a personas ausentes, inactivas o mal restringidas, y tampoco dejará fuera a personas que sí deberían ser elegibles.

Antes de terminar, asegúrate de que:
1. Ya registraste ausencias relevantes.
2. Ya configuraste disponibilidades parciales si eran necesarias.
3. Ya sabes qué colectivo usará el siguiente cálculo.

Para comprobar que la disponibilidad real ya está bien modelada:
1. Vuelve a la lista general de conductores.
2. Revisa varios perfiles representativos del colectivo.
3. Confirma que las personas ausentes tienen sus períodos correctamente registrados.
4. Confirma que las restricciones parciales no están modeladas como ausencias totales por error.
5. Pregúntate si el sistema ya podría:
   1. excluir a quien no debe trabajar,
   2. incluir a quien sí puede trabajar,
   3. y respetar restricciones parciales sin romper el cálculo.
6. Si la respuesta es sí, continúa con el siguiente quick start.
7. Si la respuesta es no, corrige los registros antes de seguir.

Para el caso de referencia, no continúes hasta poder afirmar:
1. Los conductores de L1 ya tienen bien reflejada su disponibilidad real.
2. Las ausencias están cargadas.
3. Las inactividades están diferenciadas.
4. Las restricciones parciales no se confundieron con ausencias completas.

Cuando termines esta sección, deberías tener una base de disponibilidad suficientemente fiable como para pasar a cesiones, transferencias y cambios de adscripción.

## Lecturas adicionales

- [Gestionando transferencias, cesiones y cambios de adscripción](P24_Gestionando_transferencias_cesiones_y_cambios_de_adscripcion.md)
