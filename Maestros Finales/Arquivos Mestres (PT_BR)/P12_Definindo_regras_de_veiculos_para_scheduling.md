---
title: Definindo regras de veículos para Scheduling
shortTitle: Regras de veículos
intro: 'Aprenda a configurar as regras de veículos que limitarão quais soluções de frota são válidas no Scheduling, para que o cálculo respeite a realidade operacional, a infraestrutura e a oferta validada.'
contentType: how-tos
versions:
  - '*'
---

## Preparando a base que as regras de veículos vão usar

Antes de ativar regras de veículos, você precisa verificar se a base que essas regras vão consumir já está pronta. As regras de veículos não substituem uma parametrização ruim anterior. A função delas é refinar o comportamento do cálculo para que o motor descarte combinações inviáveis ou indesejadas.

Use este quick start quando você já tiver uma oferta de serviço validada, uma linha com frota permitida e uma estrutura operacional coerente, e precisar preparar o caso antes de criar o cenário de Scheduling.

Antes de começar, certifique-se de que:
1. Você já configurou a frota permitida por linha no P4.
2. Você já definiu a versão de tempo e os tempos de percurso no P9.
3. Você já criou e validou a oferta de serviço no P10.
4. Você já revisou a estrutura operacional e o status do serviço no P11.
5. Você sabe qual linha e qual serviço vai usar como referência.

Para este quick start, use este caso de referência:

> **Vou definir as regras de veículos para a linha L1, de forma que o Scheduling use apenas uma frota coerente com a infraestrutura, a oferta validada e as restrições reais do serviço.**

Para preparar a base do caso antes de ativar regras:
1. Abra a linha que você vai usar como referência.
2. Verifique quais tipos de veículo estão permitidos.
3. Revise de qual depósito ou parking a operação vai sair.
4. Confirme que o serviço que você vai usar como entrada já está **Validado**.
5. Verifique que você não está tentando resolver com regras um problema que deveria ter sido corrigido antes na linha, na frota ou na infraestrutura.
6. Se detectar uma incoerência nessa base, corrija antes de ir para a configuração de regras.

Quando você terminar esta seção, deverá estar claro qual caso real você está tentando proteger com as regras de veículos.

## Criando ou selecionando o modelo de regras de veículos

Depois de revisar a base, você precisa entrar no modelo/catálogo de regras de veículos. Aqui não se trata de ativar tudo. Trata-se de escolher ou construir um conjunto de restrições que represente a lógica real do serviço.

Antes de começar esta seção, certifique-se de que:
1. Você sabe qual serviço validado vai usar como referência.
2. Você já confirmou quais tipos de veículo são válidos para a linha.
3. Você sabe quais problemas reais quer evitar.

Para criar ou selecionar o modelo de regras:
1. No GoalBus, vá em **Configuração** > **Veículos** > **Regras de tipos de veículos**.
ref: P12_Imagen1.png | compact
2. Verifique se já existe um modelo de regras adequado para o seu caso.
3. Se o modelo já existir, abra-o e revise a configuração.
4. Se não existir, crie um novo modelo de regras.
5. Dê um **nome** claro ao modelo.
6. Se aplicável, adicione uma **descrição** para distinguir o propósito.
7. Salve o modelo.
ref: P12_Imagen2.png | compact
8. Confirme que o modelo já está disponível para adicionar regras concretas.

Para o caso de referência, uma opção válida poderia ser:
- **Veículos - L1 dia útil**
- **Regras de frota - Serviço L1 dia útil**

Quando você terminar esta seção, deverá ter um contêiner claro para configurar as restrições de veículos do caso.

## Ativando apenas as regras de veículos que você realmente precisa

Agora sim você pode começar a ativar regras. Aqui é importante manter um critério claro: uma regra deve representar uma necessidade real de operação, segurança, infraestrutura ou conformidade. Se uma regra não responde a um problema concreto, ainda não vale a pena ativá-la.

Antes de começar esta seção, certifique-se de que:
1. Você já criou ou selecionou um modelo de regras.
2. Você sabe qual frota é válida para a linha.
3. Você sabe quais combinações devem ficar proibidas ou limitadas.

Para ativar as regras de veículos do caso:
1. Dentro do modelo, revise o catálogo de regras disponíveis clicando em **Adicionar Nova Regra**.
ref: P12_Imagen3.png
2. Identifique quais atendem às necessidades reais do seu serviço selecionando o **template** correspondente.
3. Defina um **Nome** e escreva uma **Descrição** para cada nova regra.
4. Ative apenas as regras que você realmente precisa para o caso.
5. Configure os parâmetros específicos de cada regra quando aplicável.
6. Repita até cobrir as restrições mínimas necessárias.
7. Salve as alterações.
8. Revise o modelo completo e confirme que ele não está nem restritivo demais nem aberto demais.

Para o caso de referência, pergunte-se:
1. Que situações de frota o sistema deveria impedir?
2. Quais combinações seriam fisicamente possíveis, mas não desejáveis?
3. Quais comportamentos devem ser guiados pela lógica de depósito, parking ou linha?

Quando você terminar esta seção, deverá ter um conjunto inicial de regras de veículos ativas e coerentes, similar ao da imagem a seguir:
ref: P12_Imagen4.png | compact

## Relacionando as regras com a linha, a frota e a infraestrutura

Depois de ativar as regras, você precisa verificar se elas estão alinhadas com a linha e com a infraestrutura que sustenta o caso. Uma regra de veículos não deveria contradizer a frota permitida por linha nem a geografia de depósitos e parkings.

Antes de continuar, certifique-se de que:
1. Você já ativou o conjunto inicial de regras.
2. Você já revisou os tipos de veículo permitidos.
3. Você conhece a base física de onde a operação sai.

Para verificar a coerência das regras:
1. Revise novamente a configuração da linha.
2. Confirme que as regras não contradizem os tipos de veículo permitidos.
3. Revise a relação com o depósito e o parking autorizado.
4. Verifique que as regras reforçam essa lógica em vez de quebrá-la.
5. Se uma regra tornar o serviço inviável ou contradizer a infraestrutura, corrija-a ou desative-a.
6. Salve a versão final do modelo.

Para o caso de referência, garanta que:
1. A linha L1 continua podendo usar a frota autorizada.
2. O Depósito Norte continua sendo uma saída coerente para o serviço.
3. Nenhuma regra bloqueia uma operação que deveria ser válida de acordo com a base já configurada.

Quando você terminar esta seção, deverá ter regras alinhadas com a realidade do serviço, e não com um modelo abstrato.

## Confirmando que a oferta validada continua calculável

O último passo é verificar que as regras de veículos que você acabou de ativar ainda permitem calcular a oferta validada. Uma coisa é restringir com critério; outra é fechar tanto o modelo que o serviço deixa de ser viável antes mesmo de criar o cenário.

Antes de terminar, certifique-se de que:
1. Você já ativou as regras necessárias.
2. Você já revisou a relação com linha, frota e infraestrutura.
3. Você sabe qual serviço será a entrada do Scheduling.

Para validar que o caso ainda é calculável:
1. Revise novamente o serviço validado que você vai usar como referência.
2. Verifique que a linha ainda tem acesso à frota de que precisa.
3. Revise se as regras ativadas deixam pelo menos uma solução razoável para o caso.
4. Pergunte-se se o sistema já poderia criar um cenário de Scheduling sem entrar em contradição.
5. Se a resposta for sim, continue com o próximo quick start.
6. Se a resposta for não, corrija o modelo de regras antes de seguir.

Para o caso de referência, não prossiga até poder afirmar:
1. A linha L1 mantém frota válida e autorizada.
2. O serviço de dias úteis validado continua compatível com as regras ativadas.
3. O modelo de veículos já está pronto para uso dentro do cenário de Scheduling.

Quando você terminar esta seção, deverá ser capaz de afirmar que a lógica de veículos está fechada e consistente o suficiente para passar para regras de turnos e criação do cenário.

## Leituras adicionais

- [Definindo tipos de turnos e regras de turnos](P13_Definindo_tipos_de_turnos_e_regras_de_turnos.md)

