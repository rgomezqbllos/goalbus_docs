---
title: Revisão de conflitos, cobertura e viabilidade do pessoal
shortTitle: Conflitos e cobertura
intro: Saiba como rever a solução Alocação após o cálculo, identificar conflitos de
  cobertura, distinguir se o problema vem de regras, disponibilidade ou destacamento,
  e decidir o que corrigir antes de validar a atribuição.
contentType: how-tos
versions:
- '*'
---
## Compreender o que você deve rever após o cálculo Alocação

Após executar o primeiro cálculo Alocação, o próximo passo não é validar imediatamente a solução. Primeiro, você precisa verificar se a atribuição é realmente viável. Nesta etapa, o objetivo é verificar se o sistema conseguiu cobrir o trabalho com pessoas reais respeitando restrições de trabalho, disponibilidade e contexto operacional.

Use este início rápido quando você já executou o cálculo Alocação e precisa analisar se a solução pode ser considerada completa, parcial ou conflitante.

Antes de começar, certifique-se de que:
1. Você já executou o primeiro cálculo Alocação no P25.
2. Você sabe qual a solução do Programação agiu como uma entrada.
3. Você já está claro qual grupo de Motoristas participou no cálculo.
4. Está pronto para analisar a solução antes de a validar.

Para este início rápido, use este caso de referência:

> **Vou rever a solução Alocação no Linha L1 para verificar se o trabalho foi coberto, se há conflitos de atribuição e se o resultado é viável antes de validar.**

Para entender o que revisar após o cálculo:
1. Trata a revisão como uma fase diagnóstica, não uma aprovação automática.
2. Verifique sempre três dimensões:
   1. **cobertura**,
   2. **conflitos**,
   3. **viabilidade geral**.
3. Não tome uma solução para garantido apenas porque o motor terminou o cálculo.
4. Considera que uma solução pode:
   1. cobrir todo o trabalho,
   2. Cubra-o parcialmente,
   3. ou produzir conflitos que obriguem o retorno às regras, disponibilidade ou destacamento.

Quando você terminar este Seção, você deve ser claro sobre o que significa rever uma solução de pessoal e quais perguntas responder antes de validar.

## Revisão da cobertura do trabalho atribuído

A primeira pergunta a responder é simples: **Está tudo coberto?**. Ainda não é uma questão de por que algo falhou, mas de medir se o sistema conseguiu atribuir pessoas para trabalhar herdadas de Programação.

Antes de iniciar este Seção, certifique-se de que:
1. Você já tem a solução calculada visível.
2. Sabes o trabalho total que esperavas cobrir.
3. Agora você pode rever o resultado por Linha, grupo ou coletivo.

Para rever a cobertura:
1. Abre a solução calculada Alocação.
2. Verifique a visão geral do resultado.
3. Identificar:
   1. revestido Tarefas,
   2. Descoberto Tarefas,
   3. e designações parciais, se houver.
4. Para fazer isso, sirva-se com os KPIs visíveis na solução.
ref: P26_Imagen1.png | compact
4. Verifique se a cobertura está completa ou se há lacunas graças aos KPIs diários visíveis.
ref: P26_Imagen2.png | full
5. Se o sistema exibir contadores ou resumos de cobertura (KPIs de Motoristas), verifique-os.
ref: P26_Imagen3.png | compact
6. Se a cobertura não estiver completa, não valide a solução ainda.
7. Marcar mentalmente onde as lacunas devem ser analisadas mais tarde.

Para o caso de referência, pergunte-se:
1. O trabalho da L1 estava completamente coberto?
2. Há dias ou vagas com buracos?
3. O problema afeta toda a Linha ou apenas parte do serviço?

Quando você terminar este Seção, você deve saber se a solução cobre todo o trabalho ou se não estão atribuídos Tarefas.

## Detetar conflitos e ler sua causa provável

Depois de rever a cobertura, você precisa identificar conflitos. Um conflito não significa automaticamente que há uma falta de pessoal. Isso pode significar que uma regra é muito restritiva, que uma pessoa é mal colocada, ou que um Ausência ou atribuição foi incorrectamente modelado.

Antes de iniciar este Seção, certifique-se de que:
1. Você já identificou se há Tarefas não encontrado.
2. Você já está disposto a diferenciar causas em vez de corrigir por intuição.
3. Sabe qual é a parte da solução para verificar primeiro.

Revisão útil dos conflitos:
1. Verifique o Tarefas que permaneceu inalterado ou em dificuldade.
2. Veja se o sistema mostra mensagens, indicadores ou conflitos associados.
3. Tente classificar a causa provável em um destes grupos:
   1. **regras demasiado restritivas**,
   2. **disponibilidade inadequada**,
   3. **destacamento incorreto ou habilitação**,
   4. **estrutura herdada de Programação**.
4. Se o conflito parece afetar muitas pessoas no mesmo grupo, revise as regras e o destacamento primeiro.
5. Se o conflito afetar casos individuais, verifique a disponibilidade, Ausência ou atribuição primeiro.
6. Se o problema parece vir do trabalho herdado, considere voltar para Programação.

Para o caso de referência, faça-se estas perguntas:
1. O Tarefa não estava coberto porque não havia ninguém disponível?
2. A pessoa existia, mas não estava habilitada ou ligada ao contexto correto?
3. A regra Alocação bloqueou uma atribuição que parecia possível?
4. O problema não é pessoal, mas trabalho herdado?

Quando você terminar este Seção, você deve ter uma suposição razoável sobre a causa dos grandes conflitos.

## Revisão da viabilidade global da solução

Uma solução pode ser quase coberta e ainda não boa. Assim, além de cobertura e conflitos, você precisa rever o **viabilidade geral**. Aqui a questão não é apenas se o sistema atribuído pessoas, mas se a atribuição resultante faz sentido operacional e humano.

Antes de continuar, certifique-se de que:
1. Verificou a cobertura.
2. Já identificaram grandes conflitos.
3. Você está pronto para valorizar a qualidade, não apenas a quantidade.

Revisar a viabilidade global:
1. Verifique se a distribuição do trabalho parece razoável.
2. Verifique se há sinais de desequilíbrio claro entre pessoas ou grupos.
3. Observa se a solução parece estar em conformidade com:
   1. quebras,
   2. limites,
   3. Critérios básicos de equidade,
   4. e a coerência operacional.
4. Se a solução cobre o trabalho, mas o faz com muita força, não o valide ainda.
5. Se o resultado parecer operacional, equilibrado e explicável, continua na direcção da decisão final.

Para o caso de referência, pergunte-se:
1. A cobertura foi razoavelmente alcançada ou demasiado forçada?
2. A atribuição parece equilibrada entre Motoristas?
3. Será que a solução parece ser aplicável no mundo real ou apenas válida no papel?

Quando você terminar este Seção, você deve ter uma leitura mais completa de se a solução merece avançar ou se precisa de correção.

## Decidir o que corrigir antes de validar

O último passo é transformar a análise em uma decisão prática. Aqui o objetivo não é corrigir tudo de uma só vez, mas identificar a próxima camada correta de correção.

Antes de terminar, certifique-se de que:
1. Verificou a cobertura.
2. Já analisou conflitos.
3. Já valorizaste a viabilidade global.
4. Sabe se a solução pode avançar ou não.

Para decidir o que corrigir antes de validar:
1. Se o problema principal é **regras**, volte para o P22.
2. Se o problema principal é **Ausências, inatividade ou disponibilidade**, volte para o P23.
3. Se o problema principal for **atribuição, transferência ou destacamento**, retorne para P24 ou P21, conforme apropriado.
4. Se o problema principal é o trabalho herdado, volte para Programação.
5. Se a solução for suficientemente completa e viável, prepare-a para validação.
6. Não convalide uma solução apenas porque ela quase funciona.Convalide-a quando você entende por que funciona e por que os conflitos restantes são aceitáveis ou resolvidos.

Para o caso de referência, termine este início rápido apenas quando você puder afirmar uma destas duas coisas:
1. A solução L1 é sólida o suficiente para ser Validado.
2. Você sabe exatamente que camada você precisa corrigir antes de recalcular.

Quando você terminar este Seção, você deve ter uma leitura clara de cobertura, conflitos e viabilidade, e uma decisão prática sobre o próximo passo.

## Lecturas adicionais

- [Validação e consolidação da solução Alocação](P27_Validação_E_Consolidação_Da_Solução_Alocação.md)
