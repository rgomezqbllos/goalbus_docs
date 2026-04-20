---
title: Passando de Scheduling a Rostering
shortTitle: De Scheduling a Rostering
intro: 'Aprenda o que deve estar pronto no Scheduling antes de entrar no Rostering, que informações a alocação de pessoal herda e quais problemas devem ser resolvidos antes de calcular motoristas reais.'
contentType: how-tos
versions:
  - '*'
---

## Confirmando o que deve estar fechado no Scheduling antes de passar para o Rostering

Antes de entrar no Rostering, você precisa verificar que o Scheduling já deixou uma base suficientemente estável. O Rostering não substitui o Scheduling. O Rostering parte do trabalho já construído e decide como atribuí-lo a pessoas reais.

Use este quick start quando você já tiver uma solução de Scheduling calculada e validada e precisar decidir se já pode começar a trabalhar com pessoal real.

Antes de começar, certifique-se de que:
1. Você já criou, calculou e validou o cenário de Scheduling.
2. Você já revisou a oferta de serviço e a coerência geral.
3. Você sabe quais linhas, tipo de dia e solução vai usar como referência.
4. Você tem claro que o Rostering não é o lugar para corrigir uma base estrutural ruim do Scheduling.

Para este quick start, use este caso de referência:

> **Vou confirmar que a solução validada de Scheduling para a linha L1 já está madura o suficiente para passar para Rostering e começar a atribuir trabalho a motoristas reais.**

Para confirmar que o Scheduling já está pronto:
1. Abra o cenário de Scheduling que você vai usar como referência.
2. Verifique se o status é o correto para deixar de tratá-lo como rascunho de trabalho.
3. Verifique se a oferta usada continua sendo a correta.
4. Verifique se a lógica de veículos e a lógica de turnos já foram aplicadas.
5. Confirme que não há incoerências estruturais evidentes na solução.
6. Se você ainda precisar refazer a base de veículos, tempos, serviços ou regras, volte ao Scheduling antes de seguir.
7. Se a solução já estiver estável, continue.

Para o caso de referência, não prossiga até poder afirmar:
1. A solução da L1 já foi calculada.
2. Já foi revisada.
3. Já não precisa de correções estruturais do Scheduling.
4. Já pode ser tratada como base de trabalho para o pessoal.

Quando você terminar esta seção, deverá estar claro se o Scheduling já entregou uma base utilizável para o Rostering.

## Entendendo o que o Rostering herda do Scheduling

Depois de confirmar a base, você precisa entender o que passa do Scheduling para o Rostering. A chave é não pensar que o Rostering começa do zero. O Rostering herda o trabalho já estruturado e, a partir disso, decide qual pessoa real pode assumi-lo.

Antes de começar esta seção, certifique-se de que:
1. Você já identificou a solução de Scheduling que vai usar.
2. Você sabe qual parte dessa solução deve permanecer estável.
3. Você entende que o Rostering trabalha sobre trabalho já construído, não sobre uma oferta sem estrutura.

Para entender o que o Rostering herda:
1. Revise a solução validada de Scheduling.
2. Identifique as tarefas/blocos/estruturas de trabalho que servirão de base.
3. Confirme que a solução já tem uma forma reconhecível do ponto de vista operacional.
4. Tenha em mente que, ao passar para o Rostering, o sistema já não está criando trabalho abstrato, e sim tentando atribuir esse trabalho a pessoas reais.
5. Use esta regra:
   1. Scheduling define **que trabalho existe**.
   2. Rostering define **quem fará esse trabalho**.

Para o caso de referência, pergunte-se:
1. A solução da L1 já tem trabalho claro o suficiente para atribuir?
2. Os blocos de trabalho são reconhecíveis e utilizáveis?
3. O problema restante já é de pessoas e não de estrutura?

Quando você terminar esta seção, deverá entender o que o Rostering herda e o que não deveria ser redefinido ali.

## Distinguindo quais problemas se resolvem no Scheduling e quais no Rostering

Antes de passar definitivamente para a camada de pessoal, você precisa separar muito bem as responsabilidades. Essa distinção é fundamental porque muitos erros aparecem quando se tenta corrigir no Rostering algo que deveria ter sido resolvido antes no Scheduling.

Antes de continuar, certifique-se de que:
1. Você sabe qual cenário de Scheduling será a base.
2. Você entende que o Rostering consome uma solução prévia.
3. Você está preparado para distinguir problemas estruturais de problemas de pessoal.

Para separar corretamente os domínios:
1. Trate como problema de **Scheduling** qualquer assunto relacionado a:
   1. estrutura do serviço,
   2. lógica de frota,
   3. tempos,
   4. regras de veículos,
   5. tipos de turno e construção base.
2. Trate como problema de **Rostering** qualquer assunto relacionado a:
   1. disponibilidade real do motorista,
   2. adscrição a depósito/grupo,
   3. ausências,
   4. inatividades,
   5. cessões/transferências,
   6. elegibilidade real para receber um turno.
3. Se detectar uma incoerência de trabalho que afeta toda a estrutura, volte ao Scheduling.
4. Se detectar uma incoerência de pessoa, resolva no Rostering.

Para o caso de referência:
1. Se o problema é que o trabalho da L1 ficou mal construído, volte ao Scheduling.
2. Se o problema é qual motorista real pode assumir esse trabalho, você está entrando corretamente no Rostering.

Quando você terminar esta seção, deverá conseguir explicar com clareza o que deve ser corrigido antes de passar para pessoal e o que pertence ao próximo módulo.

## Confirmando o que deve estar pronto do lado de pessoal antes de calcular o Rostering

Agora que você já sabe o que o Rostering recebe, você precisa revisar o que deve existir do lado de pessoal para que o próximo cálculo faça sentido. Não basta ter um bom Scheduling se você ainda não tem uma base mínima de pessoas, adscrições e disponibilidade.

Antes de começar esta seção, certifique-se de que:
1. Você já tem uma base válida do Scheduling.
2. Você sabe quais grupos, depósitos ou contextos operacionais afetam as pessoas.
3. Você está pronto para revisar a camada de pessoal.

Para confirmar que a base de pessoal está pronta:
1. Verifique se já existe um coletivo de pessoal que possa receber o trabalho.
2. Revise se as pessoas estão adscritas ao contexto correto quando aplicável.
3. Verifique que você não está entrando no Rostering sem informação mínima de disponibilidade.
4. Revise se já existe a estrutura necessária para:
   1. regras de Rostering,
   2. ausências,
   3. inatividades,
   4. transferências/cessões, quando aplicável.
5. Se você ainda não tiver essa base, não execute o cálculo de pessoal.
6. Se a base já existir ou estiver encaminhada, continue com os próximos quick starts de Rostering.

Para o caso de referência, pergunte-se:
1. Já existe o pessoal que poderá receber a solução da L1?
2. Esse pessoal pertence ao âmbito correto?
3. A base de disponibilidade e adscrição já está minimamente preparada?

Quando você terminar esta seção, deverá estar claro se o lado de pessoal já está pronto para entrar no Rostering.

## Deixando claro o ponto de transição entre Scheduling e Rostering

O último passo é fechar mentalmente a transição. Este quick start não pretende calcular ainda a alocação de pessoal. Pretende deixar claro quando termina o Scheduling e quando começa o Rostering para que você não misture domínios.

Antes de terminar, certifique-se de que:
1. Você já revisou a solução de Scheduling.
2. Você já entendeu o que o Rostering herda.
3. Você já separou problemas estruturais de problemas de pessoal.
4. Você já verificou se existe base mínima de pessoal.

Para fechar corretamente a transição:
1. Trate a solução validada do Scheduling como entrada formal do Rostering.
2. Não continue alterando essa base a menos que detecte um problema estrutural real.
3. Use os próximos quick starts para preparar:
   1. regras de Rostering,
   2. ausências e inatividades,
   3. transferências, cessões e mudanças de adscrição.
4. Considere que o objetivo muda a partir daqui:
   1. não se trata mais de construir trabalho,
   2. agora se trata de atribuí-lo a pessoas reais.
5. Se você puder afirmar isso com clareza, a transição está bem feita.

Para o caso de referência, finalize este quick start apenas quando puder afirmar:
1. O Scheduling já deixou uma solução estável da L1.
2. O próximo problema já não é estrutural, e sim de alocação de pessoal.
3. Você já pode entrar na camada de regras de Rostering.

Quando você terminar esta seção, deverá ter uma transição clara e controlada entre Scheduling e Rostering.

## Leituras adicionais

- [Carregando e gerenciando motoristas](P20_Carregando_e_gerenciando_motoristas.md)

