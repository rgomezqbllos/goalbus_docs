# Glosario de Dominio — GoalBus OPS
**Software de Gestión y Control de Planificación y Operación de Transporte Público de Pasajeros**

Tres idiomas: Español (ES) · Inglés (EN) · Portugués de Brasil (PT-BR)

> Este glosario es normativo. Todos los textos de la interfaz deben usar los términos aquí definidos de forma consistente. En caso de duda entre dos opciones, prevalece la entrada de este documento.

---

## A — Entidades de Red y Planificación

| Español (ES) | Inglés (EN) | PT-BR | Notas |
|---|---|---|---|
| Línea | Route / Line | Linha | Itinerario completo de una línea de transporte |
| Ruta | Route | Rota | Trayecto concreto de una línea |
| Parada | Stop | Parada | Punto de la red donde sube/baja el pasajero |
| Sección | Section | Seção | Tramo entre dos paradas |
| Viaje | Trip | Viagem | Recorrido concreto con horario asignado |
| Viaje vacío | Empty trip | Viagem vazia | Desplazamiento sin pasajeros |
| Viaje vacío en sentido contrario | Empty trip in opposite direction | Viagem vazia em sentido contrário | |
| Itinerario | Itinerary | Itinerário | Secuencia de paradas de una línea |
| Horario | Schedule / Timetable | Horário | Horas de paso por cada parada |
| Programación | Scheduling | Programação | Proceso de asignación de horarios |
| Intervalo de fechas | Date range | Intervalo de datas | |
| Fecha de inicio | Start date | Data de início | |
| Fecha de fin | End date | Data de fim | |
| Código de viaje | Trip code | Código da viagem | Identificador único del viaje |
| Tipo de viaje | Trip type | Tipo de viagem | |
| Clase de servicio | Service class | Classe de serviço | |
| Marca | Brand | Marca | Operador comercial de la línea |
| Días aplicables | Days applicable | Dias aplicáveis | Días de la semana en que opera |
| Peaje | Toll | Pedágio | |
| Punto de inicio | Start place | Local de início | |
| Punto de fin | End place | Local de fim | |
| Distancia | Distance | Distância | |
| Amplitud | Amplitude | Amplitude | Rango temporal de operación |

---

## B — Conductores y Personal

| Español (ES) | Inglés (EN) | PT-BR | Notas |
|---|---|---|---|
| Conductor | Driver | Motorista | ⚠️ No usar "conductor" ni "chofer" en PT-BR |
| Motorista virtual | Virtual driver | Motorista virtual | Conductor no real usado en simulación |
| Grupo de trabajo | Working group | Grupo de trabalho | Agrupación operativa de conductores |
| Colectivo del conductor | Driver collective | Coletivo do motorista | Convenio colectivo al que pertenece |
| Tipo de contrato | Contract kind | Tipo de contrato | |
| Nacionalidad | Nationality | Nacionalidade | |
| Calificación | Qualification | Qualificação | Habilitación del conductor para un tipo de vehículo |
| Tipo de vehículo requerido | Required vehicle type | Tipo de veículo exigido | |
| Perfil del conductor | Driver profile | Perfil do motorista | |
| Información administrativa | Admin info | Informações administrativas | |
| Depósito (asignado) | Depot | Depósito | Centro de operaciones del conductor |
| Unidad de negocio | Business unit | Unidade de negócio | |
| Entrada registrada | Book on | Entrada registrada | Marcaje de inicio de jornada |
| Salida registrada | Book off | Saída registrada | Marcaje de fin de jornada |
| Candidatos disponibles | Driver candidates | Candidatos disponíveis | Conductores propuestos para una tarea |

---

## C — Turnos y Escalonamiento

| Español (ES) | Inglés (EN) | PT-BR | Notas |
|---|---|---|---|
| Turno | Shift | Turno | Unidad básica de trabajo |
| Escala | Roster / Schedule | Escala | Planificación de turnos por período |
| Escalonamiento | Rostering | Alocação | Módulo GoalBus Rostering = Alocação en PT-BR ⚠️ Nunca "Rostering" sin traducir |
| Escenario | Scenario | Cenário | Versión de planificación |
| Escenario nominativo | Nominative scenario | Cenário nominativo | Asignado a conductores concretos |
| Ciclo | Cycle | Ciclo | Período de rotación de turnos |
| Ciclo cíclico | Cyclic scenario | Cenário cíclico | |
| Patrón de asignación | Assignment pattern | Configuração de atribuição | |
| Atribuição em massa | Massive assignment | Atribuição em massa | ⚠️ Nunca "Massive Atribuição" |
| Regla de turno | Shift rule | Regra de turno | Restricción de planificación |
| Saldo de horas | Working balance | Saldo de horas | Diferencia horas planificadas vs. trabajadas |
| Horas planificadas | Planned hours | Horas planejadas | |
| Prontidão | Stand by | Prontidão | Disponibilidad de guardia |
| Prontidão por hora | Hourly stand by | Prontidão por hora | |
| Folga | Day off | Folga | Día libre |
| Descanso | Rest day | Dia de descanso | |
| Feriado trabajado | Worked holiday | Feriado trabalhado | |
| Feriado libre | Free holiday | Feriado livre | |
| Publicar escala | Publish roster | Publicar escala | |

---

## D — Tareas y Eventos

| Español (ES) | Inglés (EN) | PT-BR | Notas |
|---|---|---|---|
| Tarea | Task | Tarefa | ⚠️ No usar "Dever" en PT-BR |
| Tarea no asignada | Unassigned task | Tarefa não atribuída | |
| Tarea asignada | Assigned task | Tarefa atribuída | |
| Tipo de evento | Event type | Tipo de evento | |
| Conexión | Connection | Conexão | Enlace entre dos servicios |
| Salida de garaje | Drive off / Garage out | Saída de garagem | |
| Entrada a garaje | Park / Garage in | Entrada na garagem | |
| Desplazamiento como pasajero | Other travelling trip as passenger | Deslocamento como passageiro | |
| Viaje vacío | Empty trip | Viagem vazia | |
| Movimiento en estación | Train movement at station | Movimento em estação | |
| División de tarea | Task split | Divisão de tarefa | |
| Recorte de tarea | Task trim | Corte de tarefa | |
| Hora de inicio de tarea | Task start hour | Hora de início da tarefa | |
| Hora de fin de tarea | Task end hour | Hora de fim da tarefa | |
| Lugar de fin de tarea | Task end place | Local de fim da tarefa | |
| Tiempo de toma de vehículo | Vehicle take time | Tempo de tomada do veículo | |
| Tiempo de entrega de vehículo | Vehicle leave time | Tempo de saída do veículo | |
| Disponibilidad de tiempo | Availability time | Disponibilidade de tempo | |
| Categoría de tarea | Task category | Categoria da tarefa | |

---

## E — Vehículos y Flota

| Español (ES) | Inglés (EN) | PT-BR | Notas |
|---|---|---|---|
| Vehículo | Vehicle | Veículo | |
| Tipo de vehículo | Vehicle type | Tipo de veículo | |
| Modelo de vehículo | Vehicle model | Modelo de veículo | |
| Flota | Fleet | Frota | |
| Garaje / Depósito | Parking / Depot | Garagem / Depósito | |
| Indisponibilidad | Unavailability | Indisponibilidade | |
| Velocidad de recarga | Recharge speed | Velocidade de recarga | Vehículos eléctricos |
| Punto de carga | Charging point | Ponto de carregamento | |
| Carregador | Charger | Carregador | |
| Tarifa eléctrica | Electricity tariff | Tarifa de eletricidade | |
| Potencia máxima | Max available power | Potência máxima disponível | |
| Tecnología de propulsión | Propulsion technology | Tecnologia de propulsão | |
| Tipo de propulsión | Propulsion type | Tipo de propulsão | |
| Diésel | Diesel | Diesel | Se mantiene igual en los tres idiomas |
| Eléctrico | Electric | Elétrico | |

---

## F — Operación en Tiempo Real

| Español (ES) | Inglés (EN) | PT-BR | Notas |
|---|---|---|---|
| Tiempo real | Real time | Tempo real | |
| Despacho | Dispatch | Despacho | |
| Estado | Status | Status | ⚠️ En PT-BR se acepta "Status" como anglicismo consolidado |
| Planificado | Planned | Planejado | |
| En ruta / En marcha | Driving / On route | Dirigindo | |
| Atrasado | Delayed | Atrasado | |
| Completado | Completed | Completo | |
| Incidencia | Incidence | Incidência | |
| Solicitud de operación | Trip operation request | Solicitação de operação de viagem | |
| Solicitud de creación | Creation request | Solicitação de criação | |
| Solicitud de cancelación | Cancellation request | Solicitação de cancelamento | |
| Solicitud de edición | Edit request | Solicitação de edição | |
| Aprobado | Approved | Aprovado | |
| Rechazado | Rejected | Rejeitado | |

---

## G — Ausencias y Solicitudes

| Español (ES) | Inglés (EN) | PT-BR | Notas |
|---|---|---|---|
| Ausencia | Absence | Ausência | |
| Tipo de ausencia | Absence type | Tipo de ausência | |
| Solicitud de ausencia | Absence request | Solicitação de ausência | |
| Solicitud de cambio | Swap request | Solicitação de troca | |
| Aprobación pendiente | Pending approval | Aprovação em andamento | |
| Aprobado | Approved | Aprovado | |
| Días restantes | Days left | Dias restantes | |
| Horas restantes | Hours left | Horas restantes | |
| Sobreposición permitida | Overlappable | Sobreposição permitida | |
| De guardia | On call | De prontidão | |

---

## H — Oferta Comercial

| Español (ES) | Inglés (EN) | PT-BR | Notas |
|---|---|---|---|
| Oferta comercial | Commercial offer | Oferta comercial | |
| Paquete comercial | Commercial pack / Package | Pacote comercial | |
| Versión | Version | Versão | ⚠️ Nunca "Version" sin traducir |
| Rascunho | Draft | Rascunho | |
| Validado | Validated | Validado | |
| Publicado | Published | Publicado | |
| Publicando | Publishing | Publicando | |
| Necesita revisión | Needs review | Necessita revisão | |
| Venda ativada | Sale activated | Venda ativada | ⚠️ Nunca "Ativado Sale" |
| Venda suspensa | Sale paused | Venda suspensa | |
| Secuencia de paradas | Stop sequence | Sequência de paradas | |
| Días de la semana | Weekdays | Dias da semana | ⚠️ Nunca "Semanadays" |

---

## I — Configuración y Administración

| Español (ES) | Inglés (EN) | PT-BR | Notas |
|---|---|---|---|
| Tenant / Cliente | Tenant | Tenant | ⚠️ Se mantiene "Tenant" como término técnico en PT-BR |
| Configuración | Settings / Configuration | Configuração | |
| Regla avanzada | Advanced rule | Regra avançada | |
| Activación | Activation | Ativação | |
| Activación desactivada | Activation disabled | Ativação desativada | |
| Aplicar en operación diaria | Apply in daily ops | Aplicar na operação diária | |
| Nombre ya existente | Name already exists | Nome já existente | |
| Gestión de usuarios | User management | Gestão de usuários | |
| Gestión de conductores | Driver management | Gestão de motoristas | |
| Patrón de trabajo | Work pattern | Padrão de trabalho | |
| Grupo de trabajo | Working group | Grupo de trabalho | |
| Fuente de datos | Data source | Fonte de dados | |
| Banco de datos | Database | Banco de dados | |
| Referencia del servidor | Server reference | Referência do servidor | |
| Preferencias globales | Global preferences | Preferências globais | |

---

## J — Mensajes del Sistema (Patrones Reutilizables)

| Situación | ES | EN | PT-BR |
|-----------|----|----|-------|
| Éxito genérico | `[X] guardado/a con éxito.` | `[X] saved successfully.` | `[X] salvo/a com sucesso.` |
| Error genérico | `Ocurrió un error inesperado. Inténtalo de nuevo.` | `An unexpected error occurred. Please try again.` | `Ocorreu um erro inesperado. Tente novamente.` |
| Confirmación destructiva | `Esta acción no puede deshacerse.` | `This action cannot be undone.` | `Esta ação não pode ser desfeita.` |
| Campo obligatorio | `Este campo es obligatorio.` | `This field is required.` | `Este campo é obrigatório.` |
| Sin datos | `No hay datos disponibles.` | `No data available.` | `Não há dados disponíveis.` |
| Sin resultados | `No se encontraron resultados.` | `No results found.` | `Nenhum resultado encontrado.` |
| Cargando | `Cargando...` | `Loading...` | `Carregando...` |
| Guardando | `Guardando...` | `Saving...` | `Salvando...` |
| Sin selección | `Ningún elemento seleccionado.` | `No item selected.` | `Nenhum item selecionado.` |
| Valor duplicado | `El valor ya existe.` | `Value already exists.` | `O valor já existe.` |
| Nombre duplicado | `El nombre ya existe.` | `Name already exists.` | `Nome já existente.` |
| No encontrado | `[X] no encontrado/a.` | `[X] not found.` | `[X] não encontrado/a.` |
| No válido | `[X] no válido/a.` | `[X] not valid.` | `[X] inválido/a.` |
| No permitido | `Operación no permitida.` | `Operation not allowed.` | `Operação não permitida.` |

---

## K — Términos Técnicos Universales (sin traducción)

Los siguientes términos se mantienen igual en los tres idiomas:

| Término | Uso en el sistema |
|---------|-----------------|
| `Status` | Estado de cualquier entidad |
| `KPI` | Indicador clave de rendimiento |
| `ID` | Identificador único |
| `Email` | Dirección de correo |
| `Latitude` / `Longitude` | Coordenadas geográficas |
| `Token` | Código de autenticación |
| `Offset` | Desplazamiento en patrón de trabajo |
| `Diesel` | Tipo de combustible |
| `PDF` | Formato de documento |
| `URL` | Dirección web |
| `GB.Driver` | Nombre del app móvil para conductores |
| `GoalBus Driver` | Nombre comercial del app de conductores |
| `GoalBus OPS` | Nombre de la suite de back-office |

---

## L — Abreviaciones Aceptadas

| Abreviación | Significado ES | Significado EN | Significado PT-BR |
|-------------|---------------|----------------|-------------------|
| `KPI` | Indicador clave de rendimiento | Key Performance Indicator | Indicador-chave de desempenho |
| `ID` | Identificador | Identifier | Identificador |
| `N/A` | No aplica / No disponible | Not applicable | Não aplicável |
| `Máx.` | Máximo | Max. | Máx. |
| `Mín.` | Mínimo | Min. | Mín. |
| `kWh` | Kilovatio hora | Kilowatt-hour | Quilowatt-hora |
| `km` | Kilómetros | Kilometres | Quilômetros |

---

*Versión 1.0 — Generado a partir de la auditoría lingüística de goalbus-ops-pt.final.json · Abril 2026*
*Idiomas cubiertos: Español (ES) · Inglés (EN) · Portugués de Brasil (PT-BR)*
