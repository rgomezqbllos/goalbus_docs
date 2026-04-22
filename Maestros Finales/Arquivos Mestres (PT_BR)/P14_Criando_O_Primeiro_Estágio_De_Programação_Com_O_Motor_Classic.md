---
title: Criando o primeiro estágio de Programação com o motor Classic
shortTitle: Estágio clássico
intro: Saiba como criar seu primeiro Programação Cenário com o motor GoalBus Classic,
  selecione corretamente as entradas de cálculo e distinga quando aplicar as regras
  Veículo e quando aplicar as regras Turno.
contentType: how-tos
versions:
- '*'
---
## Criando o Cenário com a oferta Validado como ponto de partida

Agora que você já tem a oferta Validado, a lógica Veículo e a lógica de virar, o próximo passo é criar o **Etapa Programação** que irá usar essa base para calcular uma solução executável.

Este Cenário é o ambiente controlado onde você vai combinar:
1. o **Oferta Validado**,
2. o **matriz de viagem vazia**,
3. o **modelo de regras Veículo**,
4. e o **modelo de regras Turno**.

Use este início rápido quando você já tiver a parametrização de base fechada e quer preparar o Cenário definitivo para o cálculo com o motor Classic.

Antes de começar, certifique-se de que:
1. Você já configurou e Validado a oferta de serviço em P10.
2. Já verificou a estrutura operacional da P11.
3. Você já definiu as regras Veículo no P12.
4. Você já definiu os tipos de Turnos e as regras de Turnos no P13.
5. Você já preparou a matriz de viagem vazia para P7.
6. Você sabe que tipo de dia e que Linhas será parte do cálculo.

Para este início rápido, use este caso de referência:

> **Vou criar o primeiro Cenário de Escala para Linha L1, usando a oferta funcional Validado, a matriz de viagem vazia correspondente e os modelos corretos de regras Veículo e Turno, para lançar o cálculo final com GoalBus Classic.**

Para criar o Cenário básico do seu caso:
1. Em GoalBus, abra o módulo **Planejamento**.
ref: P14_Imagen1.png | compact
2. Clique em **Novo Cenário**.
ref: P14_Imagen2.png | compact(2x)
3. Introduz a identidade básica Cenário:
   1. **Nome**
   2. **Tipo de dia**
   3. **Designação das mercadorias** se você quiser dar mais detalhes.
   4. **apenas para Veículos** Cenário ou não.
ref: P14_Imagen3.png | compact(x10)
4. Selecione os elementos básicos do Cenário:
   1. O **Serviço comercial Validado** que você quer cobrir.
   2. Selecione o **Modelo de regras de rotação**.
   3. Selecione o **Modelo das Regras Tipo de veículo** (opcional).
   4. Selecione o **matriz de viagem vazia** correspondente ao mesmo tipo de dia.
   5. Selecione o **Matriz de deslocamento Motorista** que fará parte do estágio.
ref: P14_Imagen4.png | compact(x10)
5. Selecione o Linha.
ref: P14_Imagen5.png | compact(x12)
6. Salva ou completa a criação do palco.
7. Verifique se o Cenário aparece na tabela de planejamento principal.

Para o caso de referência, uma opção válida pode ser:
- **Programação Clássico - L1 utilizável**

Quando você terminar este Seção, você deve ter um Cenário criado com sua logística correta e entradas comerciais criados como na seguinte imagem:
ref: P14_Imagen6.png | full

## Compreender quando usar as regras Veículo e quando usar as regras Turno

Antes de configurar o motor, você precisa deixar clara uma distinção importante: **As regras Veículo e as regras Turno não resolvem o mesmo problema.**.

Use o **Regras Veículo** quando quiser controlar o comportamento do Frota. Estas são as regras certas se precisar modelar:
1. Compatibilidade física de Veículos,
2. a capacidade ou os limites de alcance,
3. Restrições às infra-estruturas,
4. ou políticas operacionais ligadas à utilização do Frota.

Use o **Regras de Turno** quando quiser controlar como o trabalho humano é organizado. São as regras certas se precisar modelar:
1. horas de trabalho,
2. quebras e quebras,
3. horas de início e fim,
4. amplitude,
5. ou diferenças entre os tipos de Turno, tais como manhã, tarde ou noite.

Antes de continuar, certifique-se de que:
1. Você sabe que restrições pertencem ao Veículo.
2. Você sabe que restrições pertencem ao Turno.
3. Você não está tentando resolver um problema de pessoal com as regras Frota, ou ao contrário.

Para decidir qual o modelo a utilizar em cada caso:
1. Pergunte a si mesmo se a restrição afeta **autocarro** ou **Motorista**.
2. Se afetar **autocarro**, utilize **modelo de regras Veículo**.
3. Se afetar o **trabalho humano** ou o tipo Turno, utilize o **modelo de regras Turno**.
4. Se uma regra deve ser aplicada a todos os tipos de Turnos, revisá-la como regra global ou com o mais amplo alcance disponível.
5. Se uma regra se aplica apenas a um determinado tipo de Turno, atribua-o apenas a esse tipo.

Para o caso de referência:
1. Se você quiser limitar que Frota pode cobrir o L1, use **Regras Veículo**.
2. Se você quiser controlar como um Turno é construído amanhã ou à noite, use o **Regras de Turno**.
3. Se uma restrição misturar ambos, separe-o e configure-o no modelo certo.

Quando você terminar este Seção, você deve ser claro sobre qual modelo responde a cada necessidade e evitar cruz ou contraditório Configuraçãos.

## Selecionando o motor GoalBus Classic para o cálculo final

Agora você precisa configurar o motor de cálculo. Para este início rápido, o foco é trabalhar com **GoalBus Clássico** como o motor principal do palco. Este é o motor de otimização profunda destinado a obter a melhor solução final quando a parametrização está madura o suficiente. fileciteturn34file0L1-L20 fileciteturn34file2L1-L20

Antes de iniciar este Seção, certifique-se de que:
1. Você já tem o palco criado.
2. Você selecionou o serviço, Linhas e matriz de viagem vazia corretamente.
3. Você já está claro sobre os modelos de regras que você vai usar.
4. Estão prontos para um cálculo final ou quase final, não só para um teste tático rápido.

Para selecionar o motor Clássico:
1. Abra o Cenário que acabou de criar pressionando nele.
2. Na barra superior, clique em **Cálculo Configuração**.
ref: P14_Imagen7.png | compact
3. No painel lateral, selecione **Motor GoalBus Clássico**.
4. Confirma que o Cenário não está mais configurado com o motor de aprendizagem de máquina.
5. Determina o **Flexibilidade de programação para a primeira solução** (o padrão é 0).
6. Use um valor prudente que lhe permita encontrar uma solução inicial sem distorcer o caso.
7. Selecione o **Tempo máximo de cálculo** que o motor terá para novas soluções.
ref: P14_Imagen8.png | compact(x8)
8. Salve o Configuração.

A flexibilidade inicial aplica-se apenas ao motor GoalBus Classic e serve para garantir que a primeira solução não seja bloqueada se as restrições forem demasiado rígidas desde o início. O tempo máximo de cálculo funciona como uma garantia de entrega e força o sistema a devolver a melhor solução válida que encontrou dentro do tempo disponível. filetturn34file0L1-L20 filetturn34file2L1-L20

Para o caso de referência:
1. Use **GoalBus Clássico** como motor principal.
2. Reserve o motor de aprendizado automático apenas para validações rápidas anteriores, não como um motor de cálculo final.
3. Use flexibilidade inicial moderada se suspeitar que restrições podem bloquear a primeira solução.
4. Define um tempo máximo realista para a equipe receber uma solução viável dentro do tempo esperado. fileciteturn34file0L1-L20fileciteturn34file0L1-L20 fileciteturn34file2L1-L20

Quando você terminar este Seção, você deve ter o motor Clássico configurado com uma estrutura de cálculo controlada e realista.

## Verificar o palco antes de o lançar.

Antes de calcular, você precisa fazer uma revisão final de todo o Cenário. O objetivo é confirmar que você não está inserindo o cálculo com entradas contraditórias.

Antes de continuar, certifique-se de que:
1. Você já escolheu o serviço Validado correto.
2. Você já selecionou a matriz de viagem vazia do tipo de dia certo.
3. Você já atribuiu os modelos certos de regras Veículo e Turno.
4. Você já selecionou GoalBus Classic como um motor.
5. Já ajustaste a flexibilidade e o tempo máximo.

Para rever o Cenário antes de lançar o cálculo:
1. Verifique o nome e o tipo do dia de palco.
2. Confirme que o **serviço comercial** corresponde exatamente ao que você deseja programar.
3. Confirma que o **matriz de viagem vazia** corresponde ao mesmo contexto temporal.
4. Verifique o **modelo de regras Veículo** e confirme que ele protege a lógica Frota.
5. Verifique o **modelo de regras Turno** e confirme que protege a lógica do trabalho humano.
6. Verifique que não está a faltar a um modelo obrigatório para o seu caso.
7. Se tudo for consistente, deixe o Cenário pronto para o cálculo.

Para o caso de referência, não continue até poder dizer:
1. O L1 de trabalho usa o seu serviço Validado correto.
2. A matriz de trabalho é a certa.
3. O Modelo de veículo limita realistamente o Frota.
4. O modelo Turno organiza o trabalho de forma coerente.
5. GoalBus Classic já está selecionado.

Quando você terminar este Seção, você deve ter um limpo, coerente e pronto para o cálculo final.

## Lecturas adicionais

- [Executar e validar o primeiro cálculo do Programação](P15_Executar_E_Validar_O_Primeiro_Cálculo_Do_Programação.md)
