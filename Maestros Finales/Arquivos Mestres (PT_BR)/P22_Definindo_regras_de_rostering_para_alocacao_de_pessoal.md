---
title: Definindo regras de Rostering para a alocação de pessoal
shortTitle: Regras de Rostering
intro: 'Aprenda a configurar regras básicas e avançadas de Rostering para que a alocação de pessoal respeite limites trabalhistas, critérios de equidade e restrições operacionais reais antes de calcular a escala.'
contentType: how-tos
versions:
  - '*'
---

## Entendendo o que as regras de Rostering controlam

Antes de calcular alocações de pessoal, você precisa definir as **regras de Rostering** que guiarão como os empregados são atribuídos aos turnos. Essas regras não constroem o trabalho, porque isso já foi resolvido no Scheduling. Aqui você controla como esse trabalho é distribuído entre pessoas reais, respeitando políticas operacionais, critérios de equidade e limites trabalhistas.

Use este quick start quando você já tiver uma solução de Scheduling suficientemente estável, uma base de motoristas carregada e uma adscrição operativa revisada.

Antes de começar, certifique-se de que:
1. Você já fechou a transição desde Scheduling no P19.
2. Você já carregou e revisou motoristas no P20.
3. Você já validou a adscrição operativa no P21.
4. Você sabe qual solução de Scheduling será a base.
5. Você sabe qual coletivo/grupo de empregados será afetado pelo cálculo.

Para este quick start, use este caso de referência:

> **Vou configurar as regras de Rostering para a linha L1 e seu grupo de motoristas, de forma que o cálculo atribua pessoal real respeitando descansos, limites de trabalho e critérios operacionais.**

Para entender o papel dessas regras:
1. Trate as regras de Rostering como restrições e preferências sobre a atribuição de pessoas.
2. Use essas regras quando você quiser controlar:
   1. descansos,
   2. tempo de trabalho,
   3. padrões semanais,
   4. grupo de trabalho,
   5. emparelhamentos,
   6. e outros critérios de equidade/política interna.
3. Não use essas regras para corrigir problemas de:
   1. oferta,
   2. tempos,
   3. frota,
   4. ou construção base dos turnos.
4. Se detectar que o problema ainda é estrutural, volte ao Scheduling antes de seguir.

Quando você terminar esta seção, deverá ter claro que as regras de Rostering governam pessoas e não a estrutura base do trabalho.

## Distinguindo entre regras básicas e regras avançadas

Antes de criar um modelo de regras, você precisa distinguir dois níveis de configuração:
1. **Regras básicas**
2. **Regras avançadas**

As regras básicas servem para configurar rapidamente restrições comuns. São úteis para uma parametrização ágil ou um teste inicial. As regras avançadas servem para modelar com mais precisão restrições e preferências por meio de limites e penalidades.

Antes de começar esta seção, certifique-se de que:
1. Você sabe se o caso precisa de rapidez ou precisão.
2. Você entende que as regras básicas têm menos flexibilidade de modelagem do que as avançadas.
3. Você sabe se vai precisar de modelos diferentes conforme o uso.

Para escolher o tipo adequado:
1. Use **regras básicas** se quiser cobrir rapidamente restrições comuns.
2. Use **regras avançadas** se precisar modelar com detalhe políticas complexas, convenções ou condições específicas.
3. Lembre que regras básicas ativas se aplicam tanto na operação diária quanto em cenários de cálculo.
4. Se precisar de modelos distintos para contextos distintos, use regras avançadas.
5. Decida o enfoque antes de parametrizar.

Para o caso de referência:
1. Se você está começando e quer uma primeira camada de controle, comece por regras básicas.
2. Se você já sabe que precisará ajustar preferências, penalidades ou modelos por contexto, avance para regras avançadas.

Quando você terminar esta seção, deverá ter claro se o caso será resolvido com regras básicas, avançadas ou uma combinação controlada.

## Ativando regras básicas comuns para uma primeira alocação

Se o seu caso precisa de uma configuração inicial rápida, você pode começar pelas **regras básicas**. Elas cobrem as restrições mais habituais e permitem executar o cálculo com uma base razoável antes de entrar em níveis mais finos.

Antes de começar esta seção, certifique-se de que:
1. Você decidiu começar com regras básicas.
2. Você sabe quais restrições mínimas quer impor.
3. Você tem claro que nem todas as regras devem estar ativas por padrão.

Para ativar regras básicas:
1. No GoalBus, vá em **Configuração** > **Regras de atribuição**.
ref: P22_Imagen1.png | compact
2. Abra a seção **Regras básicas**.
3. Revise o catálogo de regras básicas disponíveis.
ref: P22_Imagen2.png | full
4. Ative apenas as que correspondem ao caso que você está construindo.
5. Configure, quando aplicável:
   1. limites gerais,
   2. limites específicos por propriedades do empregado,
   3. ou exceções para certos empregados.
6. Salve as alterações.
7. Verifique que as regras ativas refletem as políticas que você quer impor.

Uma base inicial de regras básicas pode incluir:
1. **Padrão de trabalho**
2. **Descanso entre dias**
3. **Tempo de trabalho mensal**
4. **Tempo de trabalho semanal**
5. **Folgas por semana**
6. **Primeira solução publicada**
7. **Grupo de trabalho**
8. **Emparelhamento**
9. **Compatibilidade de atribuição**
10. **Habilitação de linha**
11. **Turno da primeira solução publicada**
12. **Dias de trabalho consecutivos**, quando aplicável

Para o caso de referência, não ative uma regra apenas porque existe. Ative apenas se:
1. responde a uma necessidade real,
2. você consegue explicar por quê,
3. e sabe como afetará a alocação.

Quando você terminar esta seção, deverá ter uma primeira base de controle para a alocação de pessoal.

## Criando um modelo de regras avançadas quando você precisar de mais precisão

Se as regras básicas não forem suficientes, o próximo passo é criar um **modelo de regras avançadas**. Isso permite controlar com precisão como as alocações são geradas, ajustando limites e preferências segundo políticas da empresa, acordos trabalhistas e condições reais de operação.

Antes de começar esta seção, certifique-se de que:
1. Você identificou o que não pode ser resolvido bem com regras básicas.
2. Você sabe quais comportamentos devem ser obrigatórios e quais apenas preferidos.
3. Você precisa de um modelo mais fino que possa ser reutilizado por cenário ou contexto.

Para criar um modelo de regras avançadas:
1. Em **Configuração** > **Regras de atribuição**, abra a seção **Modelos de regras**.
2. Crie um novo modelo de regras.
3. Dê um **nome** claro ao modelo.
4. Adicione uma **descrição** para diferenciá-lo de outros.
5. Salve o modelo.
ref: P22_Imagen3.png | compact
6. Comece a adicionar regras avançadas uma a uma.
7. Para cada regra, decida:
   1. se atua como limite obrigatório,
   2. ou como preferência via penalidade.
8. Salve a configuração do modelo.
9. Ative o modelo criado.
10. Verifique que o modelo já pode ser atribuído ao cálculo de Rostering adequado.

Para o caso de referência, uma opção válida poderia ser:
- **Rostering L1 dia útil**
- **Alocação motoristas L1 - regras avançadas**

Quando você terminar esta seção, deverá ter um modelo avançado pronto para representar restrições e preferências mais complexas.

## Relacionando as regras com o coletivo correto e com o cálculo real

Depois de ativar regras básicas ou criar um modelo avançado, você precisa verificar que as regras se aplicam ao coletivo correto e que você não está impondo restrições abstratas sem relação com o cálculo real.

Antes de continuar, certifique-se de que:
1. Você já ativou regras básicas ou criou um modelo avançado.
2. Você sabe quais empregados, grupos ou depósitos participarão do cálculo.
3. Você sabe qual solução de Scheduling servirá como entrada.

Para relacionar corretamente as regras com o contexto:
1. Revise o coletivo de pessoal ao qual o Rostering se aplicará.
2. Verifique se as regras afetam:
   1. toda a base envolvida,
   2. um grupo específico,
   3. ou empregados com propriedades específicas.
3. Confirme que você não está impondo regras a pessoas que nem participarão do cálculo.
4. Revise se a lógica herdada do Scheduling continua compatível com essas regras.
5. Se uma regra tornar o reparto inviável, ajuste limite ou escopo.
6. Salve a versão final da configuração.

Para o caso de referência, pergunte-se:
1. Estas regras são para os motoristas que realmente cobrirão a L1?
2. O grupo de trabalho afetado é o correto?
3. A alocação continua viável depois de ativar essas regras?

Quando você terminar esta seção, deverá ter uma configuração de regras conectada com pessoas reais e com um cálculo concreto de Rostering.

## Confirmando que a base de regras já está pronta para calcular Rostering

O último passo é garantir que a configuração já está pronta para alimentar o cálculo. Não se trata apenas de ativar regras, mas de deixar uma base coerente, compreensível e aplicável.

Antes de terminar, certifique-se de que:
1. Você escolheu entre regras básicas e avançadas conforme o caso.
2. Você ativou/modelou as restrições necessárias.
3. Você vinculou a lógica ao coletivo correto.
4. Você confirmou que a alocação continua viável.

Para validar que a base já está pronta:
1. Revise o conjunto final de regras ativas.
2. Confirme que cada uma responde a uma necessidade real.
3. Pergunte-se se o sistema já poderia:
   1. bloquear atribuições inválidas,
   2. respeitar descansos e limites,
   3. refletir critérios de equidade e grupo,
   4. e ainda gerar uma solução utilizável.
4. Se a resposta for sim, continue com o próximo quick start.
5. Se a resposta for não, ajuste as regras antes de seguir.

Para o caso de referência, não prossiga até poder afirmar:
1. As regras de Rostering para L1 estão claras.
2. Você sabe por que ativou cada regra.
3. O sistema ainda consegue alocar pessoas reais com essa configuração.
4. A base já está pronta para tratar disponibilidade e exceções.

Quando você terminar esta seção, deverá ter uma base de regras de Rostering suficientemente sólida para passar ao tratamento de ausências, inatividades e disponibilidade.

## Leituras adicionais

- [Gerenciando ausências, inatividades e disponibilidade de pessoal](P23_Gerenciando_ausencias_inatividades_e_disponibilidade_de_pessoal.md)

