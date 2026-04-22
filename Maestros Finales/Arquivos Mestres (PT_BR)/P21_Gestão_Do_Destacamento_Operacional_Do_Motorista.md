---
title: Gestão do destacamento operacional do Motorista
shortTitle: Despacho operacional
intro: Saiba como ligar cada Motorista com seu depósito, Unidade de negócio e grupo
  de trabalho, e entender como esse destacamento condiciona sua elegibilidade real
  antes de passar para as regras Alocação, Ausências e cálculo.
contentType: how-tos
versions:
- '*'
---
## Compreender o destacamento operacional do Motorista

Antes de definir regras avançadas, cálculos Ausências ou Alocação, você precisa entender como o **em destacamento** é deixado para cada Motorista dentro da organização. No GoalBus, o destacamento operacional não é baseado em um único campo. É construído combinando três coordenadas principais:
1. **Depósito**
2. **Unidade de negócio**
3. **Grupo de trabalho**

Esta combinação define onde a pessoa trabalha, a que divisão pertence e a que tipo de Tarefas pode receber. Também condiciona a visibilidade do recurso para planejadores e gestores. fileciteturn39file3L1-L20

Use este início rápido quando você já tiver o modelo Motorista carregado e precisa se certificar de que cada pessoa está localizada no contexto operacional certo antes de seguir para as regras e disponibilidade.

Antes de começar, certifique-se de que:
1. Você já carregou e verificou o Motoristas no P20.
2. Você sabe que depósitos, unidades e grupos usam sua operação.
3. Você está claro que grupo de equipe vai participar no cálculo Alocação.
4. Você sabe que o mau destacamento pode tornar uma pessoa inelegível mesmo que exista no sistema.

Para este início rápido, use este caso de referência:

> **Vou verificar que o Motoristas que irá cobrir o L1 Linha estão ligados ao depósito correto, unidade e força Tarefa antes de configurar regras e disponibilidade.**

Para compreender o destacamento operacional:
1. Trata o **depósito** como a localização da base física do recurso.
2. Trata **Unidade de negócio** como a divisão estratégica ou modal a que a pessoa pertence.
3. Trate o **Grupo de trabalho** como a função que determina o tipo de Tarefas que você pode receber.
4. Use esta regra de leitura:
   1. o depósito responde a **onde ele trabalha**,
   2. a unidade responde a **em que negócio ou modo opera**,
   3. o grupo responde a **que tipo de trabalho você pode fazer**.
5. Não misture esses três conceitos como se fossem os mesmos.

Quando você terminar este Seção, você deve estar claro que o destacamento operacional é uma estrutura composta e não um único atributo isolado. fileciteturn39file1turn39file3

## Tanque de verificação, unidade e Grupo de trabalho em Perfil do motorista

Uma vez que a lógica é compreendida, você precisa verificar como é configurada no Perfil do motorista real. Estes campos fazem parte do DNA estrutural do empregado e são a base do seu contexto operacional. Se estiverem mal definidos, o mapeamento traseiro está contaminado da fonte. fileciteturn39file0turn39file2

Antes de iniciar este Seção, certifique-se de que:
1. Você já tem o Motoristas criado no modelo.
2. Você sabe qual Motorista ou grupo você vai usar como uma amostra.
3. Você quer rever o destacamento estrutural, ainda não uma designação temporária.

Para rever o destacamento no perfil:
1. Na lista geral de Motoristas, abra o perfil de uma pessoa.
2. Verifique a barra lateral de dados estruturais.
3. Verifique pelo menos:
   1. **Depósito principal**
   2. **Unidade de negócio**
   3. **Grupo de trabalho**
   4. **Área**, se a sua operação o usar
4. Confirma que esses valores coincidem com o contexto real em que a pessoa deve trabalhar.
5. Se um dado estiver incorreto, atualize-o no perfil.
6. Salve as mudanças.
7. Repita a revisão sobre vários Motoristas para confirmar que o modelo é consistente.

No caso de referência, considera que:
1. L1 Motoristas pertence ao tanque correto.
2. O Unidade de negócio corresponde ao modo ou negócio esperado.
3. O Grupo de trabalho realmente corresponde a **Motoristas** e não a outro papel.

Quando você terminar este Seção, você deve ter revisto o anexo estrutural de Motoristas que irá participar no cálculo. fileciteturn39file1turn39file2

## Compreender a diferença entre destacamento principal, habilitação e atribuição

Antes de continuar, você precisa distinguir três conceitos que são muitas vezes confusos:
1. **Despacho principal**
2. **Activação**
3. **Transferência ou transferência temporária**

A adscrição principal define onde a pessoa pertence estruturalmente. A habilitação responde a se **pode** funciona legalmente ou tecnicamente em outro contexto. A cessão responde a onde **Ele está mesmo a trabalhar.** por um período temporário. Estas três camadas coexistem, mas não significam o mesmo. fileciteturn39file0turn39file4

Antes de iniciar este Seção, certifique-se de que:
1. Já verificou o destacamento principal no perfil.
2. Sabe que algumas pessoas podem trabalhar fora do seu contexto principal.
3. Você quer evitar a interpretação errada entre os pertences a, pode trabalhar em e está trabalhando em.

Para distinguir corretamente estes conceitos:
1. Use o **destacamento principal** para descrever o contexto estrutural básico do Motorista.
2. Use o **classificação** para indicar que o Motorista pode trabalhar em outro tanque, grupo ou unidade.
3. Use o **atribuição** para indicar que o Motorista é temporariamente movido para outro contexto.
4. Não use uma atribuição para corrigir um destacamento principal mal definido.
5. Não uses uma classificação como se fosse um movimento ativo.
6. Mantenha estas perguntas como um guia:
   1. Onde é que esta pessoa pertence? → subscrição principal
   2. Onde eu poderia trabalhar legalmente? → Habilitação
   3. Onde você está trabalhando agora? → cessão

Para o caso de referência, pergunte-se:
1. O Motorista pertence ao Norte Garagem?
2. Pode trabalhar noutro armazém, se necessário?
3. É temporariamente transferido para outra base ou ainda está no seu contexto habitual?

Quando você terminar este Seção, você deve ter uma leitura correta da hierarquia entre destacamento, habilitação e atribuição. fileciteturn39file0turn39file4

## Validando que o destacamento permite visualizar e atribuir o Motorista corretamente

A adscrição não serve apenas para descrever o perfil do Motorista. Também condiciona como o sistema o vê e o que o Tarefas pode receber. Uma pessoa mal-adscrito pode ser deixada fora do filtro correto, aparecer no lugar errado ou receber o Tarefas que não corresponde a ele. O oposto também pode ocorrer: que uma pessoa válida está escondida ou inelegível por um anexo mal definido. fileciteturn39file3L1-L20

Antes de continuar, certifique-se de que:
1. Você já verificou armazém, unidade e grupo em vários perfis.
2. Você entende a diferença entre o destacamento e a atribuição.
3. Você já está claro qual coletivo vai participar no próximo cálculo.

Para validar o impacto operacional do destacamento:
1. Verifique qual conjunto de Motoristas deve ser visível para o contexto do seu cálculo.
2. Verifique que as pessoas certas aparecem sob o depósito direito, unidade e grupo.
3. Verifique se há Motoristas no grupo errado.
4. Verifique se há Motoristas que devem pertencer ao contexto e não aparecer como tal.
5. Se detectar um erro de destacamento, corrija-o antes de passar às regras ou à disponibilidade.
6. Salva o Configuração final dos perfis afetados.

Para o caso de referência, certifique-se de que:
1. Motoristas que irá cobrir L1 aparece no contexto operacional correto.
2. Eles não se misturam com grupos que não devem receber Dirigindo Tarefas.
3. O sistema poderia filtrar e atribuir apenas pessoal relevante.

Quando você terminar este Seção, você deve ter uma base de destacamento operacional que ajuda o sistema a ver e usar as pessoas certas.

## Confirmando que o destacamento operacional já está pronto para a próxima camada

O último passo é verificar que o destacamento foi sólido o suficiente para continuar com regras, Ausências e cálculo. Aqui o objetivo não é apenas ter campos preenchidos, mas ter deixado uma estrutura clara que o motor pode interpretar inequívocamente.

Antes de terminar, certifique-se de que:
1. Já verificou o destacamento estrutural dos perfis-chave.
2. Já distingues o destacamento, a habilitação e a atribuição.
3. Você já Validado que o coletivo visível é o certo.
4. Você corrigiu os principais desalinhamentos.

Para confirmar que o destacamento já está pronto:
1. Volte para a lista geral de Motoristas.
2. Verifique se o coletivo relevante para o seu caso aparece no contexto correto.
3. Verifique se não há erros óbvios de depósito, unidade ou grupo.
4. Pergunte-se se o sistema já poderia:
   1. filtrar adequadamente o Motoristas do caso,
   2. aplicar-lhes-á as regras do direito colectivo,
   3. e tratá-los como base para a disponibilidade e o cálculo.
5. Se a resposta for sim, continue com o próximo início rápido.
6. Se a resposta for não, corrija o destacamento antes de continuar.

Para o caso de referência, não continue até poder dizer:
1. O L1 Motoristas está ligado ao contexto correto.
2. Sabes quem pertence, quem pode trabalhar e quem está cedido.
3. A base agora está pronta para aplicar as regras Alocação e a disponibilidade.

Quando você terminar este Seção, você deve ter um destacamento operacional suficientemente claro para continuar com a próxima camada do processo.

## Lecturas adicionais

- [Definição de regras Alocação para a designação de pessoal](P22_Definição_De_Regras_Alocação_Para_A_Designação_De_Pessoal.md)
