---
title: Definindo versões de tempo e tempos de percurso para a operação
shortTitle: Versões e tempos
intro: 'Aprenda a criar versões de tempo, definir tempos de percurso e permanência por tipo de dia e faixa horária, e deixar uma referência temporal confiável antes de criar ou ajustar serviços no GoalBus.'
contentType: how-tos
versions:
  - '*'
---

## Criando a versão de tempo que o seu caso vai usar

Antes de definir tempos de percurso, você precisa criar uma **versão de tempo**. No GoalBus, uma versão não é apenas um rótulo: é a biblioteca de tempos que agrupa a lógica temporal que será aplicada a rotas específicas e a tipos de dia específicos. Isso é importante porque uma segunda-feira de manhã não se comporta como um domingo de manhã, e o sistema não deveria reutilizar um único conjunto de tempos para o ano inteiro.

Use este quick start quando você já tiver uma linha e suas rotas definidas e precisar construir a base temporal que depois servirá para calcular viagens, validar durações e comparar desvios em relação ao padrão.

Antes de começar, certifique-se de que:
1. Você já preparou a rede mestra no P6.
2. Você já revisou a rede operacional no P7.
3. Você já configurou a base de calendário de tipos de dia no P2.
4. Você já validou o ano operacional no P3.
5. Você sabe qual linha, quais rotas e qual tipo de dia vai usar como referência.

Para este quick start, use este caso de referência:

> **Vou criar uma versão de tempo para a linha L1 em dias úteis e usá-la como referência temporal antes de criar ou ajustar serviços.**

Para criar a versão de tempo do seu caso:
1. No GoalBus, abra a **visão de Rotas** da linha que você vai usar como referência.
2. Selecione o ícone/opção de **Gestão de tempos de viagem e parada**.
ref: P9_Imagen1.png | compact
3. Na parte superior da visão, crie uma nova versão selecionando **Novo conjunto de horários**.
ref: P9_Imagen2.png | compact
4. Defina um **nome** claro para a versão.
5. Adicione uma **descrição** para distinguir o contexto operacional.
6. Selecione os **tipos de dia** aos quais a versão se aplicará, por exemplo **Dias úteis**.
7. Vincule as **variações de rota** ou sequências específicas que farão parte dessa versão temporal.
8. Salve a versão.
ref: P9_Imagen3.png | compact
9. Confirme que a versão já está disponível como referência temporal para essa linha.

Para o caso de referência, uma versão válida poderia se chamar:
- **Dias úteis de inverno**
- **L1 base dia útil**

Quando você terminar esta seção, deverá ter criada uma versão de tempo que o sistema poderá usar como referência temporal para os serviços dessa linha, semelhante à imagem a seguir.
ref: P9_Imagen4.png | full

## Definindo tempos de percurso entre paradas principais

Depois de criar a versão, você precisa inserir os **tempos de percurso**. No GoalBus, esses tempos são definidos principalmente entre **paradas principais** ou **pontos temporais**, e não entre todas as paradas intermediárias. Terminais são principais por padrão e, a partir daí, constrói-se a lógica temporal que alimentará os serviços.

Além disso, o GoalBus não trabalha com um único valor por segmento. O motor usa uma lógica de **mínimo, ótimo e máximo** para dar flexibilidade controlada ao cálculo:
1. **Mínimo**: o tempo mais rápido possível.
2. **Ótimo**: o tempo-alvo para o qual o motor tende.
3. **Máximo**: o tempo mais lento aceitável.

Antes de começar esta seção, certifique-se de que:
1. Você já criou a versão de tempo.
2. Você sabe quais paradas principais vai usar como referência.
3. Você identificou qual sentido/direção quer configurar primeiro.

Para definir os tempos de percurso do seu caso:
1. Dentro da grade temporal, selecione o **segmento** entre duas paradas principais.
ref: P9_Imagen5.png | full
2. Crie uma ou mais **faixas horárias** para refletir a realidade operacional.
3. Para cada faixa, informe:
   1. o tempo **mínimo**,
   2. o tempo **ótimo**,
   3. o tempo **máximo**.
ref: P9_Imagen6.png | compact
4. Salve o segmento.
5. Repita para o próximo segmento principal.
6. Quando terminar um sentido, repita a mesma lógica para o sentido contrário.

As faixas criadas não devem ter lacunas nem sobreposições entre si. Se houver, não será possível salvar os tempos.

Para o caso de referência, uma lógica básica poderia ser:
1. **Terminal Norte → Centro**
   1. 07:00–09:00
      1. Mínimo: 12 min
      2. Ótimo: 15 min
      3. Máximo: 18 min
   2. 09:00–22:00
      1. Mínimo: 5 min
      2. Ótimo: 5 min
      3. Máximo: 5 min
   3. 22:00–06:00
      1. Mínimo: 8 min
      2. Ótimo: 10 min
      3. Máximo: 12 min
2. **Centro → Hospital**
3. **Hospital → Universidade**
4. **Universidade → Terminal Sul**

Quando você terminar esta seção, deverá ter definidos tempos de condução elásticos entre os principais pontos temporais da rota.

## Definindo tempos de permanência para regulação e recuperação

Além do tempo de condução, o GoalBus precisa saber quanto tempo um veículo pode permanecer em uma parada principal. Esses **tempos de escala** são importantes porque permitem regular a saída, absorver chegadas antecipadas e deixar margem de recuperação em terminais ou pontos de conexão.

Antes de começar esta seção, certifique-se de que:
1. Você já definiu tempos de percurso entre os principais segmentos.
2. Você sabe quais terminais ou pontos importantes precisam de regulação.
3. Você identificou onde é necessária uma margem operacional real.

Para definir os tempos de escala:
1. Na grade temporal, selecione a **coluna** de uma parada principal.
ref: P9_Imagen7.png | full
2. Escolha um terminal, cabeceira ou ponto importante de conexão.
3. Defina:
   1. **Mínimo** como tempo obrigatório de espera.
   2. **Máximo** como margem permitida para regulação ou sincronização.
4. Salve a configuração.
5. Repita para outras paradas principais em que você precise de permanência controlada.

Para o caso de referência, uma lógica possível seria:
1. **Terminal Norte**
   1. Mínimo: 4 min
   2. Máximo: 10 min
2. **Terminal Sul**
   1. Mínimo: 5 min
   2. Máximo: 12 min

Quando você terminar esta seção, deverá ter definidos os limites que o motor poderá usar para recuperar ou regular sem deformar a lógica do horário.

## Revisando faixas horárias, visão ampliada e consistência visual

Depois de ter tempos de percurso e permanência, você precisa revisar se a grade reflete uma lógica realista. O GoalBus inclui ajudas visuais para detectar erros quando você gerencia muitos pontos, muitas faixas ou várias rotas.

Antes de continuar, certifique-se de que:
1. Você já configurou pelo menos uma faixa horária.
2. Você já inseriu valores mínimo, ótimo e máximo.
3. Você já adicionou tempos de permanência nos pontos relevantes.

Para revisar visualmente a consistência da configuração:
1. Revise a grade e confirme que cada segmento principal tem uma faixa horária válida.
2. Use as ajudas visuais disponíveis para detectar valores anômalos.
3. Verifique se os horários de pico mostram tempos mais altos do que os de vale.
4. Amplie a visão se precisar ver mais detalhe ou mais paradas intermediárias.
5. Corrija qualquer valor anômalo diretamente na visão ou no painel de edição.
6. Repita a revisão até que a lógica temporal reflita uma operação crível.

Para o caso de referência, pergunte-se:
1. O horário de pico aparece com tempos mais altos do que a noite?
2. Os tempos mínimo, ótimo e máximo mantêm uma relação lógica?
3. Os terminais têm margem de regulação realista?
4. A grade já representa uma jornada operativa completa?

Quando você terminar esta seção, deverá ter uma base temporal revisada visualmente e livre de incoerências importantes.

## Aplicando a versão de tempo como referência para serviços

O objetivo final deste quick start não é apenas criar dados temporais, mas deixar uma referência que depois possa ser usada ao criar ou modificar serviços. Cada viagem deve ser medida em relação a uma **versão temporal de referência**, e essa referência é usada automaticamente quando você cria novas viagens ou altera a rota de uma viagem. Isso também permite detectar desvios se uma viagem foi importada ou modificada fora do padrão.

Antes de terminar, certifique-se de que:
1. Você já criou uma versão temporal válida.
2. Você já definiu tempos de percurso e permanência.
3. Você já revisou a consistência da grade.
4. Você sabe qual linha e qual caso vai usar para criar serviços.

Para verificar que a sua base temporal já está pronta para os serviços:
1. Revise a versão de tempo que você acabou de criar.
2. Confirme que ela está vinculada ao tipo de dia correto.
3. Confirme que inclui as rotas/variações que você vai usar.
4. Verifique se essa versão já poderia atuar como referência temporal para:
   1. criar novas viagens,
   2. recalcular horários de chegada e saída,
   3. auditar discrepâncias em relação ao padrão.
5. Se a resposta for sim, continue com o próximo quick start.
6. Se a resposta for não, volte e corrija a versão ou os tempos antes de seguir.

Quando você terminar esta seção, deverá ser capaz de afirmar que a linha já tem uma versão temporal de referência suficiente para criar serviços de forma coerente.

## Leituras adicionais

- [Criando a oferta de serviço base com viagens e horários](P10_Criando_a_oferta_de_servico_base_com_viagens_e_horarios.md)

