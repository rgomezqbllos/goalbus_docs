---
title: Gerenciando transferências, cessões e mudanças de adscrição
shortTitle: Cessões e mudanças
intro: 'Aprenda a gerenciar mudanças de contexto operacional dos motoristas, distinguindo entre transferência, cessão e mudança de adscrição para que o Rostering use cada pessoa no âmbito correto sem perder rastreabilidade.'
contentType: how-tos
versions:
  - '*'
---

## Entendendo a diferença entre transferência, cessão e mudança de adscrição

Antes de calcular o Rostering, você precisa distinguir corretamente os movimentos de pessoal entre contextos operacionais. Nem todas as situações significam a mesma coisa. Um motorista pode continuar pertencendo ao seu depósito principal, mas trabalhar temporariamente em outro. Também pode mudar de adscrição de forma mais estável. Se você misturar esses conceitos, a elegibilidade fica confusa e o cálculo pode atribuir trabalho no contexto errado.

Use este quick start quando você já tiver motoristas carregados, adscrição principal revisada e ausências/inatividades modeladas, e precisar refletir movimentos reais entre depósitos, grupos ou unidades.

Antes de começar, certifique-se de que:
1. Você já carregou e revisou motoristas no P20.
2. Você já validou a adscrição operativa no P21.
3. Você já configurou regras de Rostering no P22.
4. Você já registrou ausências, inatividades e disponibilidade no P23.
5. Você sabe quais pessoas mudarão de contexto e por qual período.

Para este quick start, use este caso de referência:

> **Vou registrar que um motorista que normalmente pertence ao Depósito Norte trabalhará temporariamente em outro contexto, e que outro motorista mudará de adscrição de forma mais estável antes do cálculo de Rostering.**

Para distinguir corretamente cada movimento:
1. Use uma **cessão** quando a pessoa continua pertencendo ao contexto principal, mas trabalhará temporariamente em outro.
2. Use uma **transferência** quando a pessoa muda de contexto de forma mais estrutural ou permanente.
3. Use uma **mudança de adscrição** quando você precisa atualizar formalmente o depósito/grupo/unidade base que o sistema deve usar.
4. Não use uma ausência para modelar mudança de contexto operacional.
5. Não use uma cessão para corrigir uma adscrição principal mal configurada.

Mantenha estas perguntas como guia:
1. Onde essa pessoa normalmente pertence?
2. Onde ela vai trabalhar de fato neste período?
3. O movimento é temporal ou estrutural?

Quando você terminar esta seção, deverá ter claro qual tipo de registro corresponde a cada mudança de contexto.

## Registrando uma cessão temporária do motorista

A cessão serve para refletir que um motorista trabalhará temporariamente fora do contexto habitual sem perder sua adscrição base. Isso é útil quando a pessoa continua pertencendo ao depósito/unidade/grupo principal, mas operará por um tempo em outro ambiente.

Antes de começar esta seção, certifique-se de que:
1. Você já identificou a pessoa que será cedida.
2. Você sabe qual é o contexto principal.
3. Você conhece o contexto de destino e as datas de aplicação.

Para registrar uma cessão temporária:
1. Abra o perfil do motorista na lista geral.
2. Vá para a seção de **movimentos**, **adscrição temporária** ou **cessões**.
3. Crie um novo registro de cessão.
4. Defina:
   1. **contexto de origem**,
   2. **contexto de destino**,
   3. **data de início**,
   4. **data de fim**,
   5. e observações necessárias.
5. Salve o registro.
6. Verifique que o motorista continua com a adscrição principal.
7. Verifique que durante o período o sistema o trata no contexto temporal correto.

Para o caso de referência, uma cessão válida seria:
1. motorista adscrito ao Depósito Norte,
2. cedido por duas semanas ao Depósito Sul,
3. sem mudar a adscrição principal histórica.

Quando você terminar esta seção, deverá ter uma cessão temporária modelada corretamente sem perder rastreabilidade estrutural.

## Registrando uma transferência ou mudança mais estável

Diferente da cessão, a transferência responde a um movimento mais estrutural. Aqui não se trata apenas de trabalhar temporariamente em outro contexto, e sim de mudar de forma mais estável o pertencimento operacional do motorista.

Antes de começar esta seção, certifique-se de que:
1. Você identificou a pessoa que mudará de contexto por mais tempo.
2. Você sabe qual depósito/unidade/grupo passará a ser o novo contexto principal.
3. Isso não é uma necessidade temporária/excepcional.

Para registrar uma transferência/mudança estrutural:
1. Abra o perfil do motorista.
2. Revise a adscrição principal atual.
3. Crie o movimento de transferência ou atualize a adscrição principal, conforme o fluxo do seu ambiente.
4. Defina:
   1. o novo **depósito principal**,
   2. a nova **unidade de negócio**,
   3. o novo **grupo de trabalho**, se mudar,
   4. e a data de efetividade.
5. Salve as alterações.
6. Verifique que o perfil reflete o novo contexto principal.
7. Confirme que a mudança não deixou dados contraditórios entre adscrição e habilitações.

Para o caso de referência, uma transferência válida seria:
1. motorista deixa de pertencer ao Depósito Norte,
2. passa a pertencer ao Depósito Sul de forma estável,
3. e a partir dessa data deve ser tratado como recurso da nova base.

Quando você terminar esta seção, deverá ter modelado corretamente uma mudança estrutural de contexto.

## Revisando o impacto do movimento em habilitações e elegibilidade

Depois de registrar cessões ou transferências, você precisa revisar o impacto operacional. Mover uma pessoa entre contextos não serve se habilitações/elegibilidade não acompanham. Aqui você confirma que o motorista não só mudou no perfil, mas também pode ser usado corretamente no novo ambiente.

Antes de continuar, certifique-se de que:
1. Você já registrou pelo menos uma cessão ou transferência.
2. Você sabe em qual contexto a pessoa deveria aparecer a partir de agora.
3. Você entende que a mudança pode exigir revisar habilitações vigentes.

Para revisar o impacto operacional:
1. Volte à aba de **habilitações/qualificações** do motorista.
2. Verifique se há habilitações vigentes para o contexto de destino.
3. Se faltar, adicione com datas corretas antes do cálculo.
4. Verifique que a pessoa não fica simultaneamente visível em contextos incompatíveis por erro.
5. Confirme que o sistema poderá considerá-la elegível no âmbito correto durante o período.
6. Se detectar contradições, corrija antes do cálculo de Rostering.

Para o caso de referência, garanta que:
1. o motorista cedido pode trabalhar legal/técnicamente no contexto de destino,
2. o motorista transferido tem habilitações alinhadas ao novo contexto,
3. a elegibilidade coincide com o movimento registrado.

Quando você terminar esta seção, deverá ter movimentos de pessoal operativamente utilizáveis.

## Confirmando que os mudanças de contexto já estão prontas para o cálculo de Rostering

O último passo é verificar que a combinação entre adscrição principal, cessões/transferências e habilitações já está clara o suficiente para alimentar o cálculo. Evite dois erros:
1. atribuir a pessoa em um contexto em que não deveria aparecer,
2. deixar de fora alguém que deveria ser elegível por mudança registrada.

Antes de terminar, certifique-se de que:
1. Você já registrou movimentos temporais/estruturais necessários.
2. Você já revisou o impacto na elegibilidade.
3. Você sabe qual coletivo participará do próximo cálculo.

Para confirmar que esta camada está preparada:
1. Volte à lista geral de motoristas.
2. Revise perfis afetados por mudanças de contexto.
3. Verifique que:
   1. cessões aparecem como temporais,
   2. transferências aparecem como estruturais,
   3. e a adscrição principal permanece coerente quando aplicável.
4. Pergunte-se se o sistema já poderia:
   1. usar o motorista correto no contexto correto,
   2. durante o período correto,
   3. sem confundir pertencimento estrutural com deslocamento temporal.
5. Se a resposta for sim, continue com o próximo quick start.
6. Se a resposta for não, corrija movimentos ou habilitações antes de seguir.

Para o caso de referência, não prossiga até poder afirmar:
1. Mudanças de contexto dos motoristas da L1 estão corretamente registradas.
2. Você sabe quem está cedido, quem foi transferido e quem mantém a adscrição original.
3. A base já está pronta para executar o primeiro cálculo de Rostering.

Quando você terminar esta seção, deverá ter o contexto organizacional do pessoal claro o suficiente para passar ao cálculo de alocação.

## Leituras adicionais

- [Executando o primeiro cálculo de Rostering](P25_Executando_o_primeiro_calculo_de_rostering.md)

