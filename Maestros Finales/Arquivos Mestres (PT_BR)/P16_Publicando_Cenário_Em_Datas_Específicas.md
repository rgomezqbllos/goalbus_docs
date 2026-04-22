---
title: Publicando Cenário em datas específicas
shortTitle: Publicar Cenário
intro: Saiba como publicar um Validado Cenário em datas específicas, controlar a solução
  que entra em operação e manter a rastreabilidade entre planejamento, validação e
  implantação operacional.
contentType: how-tos
versions:
- '*'
---
## Preparação do Validado Cenário antes do Publicando

Após o cálculo e validação de uma solução, o próximo passo é decidir que **quando** deve entrar em vigor na operação real. Publicando um Cenário não é apenas aprová-la: trata-se de inserir essa solução Validado no calendário operacional para uma data específica, sem confundi-la com um Rascunho ou um Versão ainda em revisão.

Use este início rápido quando você já tiver um estágio com uma solução no status **Validar** e precisa levá-lo para a operação por um período específico.

Antes de começar, certifique-se de que:
1. Você já executou e Validado o Cenário no P15.
2. A solução Cenário que você deseja publicar está no estado **Validar**.
3. Sabes que datas exactas que queres cobrir.
4. Você está claro que o Publicando altera o estado operacional da solução e a torna visível como um Versão implantado.

Para este início rápido, use este caso de referência:

> **Vou publicar o Validado Cenário de Linha L1 para que entre em vigor durante um período de trabalho específico sem afetar soluções que não correspondem a essas datas.**

Preparar a publicação do Cenário:
1. Abra o módulo **Planejamento Cenários**.
2. Localize o Cenário que você já tem Validado.
3. Verifique se o estado atual da solução é **Validar**.
4. Verifique o nome do palco, os Linha incluídos, o tipo de dia e a descrição.
5. Confirme que você está prestes a publicar exatamente a solução certa.
6. Se o Cenário ainda não for o Validado, volte atrás e termine o P15 antes de continuar.
7. Se o Cenário estiver correto, continue com a publicação.

Quando você terminar este Seção, você deve ter identificado claramente o Validado Cenário que você deseja implementar.

## Selecionar a janela temporária Publicando

Uma vez confirmado o Cenário, você precisa decidir que o **em que datas** vai se aplicar. A publicação não deve ser feita de forma ambígua. Deve ser clara a partir de quando e até quando essa solução será uma referência operacional.

Antes de iniciar este Seção, certifique-se de que:
1. Você já confirmou o que Cenário você vai publicar.
2. Você sabe se a publicação vai cobrir um dia, uma semana, um intervalo contínuo, ou um bloco de operação mais longo.
3. Você já está claro que o período escolhido não deve contradizer o tipo de dia e a lógica temporal do Cenário.

Para selecionar a janela temporária Publicando:
1. A partir do Validado Cenário, abra a ação **Publicar**.
ref: P16_Imagen1.png | compact
2. No formulário de publicação, você define o **Intervalo de datas**.
3. Adicionar outro **Intervalos de datas**, se você considerar e postar para outros dias não selecionados (opcional).
ref: P16_Imagen2.png | compact(x12)
4. Verifique se as datas fazem sentido para:
   1. O tipo do dia de palco,
   2. o(s) Linha envolvido(s),
   3. E a verdadeira janela de operação que queres cobrir.
5. Confirme que você não está deixando um intervalo muito largo por engano.
6. Se o Cenário só deve ser aplicado em um curto período, ele limita a janela com precisão.
7. Confirma a publicação para a data/s gama/s escolhida.

Para o caso de referência, pergunte-se:
1. A publicação abrange exactamente os dias úteis que eu quero implementar?
2. Estou evitando Publicando mais dias do que é necessário?
3. A solução corresponde realmente às datas selecionadas?

Quando você terminar este Seção, você deve ter uma janela de tempo clara e controlada definida para a implantação.

## Confirmação da publicação e alteração do estado do Cenário

Depois de selecionar o intervalo de tempo, você precisa confirmar a ação Publicando. Neste ponto, a solução deixa de ser apenas um Validado Cenário e torna-se operacional dentro do calendário.

Antes de continuar, certifique-se de que:
1. Você já selecionou as datas corretamente.
2. Você já verificou o Validado Cenário.
3. Você já está pronto para a solução para avançar em sua vida útil Ciclo.

Para publicar o Cenário:
1. Reveja o resumo da publicação pela última vez.
2. Confirma:
   1. o nome do palco,
   2. o intervalo de tempo,
   3. e o contexto operacional a que se aplicará.
3. Execute a ação **Publicar**.
4. Verifique se o estado do estágio muda para **Publicação** enquanto o sistema processa o implante.
5. Espere até o processo acabar.
6. Verifique se o estado final da solução muda para **Publicado**.
ref: P16_Imagen3.png | compact
7. Se o estado não mudar como esperado, verifique se houve um problema técnico de elegibilidade Incidência ou Cenário.

Para o caso de referência, não encerre a publicação até poder dizer:
1. A solução L1 Cenário já saiu de **Validar**.
2. A plataforma processou a publicação.
3. A solução de estado de estágio final é **Publicado**.

Quando você terminar este Seção, você deve ter um Cenário já implantado no calendário de operação para o período selecionado.

## Verificar que a solução Publicado é a que está em vigor

Após Publicando, você precisa verificar que a solução ativa é realmente a certa. Publicando não deve ser um passo cego. Você deve ser capaz de verificar qual Cenário era válido para as datas escolhidas e manter rastreabilidade na solução implementada.

Antes de iniciar este Seção, certifique-se de que:
1. A solução Cenário já atingiu o status **Publicado**.
2. Sabes que datas ele cobre.
3. Você sabe que serviço ou Linha deve ser afetado pela publicação.

Para verificar a implementação da solução:
1. Volte para a tabela principal Cenário.
2. Filtrar ou rever o Cenários por estado.
3. Confirma que a solução Publicado Cenário aparece como **Publicado**.
4. Verifique as datas de aplicação, se a vista permitir.
5. Verifique que você não está confundindo este Cenário com outro Validado, mas não implantado.
6. Se o seu processo interno o exigir, registre-se ou comunique que este Versão já é a solução operacional atual.
7. Mantém o nome, a descrição e o intervalo de tempo como base de rastreabilidade para a auditoria subsequente.

Para o caso de referência, certifique-se de que:
1. O Publicado Cenário corresponde a L1.
2. As datas correspondem ao período que queria implementar.
3. Nenhum outro Cenário foi ativado por engano.

Quando você terminar este Seção, você deve ter certeza de que solução estava no lugar e para que período exato.

## Manter a rastreabilidade e preparar a próxima iteração

Uma vez que o Cenário é o Publicado, o trabalho não desaparece: ele muda de foco. A partir daqui, a solução implementada pode se tornar uma referência para auditoria, comparação ou iteração futura. Não é aconselhável reutilizar sem controle um Publicado Cenário já para sofrer alterações estruturais; a coisa mais segura é criar uma nova iteração quando você precisa propor uma melhoria ou uma variante.

Antes de terminar, certifique-se de que:
1. O Cenário já é Publicado.
2. Está claro que intervalo de tempo ele cobre.
3. Você sabe se a próxima coisa será auditar os resultados ou preparar uma nova iteração.

Manter a rastreabilidade após a publicação:
1. Ele preserva o Publicado Cenário com um nome e descrição suficientemente claros.
2. Use o status **Publicado** como referência para distingui-lo do Cenários em Rascunho, cálculo ou validação.
3. Se você precisa propor uma melhoria, crie um novo Cenário em vez de alterar a lógica histórica do Cenário implantado.
4. Se sua equipe trabalhar com revisão posterior, use esta Publicado Versão como uma comparação de base.
5. Manter um registo interno de:
   1. o que era Publicado,
   2. quando era Publicado,
   3. e para que datas era válido.

Para o caso de referência, termine este início rápido apenas quando puder dizer:
1. A solução L1 já é Publicado.
2. Sabes exactamente quando entrou em vigor.
3. Você pode distinguir este Publicado Versão de qualquer iteração futura.

Quando você terminar este Seção, você deve ter uma solução Publicado, rastreável e pronta para servir como referência operacional ou como ponto de partida para uma nova iteração.

## Lecturas adicionais

- [Criando uma nova iteração do Cenário a partir de uma solução Publicado](iteracion-del-escenario)
