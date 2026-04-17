# Mapa de Datos ES

- Fuente principal: `data.txt`
- CSV de referencia: `translation_data.csv`
- Generado: 2026-04-16 19:05
- Idioma: Español (ES)
- Criterio de dependencia: valor no vacío repetido en más de un formulario.

## Resumen

- Formularios detectados: **29**
- Campos totales: **116**
- Campos con valor no vacío: **107**
- Valores únicos no vacíos: **64**
- Valores compartidos entre formularios: **17**
- Filas sin mapeo completo a CSV: **9**

## Campos Sin Mapeo Completo A `translation_data.csv`

| Formulario | Campo UI | Valor | Motivo |
|---|---|---|---|
| P4_imagen5 | Cabecero Línea | L1: Terminal Norte - Terminal Sur | sin regla de mapeo |
| P4_imagen5 | Nombre Línea | L1 - 1 | sin regla de mapeo |
| P4_imagen5 | Paradas | TERMINAL NORTE - TERMINAL SUR | sin regla de mapeo |
| P5_imagen1 | Cabecero Línea | L1: Terminal Norte - Terminal Sur | sin regla de mapeo |
| P5_imagen1 | Nombre Línea | L1 - 1 | sin regla de mapeo |
| P5_imagen1 | Paradas | TERMINAL NORTE - TERMINAL SUR | sin regla de mapeo |
| P9_imagen6 | Formulario de tiempos de Recorrido por franjas | (vacío) | sin regla de mapeo |
| P14_imagen8 | Tiempo máximo de cálculo | 00:05 | sin regla de mapeo |
| P25_imagen2 | Modelo de regla | Rostering L1 Laborable | sin regla de mapeo |

## Dependencias Entre Formularios (por valor compartido)

- `P2_imagen3` -> `P2_imagen5`: `1`, `LAB`, `Laborales`
- `P2_imagen3` -> `P2_imagen7`: `LAB`, `Laborales`
- `P2_imagen3` -> `P7_imagen3`: `Laborales`
- `P2_imagen3` -> `P8_imagen3`: `1`
- `P2_imagen3` -> `P10_imagen3`: `Laborales`
- `P2_imagen3` -> `P14_imagen3`: `Laborales`
- `P4_imagen2` -> `P6_imagen6`: `0`
- `P4_imagen4` -> `P4_imagen5`: `L1 - 1`, `L1: Terminal Norte - Terminal Sur`
- `P4_imagen4` -> `P5_imagen1`: `L1 - 1`, `L1: Terminal Norte - Terminal Sur`
- `P4_imagen4` -> `P8_imagen4`: `1 Seleccionados`, `L1 - 1`, `L1: Terminal Norte - Terminal Sur`, `L1: TN-TS`
- `P4_imagen4` -> `P9_imagen3`: `1 Seleccionados`
- `P4_imagen4` -> `P10_imagen3`: `1 Seleccionados`
- `P4_imagen4` -> `P14_imagen4`: `1 Seleccionados`
- `P4_imagen4` -> `P14_imagen5`: `1 Seleccionados`
- `P4_imagen4` -> `P25_imagen2`: `1 Seleccionados`
- `P4_imagen5` -> `P5_imagen1`: `TERMINAL NORTE`, `TERMINAL NORTE - TERMINAL SUR`, `TERMINAL SUR`
- `P4_imagen5` -> `P5_imagen2`: `TERMINAL NORTE`, `TERMINAL SUR`
- `P6_imagen5` -> `P6_imagen6`: `Depósito Empresa`
- `P6_imagen7` -> `P8_imagen3`: `500`, `Minibus`
- `P7_imagen3` -> `P14_imagen4`: `Vacíos - Enero de 2026`
- `P12_imagen2` -> `P14_imagen4`: `Vehículos - L1 Laborable`
- `P13_imagen2` -> `P13_Imagen4`: `TM`
- `P13_imagen2` -> `P14_imagen4`: `TM`

## Impacto Rápido Por Valor Compartido


### `Laborales`
- Origen (primera aparición): `P2_imagen3` -> `Nombre`
- Formularios donde aparece: `P2_imagen3`, `P2_imagen5`, `P2_imagen7`, `P7_imagen3`, `P10_imagen3`, `P14_imagen3`
- Si lo modificas, revisar: `P2_imagen5`, `P2_imagen7`, `P7_imagen3`, `P10_imagen3`, `P14_imagen3`

### `L1 - 1`
- Origen (primera aparición): `P4_imagen4` -> `Nombre Corto`
- Formularios donde aparece: `P4_imagen4`, `P4_imagen5`, `P5_imagen1`, `P8_imagen4`
- Si lo modificas, revisar: `P4_imagen5`, `P5_imagen1`, `P8_imagen4`

### `L1: Terminal Norte - Terminal Sur`
- Origen (primera aparición): `P4_imagen4` -> `Nombre de la Línea`
- Formularios donde aparece: `P4_imagen4`, `P4_imagen5`, `P5_imagen1`, `P8_imagen4`
- Si lo modificas, revisar: `P4_imagen5`, `P5_imagen1`, `P8_imagen4`


### `LAB`
- Origen (primera aparición): `P2_imagen3` -> `Nombre Corto`
- Formularios donde aparece: `P2_imagen3`, `P2_imagen5`, `P2_imagen7`
- Si lo modificas, revisar: `P2_imagen5`, `P2_imagen7`

### `TERMINAL NORTE`
- Origen (primera aparición): `P4_imagen5` -> `PARADA INICIAL`
- Formularios donde aparece: `P4_imagen5`, `P5_imagen1`, `P5_imagen2`
- Si lo modificas, revisar: `P5_imagen1`, `P5_imagen2`

### `TERMINAL SUR`
- Origen (primera aparición): `P4_imagen5` -> `PARADA FINAL`
- Formularios donde aparece: `P4_imagen5`, `P5_imagen1`, `P5_imagen2`
- Si lo modificas, revisar: `P5_imagen1`, `P5_imagen2`

### `TM`
- Origen (primera aparición): `P13_imagen2` -> `Nombre`
- Formularios donde aparece: `P13_imagen2`, `P13_Imagen4`, `P14_imagen4`
- Si lo modificas, revisar: `P13_Imagen4`, `P14_imagen4`


### `Depósito Empresa`
- Origen (primera aparición): `P6_imagen5` -> `Nombre Largo`
- Formularios donde aparece: `P6_imagen5`, `P6_imagen6`
- Si lo modificas, revisar: `P6_imagen6`

### `L1: TN-TS`
- Origen (primera aparición): `P4_imagen4` -> `Nombre Comercial`
- Formularios donde aparece: `P4_imagen4`, `P8_imagen4`
- Si lo modificas, revisar: `P8_imagen4`

### `Minibus`
- Origen (primera aparición): `P6_imagen7` -> `Tipo de Vehiculo`
- Formularios donde aparece: `P6_imagen7`, `P8_imagen3`
- Si lo modificas, revisar: `P8_imagen3`

### `TERMINAL NORTE - TERMINAL SUR`
- Origen (primera aparición): `P4_imagen5` -> `Paradas`
- Formularios donde aparece: `P4_imagen5`, `P5_imagen1`
- Si lo modificas, revisar: `P5_imagen1`

### `Vacíos - Enero de 2026`
- Origen (primera aparición): `P7_imagen3` -> `Nombre`
- Formularios donde aparece: `P7_imagen3`, `P14_imagen4`
- Si lo modificas, revisar: `P14_imagen4`

### `Vehículos - L1 Laborable`
- Origen (primera aparición): `P12_imagen2` -> `Nombre`
- Formularios donde aparece: `P12_imagen2`, `P14_imagen4`
- Si lo modificas, revisar: `P14_imagen4`

## Mapa Por Formulario

### `P2_imagen3`
- Campos: **4** (no vacíos: **3**)
- Valores distintos no vacíos: **3**
- Campos con valor compartido: **3**
- Depende de: formulario base / sin dependencias detectadas por valor.
- Afecta a: `P2_imagen5` (1, LAB, Laborales); `P2_imagen7` (LAB, Laborales); `P7_imagen3` (Laborales); `P8_imagen3` (1); `P10_imagen3` (Laborales); `P14_imagen3` (Laborales)

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Nombre | name | input_value | Laborales | compartido |
| Nombre Corto | shortName | input_value | LAB | compartido |
| Id Externo | externalId | input_value | 1 | compartido |
| Días de la Semana Aplicables | daysOfWeek | field_value | (vacío) | vacío |

### `P2_imagen5`
- Campos: **4** (no vacíos: **4**)
- Valores distintos no vacíos: **4**
- Campos con valor compartido: **3**
- Depende de: `P2_imagen3` (1, LAB, Laborales)
- Afecta a: sin dependencias salientes detectadas por valor.

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Nombre | name | input_value | Laborales | compartido |
| Nombre Corto | shortName | input_value | LAB | compartido |
| Id Externo | externalId | input_value | 1 | compartido |
| Días de la Semana Aplicables | daysOfWeek | field_value | 5 Seleccionados | único |

### `P2_imagen7`
- Campos: **4** (no vacíos: **4**)
- Valores distintos no vacíos: **4**
- Campos con valor compartido: **2**
- Depende de: `P2_imagen3` (LAB, Laborales)
- Afecta a: sin dependencias salientes detectadas por valor.

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Fecha | date | date_picker | 01 May 2026 | único |
| Nombre | name | input_value | Día del Trabajador | único |
| Nombre Corto | shortName | input_value | LAB | compartido |
| Tipo de Día | dayTypeId | field_value | Laborales | compartido |

### `P3_imagen3`
- Campos: **4** (no vacíos: **4**)
- Valores distintos no vacíos: **4**
- Campos con valor compartido: **0**
- Depende de: formulario base / sin dependencias detectadas por valor.
- Afecta a: sin dependencias salientes detectadas por valor.

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Nombre | name | input_value | Año 2026 | único |
| Año | dateRangesYear | input_value | 2026 | único |
| Fecha de Inicio | dateRangesStart | date_picker | 15 dic 2025 | único |
| Fecha de Fin | dateRangesEnd | date_picker | 13 dic 2026 | único |

### `P4_imagen2`
- Campos: **8** (no vacíos: **7**)
- Valores distintos no vacíos: **4**
- Campos con valor compartido: **2**
- Depende de: formulario base / sin dependencias detectadas por valor.
- Afecta a: `P6_imagen6` (0)

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Tipo de Parada | stopType | field_value | Comercial | único |
| Código | code | input_value | UNI | único |
| Nombre Corto | shortName | input_value | UNI | único |
| Nombre Largo | name | input_value | UNIVERSIDAD | único |
| Nombre Comercial | commercialName | input_value | UNIVERSIDAD | único |
| Latitud | latitude | input_value | 0 | compartido |
| Longitud | longitude | input_value | 0 | compartido |
| ID Externo | externalId | input_value | (vacío) | vacío |

### `P4_imagen4`
- Campos: **7** (no vacíos: **7**)
- Valores distintos no vacíos: **6**
- Campos con valor compartido: **5**
- Depende de: formulario base / sin dependencias detectadas por valor.
- Afecta a: `P4_imagen5` (L1 - 1, L1: Terminal Norte - Terminal Sur); `P5_imagen1` (L1 - 1, L1: Terminal Norte - Terminal Sur); `P8_imagen4` (1 Seleccionados, L1 - 1, L1: Terminal Norte - Terminal Sur, L1: TN-TS); `P9_imagen3` (1 Seleccionados); `P10_imagen3` (1 Seleccionados); `P14_imagen4` (1 Seleccionados); `P14_imagen5` (1 Seleccionados); `P25_imagen2` (1 Seleccionados)

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Nombre de la Línea | name | input_value | L1: Terminal Norte - Terminal Sur | compartido |
| Nombre Corto | shortName | input_value | L1 - 1 | compartido |
| Nombre Comercial | commercialName | input_value | L1: TN-TS | compartido |
| Parkings | parkings | field_value | 1 Seleccionados | compartido |
| Tipos de Vehículos | vehicleTypes | field_value | 1 Seleccionados | compartido |
| ID Externo | externalId | input_value | L1 | único |
| Color | color | input_value | #0288d1 | único |

### `P4_imagen5`
- Campos: **5** (no vacíos: **5**)
- Valores distintos no vacíos: **5**
- Campos con valor compartido: **5**
- Depende de: `P4_imagen4` (L1 - 1, L1: Terminal Norte - Terminal Sur)
- Afecta a: `P5_imagen1` (TERMINAL NORTE, TERMINAL NORTE - TERMINAL SUR, TERMINAL SUR); `P5_imagen2` (TERMINAL NORTE, TERMINAL SUR)

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Cabecero Línea | (sin mapeo) | (sin fila CSV) | L1: Terminal Norte - Terminal Sur | compartido |
| Nombre Línea | (sin mapeo) | (sin fila CSV) | L1 - 1 | compartido |
| Paradas | (sin mapeo) | (sin fila CSV) | TERMINAL NORTE - TERMINAL SUR | compartido |
| PARADA INICIAL | class:gs-text-ellipsis:0 | class_indexed | TERMINAL NORTE | compartido |
| PARADA FINAL | class:gs-text-ellipsis:1 | class_indexed | TERMINAL SUR | compartido |

### `P5_imagen1`
- Campos: **5** (no vacíos: **5**)
- Valores distintos no vacíos: **5**
- Campos con valor compartido: **5**
- Depende de: `P4_imagen4` (L1 - 1, L1: Terminal Norte - Terminal Sur); `P4_imagen5` (TERMINAL NORTE, TERMINAL NORTE - TERMINAL SUR, TERMINAL SUR)
- Afecta a: sin dependencias salientes detectadas por valor.

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Cabecero Línea | (sin mapeo) | (sin fila CSV) | L1: Terminal Norte - Terminal Sur | compartido |
| Nombre Línea | (sin mapeo) | (sin fila CSV) | L1 - 1 | compartido |
| Paradas | (sin mapeo) | (sin fila CSV) | TERMINAL NORTE - TERMINAL SUR | compartido |
| PARADA INICIAL | class:gs-text-ellipsis:0 | class_indexed | TERMINAL NORTE | compartido |
| PARADA FINAL | class:gs-text-ellipsis:1 | class_indexed | TERMINAL SUR | compartido |

### `P5_imagen2`
- Campos: **2** (no vacíos: **2**)
- Valores distintos no vacíos: **2**
- Campos con valor compartido: **2**
- Depende de: `P4_imagen5` (TERMINAL NORTE, TERMINAL SUR)
- Afecta a: sin dependencias salientes detectadas por valor.

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| PARADA INICIAL | class:gs-text-ellipsis:0 | class_indexed | TERMINAL NORTE | compartido |
| PARADA FINAL | class:gs-text-ellipsis:1 | class_indexed | TERMINAL SUR | compartido |

### `P6_imagen5`
- Campos: **5** (no vacíos: **4**)
- Valores distintos no vacíos: **4**
- Campos con valor compartido: **1**
- Depende de: formulario base / sin dependencias detectadas por valor.
- Afecta a: `P6_imagen6` (Depósito Empresa)

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Código | code | input_value | DP01 | único |
| Nombre Corto | nameShort | input_value | DEP EMP | único |
| Nombre Largo | name | input_value | Depósito Empresa | compartido |
| ID Externo | externalId | input_value | DEPEMP01 | único |
| Lugares Inicio/Fin Conductores | stops | field_value | (vacío) | vacío |

### `P6_imagen6`
- Campos: **7** (no vacíos: **6**)
- Valores distintos no vacíos: **5**
- Campos con valor compartido: **3**
- Depende de: `P4_imagen2` (0); `P6_imagen5` (Depósito Empresa)
- Afecta a: sin dependencias salientes detectadas por valor.

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Código | code | input_value | PKG06 | único |
| Nombre Corto | nameShort | input_value | PKGNTE1 | único |
| Nombre Largo | name | input_value | Parking Norte 1 | único |
| Latitud | latitude | input_value | 0 | compartido |
| Longitud | longitude | input_value | 0 | compartido |
| Depósito | depot | field_value | Depósito Empresa | compartido |
| Id Externo | externalId | input_value | (vacío) | vacío |

### `P6_imagen7`
- Campos: **4** (no vacíos: **4**)
- Valores distintos no vacíos: **3**
- Campos con valor compartido: **3**
- Depende de: formulario base / sin dependencias detectadas por valor.
- Afecta a: `P8_imagen3` (500, Minibus)

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Capacidad Total | capacity | input_value | 500 | compartido |
| Tipo de Vehiculo | vehicleType | field_value | Minibus | compartido |
| Flota | fleet | input_value | 100 | único |
| Capacidad Máxima | maxCapacity | input_value | 500 | compartido |

### `P7_imagen3`
- Campos: **3** (no vacíos: **2**)
- Valores distintos no vacíos: **2**
- Campos con valor compartido: **2**
- Depende de: `P2_imagen3` (Laborales)
- Afecta a: `P14_imagen4` (Vacíos - Enero de 2026)

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Nombre | name | input_value | Vacíos - Enero de 2026 | compartido |
| Día Tipo | dayTypes | field_value | Laborales | compartido |
| descripción | description | input_value | (vacío) | vacío |

### `P8_imagen3`
- Campos: **8** (no vacíos: **7**)
- Valores distintos no vacíos: **7**
- Campos con valor compartido: **3**
- Depende de: `P2_imagen3` (1); `P6_imagen7` (500, Minibus)
- Afecta a: sin dependencias salientes detectadas por valor.

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Nombre del Tipo de Vehículo | vehicleTypeName | input_value | Minibus | compartido |
| Tipo de Propulsión | propulsionTypeId | field_value | Non-electric | único |
| Capacidad | capacity | input_value | 30 | único |
| Logitud (m) | length | input_value | 8 | único |
| Autonomía Estimada (Km) | autonomy | input_value | 500 | compartido |
| Penalización por km | costPerKm | input_value | 1 | compartido |
| Mínimo de Asientos | minimumSeats | input_value | (vacío) | vacío |
| ID Externo | externalId | input_value | 3 | único |

### `P8_imagen4`
- Campos: **6** (no vacíos: **4**)
- Valores distintos no vacíos: **4**
- Campos con valor compartido: **4**
- Depende de: `P4_imagen4` (1 Seleccionados, L1 - 1, L1: Terminal Norte - Terminal Sur, L1: TN-TS)
- Afecta a: sin dependencias salientes detectadas por valor.

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Nombre de la Línea | name | input_value | L1: Terminal Norte - Terminal Sur | compartido |
| Nombre Corto | shortName | input_value | L1 - 1 | compartido |
| Nombre Comercial | commercialName | input_value | L1: TN-TS | compartido |
| Parkings | parkings | field_value | 1 Seleccionados | compartido |
| Tipos de Vehículos | vehicleTypes | field_value | (vacío) | vacío |
| ID Externo | externalId | input_value | (vacío) | vacío |

### `P9_imagen3`
- Campos: **4** (no vacíos: **4**)
- Valores distintos no vacíos: **4**
- Campos con valor compartido: **1**
- Depende de: `P4_imagen4` (1 Seleccionados)
- Afecta a: sin dependencias salientes detectadas por valor.

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Nombre | name | input_value | L1 Laborable Base | único |
| Descripción | description | input_value | Tiempos de recorrido L1 días Laborables | único |
| Día Tipo | dayTypes | field_value | 1 Seleccionados | compartido |
| Rutas | routes | field_value | 2 Seleccionados | único |

### `P9_imagen6`
- Campos: **1** (no vacíos: **0**)
- Valores distintos no vacíos: **0**
- Campos con valor compartido: **0**
- Depende de: formulario base / sin dependencias detectadas por valor.
- Afecta a: sin dependencias salientes detectadas por valor.

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Formulario de tiempos de Recorrido por franjas | (sin mapeo) | (sin fila CSV) | (vacío) | vacío |

### `P10_imagen3`
- Campos: **4** (no vacíos: **4**)
- Valores distintos no vacíos: **4**
- Campos con valor compartido: **2**
- Depende de: `P2_imagen3` (Laborales); `P4_imagen4` (1 Seleccionados)
- Afecta a: sin dependencias salientes detectadas por valor.

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Nombre | name | input_value | Día Laborable estándar - L1 | único |
| Día Tipo | dayType | field_value | Laborales | compartido |
| Líneas | lines | field_value | 1 Seleccionados | compartido |
| Descripción | description | input_value | Servicio comercial laborable para la línea 1 para días laborales | único |

### `P12_imagen2`
- Campos: **2** (no vacíos: **2**)
- Valores distintos no vacíos: **2**
- Campos con valor compartido: **1**
- Depende de: formulario base / sin dependencias detectadas por valor.
- Afecta a: `P14_imagen4` (Vehículos - L1 Laborable)

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Nombre | model | input_value | Vehículos - L1 Laborable | compartido |
| Descripción | description | input_value | Modelo de Reglas para los Vehiculos de L1 en Laborales | único |

### `P13_imagen2`
- Campos: **3** (no vacíos: **3**)
- Valores distintos no vacíos: **2**
- Campos con valor compartido: **2**
- Depende de: formulario base / sin dependencias detectadas por valor.
- Afecta a: `P13_Imagen4` (TM); `P14_imagen4` (TM)

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Nombre | name | input_value | TM | compartido |
| Nombre Corto | shortName | input_value | Turno Mañana | único |
| ID Externo | externalId | input_value | TM | compartido |

### `P13_imagen3`
- Campos: **2** (no vacíos: **2**)
- Valores distintos no vacíos: **2**
- Campos con valor compartido: **0**
- Depende de: formulario base / sin dependencias detectadas por valor.
- Afecta a: sin dependencias salientes detectadas por valor.

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Nombre | name | input_value | Turnos - L1 | único |
| Descripción | description | input_value | Reglas para Turnos de L1 | único |

### `P13_Imagen4`
- Campos: **3** (no vacíos: **3**)
- Valores distintos no vacíos: **3**
- Campos con valor compartido: **1**
- Depende de: `P13_imagen2` (TM)
- Afecta a: sin dependencias salientes detectadas por valor.

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Plantilla | template | field_value | Horarios | único |
| Nombre | name | input_value | TM | compartido |
| Descripción | description | input_value | Horarios de turno de Mañana | único |

### `P14_imagen3`
- Campos: **3** (no vacíos: **3**)
- Valores distintos no vacíos: **3**
- Campos con valor compartido: **1**
- Depende de: `P2_imagen3` (Laborales)
- Afecta a: sin dependencias salientes detectadas por valor.

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Nombre | name | input_value | Cálculo Clásico - L1 Laborable | único |
| Tipo de Día | dayType | field_value | Laborales | compartido |
| Descripción | description | input_value | Escenario con cálculo clásico para L1 Laborable | único |

### `P14_imagen4`
- Campos: **5** (no vacíos: **5**)
- Valores distintos no vacíos: **5**
- Campos con valor compartido: **4**
- Depende de: `P4_imagen4` (1 Seleccionados); `P7_imagen3` (Vacíos - Enero de 2026); `P12_imagen2` (Vehículos - L1 Laborable); `P13_imagen2` (TM)
- Afecta a: sin dependencias salientes detectadas por valor.

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Servicios | services | field_value | 1 Seleccionados | compartido |
| Modelo de Reglas de Turno | shiftRuleModel | field_value | TM | compartido |
| Modelo de Reglas de Tipos de Vehículo (Opcional) | vehicleTypeRuleModel | field_value | Vehículos - L1 Laborable | compartido |
| Matriz | emptyTripsMatrix | field_value | Vacíos - Enero de 2026 | compartido |
| Desplazamientos conductores | driverEmptyTripsMatrix | field_value | Desplazamientos | único |

### `P14_imagen5`
- Campos: **1** (no vacíos: **1**)
- Valores distintos no vacíos: **1**
- Campos con valor compartido: **1**
- Depende de: `P4_imagen4` (1 Seleccionados)
- Afecta a: sin dependencias salientes detectadas por valor.

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Líneas | lines | field_value | 1 Seleccionados | compartido |

### `P14_imagen8`
- Campos: **2** (no vacíos: **2**)
- Valores distintos no vacíos: **2**
- Campos con valor compartido: **0**
- Depende de: formulario base / sin dependencias detectadas por valor.
- Afecta a: sin dependencias salientes detectadas por valor.

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Motor de Cálculo | engineType | field_value | GoalBusClassic | único |
| Tiempo máximo de cálculo | (sin mapeo) | (sin fila CSV) | 00:05 | único |

### `P17_imagen2`
- Campos: **2** (no vacíos: **2**)
- Valores distintos no vacíos: **2**
- Campos con valor compartido: **0**
- Depende de: formulario base / sin dependencias detectadas por valor.
- Afecta a: sin dependencias salientes detectadas por valor.

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Nombre | name | input_value | Cálculo Clásico - L1 Laborable - Iteración 2 | único |
| descripción | description | input_value | Escenario con cálculo clásico para L1 Laborable iteración 2 | único |

### `P22_imagen3`
- Campos: **3** (no vacíos: **3**)
- Valores distintos no vacíos: **3**
- Campos con valor compartido: **0**
- Depende de: formulario base / sin dependencias detectadas por valor.
- Afecta a: sin dependencias salientes detectadas por valor.

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Nombre | name | input_value | Asignación L1 laborable | único |
| Categoría | category | field_value | Tareas de Conductores | único |
| Descripción | description | input_value | Modelo de reglas para la asignación | único |

### `P25_imagen2`
- Campos: **5** (no vacíos: **5**)
- Valores distintos no vacíos: **4**
- Campos con valor compartido: **1**
- Depende de: `P4_imagen4` (1 Seleccionados)
- Afecta a: sin dependencias salientes detectadas por valor.

| Campo UI | field_id CSV | type CSV | Valor | Tipo de valor |
|---|---|---|---|---|
| Nombre | nameField | input_value | L1 laborables - Asignación de conductores | único |
| Depósitos | depotsField | field_value | 1 Seleccionados | compartido |
| fechas | dateRangeField | date_picker | 20 abr 2026 - 26 abr 2026 | único |
| Modelo de regla | (sin mapeo) | (sin fila CSV) | Rostering L1 Laborable | único |
| Descripción | descriptionField | input_value | L1 laborables - Asignación de conductores | único |

## Índice De Valores Únicos (deduplicado)

| Valor | Apariciones | Formularios | Clasificación |
|---|---:|---:|---|
| #0288d1 | 1 | 1 | único |
| 0 | 4 | 2 | compartido |
| 00:05 | 1 | 1 | único |
| 01 May 2026 | 1 | 1 | único |
| 1 | 3 | 3 | compartido |
| 1 Seleccionados | 8 | 7 | compartido |
| 100 | 1 | 1 | único |
| 13 dic 2026 | 1 | 1 | único |
| 15 dic 2025 | 1 | 1 | único |
| 2 Seleccionados | 1 | 1 | único |
| 20 abr 2026 - 26 abr 2026 | 1 | 1 | único |
| 2026 | 1 | 1 | único |
| 3 | 1 | 1 | único |
| 30 | 1 | 1 | único |
| 5 Seleccionados | 1 | 1 | único |
| 500 | 3 | 2 | compartido |
| 8 | 1 | 1 | único |
| Asignación L1 laborable | 1 | 1 | único |
| Año 2026 | 1 | 1 | único |
| Comercial | 1 | 1 | único |
| Cálculo Clásico - L1 Laborable | 1 | 1 | único |
| Cálculo Clásico - L1 Laborable - Iteración 2 | 1 | 1 | único |
| DEP EMP | 1 | 1 | único |
| DEPEMP01 | 1 | 1 | único |
| Depósito Empresa | 2 | 2 | compartido |
| Desplazamientos | 1 | 1 | único |
| DP01 | 1 | 1 | único |
| Día del Trabajador | 1 | 1 | único |
| Día Laborable estándar - L1 | 1 | 1 | único |
| Escenario con cálculo clásico para L1 Laborable | 1 | 1 | único |
| Escenario con cálculo clásico para L1 Laborable iteración 2 | 1 | 1 | único |
| GoalBusClassic | 1 | 1 | único |
| Horarios | 1 | 1 | único |
| Horarios de turno de Mañana | 1 | 1 | único |
| L1 | 1 | 1 | único |
| L1 - 1 | 4 | 4 | compartido |
| L1 Laborable Base | 1 | 1 | único |
| L1 laborables - Asignación de conductores | 2 | 1 | único |
| L1: Terminal Norte - Terminal Sur | 4 | 4 | compartido |
| L1: TN-TS | 2 | 2 | compartido |
| LAB | 3 | 3 | compartido |
| Laborales | 6 | 6 | compartido |
| Minibus | 2 | 2 | compartido |
| Modelo de reglas para la asignación | 1 | 1 | único |
| Modelo de Reglas para los Vehiculos de L1 en Laborales | 1 | 1 | único |
| Non-electric | 1 | 1 | único |
| Parking Norte 1 | 1 | 1 | único |
| PKG06 | 1 | 1 | único |
| PKGNTE1 | 1 | 1 | único |
| Reglas para Turnos de L1 | 1 | 1 | único |
| Rostering L1 Laborable | 1 | 1 | único |
| Servicio comercial laborable para la línea 1 para días laborales | 1 | 1 | único |
| Tareas de Conductores | 1 | 1 | único |
| TERMINAL NORTE | 3 | 3 | compartido |
| TERMINAL NORTE - TERMINAL SUR | 2 | 2 | compartido |
| TERMINAL SUR | 3 | 3 | compartido |
| Tiempos de recorrido L1 días Laborables | 1 | 1 | único |
| TM | 4 | 3 | compartido |
| Turno Mañana | 1 | 1 | único |
| Turnos - L1 | 1 | 1 | único |
| UNI | 2 | 1 | único |
| UNIVERSIDAD | 2 | 1 | único |
| Vacíos - Enero de 2026 | 2 | 2 | compartido |
| Vehículos - L1 Laborable | 2 | 2 | compartido |
