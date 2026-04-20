---
title: Revisando conflitos, cobertura e viabilidade de pessoal
shortTitle: Conflitos e cobertura
intro: 'Aprenda a revisar a solução de Rostering após o cálculo, identificar conflitos de cobertura, distinguir se o problema vem de regras, disponibilidade ou adscrição e decidir o que corrigir antes de validar.'
contentType: how-tos
versions:
  - '*'
---

## Entendendo o que revisar após o cálculo de Rostering

Depois de executar o primeiro cálculo de Rostering, o próximo passo não é validar imediatamente a solução. Primeiro você precisa revisar se a alocação é realmente viável. O objetivo é verificar se o sistema conseguiu cobrir o trabalho com pessoas reais respeitando restrições trabalhistas, disponibilidade e contexto operacional.

Use este quick start quando você já executou o cálculo de Rostering e precisa analisar se a solução pode ser considerada completa, parcial ou conflituosa.

Antes de começar, certifique-se de que:
1. Você já executou o primeiro cálculo de Rostering no P25.
2. Você sabe qual solução de Scheduling foi a entrada.
3. Você sabe qual coletivo de motoristas participou.
4. Você está pronto para analisar a solução antes de validá-la.

Para este quick start, use este caso de referência:

> **Vou revisar a solução de Rostering da linha L1 para verificar cobertura, identificar conflitos de alocação e confirmar viabilidade antes de validar.**

Para entender o que revisar:
1. Trate a revisão como diagnóstico, não como aprovação automática.
2. Revise sempre três dimensões:
   1. **cobertura**,
   2. **conflitos**,
   3. **viabilidade geral**.
3. Não considere uma solução boa apenas porque o motor terminou.
4. Considere que uma solução pode:
   1. cobrir todo o trabalho,
   2. cobrir parcialmente,
   3. ou produzir conflitos que exigem voltar a regras, disponibilidade ou adscrição.

Quando você terminar esta seção, deverá ter claro o que significa revisar uma solução de pessoal antes de validar.

## Revisando a cobertura do trabalho atribuído

A primeira pergunta é simples: **todo o trabalho ficou coberto?**. Aqui você ainda não está diagnosticando por que algo falhou, e sim medindo se o sistema conseguiu atribuir pessoas ao trabalho herdado do Scheduling.

Antes de começar esta seção, certifique-se de que:
1. Você tem a solução calculada visível.
2. Você sabe qual volume total de trabalho esperava cobrir.
3. Você consegue revisar o resultado por linha, grupo ou coletivo.

Para revisar a cobertura:
1. Abra a solução calculada de Rostering.
2. Revise a visão geral do resultado.
3. Identifique:
   1. tarefas cobertas,
   2. tarefas não cobertas,
   3. atribuições parciais, se existirem.
4. Use os KPIs visíveis para apoiar a análise.
ref: P26_Imagen1.png | compact
4. Verifique se a cobertura é completa ou tem lacunas com os KPIs diários.
ref: P26_Imagen2.png | full
5. Se o sistema mostrar resumos de cobertura (KPIs de motoristas), revise-os.
ref: P26_Imagen3.png | compact
6. Se a cobertura não for completa, não valide ainda.
7. Anote mentalmente onde estão as lacunas.

Para o caso de referência, pergunte-se:
1. O trabalho da L1 ficou coberto por completo?
2. Há dias ou faixas com lacunas?
3. O problema afeta a linha toda ou apenas parte do serviço?

Quando você terminar esta seção, deverá saber se a solução cobre todo o trabalho ou se há tarefas sem atribuição.

## Detectando conflitos e lendo a causa provável

Depois de revisar a cobertura, você precisa identificar os conflitos. Um conflito não significa automaticamente falta de pessoal. Pode indicar regra muito restritiva, adscrição incorreta ou ausência/cessão mal modelada.

Antes de começar esta seção, certifique-se de que:
1. Você já identificou se existem tarefas não cobertas.
2. Você está disposto a diferenciar causas em vez de corrigir por intuição.
3. Você sabe qual parte da solução revisar primeiro.

Para revisar conflitos de forma útil:
1. Revise tarefas que ficaram sem atribuição ou com problema.
2. Verifique se o sistema mostra mensagens/indicadores/conflitos associados.
3. Classifique a causa provável em um destes grupos:
   1. **regras muito restritivas**,
   2. **disponibilidade insuficiente**,
   3. **adscrição ou habilitações incorretas**,
   4. **estrutura herdada do Scheduling**.
4. Se afetar muitas pessoas do mesmo coletivo, revise primeiro regras e adscrição.
5. Se afetar casos individuais, revise primeiro disponibilidade, ausência ou cessão.
6. Se o problema parecer vir do trabalho herdado, considere voltar ao Scheduling.

Para o caso de referência, pergunte-se:
1. A tarefa ficou sem cobertura por falta de pessoa disponível?
2. A pessoa existe, mas não está habilitada/adscrita ao contexto correto?
3. Uma regra de Rostering bloqueou uma atribuição possível?
4. O problema não é pessoal, mas trabalho herdado?

Quando você terminar esta seção, deverá ter uma hipótese razoável sobre a causa dos principais conflitos.

## Revisando a viabilidade geral da solução

Uma solução pode estar quase coberta e ainda assim não ser boa. Por isso, além de cobertura e conflitos, você precisa revisar a **viabilidade geral**. A pergunta não é só se o sistema atribuiu pessoas, mas se a atribuição faz sentido operacional e humano.

Antes de continuar, certifique-se de que:
1. Você já revisou a cobertura.
2. Você já identificou conflitos principais.
3. Você está pronto para avaliar qualidade, não apenas quantidade.

Para revisar viabilidade geral:
1. Verifique se a distribuição do trabalho parece razoável.
2. Verifique sinais de desequilíbrio claro entre pessoas ou grupos.
3. Observe se a solução parece cumprir:
   1. descansos,
   2. limites,
   3. critérios básicos de equidade,
   4. consistência operacional.
4. Se a solução cobre o trabalho mas de forma muito forçada, não valide ainda.
5. Se o resultado parecer operacional, equilibrado e explicável, avance.

Para o caso de referência, pergunte-se:
1. A cobertura foi atingida de forma razoável ou forçada?
2. A atribuição parece equilibrada entre motoristas?
3. A solução parece aplicável no mundo real ou apenas no papel?

Quando você terminar esta seção, deverá ter uma leitura mais completa sobre se a solução merece avançar ou precisa de correção.

## Decidindo o que corrigir antes de validar

O último passo é converter a análise em decisão prática. O objetivo não é corrigir tudo de uma vez, mas identificar a camada correta de correção.

Antes de terminar, certifique-se de que:
1. Você revisou cobertura.
2. Você analisou conflitos.
3. Você avaliou viabilidade geral.
4. Você sabe se a solução pode avançar.

Para decidir o que corrigir:
1. Se o problema principal é de **regras**, volte ao P22.
2. Se o problema principal é de **ausências/inatividades/disponibilidade**, volte ao P23.
3. Se o problema principal é de **cessão/transferência/adscrição**, volte ao P24 ou P21.
4. Se o problema principal é do trabalho herdado, volte ao Scheduling.
5. Se a solução for suficientemente completa e viável, prepare para validação.
6. Não valide uma solução só porque “quase funciona”. Valide quando você entende por que funciona e por que conflitos restantes são aceitáveis ou resolvidos.

Para o caso de referência, finalize este quick start apenas quando puder afirmar:
1. A solução da L1 já é sólida o suficiente para validar.
2. Você sabe exatamente que camada deve corrigir antes de recalcular.

Quando você terminar esta seção, deverá ter uma leitura clara de cobertura, conflitos e viabilidade, e uma decisão prática sobre o próximo passo.

## Leituras adicionais

- [Validando e consolidando a solução de Rostering](P27_Validando_e_consolidando_a_solucao_de_rostering.md)

