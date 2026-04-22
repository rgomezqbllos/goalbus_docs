---
title: Definir os tipos de Turnos e as regras de Turnos
shortTitle: Tipos e regras
intro: Saiba como criar tipos Turno, organizá-los dentro de modelos de regras e ativar
  as restrições ou sanções necessárias para que o Programação construa Tarefas legalmente
  válido e operacionalmente coerente.
contentType: how-tos
versions:
- '*'
---
## Criando os tipos de Turnos que irão estruturar o trabalho

Antes de configurar as regras do Turno, você precisa definir o **tipos de Turnos** que o sistema irá usar para agrupar o Viagems em trabalho humano coerente. Um tipo Turno não é apenas uma tag visual. É a categoria lógica que guia o motor para construir Tarefas reconhecível e utilizável mais tarde em listas, operação diária e integração com outros sistemas.

Use este início rápido quando você já tiver uma oferta Validado, uma lógica definida Veículo, e você precisa dizer ao sistema quais formas de trabalho são válidas para o seu caso.

Antes de começar, certifique-se de que:
1. Você já criou e Validado a oferta de serviço na P10.
2. Você já tem Validado a estrutura operacional em P11.
3. Você já definiu as regras Veículo no P12.
4. Você está claro que serviço e contexto operacional você vai usar como referência.

Para este início rápido, use este caso de referência:

> **Vou definir os tipos Turno de Linha L1 para que Programação possa construir Tarefas coerente antes de criar o cálculo Cenário.**

Para criar os tipos Turno do seu caso:
1. Em GoalBus, vá para **Configuração** > **Pessoal** > **Tipos de Turnos**.
ref: P13_Imagen1.png | compact
2. Verifique se já existem tipos apropriados de Turnos para o seu caso.
3. Se o tipo já existir, abra-o e verifique se ainda é válido.
4. Se não existir, crie um novo.
5. Define estes campos:
   1. **Nome completo**, com um nome claro e descritivo.
   2. **Denominação curta**, para visões compactas e cartões de operação.
   3. **Identificação externa**, se o cliente precisar de integração com sistemas de RH ou folha de pagamento.
ref: P13_Imagen2.png | compact
6. Marca o tipo como **Ativos** se você deve participar em cálculos futuros.
7. Salve o tipo Turno.
8. Repita o processo para cada categoria de trabalho que você realmente precisa no seu caso.

Para o caso de referência, você pode criar tipos como:
1. **Vira amanhã.**
2. **Viragem tardia**
3. **Viração quebrada**, se a operação necessitar

Quando você terminar este Seção, você deve ter os tipos de Turnos que vão servir como .DNA . do Tarefas que Programação irá construir.

## Criar ou selecionar o modelo de regra de viragem

Depois de criar os tipos Turno, você precisa definir o contêiner onde as regras vão viver. As regras de turno não são gerenciadas como uma lista plana, mas dentro do **modelos** que agrupa um conjunto coerente de restrições para um estágio, um período, ou uma simulação de concreto. Isso permite que você mantenha vários Configuraçãos sem misturar regras históricas com regras ativas.

Antes de iniciar este Seção, certifique-se de que:
1. Você já criou ou Validado os tipos de Turnos que você vai usar.
2. Você sabe que serviço ou simulação você vai usar como referência.
3. Você já está claro se este modelo será reutilizável ou específico de caso.

Para criar ou selecionar o modelo de regra:
1. Em GoalBus, vá para **Configuração** > **Pessoal** > **Regras de Turno**.
2. Verifique se já existe um **Regras-modelo** adequado para o seu caso.
3. Se o modelo já existe, abra-o e verifique se ainda é válido.
4. Se não existir, crie um novo modelo clicando em **Adicionar um novo modelo**.
5. Atribui um **Nome** claro ao modelo.
6. Se aplicável, adicione um **Designação das mercadorias** que identifique o seu uso.
7. Salve o modelo.
ref: P13_Imagen3.png | compact
8. Confirme que você já pode adicionar regras dentro desse recipiente.

Para o caso de referência, uma opção válida pode ser:
- **Virações - L1**
- **Regras de Turno**

Quando você terminar este Seção, você deve ter um modelo de regras preparadas para receber restrições e sanções específicas.

## Ativar regras de turno, tais como restrições ou sanções

Agora você pode começar a definir as regras. Aqui é importante distinguir duas lógicas:
1. **Restrições**, que são obrigatórios e bloqueiam Tarefas inválido.
2. **Sanções**, que não bloqueiam, mas empurram o otimizador para soluções preferidas.

Esta diferença é fundamental porque nem tudo o que você deseja na operação deve se tornar uma proibição absoluta. Algumas condições devem agir como um guia e não como uma parede.

Antes de iniciar este Seção, certifique-se de que:
1. Você já tem um modelo de regras criadas ou selecionadas.
2. Você sabe que comportamento de trabalho você quer Parada.
3. Sabes o comportamento que queres favorecer sem torná-lo obrigatório.

Para gerenciar as regras de turno do seu caso:
1. Se quiser criar uma nova regra, toque em **Adicionar uma nova regra**.
2. Dentro do modelo de regra, verifique o **Modelos de regras** disponível e dê um **Nome** e um **Designação das mercadorias** à nova regra.
3. Selecione o modelo que corresponde ao controle que deseja aplicar.
4. Crie um **regra específica** a partir desse modelo clicando no **Confirmar**.
ref: P13_Imagen4.png | compact
6. Decida **A que tipos de Turnos se aplica cada regra**. Nem todas as regras devem se aplicar a todos os tipos. Algumas podem ser globais e outras devem abordar categorias específicas, como amanhã, tarde ou partida.
7. Digite os parâmetros específicos da regra.
8. Mantenha a regra.
9. Repita o processo apenas para as regras que o seu caso realmente precisa.
10. Verifique se as regras que você precisa aplicar estão ativas ou não. Para podar uma regra, ela deve ter sido atribuída a pelo menos um tipo de turno.
ref: P13_Imagen5.png | compact(x19)

Para o caso de referência, pense em exemplos como:
1. O Turno de amanhã deve começar dentro de uma janela específica.
2. Uma rotação dividida não deve exceder um certo nível de amplitude.
3. Uma sequência indesejável pode ser penalizada em vez de proibida.

Quando você terminar este Seção, você deve ter um conjunto inicial de regras que refletem tanto limites obrigatórios como preferências operacionais.

## Verificando que as regras são atribuídas ao tipo Turno correto

Uma vez que as regras foram ativadas, você precisa verificar o **a que tipos de Turnos são aplicados cada**. Nem todas as regras devem ser aplicadas a todos os tipos. Algumas podem ser globais e outras devem ser direcionadas para categorias específicas, como amanhã, tarde ou correspondência.

Antes de continuar, certifique-se de que:
1. Já ativaste pelo menos uma regra dentro do modelo.
2. Você já definiu os tipos de Turnos envolvidos no caso.
3. Sabes se a regra deve ser global ou específica.

Revisar adequadamente o âmbito de aplicação:
1. Selecione cada regra que você criou.
2. Verifique o **Tipos de Turnos aplicáveis** Seção.
3. Selecione os tipos específicos aos quais a regra deve ser aplicada.
4. Se a regra deve afetar todos os tipos do Cenário, configure-o como global selecionando o **todos os tipos de Turno**.
5. Verifique se não existem duas regras ativas do mesmo modelo que se aplicam ao mesmo tipo de Turno se isso gerar um conflito lógico.
6. Salve o Configuração.
7. Repita a revisão para cada regra de modelo.

Para o caso de referência:
1. Uma janela de início precoce só pode ser aplicada ao **Vira amanhã.**.
2. Uma regra de descanso pode ser aplicada a vários tipos.
3. Uma preferência geral poderia ser global.

Quando você terminar este Seção, você deve ter regras com um escopo claro e sem conflitos lógicos entre si semelhantes à seguinte imagem:
ref: P13_Imagen6.png | compact(x19)

## Verificando que a lógica Turno permanece compatível com o serviço

O último passo é verificar que os tipos de Turnos e as regras que você acabou de definir ainda são compatíveis com a oferta Validado e com a lógica de Veículos que você já fechou. Não é útil ter regras de "boa" se o resultado deixar o serviço sem uma maneira realista de ser programado.

Antes de terminar, certifique-se de que:
1. Você já criou os tipos de Turnos que você precisa.
2. Já ativaste e atribuiste as regras correspondentes.
3. Você está claro que serviço a entrada para o estágio Programação será.

Para validar que o caso ainda é viável:
1. Verifique o serviço Validado que você irá usar como referência.
2. Verifique que os tipos de Turnos que você criou podem organizar esse trabalho.
3. Verifique se quaisquer regras do Turno deixam o caso muito rígido.
4. Verifica que não há forte contradição com as regras Veículo já ativadas.
5. Pergunte-se se o sistema já poderia construir Tarefas legalmente e operacionalmente consistente com esta base.
6. Se a resposta for sim, continue com o próximo início rápido.
7. Se a resposta for não, corrija os tipos ou regras antes de seguir.

Para o caso de referência, não continue até poder dizer:
1. A oferta Validado L1 permanece compatível com os tipos definidos de Turno.
2. As regras não bloqueiam desnecessariamente o caso.
3. O modelo já está pronto para entrar no estágio de Programação.

Quando você terminar este Seção, você deve ser capaz de dizer que a lógica de Turnos já está fechada o suficiente para passar para a criação do Programação Cenário.

## Lecturas adicionais

- [Criando o primeiro estágio de Programação](P14_Criando_O_Primeiro_Estágio_De_Programação_Com_O_Motor_Classic.md)
