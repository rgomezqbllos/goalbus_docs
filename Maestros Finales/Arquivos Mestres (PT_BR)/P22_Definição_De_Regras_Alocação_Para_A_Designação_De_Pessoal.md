---
title: Definição de regras Alocação para a designação de pessoal
shortTitle: Regras Alocação
intro: Saiba como configurar regras básicas e avançadas do Alocação para que a tarefa
  da equipe respeite os limites de trabalho, critérios de equidade e restrições operacionais
  reais antes de calcular a tabela de pessoal.
contentType: how-tos
versions:
- '*'
---
## Compreender o que eles controlam as regras de Alocação

Antes de calcular as atribuições da equipe, você precisa definir o **Regras Alocação** que guiará como os funcionários são atribuídos ao Turnos. Essas regras não constroem trabalho, porque esse passo já foi resolvido pelo Programação. Aqui, o que você faz é controlar como esse trabalho é compartilhado entre pessoas reais, respeitando políticas operacionais, critérios de equidade e limites de trabalho.

Use este início rápido quando você já tiver uma solução Programação estável suficiente, um modelo Motorista carregado, e um destacamento operacional revisado.

Antes de começar, certifique-se de que:
1. Você já fechou a transição de Programação no P19.
2. Você já carregou e verificou o Motoristas no P20.
3. Você já tem Validado o destacamento operacional para P21.
4. Você já está claro que solução Programação atuará como uma base.
5. Você sabe que coletivo ou grupo de empregados serão afetados pelo cálculo.

Para este início rápido, use este caso de referência:

> **Vou configurar as regras Alocação para o L1 Linha e seu grupo de Motoristas, de modo que o cálculo atribui pessoal real respeitando pausas, limites de trabalho e critérios operacionais.**

Compreender o papel destas regras:
1. Trata as regras da Alocação como restrições e preferências na atribuição de pessoas.
2. Use estas regras quando quiser controlar:
   1. quebras,
   2. tempo de trabalho,
   3. padrões semanais,
   4. Grupo de trabalho,
   5. emparelhamentos,
   6. e outros critérios de equidade ou política interna.
3. Não utilize estas regras para corrigir problemas de:
   1. Oferta,
   2. vezes,
   3. flutuadores,
   4. ou Turno construção de base.
4. Se você descobrir que o problema permanece estrutural, volte para Programação antes de continuar.

Quando você terminar este Seção, você deve estar claro que as regras Alocação governam as pessoas e não a estrutura de base do trabalho.

## Distinção entre regras de base e regras avançadas

Antes de criar um modelo de regra, você precisa distinguir dois níveis Configuração:
1. **Regras de base**
2. **Regras Avançadas**

As regras básicas são concebidas para configurar rapidamente restrições comuns. São úteis quando você quer uma parametrização ágil ou um teste inicial. As regras avançadas são concebidas para modelar restrições e preferências mais precisas através de limites e penalizações.

Antes de iniciar este Seção, certifique-se de que:
1. Sabes se o teu caso precisa de velocidade ou precisão.
2. Você entende que as regras básicas têm menos flexibilidade de modelagem do que as avançadas.
3. Você sabe se você vai precisar de modelos diferentes dependendo do uso.

Para escolher o tipo certo de regras:
1. Use **Regras de base** se quiser cobrir rapidamente as restrições comuns.
2. Use **Regras avançadas** se precisar modelar políticas complexas, acordos ou condições operacionais específicas em detalhes.
3. Note que as regras básicas ativas aplicam-se tanto na operação diária como no cálculo de atribuição Cenários.
4. Se você precisar de modelos diferentes para diferentes contextos, por exemplo um para operação diária e outro para cálculos futuros, trabalhe com regras avançadas.
5. Decida que abordagem você vai usar antes de começar a parametrizar.

Para o caso de referência, utilize esta lógica:
1. Se você está começando e quer uma primeira camada de controle, comece com regras básicas.
2. Se você já sabe que você vai precisar ajustar preferências, penalidades ou modelos por contexto, continue com regras avançadas.

Quando você terminar este Seção, você deve ser claro se seu caso será resolvido com regras básicas, avançadas ou uma combinação controlada de ambos.

## Ativar as regras básicas mais comuns para uma primeira atribuição

Se o seu caso precisar de uma configuração inicial rápida, você pode começar com o **Regras de base**. Estas abrangem as restrições mais comuns e permitem que você inicie o cálculo numa base razoável antes de introduzir níveis de controle mais finos.

Antes de iniciar este Seção, certifique-se de que:
1. Já decidiste começar com as regras básicas.
2. Sabes que restrições mínimas que queres impor.
3. Você está claro que nem todas as regras devem ser ativadas por padrão.

Para activar as regras básicas:
1. Em GoalBus, vá para **Configuração** > **Regras de atribuição**.
ref: P22_Imagen1.png | compact
2. Abra o **Regras de base** Seção.
3. Verifique o catálogo das regras básicas disponíveis.
ref: P22_Imagen2.png | full
4. Ativa apenas aqueles que correspondem ao caso que estás a construir.
5. Conjuntos, quando aplicados:
   1. limites gerais,
   2. limites específicos para as propriedades dos trabalhadores,
   3. ou excepções para certos empregados.
6. Salve as mudanças.
7. Verifique que as regras ativas realmente refletem as políticas que você quer impor.

Uma base inicial das regras de base pode incluir:
1. **Padrão de trabalho**
2. **Descanso entre dias**
3. **Tempo de trabalho mensal**
4. **Tempo de trabalho semanal**
5. **Folga por semana**
6. **Primeira solução Publicado**
7. **Grupo de trabalho**
8. **Emparelhamento**
9. **Compatibilidade com a atribuição**
10. **Linha Activação**
11. **Virar a primeira solução Publicado**
12. **Dias úteis consecutivos**, quando aplicado

Para o caso de referência, não ative uma regra apenas porque ela existe. Ative-a apenas se:
1. responde a uma necessidade real,
2. Você pode explicar porque você precisa dele,
3. E você sabe como isso vai afetar a missão.

Quando você terminar este Seção, você deve ter uma primeira base de controle para a atribuição de pessoal.

## Criando um modelo de regras avançadas quando você precisa de mais precisão

Se as regras básicas não forem suficientes, o próximo passo é criar um **modelo de regras avançadas**. Esta abordagem permite controlar com precisão como as atribuições são geradas, ajustando limites e preferências de acordo com as políticas da empresa, acordos de trabalho e condições operacionais reais.

Antes de iniciar este Seção, certifique-se de que:
1. Você já identificou que parte do caso não pode ser resolvido bem com regras básicas.
2. Sabe que comportamentos devem ser obrigatórios e que só preferiram.
3. Você já precisa de um modelo mais fino que pode ser reutilizado por Cenário ou contexto.

Criar um modelo de regras avançadas:
1. Em **Configuração** > **Regras de atribuição**, abra o **Regras Modelo** Seção.
2. Cria um novo modelo de regras.
3. Atribui um **nome** claro ao modelo.
4. Adicione um **Descrição** que lhe permita distingui-lo de outros modelos.
5. Salve o modelo.
ref: P22_Imagen3.png | compact
6. Comece a adicionar regras avançadas um por um.
7. Para cada regra, decidir:
   1. se for um limite obrigatório,
   2. ou se atua como uma preferência por sanção.
8. Salva o modelo Configuração.
9. Ativa o modelo de regra criado.
10. Verifique se o modelo já pode ser atribuído ao cálculo Alocação adequado.

Para o caso de referência, uma opção válida pode ser:
- **Alocação L1 utilizável**
- **Atribuição L1 Motorista - Regras Avançadas**

Quando você terminar este Seção, você deve ter um modelo avançado pronto para representar restrições e preferências mais complexas.

## Relação das regras com o correcto conjunto e com o cálculo real

Depois de ativar regras básicas ou criar um modelo avançado, você precisa verificar que as regras se aplicam ao coletivo correto e que você não está impondo restrições abstratas não relacionadas ao cálculo real.

Antes de continuar, certifique-se de que:
1. Você já ativou regras básicas ou criou um modelo avançado.
2. Você sabe que funcionários, grupos ou depósitos participarão no cálculo.
3. Você está claro o que a solução Programação servirá como entrada.

Relacionar corretamente as regras ao contexto de cálculo:
1. Verifique o grupo de pessoal para o qual o Alocação se aplicará.
2. Verificar se as regras afetam:
   1. todo o pessoal envolvido,
   2. a um grupo específico,
   3. ou empregados com propriedades específicas.
3. Confirme que não está a impor regras às pessoas que nem sequer participarão nesse cálculo.
4. Verifique se a lógica do Programação Cenário ainda é compatível com essas regras.
5. Se uma regra torna a divisão do trabalho impraticável, ajusta o seu limite ou escopo.
6. Salva o Versão final do Configuração.

Para o caso de referência, pergunte-se:
1. Estas regras são destinadas ao Motoristas que irá realmente cobrir L1?
2. O Grupo de trabalho está relacionado com o direito?
3. A atribuição ainda é viável após a ativação destas regras?

Quando você terminar este Seção, você deve ter um conjunto de regras conectadas a pessoas reais e com um cálculo específico Alocação.

## Confirmando que a base de regra já está pronta para calcular Alocação

O último passo é certificar-se de que o seu Configuração está pronto para alimentar o cálculo da equipe. Não é apenas sobre ativar regras, mas tendo deixado uma base coerente, compreensível e aplicável.

Antes de terminar, certifique-se de que:
1. Você já escolheu entre regras básicas e avançadas, conforme o caso.
2. Você já ativou ou modelou as restrições necessárias.
3. Já ligaste a lógica ao coletivo certo.
4. Já verificou que a missão ainda é viável.

Para validar que a base de regras já está pronta:
1. Verifique o conjunto final de regras ativas.
2. Confirma que cada um responde a uma necessidade real.
3. Pergunte-se se o sistema já poderia:
   1. bloquear as atribuições inválidas,
   2. respeitar os descansos e os limites,
   3. refletir critérios de capital próprio e Grupo de trabalho,
   4. e continuar a gerar uma solução utilizável.
4. Se a resposta for sim, continue com o próximo início rápido.
5. Se a resposta for não, ajuste as regras antes de seguir.

Para o caso de referência, não continue até poder dizer:
1. As regras Alocação para L1 estão agora claras.
2. Sabes porque activaste todas as regras.
3. O sistema ainda pode atribuir pessoas reais com esse Configuração.
4. A base já está pronta para lidar com a disponibilidade de pessoal e excepções.

Quando você terminar este Seção, você deve ter uma base de regra Alocação suficientemente forte para passar para o tratamento de Ausências, inatividade e disponibilidade.

## Lecturas adicionais

- [Gerenciando Ausências, inatividade e disponibilidade de pessoal](P23_Gerenciando_Ausências_Inatividade_E_Disponibilidade_De_Pessoal.md)
