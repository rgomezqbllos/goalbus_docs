---
title: Analisando e comparando Programação Cenários
shortTitle: Comparar Cenários
intro: Saiba como comparar Programação Cenários, rever KPI e diferenças operacionais
  e decidir com critérios qual solução deve ser mantida como referência ou avançar
  para uma nova iteração.
contentType: how-tos
versions:
- '*'
---
## Identificando qual Cenários você vai comparar

Depois de criar, calcular, validar e Publicando Cenários, o próximo passo natural é compará-los. Comparar Cenários não é apenas ver o que foi melhor intuitivamente. Consiste em rever o que mudou, o impacto que essa mudança teve, e se a nova iteração realmente melhora a solução de referência.

Use este início rápido quando já tiver pelo menos dois Cenários comparáveis, por exemplo uma solução Publicado e uma nova iteração calculada, e você precisa decidir qual deve ser mantido como referência operacional ou qual merece avançar na vida útil Ciclo.

Antes de começar, certifique-se de que:
1. Você já criou e calculou pelo menos uma base Cenário.
2. Você já tem uma segunda Versão, iteração ou variante que você quer comparar.
3. Você sabe o que Linha, que tipo de dia e que contexto operacional você está revisando.
4. Está claro qual é a referência atual Versão.

Para este início rápido, use este caso de referência:

> **Vou comparar o Publicado Cenário de Linha L1 com uma nova iteração calculada para decidir se a nova solução realmente melhora a programação atual.**

Para identificar corretamente o Cenários a ser comparado:
1. Em GoalBus, abra o módulo **Planejamento Cenários**.
ref: P18_Imagen1.png | compact
2. Localiza o Cenário que atua como a referência atual.
3. Localize o novo Cenário ou iteração que você deseja avaliar.
4. Verifica que ambos os Cenários pertencem ao mesmo contexto funcional:
   1. o mesmo conjunto Linha ou comparável de Linhas,
   2. o mesmo tipo de dia,
   3. a mesma lógica operacional geral.
5. Verifique o nome, a descrição e o estado de cada Cenário.
6. Confirma o que é:
   1. a corrente ou Publicado Versão;
   2. e qual é a nova proposta.
7. Se o Cenários não for comparável entre si, não continue a corrigir esse ponto.

Para o caso de referência, certifique-se de que:
1. Ambos os Cenários pertencem a Linha L1.
2. Ambos estão trabalhando ou respondem ao mesmo contexto temporal.
3. Um age como referência e o outro como alternativa.

Quando você terminar este Seção, você deve ter identificado claramente o Cenários que você vai comparar e o papel que cada um desempenha.

## Revisão do IPC, da carga de trabalho e do equilíbrio global

Uma vez selecionado o Cenários, você precisa começar com uma comparação de alto nível. Aqui o objetivo é rever indicadores gerais antes de entrar em detalhes ou regras do Tarefa. Esta primeira comparação ajuda a detectar se a nova solução está realmente melhor equilibrada ou se só altera o resultado sem trazer valor real.

Antes de iniciar este Seção, certifique-se de que:
1. Você sabe o que dois Cenários você vai comparar.
2. Já identificaste a referência.
3. Você já tem acesso a KPIs de estágio visível ou métricas comparáveis.

Para rever o KPI geral Cenários:
1. Abre a primeira etapa e revisa os seus principais KPIs.
2. Observe ou recorde pelo menos:
   1. carga de trabalho total,
   2. número de Tarefas,
   3. tempo total,
   4. Distância ou magnitude operacional relevante,
   5. qualquer outro indicador visível na interface.
3. Abra a segunda etapa e verifique os mesmos KPIs.
4. Comparar se a nova iteração:
   1. reduz a complexidade desnecessária,
   2. melhora o equilíbrio,
   3. ou desloca o problema de um lugar para outro.
5. Evite uma boa iteração só porque muda os números. O importante é que a mudança faz sentido operacional.

Para o caso de referência, pergunte-se:
1. A nova iteração reduz Tarefas desnecessário?
2. Será que o equilíbrio geral parece mais razoável?
3. O volume total ainda é consistente com a oferta Validado?
4. A melhoria é real ou é apenas uma redistribuição sem benefícios claros?

Quando você terminar este Seção, você deve ter uma leitura global de se a nova solução merece uma revisão mais profunda.

## Comparar o impacto sobre Veículos e Turnos

Depois de rever KPIs globais, você precisa descer para a lógica funcional. Nesta fase, a comparação deve separar duas coisas:
1. o impacto sobre **Veículos**,
2. e impacto sobre **Turnos**.

Isto é importante porque uma iteração pode melhorar a lógica do Frota e piorar a lógica do Turnos, ou ao contrário. Se você misturar ambas as dimensões, a leitura torna-se confusa.

Antes de iniciar este Seção, certifique-se de que:
1. Você já verificou os KPIs gerais.
2. Você sabe o que as regras Veículo e Turno estão envolvidas na mudança.
3. Você já está claro sobre o propósito da iteração.

Para comparar o impacto no Veículos:
1. Verifique como a solução se comporta em relação a:
   1. Frota utilizado,
   2. Compatibilidades,
   3. partidas de armazéns ou espaços Garagem,
   4. e quilometragem não produtiva, visível ou dedutível.
2. Verifique se a iteração melhora a consistência entre Linha, Frota e infraestrutura.
3. Ele detecta se a nova Cenário força soluções que anteriormente eram mais realistas.

Para comparar o impacto no Turnos:
1. Verifique como Tarefas ou blocos de trabalho são construídos.
2. Verifique se os tipos Turno ativos ainda fazem sentido.
3. Ver se a nova solução:
   1. melhora a clareza do trabalho,
   2. piora a estrutura,
   3. ou introduzir rigidez desnecessárias.
4. Relacionou a mudança com o modelo Regra de turno que você usou.

Para o caso de referência, pergunte-se:
1. A nova iteração melhora a lógica do Veículos sem punir a lógica do Turnos?
2. A lógica Turno melhora sem piorar o Frota?
3. Qual das duas dimensões ganha ou perde?
4. O resultado global é mais robusto ou apenas mais diferente?

Quando você terminar este Seção, você deve entender onde cada Cenário fica melhor e onde fica pior.

## Decidir se a nova iteração traz valor real

Agora você precisa transformar a comparação em uma decisão. Nem todos os novos Cenário merecem avançar. Às vezes, uma nova iteração serve apenas como aprendizagem interna e a melhor decisão é manter o atual Versão. Outras vezes a melhoria é suficientemente clara para justificar um novo Ciclo de validação e publicação.

Antes de continuar, certifique-se de que:
1. Já comparaste os KPIs gerais.
2. Você já verificou em Veículos e Turnos.
3. Sabes qual era o objectivo original da nova iteração.

Para decidir se a iteração traz valor real:
1. Resume mentalmente qual era o propósito do novo Cenário.
2. Verificar se esse objectivo foi claramente alcançado.
3. Pergunte-se se a melhora é:
   1. Visível operacionalmente,
   2. Tecnicamente defensíveis,
   3. e estável o suficiente para continuar a avançar.
4. Se a iteração melhorar claramente a referência, prepare-a para validação ou publicação, conforme adequado.
5. Se a iteração não melhorar a referência, mantenha-a como aprendizado e mantenha o atual Versão.
6. Não promova uma iteração apenas porque é mais recente. Promova-a apenas se for melhor para o caso.

Para o caso de referência, termine este Seção apenas quando você puder afirmar uma destas duas coisas:
1. A nova iteração L1 melhora claramente a solução Publicado e merece avançar.
2. A solução Publicado permanece a melhor referência e a nova iteração permanece como uma análise.

Quando você terminar este Seção, você deve ter uma decisão clara e justificável sobre qual Cenário deve ser mantido como referência.

## Deixando a rastreabilidade da comparação para futuras iterações

O último passo é deixar um traço da comparação. Comparar Cenários sem deixar forças de rastreabilidade para repetir a análise no futuro e torna mais difícil explicar por que um Versão foi promovido ou descartado.

Antes de terminar, certifique-se de que:
1. Já tomaste uma decisão no palco.
2. Sabes o que resta como referência.
3. Está claro qual foi a principal razão da decisão.

Para deixar a rastreabilidade da comparação:
1. Verifique o nome e a descrição de ambos Cenários.
2. Se necessário, atualize a descrição do novo Cenário para refletir melhor o seu objetivo ou resultado.
3. Mantém identificada a referência Versão como:
   1. Publicado,
   2. Validado,
   3. ou mantido como base oficial.
4. Mantenha a iteração não promovida como referência comparativa se ela trazer valor histórico.
5. Se seu processo interno o requer, registre o que mudou entre os dois Cenários e por que a decisão final foi tomada.

Para o caso de referência, certifique-se de que:
1. Você pode explicar por que o novo Cenário melhora ou não para o atual L1.
2. A decisão reflecte-se em nomes, descrições ou processo interno.
3. A próxima iteração, se existir, não partirá da confusão.

Quando você terminar este Seção, você deve ter não só uma comparação feita, mas uma decisão rastreável e útil para futuras iterações.

## Lecturas adicionais

- [Mudança de Programação para Alocação](P19_Mudança_De_Programação_Para_Alocação.md)
