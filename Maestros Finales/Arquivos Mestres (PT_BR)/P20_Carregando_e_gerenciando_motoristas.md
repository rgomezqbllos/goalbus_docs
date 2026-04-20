---
title: Carregando e gerenciando motoristas
shortTitle: Motoristas
intro: 'Aprenda a criar, importar e manter a base de motoristas no GoalBus, revisar o perfil operacional e deixar uma base confiável antes de passar para adscrição, regras e cálculo de Rostering.'
contentType: how-tos
versions:
  - '*'
---

## Criando ou importando a base de motoristas

Antes de falar de regras de Rostering, ausências ou atribuição de turnos, você precisa ter uma base confiável de motoristas. No GoalBus, a gestão de motoristas atua como a principal fonte de verdade para a operação humana: permite combinar criação manual e carga em massa e concentra identidade, vínculo ao depósito e disponibilidade em um único diretório.

Use este quick start quando você já tiver clara a transição de Scheduling para Rostering e precisar preparar o coletivo real de pessoas que participará da alocação.

Antes de começar, certifique-se de que:
1. Você já fechou a transição desde Scheduling no P19.
2. Você sabe qual coletivo de motoristas participará do cálculo.
3. Você sabe se vai cadastrar poucos motoristas manualmente ou se precisa de carga em massa.
4. Você tem acesso ao ambiente com permissões para gerenciar pessoal.

Para este quick start, use este caso de referência:

> **Vou carregar e revisar a base de motoristas que poderá cobrir a solução da L1 antes de entrar em adscrição, regras e disponibilidade.**

Para criar ou importar a base de motoristas:
1. No GoalBus, vá em **Configuração** > **Pessoal** > **Gestão de motoristas**.
ref: P20_Imagen1.png | compact
2. Verifique se os motoristas do caso já existem na lista geral.
3. Se você precisar criar poucos motoristas, clique em **Novo Motorista**.
ref: P20_Imagen2.png | compact
4. Se precisar carregar muitos motoristas, faça uma importação em massa via CSV em **Carga de pessoal**.
ref: P20_Imagen3.png | compact
5. Se escolher importação em massa, prepare o arquivo com os dados mínimos para identificar corretamente cada pessoa. A janela de importação ajuda a preparar o CSV.
ref: P20_Imagen4.png
6. Execute a carga e revise o resultado.
7. Volte à lista geral e confirme que os motoristas aparecem corretamente.
8. Se detectar duplicados ou registros incompletos, corrija antes de seguir.

Para o caso de referência, finalize esta seção apenas quando puder afirmar:
1. Os motoristas da L1 já estão cadastrados ou importados.
2. A lista geral reflete uma única base de referência.
3. Você já consegue abrir o perfil de cada motorista para revisar o contexto operacional.

Quando você terminar esta seção, deverá ter uma base de motoristas carregada e visível no sistema.

## Revisando o perfil do motorista e seus dados estruturais

Depois de criar a base, você precisa revisar o **perfil do motorista**. O perfil não é apenas uma ficha de contato: é o dossiê digital completo do empregado na operação. Ali convivem dados estáticos, contexto operacional e atributos que o sistema usará mais adiante para raciocinar sobre elegibilidade.

Antes de começar esta seção, certifique-se de que:
1. Você já tem motoristas visíveis na lista geral.
2. Você sabe qual motorista ou grupo vai usar como amostra.
3. Você quer validar que o registro é operacional, e não apenas administrativo.

Para revisar o perfil do motorista:
1. Na lista geral, clique no nome de um motorista.
ref: P20_Imagen5.png | full
2. Revise a barra lateral de dados estáticos.
3. Verifique ao menos estes grupos de informação:
   1. dados básicos como nome e código,
   2. dados operacionais como acordo coletivo ou tipo de contrato,
   3. vínculos operacionais como depósito principal, grupo de trabalho, área ou tipos de veículos autorizados.
4. Se faltar algum dado estrutural importante, complete antes de seguir.
5. Salve qualquer alteração necessária.
6. Repita a revisão em vários motoristas para confirmar consistência na base.

Para o caso de referência, revise ao menos:
1. O código do motorista.
2. O depósito principal.
3. O grupo de trabalho.
4. Propriedades operacionais que condicionam a alocação posterior.

Quando você terminar esta seção, deverá estar claro que cada motorista tem um registro operacional coerente e utilizável.

## Revisando o contexto operacional e os dados dinâmicos do motorista

Além dos dados estruturais, o perfil do motorista pode incluir dados dinâmicos que afetam diretamente como o sistema raciocina sobre a pessoa. Na aba de administração, você pode revisar contadores e padrões de trabalho usados mais adiante pela lógica de alocação.

Antes de começar esta seção, certifique-se de que:
1. Você já revisou os dados estáticos do perfil.
2. Você sabe se a operação usa contadores ou padrões cíclicos.
3. Você quer verificar que o motorista tem um contexto operacional interpretável.

Para revisar o contexto operacional dinâmico:
1. Dentro do perfil do motorista, abra a aba **Detalhes de administração**.
2. Revise os **contadores** ou KPIs associados ao motorista, se existirem.
3. Verifique se o motorista está vinculado a algum **padrão de trabalho**.
4. Se a operação usa padrões cíclicos, revise o deslocamento/posição atual do motorista dentro do padrão.
5. Confirme que esses dados fazem sentido para o contexto real.
6. Se a informação dinâmica não estiver correta, ajuste antes de passar para regras ou cálculo.

Para o caso de referência, pergunte-se:
1. Este motorista tem o padrão que deveria ter?
2. Contadores/KPIs estão disponíveis se o processo precisar?
3. O sistema conseguiria raciocinar corretamente sobre essa pessoa em um cálculo de alocação?

Quando você terminar esta seção, deverá ter validado não apenas a identidade do motorista, mas também seu contexto operacional dinâmico.

## Validando habilitações antes de usar o motorista no Rostering

Antes de considerar um motorista elegível, você precisa revisar suas **habilitações**. Elas respondem: “essa pessoa pode trabalhar legal ou tecnicamente neste depósito, grupo ou unidade?”. Elas são gerenciadas em uma linha do tempo com datas de início e fim, e o sistema mostra estados como ativo, futuro, expirado ou prestes a expirar. Se uma pessoa não estiver habilitada para o contexto requerido, o motor gera erro ao tentar alocá-la.

Antes de começar esta seção, certifique-se de que:
1. Você já revisou o perfil do motorista.
2. Você sabe qual depósito, grupo ou unidade é necessário no seu caso.
3. Você entende que habilitação não é o mesmo que cessão ou adscrição temporária.

Para revisar e validar habilitações:
1. Dentro do perfil do motorista, abra a aba **Habilitações / Qualificações**.
2. Verifique se existem registros vigentes para:
   1. depósitos,
   2. grupos de trabalho,
   3. unidades de negócio.
3. Verifique o status de cada habilitação:
   1. ativa,
   2. futura,
   3. prestes a expirar,
   4. expirada.
4. Se faltar uma habilitação necessária, adicione com as datas corretas.
5. Se uma habilitação já expirou e não deve ser usada, mantenha como histórico.
6. Salve as alterações.
7. Confirme que o motorista já está habilitado para o contexto onde você espera usá-lo.

Para o caso de referência, não prossiga até poder afirmar:
1. O motorista está habilitado para o depósito correto.
2. O grupo de trabalho requerido está coberto.
3. Não há expirações que quebrem a elegibilidade atual.

Quando você terminar esta seção, deverá ter motoristas que não só existem na base, mas também são elegíveis do ponto de vista operacional e normativo.

## Confirmando que a base já está pronta para a próxima camada de Rostering

O último passo é verificar que a base de motoristas já está pronta para entrar na próxima camada: adscrição operativa, regras, ausências e cálculo. O objetivo aqui não é só ter nomes carregados, mas uma base coerente, rastreável e utilizável pelo motor.

Antes de terminar, certifique-se de que:
1. Você já carregou ou importou a base.
2. Você já revisou os perfis principais.
3. Você já conferiu dados estruturais e dinâmicos.
4. Você já validou habilitações essenciais.

Para confirmar que a base está preparada:
1. Volte à lista geral de motoristas.
2. Verifique que o coletivo necessário para o seu caso está presente.
3. Confirme que perfis críticos não têm lacunas importantes.
4. Garanta que as pessoas que você espera usar estão habilitadas para o contexto correto.
5. Pergunte-se se o sistema já poderia usar essa base como ponto de partida para:
   1. adscrição operativa,
   2. regras de Rostering,
   3. e disponibilidade real.
6. Se a resposta for sim, continue com o próximo quick start.
7. Se a resposta for não, corrija a base de motoristas antes de seguir.

Para o caso de referência, finalize este quick start apenas quando puder afirmar:
1. A base de motoristas da L1 já está carregada.
2. Perfis-chave já foram revisados.
3. Habilitações essenciais já estão vigentes.
4. A base já está pronta para passar para adscrição operativa.

Quando você terminar esta seção, deverá ter uma base de motoristas suficientemente sólida para continuar com a próxima camada do Rostering.

## Leituras adicionais

- [Gerenciando a adscrição operacional do motorista](P21_Gerenciando_a_adscricao_operacional_do_motorista.md)

