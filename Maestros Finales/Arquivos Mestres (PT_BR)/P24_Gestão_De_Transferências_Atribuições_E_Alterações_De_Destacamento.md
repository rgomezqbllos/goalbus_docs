---
title: Gestão de transferências, atribuições e alterações de destacamento
shortTitle: Atribuições e alterações
intro: Saiba como gerenciar mudanças no contexto operacional do Motoristas, distinguindo
  entre transferência, atribuição e mudança de destacamento para que o Alocação use
  cada pessoa na área certa sem perder a rastreabilidade.
contentType: how-tos
versions:
- '*'
---
## Compreender a diferença entre transferência, atribuição e mudança de destacamento

Antes de calcular o Alocação, você precisa distinguir corretamente os movimentos da equipe entre contextos operacionais. Nem todas as situações significam a mesma coisa. Um Motorista ainda pode pertencer ao seu depósito principal, mas trabalhar temporariamente em outro. Ele também pode mudar o destacamento mais estável. Se você misturar esses conceitos, a elegibilidade da equipe torna-se confusa e o cálculo pode atribuir o trabalho no contexto errado.

Use este início rápido quando você já tiver o Motoristas carregado, revise seu destacamento principal e modele seu Ausências e inatividades, e você precisa refletir movimentos reais entre tanques, grupos ou unidades.

Antes de começar, certifique-se de que:
1. Você já carregou e verificou o Motoristas no P20.
2. Você já tem Validado o destacamento operacional para P21.
3. Você já definiu as regras Alocação para P22.
4. Você já registrou Ausências, inatividade e disponibilidade no P23.
5. Você sabe o que as pessoas vão mudar de contexto e durante que período.

Para este início rápido, use este caso de referência:

> **Vou gravar que um dos Motoristas que normalmente pertence ao Depósito Norte irá trabalhar temporariamente em outro contexto, e que outro Motorista irá mudar o destacamento mais estável antes do cálculo Alocação.**

Para distinguir corretamente cada movimento:
1. Ele usa um **atribuição** quando a pessoa ainda pertence ao seu contexto principal, mas vai trabalhar temporariamente em outro.
2. Use um **transferência** quando a pessoa mudar de contexto de forma mais estrutural ou permanente.
3. Use um **Alteração do destacamento** quando você precisar atualizar formalmente o tanque, grupo ou unidade base a partir do qual o sistema deve tratar o Motorista.
4. Não use um Ausência para modelar uma mudança de contexto operacional.
5. Não use uma atribuição para corrigir um destacamento principal mal configurado.

Mantenha estas perguntas como um guia:
1. Onde é que esta pessoa normalmente pertence?
2. Onde você vai realmente trabalhar durante este período?
3. Esse movimento é temporário ou estrutural?

Quando você terminar este Seção, você deve estar claro que tipo de registro corresponde a cada mudança de contexto.

## Gravação de uma transferência temporária do Motorista

A cessão serve para refletir que um Motorista trabalhará temporariamente fora do seu contexto habitual sem perder seu destacamento base. Isto é útil quando uma pessoa continua a pertencer ao seu depósito, unidade ou grupo principal, mas vai operar por algum tempo em outro ambiente.

Antes de iniciar este Seção, certifique-se de que:
1. Já identificou a pessoa que será transferida.
2. Sabes qual é o contexto principal deles.
3. Você já conhece o contexto de destino temporário e as datas de aplicação.

Para registar uma designação temporária:
1. Abra o perfil do Motorista na lista geral.
2. Vá para o **movimentos**, **Despacho temporário** ou **atribuições** Seção, dependendo da vista disponível.
3. Cria um novo registro de atribuições.
4. Definir:
   1. o **contexto de origem**,
   2. o **Contexto de destino**,
   3. o **Data de início**,
   4. o **Data de fim**,
   5. e quaisquer observações necessárias.
5. Mantém o registo.
6. Verifique se o Motorista ainda mantém o seu destacamento principal.
7. Constata que durante o período de atribuição o sistema pode lidar com ele no período de tempo correto.

Para o caso de referência, uma designação válida seria:
1. Motorista ligado ao Norte Garagem,
2. Cedido durante duas semanas ao Depósito Sul,
3. sem alterar o seu destacamento histórico principal.

Quando você terminar este Seção, você deve ter uma atribuição temporária modelada corretamente sem perder rastreabilidade estrutural.

## Gravar uma transferência ou alteração mais estável

Ao contrário da cessão, uma transferência responde a um movimento mais estrutural. Aqui não é mais apenas uma questão de trabalhar temporariamente em outro contexto, mas de mover mais estávelmente a pertenência operacional do Motorista.

Antes de iniciar este Seção, certifique-se de que:
1. Você já identificou a pessoa que vai mudar de contexto de uma forma mais duradoura.
2. Você sabe que depósito, unidade ou grupo se tornará seu novo contexto principal.
3. Você já não está falando de uma necessidade temporária ou excepcional.

Para registar uma transferência ou alteração estrutural:
1. Abra o perfil do Motorista.
2. Revise o seu actual destacamento principal.
3. Crie o movimento de transferência ou atualize o destacamento principal, dependendo do fluxo que o seu ambiente usa.
4. Definir:
   1. o novo **depósito principal**,
   2. o novo **Unidade de negócio**,
   3. o novo **Grupo de trabalho**, se alterado,
   4. e a data de eficácia.
5. Salve as mudanças.
6. Verifique se o perfil já reflete o novo contexto principal.
7. Verifica que a alteração não deixou dados contraditórios entre o destacamento principal e as classificações.

Para o caso de referência, uma transferência válida seria:
1. Motorista que deixa de pertencer ao Norte Garagem,
2. torna-se um membro estável do Depósito Sul,
3. e a partir dessa data deverá ser tratada como um recurso contra essa nova base.

Quando você terminar este Seção, você deve ter modelado corretamente uma mudança de contexto estrutural.

## Revisão do impacto dos movimentos nas classificações e na elegibilidade

Depois de registrar as atribuições ou transferências, você precisa rever o seu impacto operacional. Mover uma pessoa entre contextos é inútil se a sua classificação ou elegibilidade não acompanhar a mudança. Aqui você deve confirmar que o Motorista não só mudou o contexto no perfil, mas também pode ser usado corretamente nesse novo ambiente.

Antes de continuar, certifique-se de que:
1. Já registaste pelo menos uma transferência ou transferência.
2. Você sabe em que contexto operacional a pessoa deve ser vista a partir de agora.
3. Você entende que uma mudança de contexto pode exigir a revisão de classificações atuais.

Revisão do impacto operacional do movimento:
1. Volte para a guia **classificações/Qualificaçãos** do Motorista.
2. Verifica as classificações atuais para o contexto de alvo.
3. Se faltar, adicione-as com as datas corretas antes do cálculo.
4. Verifica que a pessoa não é simultaneamente visível em contextos incompatíveis devido a um erro Configuração.
5. Verifica que o sistema pode considerar a pessoa elegível na área correta durante o período relevante.
6. Se você detectar contradições, corrija-as antes de ir para o cálculo do Alocação.

Para o caso de referência, certifique-se de que:
1. O Motorista transferido pode funcionar legalmente ou tecnicamente no contexto do destino,
2. o Motorista transferido já tem suas avaliações de acordo com o novo contexto,
3. a elegibilidade coincide com o movimento registado.

Quando você terminar este Seção, você deve ter movimentos de pessoal que também são operacionalmente utilizáveis.

## Confirmando que as alterações de contexto já estão prontas para o cálculo do Alocação

O último passo é verificar que a combinação entre destacamento principal, atribuições, transferências e avaliações já está suficientemente clara para alimentar o cálculo. Aqui o objetivo é evitar dois erros:
1. atribuir a uma pessoa num contexto em que não deve aparecer,
2. ou excluir uma pessoa que deve ser elegível para uma mudança já registada.

Antes de terminar, certifique-se de que:
1. Já registaste os movimentos temporais ou estruturais necessários.
2. Já revisou o impacto deles na elegibilidade.
3. Você sabe que coletivo vai participar no seguinte cálculo.

Para confirmar que esta camada já está pronta:
1. Volte para a lista geral de Motoristas.
2. Revisar vários perfis afetados por mudanças de contexto.
3. Verifica que:
   1. as atribuições são consideradas temporárias,
   2. as transferências reflectem-se como alterações estruturais,
   3. e o destacamento principal permanece coerente, se for caso disso.
4. Pergunte-se se o sistema já poderia:
   1. utilizar o Motorista correto no contexto correto,
   2. durante o período correto,
   3. sem confusão de pertencimento estrutural com deslocamento temporário.
5. Se a resposta for sim, continue com o próximo início rápido.
6. Se a resposta for não, corrigir movimentos ou avaliações antes de continuar.

Para o caso de referência, não continue até poder dizer:
1. As alterações de contexto de L1 Motoristas já estão gravadas corretamente.
2. Sabes quem foi cedido, quem foi transferido e quem mantém o destacamento original.
3. A base já está pronta para executar o primeiro cálculo Alocação.

Quando você terminar este Seção, você deve ter o contexto organizacional da equipe suficientemente claro para passar para o cálculo de atribuição.

## Lecturas adicionais

- [Executando o primeiro cálculo Alocação](P25_Executando_O_Primeiro_Cálculo_Alocação.md)
