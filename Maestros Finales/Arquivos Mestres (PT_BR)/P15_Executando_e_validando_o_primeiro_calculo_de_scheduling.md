---
title: Executando e validando o primeiro cálculo de Scheduling
shortTitle: Calcular e validar
intro: 'Aprenda a executar o primeiro cálculo de Scheduling, revisar o ciclo de vida do cenário, validar a solução preparada e deixar o cenário pronto para publicação ou auditoria posterior.'
contentType: how-tos
versions:
  - '*'
---

## Executando o cálculo do cenário

Agora que você já tem o cenário criado e configurado com a oferta validada, as matrizes corretas e os modelos de regras de veículos e de turnos, o próximo passo é executar o cálculo.

Nesta fase, o motor usa:
1. a oferta validada,
2. as regras ativas,
3. a logística de viagens em vazio,
4. e a estrutura do cenário,

para construir tarefas lógicas programáveis.

Use este quick start quando você já tiver preparado o cenário de Scheduling e precisar obter a primeira solução calculada antes de revisá-la e validá-la.

Antes de começar, certifique-se de que:
1. Você já criou o cenário no P14.
2. Você já selecionou o serviço validado correto.
3. Você já atribuiu a matriz de viagens em vazio adequada.
4. Você já selecionou o modelo correto de regras de veículos.
5. Você já selecionou o modelo correto de regras de turnos.
6. Você já configurou o motor Classic e os parâmetros de cálculo.

Para este quick start, use este caso de referência:

> **Vou executar o primeiro cálculo do cenário de Scheduling da linha L1, revisar se a solução é coerente e deixar o cenário pronto para validação.**

Para executar o cálculo do cenário:
1. Abra o cenário que você quer calcular.
2. Revise uma última vez se as entradas do cenário estão corretas.
3. Execute **Calcular** / **Iniciar cálculo**.
ref: P15_Imagen1.png | compact
ref: P15_Imagen2.png | compact
4. Verifique se o status do cenário muda de **Solução pendente** para **Cálculo da solução**.
ref: P15_Imagen3.png | full
ref: P15_Imagen4.png | full
5. Aguarde o motor terminar o processo.
ref: P15_Imagen5.png | full
6. Revise o novo status do cenário.
7. Se o cálculo terminar corretamente, confirme que o cenário passa para **Solução preparada**.
ref: P15_Imagen6.png | compact
8. Se a solução exigir ajustes manuais, entre em **Edição** para refinamento.
9. Se o motor não devolver uma solução válida, volte a revisar:
   1. a oferta,
   2. a matriz de viagens em vazio,
   3. as regras,
   4. e os parâmetros do cenário.

Para o caso de referência, confirme que:
1. O cenário da L1 sai do status inicial.
2. O motor termina o cálculo sem travar.
3. O cenário chega a uma solução preparada ou a uma fase de edição razoável.

Além disso, caso o tipo de cenário escolhido seja para veículos e para turnos, será possível ver a solução de turnos gerada na visão de pessoal.
ref: P15_Imagen12.png | compact

Quando você terminar esta seção, deverá ter uma primeira solução calculada ou um sinal claro de qual parte da parametrização precisa de correção.

## Revisando o status do cenário e o resultado do cálculo

Depois de executar o cálculo, você precisa entender em que ponto do ciclo de vida o cenário ficou. Isso é importante porque cada status tem um significado operacional diferente e diz quais ações você pode fazer em seguida.

Antes de começar esta seção, certifique-se de que:
1. Você já executou o cálculo.
2. Você sabe o nome do cenário que está revisando.
3. Você sabe se esperava uma solução pronta ou uma fase de refinamento.

Para revisar o status e o resultado:
1. Volte para a tabela principal de cenários ou permaneça dentro do cenário.
2. Revise o status atual.
3. Interprete o status segundo esta lógica:
   1. **Solução pendente**: o cenário ainda não foi calculado.
   2. **Cálculo da solução**: o motor está processando a solução.
   3. **Edição**: um usuário está ajustando manualmente a solução.
   4. **Solução preparada**: a fase de cálculo/edição terminou e o cenário está pronto para revisão.
   5. **Validado**: a solução foi aprovada e bloqueada.
   6. **Publicação**: a solução está sendo incorporada ao calendário operacional.
   7. **Publicado**: a solução já foi implantada na operação.
4. Se o cenário estiver em **Solução preparada**, continue com a revisão de coerência.
5. Se o cenário estiver em **Edição**, finalize primeiro os ajustes manuais necessários.
6. Se o cenário ficar em **Cálculo da solução** por tempo demais, verifique se houve um problema técnico ou uma configuração muito restritiva.

Para o caso de referência, você deve esperar que o cenário termine pelo menos em:
1. **Solução preparada**, se você não precisa mais mexer na estrutura, ou
2. **Edição**, se você ainda quer refinar manualmente.

Quando você terminar esta seção, deverá entender com clareza o que o status atual significa e qual ação vem depois.

## Revisando KPIs, erros e consistência antes de validar

Antes de validar o cenário, você precisa revisá-lo. Validar não é apenas um clique administrativo. É a porta de aprovação formal que congela a solução e evita alterações acidentais posteriores.

Antes de começar esta seção, certifique-se de que:
1. O cenário já está em **Solução preparada** ou você já terminou a fase de **Edição**.
2. Você sabe que, após validar, o cenário deixará de ser editável.
3. Você está pronto para uma revisão final antes da aprovação.

Para revisar a solução antes de validar:
1. Abra o cenário no status atual.
2. Revise os KPIs disponíveis.
ref: P15_Imagen7.png | full
3. Verifique se existem erros, avisos ou incoerências visíveis.
ref: P15_Imagen8.png | compact
4. Use os filtros disponíveis para inspecionar a solução de diferentes ângulos.
ref: P15_Imagen9.png | compact
5. Confirme que as atribuições e a estrutura do cenário fazem sentido operacional.
6. Se detectar um problema menor e o cenário ainda for editável, corrija antes de continuar.
7. Se detectar um problema importante depois de bloquear, você precisará desbloquear com permissões adequadas ou voltar a um cenário editável.

Para o caso de referência, garanta que:
1. Os KPIs da solução da L1 são razoáveis.
2. Não há erros graves que invalidem a solução.
3. A solução pode passar da revisão técnica para a aprovação formal.

Quando você terminar esta seção, deverá ter confiança suficiente para validar o cenário.

## Validando o cenário e bloqueando a solução

Agora sim você pode executar a **validação do cenário**. Este passo marca o encerramento oficial das fases de cálculo e edição. A partir daqui, a solução fica protegida, o cenário deixa de ser editável e não pode ser recalculado enquanto permanecer validado.

Antes de começar esta seção, certifique-se de que:
1. O cenário está em **Solução preparada**.
2. Você já terminou a revisão de KPIs e erros.
3. Você não precisa fazer mais ajustes manuais antes de aprovar.

Para validar o cenário:
1. Na tabela de cenários, abra o menu de ações do cenário.
2. Selecione **Validar**.
3. Se preferir fazer dentro do cenário, use o botão **Validar** na parte superior da tela.
ref: P15_Imagen10.png | compact
4. Confirme a validação quando o sistema solicitar.
5. Verifique se o status da solução muda para **Validada**.
ref: P15_Imagen11.png | compact
6. Confirme que:
   1. o cenário não é mais editável,
   2. não pode mais ser recalculado,
   3. e os dados principais ficam protegidos.
7. Se descobrir um erro de última hora após validar, use o fluxo de desbloqueio apenas com as permissões adequadas.

Para o caso de referência, não prossiga até poder afirmar:
1. A solução da L1 já foi revisada.
2. A solução do cenário mudou para status **Validada**.
3. A organização já pode tratar esse cenário como uma versão aprovada.

Quando você terminar esta seção, deverá ter uma solução formalmente aprovada e bloqueada para evitar alterações acidentais.

## Deixando o cenário pronto para publicação ou auditoria posterior

Depois de validado, o cenário fica pronto para dois caminhos:
1. **publicação**, se você quer levá-lo ao calendário operacional real,
2. ou **auditoria**, se você ainda precisa revisá-lo antes de publicar.

Neste ponto, o cenário fica como uma solução aprovada e protegida. Você ainda pode consultá-lo, revisar KPIs, filtrar informações e usá-lo como referência, mas não deve tratá-lo como rascunho de trabalho.

Antes de terminar, certifique-se de que:
1. A solução do cenário está em status **Validada**.
2. Você conhece a diferença entre validar e publicar.
3. Você sabe se o próximo passo será implantar ou auditar.

Para deixar o cenário pronto para o próximo passo:
1. Revise a tabela de cenários e confirme o status **Validada**.
2. Se o plano já estiver aprovado para implantação, prepare o fluxo de **Publicar**.
3. Se você ainda precisar de revisão interna, mantenha o cenário validado como base de auditoria.
4. Use filtros, ícones informativos e revisão de status para controlar quais cenários estão pendentes, validados ou já publicados.
5. Se precisar iterar uma nova versão, considere duplicar o cenário em vez de alterar um já aprovado.

Para o caso de referência, termine este quick start apenas quando puder afirmar:
1. O cenário da L1 já foi calculado.
2. A solução foi revisada.
3. A solução do cenário está **Validada**.
4. O próximo passo não é mais calcular, e sim decidir se publica ou se audita.

Quando você terminar esta seção, deverá ter um cenário calculado, revisado e validado, pronto para produção ou revisão final.

## Leituras adicionais

- [Publicando o cenário em datas específicas](P16_Publicando_o_cenario_em_datas_especificas.md)

