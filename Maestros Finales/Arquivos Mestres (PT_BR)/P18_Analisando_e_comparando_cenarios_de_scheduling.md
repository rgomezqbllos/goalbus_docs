---
title: Analisando e comparando cenários de Scheduling
shortTitle: Comparar cenários
intro: 'Aprenda a comparar cenários de Scheduling, revisar KPIs e diferenças operacionais e decidir com critério qual solução deve se manter como referência ou avançar para uma nova iteração.'
contentType: how-tos
versions:
  - '*'
---

## Identificando quais cenários você vai comparar

Depois de criar, calcular, validar e publicar cenários, o próximo passo natural é compará-los. Comparar cenários não é apenas “qual ficou melhor” de forma intuitiva. É revisar o que mudou, qual impacto isso teve e se a nova iteração realmente melhora a solução de referência.

Use este quick start quando você já tiver pelo menos dois cenários comparáveis (por exemplo, uma solução publicada e uma nova iteração calculada) e precisar decidir qual deve permanecer como referência operacional ou qual merece avançar no ciclo de vida.

Antes de começar, certifique-se de que:
1. Você já criou e calculou pelo menos um cenário base.
2. Você tem uma segunda versão/iteração/variante que quer comparar.
3. Você sabe qual linha, tipo de dia e contexto operacional está revisando.
4. Você tem claro qual é a versão de referência atual.

Para este quick start, use este caso de referência:

> **Vou comparar o cenário publicado da linha L1 com uma nova iteração calculada para decidir se a nova solução realmente melhora a programação atual.**

Para identificar corretamente os cenários a comparar:
1. No GoalBus, abra o módulo de **Cenários de planejamento**.
ref: P18_Imagen1.png | compact
2. Localize o cenário que atua como referência atual.
3. Localize o cenário novo ou a iteração que você quer avaliar.
4. Verifique se ambos pertencem ao mesmo contexto funcional:
   1. mesma linha (ou conjunto comparável de linhas),
   2. mesmo tipo de dia,
   3. mesma lógica operacional geral.
5. Revise nome, descrição e status de cada cenário.
6. Confirme qual é:
   1. a versão vigente/publicada,
   2. e qual é a nova proposta.
7. Se os cenários não forem comparáveis, não prossiga até corrigir isso.

Para o caso de referência, garanta que:
1. Ambos os cenários pertencem à linha L1.
2. Ambos são de dias úteis (ou o mesmo contexto temporal).
3. Um é a referência e o outro é a alternativa.

Quando você terminar esta seção, deverá ter claramente identificados os cenários que vai comparar e o papel de cada um.

## Revisando KPIs, volume de trabalho e equilíbrio geral

Depois de selecionar os cenários, comece com uma comparação de alto nível. O objetivo é revisar indicadores gerais antes de entrar em detalhes de tarefas ou regras. Isso ajuda a detectar se a nova solução está realmente mais equilibrada ou apenas diferente.

Antes de começar esta seção, certifique-se de que:
1. Você sabe quais dois cenários vai comparar.
2. Você identificou qual é a referência.
3. Você tem acesso aos KPIs visíveis ou a métricas comparáveis.

Para revisar os KPIs gerais:
1. Abra o primeiro cenário e revise os KPIs principais.
2. Anote ou memorize ao menos:
   1. volume total de trabalho,
   2. número de tarefas,
   3. tempo total,
   4. distância/magnitude relevante,
   5. qualquer outro indicador visível.
3. Abra o segundo cenário e revise os mesmos KPIs.
4. Compare se a nova iteração:
   1. reduz complexidade desnecessária,
   2. melhora o equilíbrio,
   3. ou apenas desloca o problema.
5. Evite aprovar uma iteração apenas porque os números mudaram. O importante é o sentido operacional.

Para o caso de referência, pergunte-se:
1. A nova iteração reduz tarefas desnecessárias?
2. O equilíbrio geral parece mais razoável?
3. O volume total continua coerente com a oferta validada?
4. A melhoria é real ou só redistribuição sem benefício claro?

Quando você terminar esta seção, deverá ter uma visão global sobre se a nova solução merece uma revisão mais profunda.

## Comparando o impacto em veículos e em turnos

Depois de revisar os KPIs globais, você precisa descer para a lógica funcional separando:
1. impacto em **veículos**,
2. impacto em **turnos**.

Isso é importante porque uma iteração pode melhorar a lógica de frota e piorar a lógica de turnos, ou o contrário.

Antes de começar esta seção, certifique-se de que:
1. Você já revisou os KPIs gerais.
2. Você sabe quais regras de veículos e de turnos estão envolvidas na mudança.
3. Você sabe qual era o objetivo da iteração.

Para comparar o impacto em veículos:
1. Revise como a solução se comporta em relação a:
   1. frota utilizada,
   2. compatibilidades,
   3. saídas de depósitos/parkings,
   4. quilometragem não produtiva, se visível ou dedutível.
2. Verifique se a iteração melhora a coerência entre linha, frota e infraestrutura.
3. Detecte se o novo cenário força soluções menos realistas do que antes.

Para comparar o impacto em turnos:
1. Revise como as tarefas/blocos de trabalho são construídos.
2. Verifique se os tipos de turno ativos continuam fazendo sentido.
3. Observe se a nova solução:
   1. melhora a clareza do trabalho,
   2. piora a estrutura,
   3. ou introduz rigidez desnecessária.
4. Relacione a mudança com o modelo de regras de turnos usado.

Para o caso de referência, pergunte-se:
1. A nova iteração melhora a lógica de veículos sem castigar a lógica de turnos?
2. Melhora a lógica de turnos sem piorar a frota?
3. Qual dimensão melhora ou piora?
4. O resultado global é mais robusto ou apenas mais diferente?

Quando você terminar esta seção, deverá entender onde cada cenário melhora e onde piora.

## Decidindo se a nova iteração traz valor real

Agora você precisa transformar a comparação em decisão. Nem todo cenário novo merece avançar. Às vezes, a iteração serve apenas como aprendizado interno e a melhor decisão é manter a versão vigente. Outras vezes, a melhoria é clara o suficiente para justificar um novo ciclo de validação e publicação.

Antes de continuar, certifique-se de que:
1. Você já comparou KPIs gerais.
2. Você já revisou impacto em veículos e em turnos.
3. Você sabe qual era o objetivo original da iteração.

Para decidir se a iteração traz valor real:
1. Resuma qual era o propósito do novo cenário.
2. Verifique se esse objetivo foi atingido de forma clara.
3. Pergunte-se se a melhoria é:
   1. visível na operação,
   2. tecnicamente defensável,
   3. estável o suficiente para avançar.
4. Se a iteração melhorar claramente a referência, prepare-a para validação/publicação conforme necessário.
5. Se não melhorar, mantenha como aprendizado e preserve a versão atual.
6. Não promova uma iteração só porque é mais nova. Promova apenas se for melhor.

Para o caso de referência, finalize esta seção apenas quando puder afirmar uma destas:
1. A nova iteração da L1 melhora claramente a solução publicada e merece avançar.
2. A solução publicada continua sendo a melhor referência e a iteração fica apenas como análise.

Quando você terminar esta seção, deverá ter uma decisão clara e justificável sobre qual cenário deve se manter como referência.

## Deixando rastreabilidade da comparação para futuras iterações

O último passo é deixar registro da comparação. Comparar cenários sem rastreabilidade obriga a repetir o trabalho no futuro e dificulta explicar por que uma versão foi promovida ou descartada.

Antes de terminar, certifique-se de que:
1. Você já tomou uma decisão.
2. Você sabe qual cenário fica como referência.
3. Você tem claro qual foi o motivo principal da decisão.

Para deixar rastreabilidade:
1. Revise nome e descrição de ambos os cenários.
2. Se necessário, atualize a descrição do cenário novo para refletir melhor o propósito ou o resultado.
3. Mantenha a versão de referência claramente identificada como:
   1. publicada,
   2. validada,
   3. ou mantida como base oficial.
4. Mantenha a iteração não promovida como referência comparativa se ela tiver valor histórico.
5. Se o seu processo interno exigir, registre o que mudou e por que a decisão final foi tomada.

Para o caso de referência, garanta que:
1. Você consegue explicar por que o cenário novo melhora (ou não) a L1 vigente.
2. A decisão fica refletida em nomes/descrições ou no processo interno.
3. A próxima iteração não vai partir de confusão.

Quando você terminar esta seção, deverá ter não apenas uma comparação, mas uma decisão rastreável e útil para futuras iterações.

## Leituras adicionais

- [Passando de Scheduling a Rostering](P19_Passando_de_scheduling_a_rostering.md)

