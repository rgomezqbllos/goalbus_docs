---
title: Publicando o cenário em datas específicas
shortTitle: Publicar cenário
intro: 'Aprenda a publicar um cenário validado em datas específicas, controlar qual solução entra em operação e manter rastreabilidade entre planejamento, validação e implantação operacional.'
contentType: how-tos
versions:
  - '*'
---

## Preparando o cenário validado antes de publicar

Depois de calcular e validar uma solução, o próximo passo é decidir **quando** ela deve entrar em vigor na operação real. Publicar um cenário não é apenas aprová-lo: é inserir essa solução validada no calendário operacional para datas específicas, sem confundi-la com um rascunho ou com uma versão ainda em revisão.

Use este quick start quando você já tiver um cenário com solução em status **Validada** e precisar levá-lo à operação por um período específico.

Antes de começar, certifique-se de que:
1. Você já executou e validou o cenário no P15.
2. A solução do cenário que você quer publicar está em status **Validada**.
3. Você sabe quais datas exatas quer cobrir.
4. Você tem claro que publicar muda o status operativo da solução e a torna visível como versão implantada.

Para este quick start, use este caso de referência:

> **Vou publicar o cenário validado da linha L1 para que ele entre em vigor durante um período específico de dias úteis sem afetar soluções que não correspondem a essas datas.**

Para preparar a publicação do cenário:
1. Abra o módulo de **Cenários de planejamento**.
2. Localize o cenário que você já validou.
3. Verifique se o status atual da solução é **Validada**.
4. Revise o nome do cenário, a(s) linha(s) incluída(s), o tipo de dia e a descrição.
5. Confirme que você está prestes a publicar exatamente a solução correta.
6. Se o cenário ainda não estiver validado, volte e finalize o P15 antes de seguir.
7. Se o cenário estiver correto, prossiga para a publicação.

Quando você terminar esta seção, deverá ter identificado com clareza o cenário validado que quer implantar.

## Selecionando a janela temporal de publicação

Depois de confirmar o cenário, você precisa decidir **em quais datas** ele será aplicado. A publicação não deve ser ambígua. Deve ficar claro a partir de quando e até quando essa solução será a referência operacional.

Antes de começar esta seção, certifique-se de que:
1. Você já confirmou qual cenário vai publicar.
2. Você sabe se a publicação cobrirá um dia, uma semana, um intervalo contínuo ou um bloco operacional maior.
3. Você tem claro que o período escolhido não deve contradizer o tipo de dia e a lógica temporal do cenário.

Para selecionar a janela temporal de publicação:
1. No cenário validado, abra a ação **Publicar**.
ref: P16_Imagen1.png | compact
2. No formulário de publicação, defina o **Intervalo de datas**.
3. Adicione outros **Intervalos de datas**, se necessário (opcional).
ref: P16_Imagen2.png | compact
4. Revise se as datas fazem sentido para:
   1. o tipo de dia do cenário,
   2. a(s) linha(s) envolvida(s),
   3. e a janela operacional real que você quer cobrir.
5. Confirme que você não está deixando um intervalo amplo demais por engano.
6. Se o cenário deve se aplicar a um período curto, limite a janela com precisão.
7. Confirme a publicação para o(s) intervalo(s) escolhido(s).

Para o caso de referência, pergunte-se:
1. A publicação cobre exatamente os dias úteis que eu quero implantar?
2. Eu estou evitando publicar mais dias do que o necessário?
3. A solução corresponde de fato às datas selecionadas?

Quando você terminar esta seção, deverá ter definido uma janela temporal clara e controlada para a implantação.

## Confirmando a publicação e mudando o status do cenário

Depois de selecionar o intervalo temporal, você precisa confirmar a ação de publicação. Neste ponto, a solução deixa de ser apenas um cenário validado e passa a ter papel operacional no calendário.

Antes de continuar, certifique-se de que:
1. Você selecionou as datas corretamente.
2. Você revisou o cenário validado.
3. Você está pronto para que a solução avance no ciclo de vida.

Para publicar o cenário:
1. Revise pela última vez o resumo de publicação.
2. Confirme:
   1. o nome do cenário,
   2. o intervalo temporal,
   3. e o contexto operacional ao qual se aplicará.
3. Execute **Publicar**.
4. Verifique se o status do cenário muda para **Publicação** enquanto o sistema processa a implantação.
5. Aguarde o processo terminar.
6. Verifique se o status final da solução muda para **Publicada**.
ref: P16_Imagen3.png | compact
7. Se o status não mudar como esperado, verifique se houve um problema técnico ou de elegibilidade do cenário.

Para o caso de referência, não considere a publicação concluída até poder afirmar:
1. A solução do cenário de L1 saiu de **Validada**.
2. A plataforma processou a publicação.
3. O status final da solução do cenário é **Publicada**.

Quando você terminar esta seção, deverá ter um cenário implantado no calendário operacional para o período selecionado.

## Verificando que a solução publicada é a que ficou em vigor

Depois de publicar, você precisa confirmar que a solução que ficou ativa é realmente a correta. Publicar não deve ser um passo cego. Você deve conseguir verificar qual cenário ficou vigente para as datas escolhidas e manter rastreabilidade sobre a solução implantada.

Antes de começar esta seção, certifique-se de que:
1. A solução do cenário já chegou ao status **Publicada**.
2. Você sabe quais datas ela cobre.
3. Você sabe qual serviço/linha deve ser afetado pela publicação.

Para verificar a implantação:
1. Volte para a tabela principal de cenários.
2. Filtre ou revise cenários por status.
3. Confirme que o cenário publicado aparece como **Publicada**.
4. Revise as datas de aplicação, se a visão permitir.
5. Confirme que você não está confundindo este cenário com outro validado mas não implantado.
6. Se o seu processo interno exigir, registre ou comunique que esta versão já é a solução operacional vigente.
7. Preserve nome, descrição e intervalo temporal como base de rastreabilidade para auditoria posterior.

Para o caso de referência, garanta que:
1. O cenário publicado corresponde à L1 dia útil.
2. As datas coincidem com o período que você queria implantar.
3. Nenhum outro cenário ficou ativo por engano.

Quando você terminar esta seção, deverá ter certeza de qual solução ficou em vigor e para qual período exato.

## Mantendo rastreabilidade e preparando a próxima iteração

Depois de publicar o cenário, o trabalho não some: muda de foco. A solução implantada pode virar referência para auditoria, comparação ou uma iteração futura. Não é recomendável reutilizar sem controle um cenário já publicado para experimentar mudanças estruturais; o mais seguro é criar uma nova iteração quando você precisar propor uma melhoria.

Antes de terminar, certifique-se de que:
1. O cenário já está publicado.
2. Está claro qual intervalo temporal ele cobre.
3. Você sabe se o próximo passo será auditar resultados ou preparar uma nova iteração.

Para manter rastreabilidade após publicar:
1. Mantenha o cenário publicado com nome e descrição claros.
2. Use o status **Publicada** como referência para distingui-lo de cenários em rascunho, cálculo ou validação.
3. Se precisar propor uma melhoria, crie um novo cenário em vez de alterar a lógica histórica do cenário implantado.
4. Se a sua equipe faz revisão posterior, use esta versão publicada como linha de base de comparação.
5. Mantenha um registro interno de:
   1. o que foi publicado,
   2. quando foi publicado,
   3. e para quais datas ficou vigente.

Para o caso de referência, finalize este quick start apenas quando puder afirmar:
1. A solução da L1 já está publicada.
2. Você sabe exatamente a partir de que data ela ficou vigente.
3. Você consegue distinguir esta versão publicada de qualquer iteração futura.

Quando você terminar esta seção, deverá ter uma solução publicada, rastreável e pronta para servir como referência operacional ou como ponto de partida para uma nova iteração.

## Leituras adicionais

- [Criando uma nova iteração do cenário a partir de uma solução publicada](P17_Criando_uma_nova_iteracao_do_cenario.md)

