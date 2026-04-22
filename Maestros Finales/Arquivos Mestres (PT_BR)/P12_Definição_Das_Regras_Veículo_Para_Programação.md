---
title: Definição das Regras Veículo para Programação
shortTitle: Regras Veículo
intro: Saiba como configurar as regras do Veículo que irão limitar quais soluções
  do Frota são válidas no Programação, de modo que o cálculo respeite a realidade
  operacional, infraestrutura e oferta do Validado.
contentType: how-tos
versions:
- '*'
---
## Preparar a base que irá usar as regras Veículo

Antes de ativar as regras Veículo, você precisa verificar que a base que essas regras vão consumir já está pronta. As regras Veículo não substituem uma parametrização ruim anterior. Sua função é refinar o comportamento de cálculo para que o motor descarte combinações inviáveis ou indesejadas.

Use este início rápido quando você já tiver uma oferta de serviço Validado, um Linha com Frota permitido e uma estrutura operacional coerente, e você precisa preparar o caso antes de criar o Programação Cenário.

Antes de começar, certifique-se de que:
1. Você já configurou o Frota permitido por Linha no P8.
2. Você já definiu o tempo Versão e tempos de viagem em P9.
3. Você já criou e Validado a oferta de serviço na P10.
4. Já verificou a estrutura operacional e o estado do serviço na P11.
5. Você está claro o que Linha e serviço que você vai usar como referência.

Para este início rápido, use este caso de referência:

> **Vou definir as regras Veículo para Linha L1, para que Programação use apenas uma Frota consistente com infraestrutura, oferta Validado e restrições de serviço reais.**

Preparar a base de casos antes da ativação das regras:
1. Abra o Linha que irá usar como referência.
2. Verifique que tipos de Veículo são permitidos.
3. Verifique a partir de qual depósito ou Garagem a operação deixará.
4. Confirme que o serviço que você vai usar como entrada já é **Validação**.
5. Verifique que você não está tentando resolver com regras um problema que deveria ter sido corrigido mais cedo online, Frota ou infraestrutura.
6. Se você detectar uma inconsistência nessa base, corrija-a antes de passar às regras Configuração.

Quando você terminar este Seção, você deve ser claro sobre o caso real que você está tentando proteger por regras Veículo.

## Criar ou selecionar o modelo de regras Veículo

Uma vez verificada a base, você precisa inserir o modelo ou catálogo das regras do Veículo. Neste ponto, não se trata de ativar tudo. Trata-se de escolher ou construir um conjunto de restrições que represente a lógica real do serviço.

Antes de iniciar este Seção, certifique-se de que:
1. Você sabe que serviço Validado você vai usar como referência.
2. Você já confirmou que tipos de Veículo são válidos para o Linha.
3. Sabes quais são os verdadeiros problemas que queres evitar.

Para criar ou selecionar o modelo de regra:
1. Em GoalBus ver **Configuração** > **Veículos** > **Regras Tipo de veículo**.
ref: P12_Imagen1.png | compact
2. Verifique se já existe um modelo adequado de regras para o seu caso.
3. Se o modelo já existir, abra-o e verifique o seu Configuração.
4. Se não existir, crie um novo modelo de regras.
5. Atribui um **nome** claro ao modelo.
6. Se aplicável, adicione um **Descrição** que lhe permita distinguir seu propósito.
7. Salve o modelo.
ref: P12_Imagen2.png | compact
8. Confirma que o modelo já está disponível para adicionar regras concretas.

Para o caso de referência, uma opção válida pode ser:
- **Veículos - L1 utilizável**
- **Regras Frota - Serviço Funcional L1**

Quando você terminar este Seção, você deve ter um recipiente claro para configurar as restrições Veículo do caso.

## Ativar apenas as regras Veículo que você realmente precisa

Agora você pode começar a ativar regras. Aqui é importante manter um critério claro: uma regra deve representar uma necessidade real de operação, segurança, infraestrutura ou conformidade. Se uma regra não responde a um problema em particular, não é apropriado atuá-lo ainda.

Antes de iniciar este Seção, certifique-se de que:
1. Você já criou ou selecionou um modelo de regras.
2. Você sabe o que o Frota é válido para o Linha.
3. Sabe que combinações devem ser proibidas ou limitadas.

Para ativar as regras Veículo do caso:
1. Dentro do modelo de regras, verifique o catálogo de regras disponíveis clicando em **Adicionar uma nova regra**.
ref: P12_Imagen3.png
2. Identifique quais respondem às necessidades reais do seu serviço selecionando o **Modelo** apropriado.
3. Defina um **Nome** e digite um **Designação das mercadorias** para cada nova regra.
4. Ativa apenas as regras que realmente precisas para o caso.
5. Configurar os parâmetros específicos de cada regra ao aplicar.
6. Repita o processo para cobrir as restrições mínimas exigidas.
7. Salve as mudanças.
8. Revisar o modelo completo e confirmar que não é muito restritivo ou demasiado aberto.

Para o caso de referência, pergunte-se:
1. Que situações Frota deve o sistema prevenir?
2. Que combinações seriam fisicamente possíveis, mas não desejáveis?
3. Que comportamentos devem ser guiados pela lógica do depósito, Garagem ou Linha?

Quando você terminar este Seção, você deve ter um conjunto inicial de regras ativas e consistentes Veículo semelhante àquela na seguinte imagem:
ref: P12_Imagen4.png | compact(20x)

## Relativamente às regras Linha, Frota e infra-estrutura

Depois de ativar as regras, você precisa verificar que elas estão realmente alinhadas com o Linha e infraestrutura que sustenta o caso. Uma regra Veículo não deve contradizer o Frota permitido por Linha ou a geografia de armazéns e Garagem.

Antes de continuar, certifique-se de que:
1. Já ativaste o conjunto inicial de regras.
2. Você já verificou os tipos Veículo permitidos.
3. Conheces a base física de onde a operação sai.

Para verificar a coerência das regras:
1. Verifique novamente o Linha Configuração.
2. Confirma que as regras não contradizem os tipos Veículo permitidos.
3. Verifique a relação com o armazém e o Garagem autorizado.
4. Prova que as regras reforçam essa lógica, em vez de a quebrar.
5. Se uma regra torna o serviço impraticável ou contradiz a infraestrutura, corrija-o ou desactive-o.
6. Salve o Versão final do modelo.

Para o caso de referência, certifique-se de que:
1. Linha L1 ainda pode usar o Frota autorizado.
2. O North Garagem continua a ser uma saída coerente para o serviço.
3. Nenhuma regra bloqueia uma operação que deve ser válida de acordo com a base já configurada.

Quando você terminar este Seção, você deve ter regras alinhadas com a realidade do serviço, não com um modelo abstrato ou genérico.

## Confirmando que a oferta Validado ainda é calculável

O último passo é verificar que as regras Veículo que você acabou de ativar continuam a permitir o cálculo da oferta Validado. Uma coisa é restringir com critérios, e outra é fechar o modelo tanto que o serviço deixa de ser viável antes mesmo de criar o Cenário.

Antes de terminar, certifique-se de que:
1. Já activaste as regras necessárias.
2. Já verificou a relação dele com Linha, Frota e infra-estrutura.
3. Está claro qual será a entrada do serviço Programação.

Para validar que o caso ainda é viável:
1. Verifique novamente o serviço Validado que você irá usar como referência.
2. Verifique se o Linha ainda tem acesso ao Frota que necessita.
3. Verifique se as regras activadas deixam pelo menos uma solução razoável para o caso.
4. Pergunte a si mesmo se o sistema já poderia criar um Programação Cenário sem cair em contradição.
5. Se a resposta for sim, continue com o próximo início rápido.
6. Se a resposta for não, corrija o modelo de regra antes de seguir.

Para o caso de referência, não continue até poder dizer:
1. O Linha L1 mantém um Frota válido e autorizado.
2. O serviço funcional Validado permanece compatível com as regras ativadas.
3. O Modelo de veículo está agora pronto para uso dentro do Programação Cenário.

Quando você terminar este Seção, você deve ser capaz de dizer que a lógica do Veículos já está fechada e é consistente o suficiente para passar para a definição de regras do Turno e a criação do Cenário.

## Lecturas adicionais

- [Definir os tipos de Turnos e as regras de Turnos](P13_Definir_Os_Tipos_De_Turnos_E_As_Regras_De_Turnos.md)
