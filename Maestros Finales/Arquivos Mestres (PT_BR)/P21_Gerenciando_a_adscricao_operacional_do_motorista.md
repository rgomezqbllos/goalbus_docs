---
title: Gerenciando a adscrição operacional do motorista
shortTitle: Adscrição operativa
intro: 'Aprenda a vincular cada motorista ao seu depósito, unidade de negócio e grupo de trabalho e entender como essa adscrição condiciona a elegibilidade real antes de passar para regras, ausências e cálculo de Rostering.'
contentType: how-tos
versions:
  - '*'
---

## Entendendo a adscrição operacional do motorista

Antes de definir regras avançadas, ausências ou cálculos de Rostering, você precisa entender como cada motorista fica **adscrito** dentro da organização. No GoalBus, a adscrição operativa não se baseia em um único campo. Ela é construída combinando três coordenadas principais:
1. **Depósito**
2. **Unidade de negócio**
3. **Grupo de trabalho**

Essa combinação define de onde a pessoa trabalha, a que divisão pertence e que tipo de tarefas pode receber. Também condiciona a visibilidade do recurso para planejadores e gerentes.

Use este quick start quando você já tiver carregado a base de motoristas e precisar garantir que cada pessoa está no contexto operacional correto antes de passar para regras e disponibilidade.

Antes de começar, certifique-se de que:
1. Você já carregou e revisou motoristas no P20.
2. Você sabe quais depósitos, unidades e grupos a operação usa.
3. Você tem claro qual coletivo participará do cálculo de Rostering.
4. Você sabe que uma adscrição ruim pode tornar uma pessoa inelegível mesmo existindo no sistema.

Para este quick start, use este caso de referência:

> **Vou revisar que os motoristas que cobrirão a linha L1 estão adscritos ao depósito, unidade e grupo de trabalho corretos antes de configurar regras e disponibilidade.**

Para entender a adscrição operativa:
1. Trate o **depósito** como a base física do recurso.
2. Trate a **unidade de negócio** como a divisão estratégica/modal à qual a pessoa pertence.
3. Trate o **grupo de trabalho** como a função que determina que tipo de tarefas pode receber.
4. Use esta regra:
   1. depósito responde a **onde trabalha**,
   2. unidade responde a **em qual negócio/modo opera**,
   3. grupo responde a **que tipo de trabalho pode fazer**.
5. Não misture esses conceitos como se fossem a mesma coisa.

Quando você terminar esta seção, deverá ter claro que a adscrição operativa é uma estrutura composta e não um atributo isolado.

## Revisando depósito, unidade e grupo de trabalho no perfil do motorista

Depois de entender a lógica, você precisa verificar como ela está configurada no perfil real do motorista. Esses campos fazem parte do “DNA estrutural” do empregado e são a base do contexto operacional. Se estiverem mal definidos, a alocação posterior fica contaminada desde a origem.

Antes de começar esta seção, certifique-se de que:
1. Você já tem motoristas cadastrados na base.
2. Você sabe qual motorista (ou grupo) vai usar como amostra.
3. Você quer revisar a adscrição estrutural e não uma cessão temporária.

Para revisar a adscrição no perfil:
1. Na lista geral de motoristas, abra o perfil de uma pessoa.
2. Revise a barra lateral de dados estruturais.
3. Verifique ao menos:
   1. **Depósito principal**
   2. **Unidade de negócio**
   3. **Grupo de trabalho**
   4. **Área**, se a operação usar
4. Confirme que esses valores coincidem com o contexto real onde a pessoa deveria trabalhar.
5. Se um dado estiver incorreto, atualize no perfil.
6. Salve as alterações.
7. Repita a revisão em vários motoristas para confirmar consistência.

Para o caso de referência, verifique que:
1. Os motoristas da L1 pertencem ao depósito correto.
2. A unidade de negócio coincide com o modo/negócio esperado.
3. O grupo de trabalho é realmente **Motoristas** e não outro papel.

Quando você terminar esta seção, deverá ter revisado a adscrição estrutural dos motoristas que participarão do cálculo.

## Entendendo a diferença entre adscrição principal, habilitação e cessão

Antes de seguir, você precisa distinguir três conceitos que costumam ser confundidos:
1. **Adscrição principal**
2. **Habilitação**
3. **Cessão/transferência temporária**

A adscrição principal define onde a pessoa pertence de forma estrutural. A habilitação responde se ela **pode** trabalhar legal/técnicamente em outro contexto. A cessão responde onde **está trabalhando de fato** durante um período. Essas camadas convivem, mas não significam a mesma coisa.

Antes de começar esta seção, certifique-se de que:
1. Você já revisou a adscrição principal no perfil.
2. Você sabe que algumas pessoas podem trabalhar fora do contexto principal.
3. Você quer evitar confusões entre “pertence a”, “pode trabalhar em” e “está trabalhando em”.

Para distinguir corretamente:
1. Use **adscrição principal** para descrever o contexto estrutural base do motorista.
2. Use **habilitação** para indicar que o motorista pode trabalhar em outro depósito, grupo ou unidade.
3. Use **cessão** para indicar que o motorista está temporariamente deslocado para outro contexto.
4. Não use uma cessão para corrigir uma adscrição principal mal definida.
5. Não use uma habilitação como se fosse um deslocamento ativo.
6. Mantenha estas perguntas como guia:
   1. Onde a pessoa pertence? → adscrição principal
   2. Onde poderia trabalhar legalmente? → habilitação
   3. Onde está trabalhando agora? → cessão

Para o caso de referência, pergunte-se:
1. O motorista pertence ao Depósito Norte?
2. Ele pode trabalhar em outro depósito se necessário?
3. Ele está cedido temporariamente para outra base ou segue no contexto habitual?

Quando você terminar esta seção, deverá ter uma leitura correta da hierarquia entre adscrição, habilitação e cessão.

## Validando que a adscrição permite ver e atribuir corretamente o motorista

A adscrição não serve apenas para descrever o perfil. Ela também condiciona como o sistema vê a pessoa e que tarefas ela pode receber. Uma pessoa mal adscrita pode ficar fora do filtro correto, aparecer no lugar errado ou receber tarefas indevidas. O contrário também pode ocorrer: uma pessoa válida pode ficar oculta/inelegível por uma adscrição mal definida.

Antes de continuar, certifique-se de que:
1. Você já revisou depósito, unidade e grupo em vários perfis.
2. Você entende a diferença entre adscrição e cessão.
3. Você sabe qual coletivo participará do próximo cálculo.

Para validar o impacto operativo da adscrição:
1. Revise qual conjunto de motoristas deveria estar visível no contexto do seu cálculo.
2. Verifique que as pessoas corretas aparecem no depósito, unidade e grupo corretos.
3. Revise se há motoristas no grupo errado.
4. Revise se há motoristas que deveriam pertencer ao contexto e não aparecem.
5. Se detectar erro de adscrição, corrija antes de passar para regras ou disponibilidade.
6. Salve a configuração final dos perfis afetados.

Para o caso de referência, garanta que:
1. Os motoristas que cobrirão L1 aparecem no contexto operacional correto.
2. Não se misturam com coletivos que não deveriam receber tarefas de condução.
3. O sistema conseguiria filtrar e atribuir apenas o pessoal relevante.

Quando você terminar esta seção, deverá ter uma base de adscrição operativa que ajuda o sistema a ver e usar as pessoas corretas.

## Confirmando que a adscrição operativa já está pronta para a próxima camada

O último passo é verificar que a adscrição ficou sólida o suficiente para continuar com regras, ausências e cálculo. O objetivo aqui não é apenas preencher campos, e sim deixar uma estrutura clara que o motor possa interpretar sem ambiguidades.

Antes de terminar, certifique-se de que:
1. Você já revisou a adscrição estrutural dos perfis-chave.
2. Você já distingue adscrição, habilitação e cessão.
3. Você já validou que o coletivo visível é o correto.
4. Você já corrigiu os principais desajustes.

Para confirmar que a adscrição está preparada:
1. Volte à lista geral de motoristas.
2. Verifique que o coletivo relevante para o caso aparece no contexto correto.
3. Confirme que não há erros óbvios de depósito, unidade ou grupo.
4. Pergunte-se se o sistema já poderia:
   1. filtrar corretamente os motoristas do caso,
   2. aplicar regras do coletivo correto,
   3. e tratá-los como base para disponibilidade e cálculo.
5. Se a resposta for sim, continue com o próximo quick start.
6. Se a resposta for não, corrija a adscrição antes de seguir.

Para o caso de referência, não prossiga até poder afirmar:
1. Os motoristas da L1 estão adscritos ao contexto correto.
2. Você sabe distinguir quem pertence, quem pode trabalhar e quem está cedido.
3. A base já está pronta para aplicar regras de Rostering e disponibilidade.

Quando você terminar esta seção, deverá ter uma adscrição operativa suficientemente clara para continuar com a próxima camada do processo.

## Leituras adicionais

- [Definindo regras de Rostering para a alocação de pessoal](P22_Definindo_regras_de_rostering_para_alocacao_de_pessoal.md)

