---
title: Criando o primeiro cenário de Scheduling com o motor Classic
shortTitle: Cenário Classic
intro: 'Aprenda a criar o seu primeiro cenário de Scheduling com o motor GoalBus Classic, selecionar corretamente as entradas do cálculo e distinguir quando aplicar regras de veículos e quando aplicar regras de turnos.'
contentType: how-tos
versions:
  - '*'
---

## Criando o cenário com a oferta validada como ponto de partida

Agora que você já tem a oferta validada, a lógica de veículos e a lógica de turnos, o próximo passo é criar o **cenário de Scheduling** que vai usar essa base para calcular uma solução executável.

Este cenário é o ambiente controlado onde você vai combinar:
1. a **oferta validada**,
2. a **matriz de viagens em vazio**,
3. o **modelo de regras de veículos**,
4. e o **modelo de regras de turnos**.

Use este quick start quando você já tiver fechado a parametrização base e quiser preparar o cenário definitivo para cálculo com o motor Classic.

Antes de começar, certifique-se de que:
1. Você já configurou e validou a oferta de serviço no P10.
2. Você já revisou a estrutura operacional no P11.
3. Você já definiu as regras de veículos no P12.
4. Você já definiu os tipos de turnos e as regras de turnos no P13.
5. Você já preparou a matriz de viagens em vazio no P8.
6. Você sabe qual tipo de dia e quais linhas farão parte do cálculo.

Para este quick start, use este caso de referência:

> **Vou criar o primeiro cenário de Scheduling para a linha L1, usando a oferta de dias úteis validada, a matriz de viagens em vazio correspondente e os modelos corretos de regras de veículos e turnos, para executar o cálculo final com o GoalBus Classic.**

Para criar o cenário base do seu caso:
1. No GoalBus, abra o módulo **Planejamento**.
ref: P14_Imagen1.png | compact
2. Clique em **Novo cenário**.
ref: P14_Imagen2.png | compact
3. Informe a identidade básica do cenário:
   1. **Nome**
   2. **Tipo de dia**
   3. **Descrição** (opcional)
   4. Cenário **somente veículos** (ou não)
ref: P14_Imagen3.png | compact
4. Selecione os elementos básicos do cenário:
   1. O **serviço comercial validado** que você quer cobrir
   2. O **Modelo de Regras de Turnos**
   3. O **Modelo de Regras de Tipos de Veículos** (opcional)
   4. A **matriz de viagens em vazio** que corresponde ao mesmo tipo de dia
   5. A **matriz de deslocamentos de motoristas** que fará parte do cenário
ref: P14_Imagen4.png | compact
5. Selecione a linha.
ref: P14_Imagen5.png | compact
6. Salve/finalize a criação do cenário.
7. Verifique se o cenário aparece na tabela principal de planejamento.

Para o caso de referência, uma opção válida poderia ser:
- **Scheduling Classic - L1 dia útil**

Quando você terminar esta seção, deverá ter um cenário criado com as entradas logísticas e comerciais corretas, como na imagem a seguir:
ref: P14_Imagen6.png | full

## Entendendo quando usar regras de veículos e quando usar regras de turnos

Antes de configurar o motor, é importante deixar clara uma distinção: **regras de veículos e regras de turnos não resolvem o mesmo problema**.

Use **regras de veículos** quando você quiser controlar o comportamento da frota. Elas são as regras corretas se você precisa modelar:
1. compatibilidade física dos veículos,
2. limites de capacidade ou alcance,
3. restrições de infraestrutura,
4. políticas operacionais ligadas ao uso da frota.

Use **regras de turnos** quando você quiser controlar como o trabalho humano é organizado. Elas são as regras corretas se você precisa modelar:
1. jornadas de trabalho,
2. pausas e descansos,
3. horários de início e fim,
4. amplitude,
5. diferenças entre tipos de turno, como manhã, tarde ou noite.

Antes de continuar, certifique-se de que:
1. Você sabe quais restrições pertencem ao veículo.
2. Você sabe quais restrições pertencem ao turno.
3. Você não está tentando resolver um problema de pessoal com regras de frota, nem o contrário.

Para decidir qual modelo usar em cada caso:
1. Pergunte-se se a restrição afeta o **ônibus** ou o **motorista**.
2. Se afetar o **ônibus**, use o **modelo de regras de veículos**.
3. Se afetar o **trabalho humano** ou o tipo de turno, use o **modelo de regras de turnos**.
4. Se uma regra deve se aplicar a todos os tipos de turno, configure-a como global ou com o escopo mais amplo disponível.
5. Se uma regra se aplica apenas a um tipo específico, atribua-a somente a esse tipo.

Para o caso de referência:
1. Se você quer limitar qual frota pode cobrir a L1, use **regras de veículos**.
2. Se você quer controlar como se constrói um turno de manhã ou de noite, use **regras de turnos**.
3. Se uma restrição mistura as duas coisas, separe e configure no modelo correto.

Quando você terminar esta seção, deverá estar claro qual modelo responde a cada necessidade e você evitará configurações cruzadas ou contraditórias.

## Selecionando o motor GoalBus Classic para o cálculo final

Agora você precisa configurar o motor de cálculo. Para este quick start, o foco é trabalhar com **GoalBus Classic** como motor principal do cenário. Esse é o motor de otimização profunda orientado a obter a melhor solução final quando a parametrização já está suficientemente madura.

Antes de começar esta seção, certifique-se de que:
1. Você já criou o cenário.
2. Você já selecionou corretamente serviço, linhas e matriz de viagens em vazio.
3. Você sabe quais modelos de regras vai usar.
4. Você está pronto para um cálculo final (ou quase final), e não apenas um teste rápido.

Para selecionar o motor Classic:
1. Abra o cenário que você acabou de criar.
2. Na barra superior, clique em **Configurações de cálculo**.
ref: P14_Imagen7.png | compact
3. No painel lateral, selecione **Motor GoalBus Classic**.
4. Confirme que o cenário não está configurado com o motor de aprendizagem automática.
5. Defina a **Flexibilidade de programação para a primeira solução** (padrão é 0).
6. Use um valor prudente que permita encontrar a primeira solução sem desvirtuar o caso.
7. Selecione o **Tempo máximo de cálculo** para obtenção de novas soluções.
ref: P14_Imagen8.png | compact
8. Salve a configuração.

A flexibilidade inicial aplica-se ao motor GoalBus Classic e serve para que a primeira solução não seja bloqueada se as restrições estiverem rígidas demais. O tempo máximo de cálculo atua como garantia de entrega e obriga o sistema a devolver a melhor solução válida encontrada dentro do prazo.

Para o caso de referência:
1. Use **GoalBus Classic** como motor principal.
2. Deixe o motor de aprendizagem automática apenas para validações rápidas prévias, não como motor do cálculo final.
3. Use flexibilidade inicial moderada se suspeitar que restrições podem bloquear a primeira solução.
4. Defina um tempo máximo realista para que a equipe receba uma solução viável dentro do prazo esperado.

Quando você terminar esta seção, deverá ter o motor Classic configurado com um marco de cálculo controlado e realista.

## Revisando o cenário antes de executá-lo

Antes de calcular, você precisa fazer uma revisão final do cenário completo. O objetivo é confirmar que você não está entrando no cálculo com entradas contraditórias.

Antes de continuar, certifique-se de que:
1. Você escolheu o serviço validado correto.
2. Você selecionou a matriz de viagens em vazio do tipo de dia correto.
3. Você atribuiu os modelos corretos de regras de veículos e de turnos.
4. Você selecionou o GoalBus Classic como motor.
5. Você ajustou flexibilidade e tempo máximo.

Para revisar o cenário antes de executar o cálculo:
1. Revise o nome e o tipo de dia do cenário.
2. Confirme que o **serviço comercial** corresponde exatamente ao que você quer programar.
3. Confirme que a **matriz de viagens em vazio** corresponde ao mesmo contexto temporal.
4. Revise o **modelo de regras de veículos** e confirme que protege a lógica de frota.
5. Revise o **modelo de regras de turnos** e confirme que protege a lógica de trabalho humano.
6. Verifique se você não está omitindo um modelo obrigatório para o seu caso.
7. Se tudo estiver coerente, deixe o cenário pronto para cálculo.

Para o caso de referência, não prossiga até poder afirmar:
1. A L1 dia útil usa o serviço validado correto.
2. A matriz de dia útil é a correta.
3. O modelo de veículos limita a frota de forma realista.
4. O modelo de turnos organiza o trabalho de forma coerente.
5. O GoalBus Classic está selecionado.

Quando você terminar esta seção, deverá ter um cenário limpo, coerente e pronto para o cálculo final.

## Leituras adicionais

- [Executando e validando o primeiro cálculo de Scheduling](P15_Executando_e_validando_o_primeiro_calculo_de_scheduling.md)

