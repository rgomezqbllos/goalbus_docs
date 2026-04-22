---
title: Executar e validar o primeiro cálculo da Programação
shortTitle: Calcular e validar
intro: Saiba como executar o primeiro cálculo da Programação, rever a vida útil do
  estágio Ciclo, validar a solução preparada e deixar o Cenário pronto para publicação
  ou auditoria subsequente.
contentType: how-tos
versions:
- '*'
---
## Executando o cálculo Cenário

Agora que você já tem o Cenário criado e configurado com a oferta Validado, as matrizes corretas e os modelos de regras e voltas Veículo, o próximo passo é executar o cálculo.

Neste estágio, o motor toma:
1. a oferta Validado,
2. Regras activas,
3. a logística das viagens vazias,
4. e a estrutura do palco,

para construir o Tarefas lógico programável.

Use este início rápido quando você tiver o programado Cenário pronto e precisar obter a primeira solução calculada antes de revisá-lo e convalidá-lo.

Antes de começar, certifique-se de que:
1. Já preparaste o palco na P14.
2. Você já selecionou o serviço Validado correto.
3. Já atribuíste a matriz de viagem vazia apropriada.
4. Você já selecionou o modelo certo de regras Veículo.
5. Você já selecionou o modelo certo de regras Turno.
6. Você já configurou o motor Clássico e os parâmetros de cálculo.

Para este início rápido, use este caso de referência:

> **Vou executar o primeiro cálculo do Cenário programado no Linha L1, verifique se a solução é consistente e deixe o Cenário pronto para validação.**

Para executar o cálculo do Cenário:
1. Abra o Cenário que deseja calcular.
2. Verifique uma última vez que os bilhetes do palco estão corretos.
3. Lançar a ação **Calcular** ou **Início do cálculo**.
ref: P15_Imagen1.png | compact(3x)
ref: P15_Imagen2.png | compact
4. Verifique se o estado do estágio muda de **Solução pendente** para **Cálculo da solução**.
ref: P15_Imagen3.png | full
ref: P15_Imagen4.png | full
5. Espere pelo motor para terminar o processo.
ref: P15_Imagen5.png | compact(1x18)
6. Verifique o novo estado do palco.
7. Se o cálculo concluir corretamente, confirma que o Cenário passa para o **Solução preparada**.
ref: P15_Imagen6.png | compact(x7)
8. Se a solução requer ajustes manuais, digite o status **Edição** para refinamento.
9. Se o motor não devolver uma solução válida, verifique novamente:
   1. a oferta,
   2. a matriz de viagem vazia,
   3. as regras,
   4. e os parâmetros do Cenário.

Para o caso de referência, confirma que:
1. O L1 Cenário sai do estado inicial.
2. O motor completa o cálculo sem bloquear.
3. O Cenário vem a uma solução preparada ou uma fase de edição razoável.

Além disso, no caso de o tipo de Cenário escolhido ser para Veículos e Turnos, você pode ver a solução gerada a partir de Turnos da vista da equipe.
ref: P15_Imagen12.png | compact

Quando você terminar este Seção, você deve ter uma primeira solução calculada ou um sinal claro de qual parte da parametrização precisa de correção.

## Revisão do estado do Cenário e do resultado do cálculo

Depois de executar o cálculo, você precisa entender em que ponto na vida Ciclo o Cenário permaneceu. Isto é importante porque cada estado tem um significado operacional diferente e lhe diz que ações você pode fazer a seguir.

Antes de iniciar este Seção, certifique-se de que:
1. Já controlaste o cálculo.
2. Sabes o nome do cenário que estás a rever.
3. Você sabe se você estava esperando uma solução pronta ou uma fase de refinamento.

Para rever o status e o resultado:
1. Volte para a mesa principal Cenário ou fique no cenário.
2. Verifique o estado actual.
3. Ele interpreta o estado de acordo com esta lógica:
   1. **Solução pendente**: O Cenário ainda não foi calculado.
   2. **Cálculo da solução**: O motor está processando a solução.
   3. **Edição**: Um usuário está ajustando manualmente a solução.
   4. **Solução preparada**: A fase de cálculo ou edição acabou e o Cenário está pronto para revisão.
   5. **Validação**: A solução já foi Aprovado e bloqueada.
   6. **Publicação**: A solução está sendo incorporada no calendário operacional.
   7. **Publicado**: A solução já estava implantada na operação.
4. Se o Cenário estiver em **Solução preparada**, continue com a revisão da consistência.
5. Se o Cenário estiver em **Edição**, terminar o manual necessário Configuração primeiro.
6. Se o Cenário ainda estiver em **Cálculo da solução** por muito tempo, verifique se houve um Incidência técnico demasiado restritivo ou Configuração.

Para o caso de referência, você deve esperar que o Cenário termine pelo menos em:
1. **Solução preparada**, se você não precisa mais tocar na estrutura,
2. ou **Edição**, se você ainda quiser refinar manualmente.

Quando você terminar este Seção, você deve entender claramente o que o estado de estágio atual significa e o que ação segue.

## Verificar o KPI, erros e consistência antes de validar

Antes de validar o Cenário, você precisa revisá-lo. A validação não é um simples clique administrativo. É a porta de aprovação formal que congela a solução e evita alterações subsequentes acidentais.

Antes de iniciar este Seção, certifique-se de que:
1. O estágio já está em **Solução preparada** ou você terminou a fase **Edição**.
2. Você sabe, depois de validar, o Cenário não será mais editável.
3. Está pronto para uma revisão final antes da aprovação.

Para rever a solução antes de a validar:
1. Ele abre o palco em seu estado atual.
2. Verifique os KPIs disponíveis.
ref: P15_Imagen7.png | full
3. Verifique se há erros visíveis, avisos ou inconsistências.
ref: P15_Imagen8.png | compact(x7)
4. Use os filtros disponíveis para inspecionar a solução de diferentes ângulos.
ref: P15_Imagen9.png | compact(3x)
5. Verifica que os mapeamentos e a estrutura Cenário fazem sentido operacional.
6. Se você detectar um problema menor e o Cenário ainda é editável, corrija-o antes de continuar.
7. Se você detectar um problema importante depois de o ter bloqueado mais tarde, você deve desbloqueá-lo com permissões apropriadas ou voltar a um Cenário editável.

Para o caso de referência, certifique-se de que:
1. Os KPIs de solução L1 são razoáveis.
2. Não há erros graves que invalidem a solução.
3. A solução agora pode passar da revisão técnica para aprovação formal.

Quando você terminar este Seção, você deve ter confiança suficiente para validar o Cenário.

## Validação do estágio e bloqueio da solução

Agora você pode executar o **validação do Cenário**. Esta etapa marca o fechamento oficial da fase de cálculo e edição. A partir daqui, a solução torna-se protegida, o Cenário deixa de ser editável e não pode mais ser recalculado enquanto permanece Validado.

Antes de iniciar este Seção, certifique-se de que:
1. O palco é em **Solução preparada**.
2. Você terminou a revisão do KPI e erros.
3. Você não precisa fazer mais ajustes manuais antes de aprovar a solução.

Para validar o Cenário:
1. A partir da tabela Cenário, abra o menu de ação do palco.
2. Selecione **Validar**.
3. Se você preferir fazê-lo de dentro do palco, use o botão **Validar** no topo da tela.
ref: P15_Imagen10.png | compact(2x)
4. Confirme a validação quando o sistema o solicitar.
5. Verifique se o estado da solução de estágio muda para **Validar**.
ref: P15_Imagen11.png | compact(2x)
6. Verifique isso:
   1. o Cenário já não é editável,
   2. não pode mais ser recalculado,
   3. e os seus principais dados estão protegidos.
7. Se você descobrir um erro de última hora após a validação, use o fluxo de desbloqueio apenas com as permissões certas.

Para o caso de referência, não continue até poder dizer:
1. A solução L1 já foi revista.
2. A solução Cenário mudou para status **Validar**.
3. A organização já pode tratar esse Cenário como um Aprovado Versão.

Quando você terminar este Seção, você deve ter formalmente um Aprovado e solução bloqueada para evitar alterações acidentais.

## Deixando o Cenário pronto para publicação ou auditoria subsequente

Uma vez que Validado, o Cenário está pronto para dois caminhos:
1. **publicação**, se você quiser levá-lo para o calendário operacional real,
2. ou **auditoria**, se você ainda precisar revisá-lo antes de Publicando.

Neste ponto, o Cenário permanece uma solução Aprovado e protegida. Você ainda pode consultá-lo, revisar o KPI, filtrar informações e usá-lo como referência, mas você não deve mais tratá-lo como um Rascunho funcional.

Antes de terminar, certifique-se de que:
1. A solução de estágio já está em estado **Validar**.
2. Você sabe a diferença entre validar e Publicando.
3. Você sabe se seu próximo passo será implantar a solução ou continuar a auditá-la.

Para deixar o palco pronto para o próximo passo:
1. Verifique a tabela Cenário e confirme o estado **Validar**.
2. Se o plano já for Aprovado para implementação, prepare o fluxo **Publicar**.
3. Se você ainda precisar de revisão interna, mantenha o Validado Cenário como base de auditoria.
4. Use filtros, ícones de informação e revisão de estado para controlar quais Cenários estão pendentes, Validado, ou já Publicado.
5. Se você precisar iterar um novo Versão, considere duplicar o Cenário em vez de alterar um já Aprovado.

Para o caso de referência, termine este início rápido apenas quando puder dizer:
1. O L1 Cenário já foi calculado.
2. A solução foi revista.
3. A solução de estágio é **Validar**.
4. O próximo passo não é mais calcular, mas decidir se é Publicado ou auditado.

Quando você terminar este Seção, você deve ter um calculado, revisado e Validado Cenário, pronto para a produção ou revisão final.

## Lecturas adicionais

- [Publicando Cenário em datas específicas](publicacion-del-escenario)
