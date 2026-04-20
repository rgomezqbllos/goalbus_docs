---
title: Atribuindo tarefas lógicas a veículos reais
shortTitle: Atribuição de veículos
intro: 'Aprenda a atribuir as tarefas lógicas de material obtidas no Scheduling aos veículos reais carregados ou criados previamente.'
contentType: how-tos
versions:
  - '*'
---

## Carregando ou criando os veículos reais que serão usados na atribuição

Depois que você tiver as soluções de Scheduling e de Rostering validadas e publicadas (a de Rostering não é indispensável), você pode criar ou carregar os veículos reais que serão usados para atribuir as tarefas lógicas calculadas na solução de Scheduling de veículos.

Use este quick start quando você já executou o cálculo de Scheduling e (opcionalmente) Rostering e precisa iniciar a atribuição de veículos.

Antes de começar, certifique-se de que:
1. Você já publicou a solução de Scheduling no P16.
2. Você já validou e consolidou a solução de Rostering no P27.

Para este quick start, use este caso de referência:

> **Vou atribuir as tarefas lógicas calculadas no Scheduling de veículos às placas dos veículos carregados ou criados.**

Para carregar ou criar novas placas:
1. Abra **Configuração** > **Veículos** > **Veículos registrados**.
ref: P28_Imagen1.png | compact
2. Se quiser criar várias placas ao mesmo tempo, a melhor opção é importar.
3. Selecione o botão de importação de placas.
ref: P28_Imagen2.png | compact
4. Carregue o CSV com os novos veículos seguindo as instruções.
ref: P28_Imagen3.png | compact
5. Se não houver erros, os veículos ficarão registrados.
6. Se preferir criar um a um, selecione **Novo veículo**.
ref: P28_Imagen4.png | compact
7. Na janela, preencha:
   1. **Placa** do veículo.
   2. **Depósito** ao qual pertence.
   3. **Modelo** do veículo.
   4. **Ano de fabricação** (opcional).
   5. **Data de início de operação** a partir da qual será possível atribuir tarefas.
ref: P28_Imagen5.png | compact
8. Salve as alterações.
9. O registro criado aparecerá na lista de veículos.

Para o caso de referência, não prossiga até poder afirmar:
1. Todas as placas necessárias estão carregadas ou criadas.
2. Os veículos estão associados ao **modelo** correspondente.
3. Você não precisa de mais veículos além dos carregados/criados.

Quando você terminar esta seção, deverá ter todas as placas necessárias para realizar a atribuição.

Para o caso de referência, você pode criar placas com um formato como:
- **001-LFX**
- **002-LFX**
...
- **NNN-LFX**

## Atribuindo tarefas lógicas do Scheduling a veículos reais

Depois que todos os veículos necessários estiverem carregados/criados, você pode iniciar a atribuição.

Antes de começar esta seção, certifique-se de que:
1. Você já tem todos os veículos no sistema.
2. Você sabe qual critério quer usar na atribuição.
3. Você tem uma solução de Rostering validada.

Para começar a atribuição de veículos:
1. Abra o módulo de **Atribuição de veículos**.
ref: P28_Imagen6.png | compact
2. Revise na barra superior as tarefas sem atribuição.
ref: P28_Imagen7.png | compact
3. No painel direito aparecerão as tarefas para atribuir manualmente.
ref: P28_Imagen8.png
4. Ao selecionar **atribuir tarefa**, o sistema mostrará os veículos disponíveis (sem tarefas ou sem sobreposições).
Ref: P28_Imagen9.png
5. Atribua as tarefas aos veículos correspondentes.
6. Ao terminar, você pode **Confirmar** para **publicar** as mudanças.
ref: P28_Imagen10.png
7. Se ainda houver tarefas sem atribuição ou você não quiser fazer tudo manualmente, use **Otimizar atribuição de frota**.
ref: P28_Imagen11.png
8. Repita o processo para todos os dias necessários.

Para o caso de referência, garanta que:
1. Todas as tarefas foram atribuídas a um veículo.
2. Há coerência nas atribuições.
3. Todos os dias necessários estão cobertos.

Quando você terminar esta seção, deverá ter uma solução de veículos atribuída.

