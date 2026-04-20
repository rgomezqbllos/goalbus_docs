---
title: Criando uma nova iteração do cenário a partir de uma solução publicada
shortTitle: Nova iteração
intro: 'Aprenda a criar uma nova iteração de um cenário já publicado para testar melhorias, ajustar parâmetros ou introduzir mudanças sem alterar a versão que já está vigente em operação.'
contentType: how-tos
versions:
  - '*'
---

## Partindo de uma solução publicada sem alterar a versão vigente

Depois de publicar uma solução, é normal que você precise continuar trabalhando sobre ela. Talvez você queira ajustar regras, testar outra lógica de turnos, incorporar mudanças de oferta ou preparar uma melhoria para um período futuro. Nesse caso, você não deve modificar diretamente a versão já publicada. O correto é criar uma **nova iteração** do cenário para manter a rastreabilidade e proteger a versão que já está vigente.

Use este quick start quando você já tiver um cenário com solução em status **Publicada** e precisar gerar uma nova variante sem perder a referência histórica da solução implantada.

Antes de começar, certifique-se de que:
1. Você já publicou o cenário anterior no P16.
2. A solução do cenário que você vai usar como base está em status **Publicada**.
3. Você sabe qual aspecto quer revisar ou melhorar na próxima iteração.
4. Você tem claro que a nova iteração não deve substituir automaticamente a versão vigente até passar novamente por cálculo, validação e publicação.

Para este quick start, use este caso de referência:

> **Vou criar uma nova iteração do cenário publicado da linha L1 para testar melhorias na solução sem mexer na versão que já está vigente na operação.**

Para partir de uma solução publicada com segurança:
1. No GoalBus, abra o módulo de **Cenários de planejamento**.
2. Localize o cenário cuja solução está em status **Publicada**.
3. Revise nome, descrição, tipo de dia e linhas associadas.
4. Confirme que é realmente a versão que você quer usar como referência.
5. Evite editar essa versão diretamente como se fosse um novo rascunho.
6. Decida qual mudança quer introduzir na nova iteração:
   1. regras,
   2. parâmetros,
   3. oferta,
   4. ou ajustes estruturais permitidos.

Quando você terminar esta seção, deverá ter identificado com clareza o cenário publicado que servirá de base para a nova iteração.

## Criando a nova iteração a partir do cenário publicado

Depois de identificar a base, o próximo passo é criar uma **nova iteração**. O objetivo é conservar a versão publicada como referência histórica e abrir uma nova ramificação de trabalho controlada sobre a mesma lógica operacional.

Antes de começar esta seção, certifique-se de que:
1. Você já identificou a solução publicada correta.
2. Você sabe por que precisa de uma nova iteração.
3. Você tem claro que a nova iteração deve se diferenciar claramente da versão anterior.

Para criar a nova iteração:
1. Na tabela de cenários, abra o menu de ações do cenário publicado.
2. Selecione a opção de **criar uma nova iteração** duplicando o cenário como base de trabalho.
ref: P17_Imagen1.png | compact
3. Informe um **novo nome** para a iteração.
4. Se aplicável, atualize a **descrição** para refletir o objetivo da mudança.
5. Salve a nova iteração.
ref: P17_Imagen2.png | compact
6. Verifique que o novo cenário aparece como uma entidade separada do cenário publicado.
ref: P17_Imagen3.png | full
7. Verifique que a versão original publicada continua intacta e diferenciada da nova.

Para o caso de referência, uma opção válida poderia ser:
- **Cálculo Classic - L1 dia útil - Iteração 2**
- **L1 dia útil - melhoria de regras de turnos**

Quando você terminar esta seção, deverá ter uma nova iteração criada sem perder a rastreabilidade da versão publicada.

## Definindo quais mudanças pertencem à nova iteração

Depois de criar a iteração, você precisa decidir o que vai mudar de fato. Nem todas as iterações perseguem o mesmo objetivo. Algumas ajustam regras, outras melhoram eficiência, outras refletem uma nova oferta ou uma variação operacional futura.

Antes de começar esta seção, certifique-se de que:
1. Você já criou a nova iteração.
2. Você sabe qual aspecto da solução anterior quer revisar.
3. Você está disposto a limitar a mudança a um objetivo claro para não misturar muitas variáveis.

Para definir o escopo da iteração:
1. Abra o novo cenário.
2. Revise quais elementos você quer manter exatamente iguais à versão publicada.
3. Decida qual elemento vai mudar primeiro:
   1. **regras de veículos**,
   2. **regras de turnos**,
   3. **parâmetros do motor**,
   4. **oferta de serviço**,
   5. **matrizes logísticas**.
4. Evite mudar muitas coisas ao mesmo tempo na primeira iteração, a menos que seja estritamente necessário.
5. Documente o objetivo no nome ou na descrição.
6. Salve as alterações descritivas antes de calcular.

Para o caso de referência:
1. Manter a mesma oferta de dias úteis da L1.
2. Ajustar apenas o modelo de regras de turnos.
3. Recalcular para comparar a nova solução com a publicada.

Quando você terminar esta seção, deverá ter uma nova iteração com objetivo claro e delimitado.

## Recalculando a iteração e comparando com a versão anterior

Depois de definir o escopo, você precisa recalcular a iteração. A vantagem é que você já não começa do zero: começa de uma solução conhecida e pode comparar melhor o impacto da mudança.

Antes de começar esta seção, certifique-se de que:
1. Você já criou a nova iteração.
2. Você já definiu o objetivo da mudança.
3. Você já revisou quais regras, parâmetros ou entradas vai modificar.

Para recalcular a nova iteração:
1. Revise o cenário iterado e confirme que as entradas continuam coerentes.
2. Ajuste o elemento que você quer modificar.
3. Salve a configuração.
4. Execute o cálculo do novo cenário.
5. Aguarde o cenário completar a fase de cálculo.
6. Verifique se a iteração passa para **Solução preparada** ou **Edição**.
7. Compare o resultado com a versão anterior usando:
   1. KPIs,
   2. estrutura geral,
   3. lógica de tarefas,
   4. e coerência operacional.
8. Se a mudança melhorar o resultado, continue com a revisão formal.
9. Se a mudança piorar o resultado, mantenha a versão publicada como referência e decida se quer corrigir ou descartar esta iteração.

Para o caso de referência, compare:
1. A solução publicada da L1.
2. A nova iteração com ajuste de regras.
3. O que mudou em qualidade, viabilidade ou equilíbrio.

Quando você terminar esta seção, deverá ter uma nova solução calculada e uma base clara para compará-la com a versão já publicada.

## Decidindo se a nova iteração vai substituir a versão vigente

O último passo é decidir se esta iteração merece virar a nova versão operacional. Uma iteração nova não substitui automaticamente a publicação anterior. Para chegar à produção, ela precisa voltar a passar por revisão, validação e publicação no próprio ciclo de vida.

Antes de terminar, certifique-se de que:
1. Você já calculou a nova iteração.
2. Você já comparou o resultado com a solução publicada.
3. Você sabe se a mudança traz uma melhoria real ou apenas uma variante sem valor operacional.

Para fechar a decisão sobre a iteração:
1. Revise a nova solução do ponto de vista técnico e operacional.
2. Se a iteração melhorar claramente a solução vigente, prepare para:
   1. validação,
   2. e publicação posterior.
3. Se a iteração não melhorar o resultado, mantenha a versão publicada atual como referência vigente.
4. Não elimine a publicação anterior só porque existe uma nova iteração.
5. Mantenha ambas as versões bem identificadas para auditoria e comparação histórica.
6. Se decidir seguir adiante, trate a iteração como um novo cenário que deve percorrer o próprio fluxo até chegar a **Publicada**.

Para o caso de referência, finalize este quick start apenas quando puder afirmar uma destas duas coisas:
1. A nova iteração da L1 melhora a versão publicada e merece continuar o ciclo.
2. A versão publicada atual continua melhor e a iteração ficará apenas como teste ou referência.

Quando você terminar esta seção, deverá ter uma nova iteração calculada, comparada e pronta para virar nova versão ou para ficar como variante de análise.

## Leituras adicionais

- [Executando e validando o primeiro cálculo de Scheduling](P15_Executando_e_validando_o_primeiro_calculo_de_scheduling.md)

