# Guía de Traducción JSON — GoalBus OPS
**Software de Gestión y Control de Planificación y Operación de Transporte Público de Pasajeros**
**Idiomas:** Español (ES) · Inglés (EN) · Portugués de Brasil (PT-BR)

---

## 1. Contexto del Producto

GoalBus OPS es una suite empresarial de optimización para operadores de transporte público. Sus módulos principales cubren:

- **Planificación** de líneas, rutas, paradas, viajes y horarios
- **Rostering / Escalonamiento** de conductores y vehículos
- **Operación diaria** con asignaciones, turnos, ausencias e incidencias
- **Tiempo real** con despacho, seguimiento y eventos de tarea
- **Oferta comercial** con paquetes, itinerarios y gestión de versiones
- **Configuración de tenant** con reglas, usuarios y grupos de trabajo

Todo el texto visible al usuario final debe estar traducido al idioma objetivo. Los identificadores técnicos internos (claves del JSON) nunca se muestran al usuario.

---

## 2. Estructura del Archivo JSON

El archivo de traducciones es un JSON plano (sin anidación) con pares clave-valor:

```json
{
  "modulo.submodulo.componente.elemento": "Texto visible al usuario"
}
```

### 2.1 Lectura de la clave (key)

La clave es una guía del contenido. Sus segmentos, de izquierda a derecha, indican:

```
planning . stops . form . fields . name
  │          │       │       │       └── elemento concreto → "name" = campo nombre
  │          │       │       └────────── contexto → "fields" = campo de formulario
  │          │       └────────────────── componente → "form" = formulario
  │          └────────────────────────── entidad → "stops" = paradas
  └───────────────────────────────────── módulo → "planning" = planificación
```

**El último segmento de la clave es la pista más importante** para entender qué tipo de texto es:

| Último segmento | Tipo de texto | Ejemplo |
|----------------|--------------|---------|
| `.title` | Título de sección o modal | `"Editar Parada"` |
| `.label` | Etiqueta de campo | `"Nombre"` |
| `.placeholder` | Texto de ayuda dentro de un campo | `"Buscar por nombre..."` |
| `.description` | Texto explicativo | `"Esta acción no puede deshacerse."` |
| `.success` | Mensaje de confirmación | `"Parada creada con éxito."` |
| `.error` / `.errors.*` | Mensaje de error | `"El nombre ya existe."` |
| `.cancel` | Botón cancelar | `"Cancelar"` |
| `.submit` / `.save` | Botón de acción principal | `"Guardar"` |
| `.confirmation` | Texto de confirmación de acción destructiva | `"¿Estás seguro?"` |
| `.tooltip` | Texto de ayuda emergente | `"Haz clic para expandir"` |
| `.column.*` / `.headers.*` | Cabecera de tabla | `"Fecha de inicio"` |

---

## 3. Reglas Generales de Traducción

### 3.1 Qué SIEMPRE se traduce

- Todo texto visible al usuario: botones, etiquetas, mensajes, títulos, descripciones, errores
- Mensajes de éxito y error, incluyendo los que mezclan variables: `"Pacote {{name}} excluído com sucesso."`
- Textos en UPPERCASE que son etiquetas de pantalla: `PLANEJADO`, `ATRASADO`, `COMPLETO`

### 3.2 Qué NUNCA se traduce

| Elemento | Motivo | Ejemplo |
|----------|--------|---------|
| Nombres de producto o app | Son marcas comerciales | `GoalBus Driver`, `GB.Driver` |
| Placeholders de variables | Son tokens técnicos | `{{driverName}}`, `{{count}}`, `{date}` |
| Claves del JSON | No son visibles al usuario | `planning.stops.form.name` |
| Valores puramente numéricos | No tienen traducción | `"0"`, `"100"` |
| URLs, emails, códigos de país | Identificadores técnicos | `"es-ES"`, `"https://..."` |
| Abreviaciones universales | Aceptadas en todos los idiomas | `"ID"`, `"KPI"`, `"URL"`, `"PDF"` |

### 3.3 Términos técnicos aceptados sin traducción

Los siguientes términos se consideran universalmente aceptados en el sector y en PT-BR:

`Status` · `Email` · `Latitude` · `Longitude` · `Offset` · `KPI` · `ID` · `Diesel` · `Linear` · `Amplitude` · `Tenants` · `Token`

---

## 4. Normas por Idioma

### 4.1 Español (ES)

- Tuteo: usar **tú** (no voseo ni ustedeo).
  - ✅ `"¿Estás seguro de que quieres eliminar?"`
  - ❌ `"¿Está seguro de que quiere eliminar?"`
- Género: respetar el género gramatical de cada entidad del dominio.
  - `la ruta`, `el conductor`, `la parada`, `el turno`, `la ausencia`
- Mensajes de éxito: estructura `[Entidad] [acción] con éxito.`
  - ✅ `"Parada creada con éxito."`
  - ❌ `"Successfully created stop."`
- Mensajes de error: estructura `Error al [acción] [entidad].`
  - ✅ `"Error al actualizar la parada."`
  - ❌ `"Update stop error."`
- No usar anglicismos innecesarios cuando existe término en español.

### 4.2 Inglés (EN)

- Tono: profesional pero directo. Sin formulismos excesivos.
- Capitalización de títulos (Title Case) para títulos y botones principales:
  - ✅ `"Edit Stop"`, `"Create New Route"`
- Sentence case para descripciones y mensajes:
  - ✅ `"This action cannot be undone."`
- Mensajes de éxito: `[Entity] [past participle] successfully.`
  - ✅ `"Stop created successfully."`
- Mensajes de error: `Error [verb-ing] [entity].` o `Failed to [verb] [entity].`
  - ✅ `"Error updating stop."` / `"Failed to update stop."`

### 4.3 Portugués de Brasil (PT-BR)

- Tratamiento: usar **você** (no `tu` ni `vós`).
  - ✅ `"Tem certeza que deseja excluir?"`
  - ❌ `"Tens a certeza que queres excluir?"` (PT-PT)
- Género: respetar concordancia de género y número en toda la oración.
  - `a rota`, `o motorista`, `a parada`, `o turno`, `a ausência`
- Verbos de acción en botones: infinitivo.
  - ✅ `"Salvar"`, `"Excluir"`, `"Cancelar"`, `"Confirmar"`
  - ❌ `"Save"`, `"Delete"`, `"Cancel"`
- Mensajes de éxito: estructura `[Entidade] [particípio] com sucesso.`
  - ✅ `"Parada criada com sucesso."`
  - ❌ `"Parada created successfully."`
- Mensajes de error: `Erro ao [infinitivo] [entidade].`
  - ✅ `"Erro ao atualizar a parada."`
  - ❌ `"Erro updating parada."`
- **Diferencias clave PT-BR vs PT-PT** a tener en cuenta:

| Concepto | PT-BR ✅ | PT-PT ❌ |
|----------|---------|---------|
| Autobús | Ônibus | Autocarro |
| Depósito / garaje | Garagem / Depósito | Garagem |
| Conductor | Motorista | Condutor |
| Celular / móvil | Celular | Telemóvel |
| Aplicación | Aplicativo | Aplicação |
| Verificar | Verificar | Verificar |
| Eliminar | Excluir | Eliminar |
| Desactivado | Desativado | Desativado |
| Horario | Horário | Horário |

---

## 5. Patrones de Traducción Frecuentes

### 5.1 Botones y acciones

| EN | ES | PT-BR |
|----|----|----|
| Save | Guardar | Salvar |
| Cancel | Cancelar | Cancelar |
| Delete / Remove | Eliminar | Excluir |
| Edit | Editar | Editar |
| Create / New | Crear / Nuevo | Criar / Novo |
| Update | Actualizar | Atualizar |
| Confirm | Confirmar | Confirmar |
| Close | Cerrar | Fechar |
| Back | Volver | Voltar |
| Next | Siguiente | Próximo |
| Search | Buscar | Pesquisar |
| Filter | Filtrar | Filtrar |
| Clear | Limpiar | Limpar |
| Show | Mostrar | Mostrar |
| Hide | Ocultar | Ocultar |
| Publish | Publicar | Publicar |
| Validate | Validar | Validar |
| Reject | Rechazar | Rejeitar |
| Download | Descargar | Baixar |
| Upload | Cargar | Carregar |

### 5.2 Mensajes de estado

| EN | ES | PT-BR |
|----|----|----|
| `[X] created successfully.` | `[X] creado/a con éxito.` | `[X] criado/a com sucesso.` |
| `[X] updated successfully.` | `[X] actualizado/a con éxito.` | `[X] atualizado/a com sucesso.` |
| `[X] deleted successfully.` | `[X] eliminado/a con éxito.` | `[X] excluído/a com sucesso.` |
| `[X] not found.` | `[X] no encontrado/a.` | `[X] não encontrado/a.` |
| `Error creating [X].` | `Error al crear [X].` | `Erro ao criar [X].` |
| `Error updating [X].` | `Error al actualizar [X].` | `Erro ao atualizar [X].` |
| `Error deleting [X].` | `Error al eliminar [X].` | `Erro ao excluir [X].` |
| `This action cannot be undone.` | `Esta acción no puede deshacerse.` | `Esta ação não pode ser desfeita.` |
| `Are you sure?` | `¿Estás seguro?` | `Tem certeza?` |
| `Loading...` | `Cargando...` | `Carregando...` |
| `No data available.` | `No hay datos disponibles.` | `Não há dados disponíveis.` |
| `[X] not valid.` | `[X] no válido/a.` | `[X] inválido/a.` |
| `Not allowed.` | `No permitido.` | `Não permitido.` |

### 5.3 Etiquetas de campos comunes

| EN | ES | PT-BR |
|----|----|----|
| Name | Nombre | Nome |
| Code | Código | Código |
| Description | Descripción | Descrição |
| Date | Fecha | Data |
| Start date | Fecha de inicio | Data de início |
| End date | Fecha de fin | Data de fim |
| Date range | Intervalo de fechas | Intervalo de datas |
| Time | Hora | Hora |
| Start time | Hora de inicio | Hora de início |
| End time | Hora de fin | Hora de término |
| Duration | Duración | Duração |
| Status | Estado / Status | Status |
| Type | Tipo | Tipo |
| Version | Versión | Versão |
| Active | Activo | Ativo |
| Inactive | Inactivo | Inativo |
| Enabled | Habilitado | Habilitado |
| Disabled | Deshabilitado | Desativado |
| External ID | ID externo | ID externo |
| Short name | Nombre corto | Nome curto |
| Distance | Distancia | Distância |
| Brand | Marca | Marca |

---

## 6. Errores Comunes a Evitar

### 6.1 Mezcla de idiomas (Portunhol / Spanglish)

❌ `"Pacote rejected com sucesso!"`
✅ `"Pacote rejeitado com sucesso!"`

❌ `"Erro updating parada"`
✅ `"Erro ao atualizar a parada"`

❌ `"New serviço"`
✅ `"Novo serviço"`

❌ `"Pacote comercial not found"`
✅ `"Pacote comercial não encontrado"`

### 6.2 Textos corrompidos por sustitución automática

Señales de alerta: palabras con capitalización extraña, sufijos incorrectos o palabras fusionadas.

❌ `"Adicionared"` → ✅ `"Adicionado"`
❌ `"Removerd"` → ✅ `"Removido"`
❌ `"Semanadays"` → ✅ `"Dias da semana"`
❌ `"Atétal"` → ✅ `"Total"`
❌ `"Publish Desativadoer"` → ✅ `"Publicar"`
❌ `"Idadency not found"` → ✅ `"Agência não encontrada"`
❌ `"Editarion not allowed"` → ✅ `"Edição não permitida"`

### 6.3 Orden de palabras incorrecto

❌ `"Massive Atribuição"` → ✅ `"Atribuição em Massa"`
❌ `"Motorista com sucesso booked on"` → ✅ `"Entrada do motorista registrada com sucesso"`
❌ `"Viagem com sucesso validated!"` → ✅ `"Viagem validada com sucesso!"`

### 6.4 Usar el key-name como valor

❌ `"Pagetitle"` → ✅ `"Título da página"`
❌ `"Activationdisabled"` → ✅ `"Ativação desativada"`
❌ `"Namealreadyexists"` → ✅ `"Nome já existente"`

### 6.5 Falsos cognados ES → PT-BR

| Español | ❌ PT-BR incorrecto | ✅ PT-BR correcto |
|---------|-------------------|-----------------|
| Borrar | Borrar | Excluir / Apagar |
| Desactivado | Desactivado | Desativado |
| Colectivo | Colectivo | Coletivo |
| Nacionalidad | Nacionalidad | Nacionalidade |
| Disponibilidad | Disponibilidad | Disponibilidade |
| Operación diaria | Operação diária | Operação diária ✅ |

---

## 7. Placeholders — Reglas de Manejo

Los placeholders son tokens dinámicos que el sistema sustituye en tiempo de ejecución. **Nunca deben modificarse.**

```
{{driverName}}   →  nombre del conductor
{{count}}        →  número dinámico
{{date}}         →  fecha dinámica
{{from}} {{to}}  →  rango de fechas/horas
```

**Regla:** Los placeholders deben conservarse exactamente como están, incluyendo las llaves `{{ }}` y el nombre interno.

✅ `"O motorista {{driverName}} foi atribuído com sucesso."`
❌ `"O motorista {{nombreConductor}} foi atribuído com sucesso."`
❌ `"O motorista {{driverName foi atribuído com sucesso."` ← placeholder roto

---

## 8. Proceso de Revisión Recomendado

Al recibir un archivo JSON para revisión, verificar en este orden:

1. **Campos vacíos** — ningún valor debe ser `""` o solo espacios
2. **Placeholders rotos** — buscar `{` sin su correspondiente `}`
3. **Textos corrompidos** — palabras con CamelCase raro, sufijos incorrectos, palabras fusionadas
4. **Mezcla de idiomas** — palabras en inglés dentro de frases en PT-BR / ES
5. **Key-names como valor** — valores que repiten el nombre de la clave
6. **Coherencia terminológica** — usar siempre el mismo término para el mismo concepto (ver Glosario)
7. **Naturalidad lingüística** — la frase debe sonar natural para un hablante nativo

---

## 9. Módulos de la Suite y su Alcance

| Módulo (prefijo key) | Área funcional |
|---------------------|---------------|
| `planning` | Planificación de red: líneas, rutas, paradas, viajes, secciones, peajes |
| `rostering` | Escalonamiento de conductores y vehículos, ciclos, escenarios |
| `scheduling` | Programación de turnos y reglas de turno |
| `assignmentManagement` | Asignación diaria de conductores a tareas |
| `dashboard` | Panel principal, información de conductor y vehículo |
| `realtime` | Operación en tiempo real, despacho, estado de viajes |
| `commercialOffer` | Oferta comercial, paquetes, itinerarios, versiones |
| `driverProfile` | Perfil del conductor, datos personales, cualificaciones |
| `vehicleRoster` | Asignación y gestión de vehículos |
| `chargingPoints` | Puntos de carga eléctrica |
| `tenantConfiguration` | Configuración de cliente: reglas, usuarios, grupos de trabajo |
| `task-events` | Tipos de eventos en las tareas (conexión, garaje, viaje vacío…) |
| `absenceManagement` | Gestión de ausencias y solicitudes |
| `swapRequest` | Solicitudes de intercambio de turno |
| `reports` | Generación y descarga de informes |
| `notifications` | Notificaciones del sistema |

