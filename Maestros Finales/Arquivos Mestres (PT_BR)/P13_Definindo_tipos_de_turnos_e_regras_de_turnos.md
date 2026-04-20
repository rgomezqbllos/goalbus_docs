---
title: Definindo tipos de turnos e regras de turnos
shortTitle: Tipos e regras
intro: 'Aprenda a criar tipos de turnos, organizá-los dentro de modelos de regras e ativar as restrições ou penalidades necessárias para que o Scheduling construa tarefas legalmente válidas e operacionalmente coerentes.'
contentType: how-tos
versions:
  - '*'
---

## Criando os tipos de turnos que estruturarão o trabalho

Antes de configurar regras de turnos, você precisa definir os **tipos de turnos** que o sistema vai usar para agrupar viagens em trabalho humano coerente. Um tipo de turno não é apenas um rótulo visual. É a categoria lógica que guia o motor para construir tarefas reconhecíveis e utilizáveis depois no Rostering, na operação diária e em integrações com outros sistemas.

Use este quick start quando você já tiver uma oferta validada, uma lógica de veículos definida e precisar dizer ao sistema quais formas de trabalho são válidas para o seu caso.

Antes de começar, certifique-se de que:
1. Você já criou e validou a oferta de serviço no P10.
2. Você já validou a estrutura operacional no P11.
3. Você já definiu as regras de veículos no P12.
4. Você sabe qual serviço e qual contexto operacional vai usar como referência.

Para este quick start, use este caso de referência:

> **Vou definir os tipos de turnos da linha L1 para que o Scheduling possa construir tarefas coerentes antes de criar o cenário de cálculo.**

Para criar os tipos de turnos do seu caso:
1. No GoalBus, vá em **Configuração** > **Pessoal** > **Tipos de turnos**.
ref: P13_Imagen1.png | compact
2. Verifique se já existem tipos de turnos adequados para o seu caso.
3. Se o tipo já existir, abra-o e confira se continua válido.
4. Se não existir, crie um novo.
5. Defina estes campos:
   1. **Nome completo**, com um nome claro e descritivo.
   2. **Nome abreviado**, para visualizações compactas e cartões operacionais.
   3. **ID externo**, se o cliente precisar integrar com sistemas de RH ou folha.
ref: P13_Imagen2.png | compact
6. Marque o tipo como **Ativo** se ele deve participar de cálculos futuros.
7. Salve o tipo de turno.
8. Repita para cada categoria de trabalho que você realmente precisa no seu caso.

Para o caso de referência, você poderia criar tipos como:
1. **Turno manhã**
2. **Turno tarde**
3. **Turno partido**, se a operação exigir

Quando você terminar esta seção, deverá ter os tipos de turnos que servirão como o “DNA” das tarefas que o Scheduling construirá.

## Criando ou selecionando o modelo de regras de turnos

Depois de criar os tipos de turnos, você precisa definir o contêiner onde as regras vão viver. As regras de turnos não são gerenciadas como uma lista plana, e sim dentro de **modelos** que agrupam um conjunto coerente de restrições para um cenário, um período ou uma simulação. Isso permite manter várias configurações sem misturar regras históricas com regras ativas.

Antes de começar esta seção, certifique-se de que:
1. Você já criou ou validou os tipos de turnos que vai usar.
2. Você sabe qual serviço ou simulação vai usar como referência.
3. Você tem claro se este modelo será reutilizável ou específico do caso.

Para criar ou selecionar o modelo de regras:
1. No GoalBus, vá em **Configuração** > **Pessoal** > **Regras de turnos**.
2. Verifique se já existe um **modelo de regras** adequado para o seu caso.
3. Se o modelo já existir, abra-o e confira se continua válido.
4. Se não existir, crie um novo modelo clicando em **Adicionar Novo Modelo**.
5. Dê um **Nome** claro ao modelo.
6. Se aplicável, adicione uma **Descrição** que identifique o uso.
7. Salve o modelo.
ref: P13_Imagen3.png | compact
8. Confirme que você já pode adicionar regras dentro desse contêiner.

Para o caso de referência, uma opção válida poderia ser:
- **Turnos - L1**
- **Regras de turnos**

Quando você terminar esta seção, deverá ter um modelo de regras pronto para receber restrições e penalidades específicas.

## Ativando regras de turnos como restrições ou penalidades

Agora você pode começar a configurar as regras. É importante distinguir duas lógicas:
1. **Restrições**, que são obrigatórias e bloqueiam tarefas inválidas.
2. **Penalidades**, que não bloqueiam, mas empurram o otimizador para soluções preferidas.

Isso é essencial porque nem tudo o que você quer na operação deve virar uma proibição absoluta. Algumas condições devem atuar como guia, não como muro.

Antes de começar esta seção, certifique-se de que:
1. Você já criou ou selecionou um modelo de regras.
2. Você sabe qual comportamento de trabalho quer impedir.
3. Você sabe qual comportamento quer favorecer sem torná-lo obrigatório.

Para gerenciar as regras de turnos do seu caso:
1. Se quiser criar uma nova regra, clique em **Adicionar Nova Regra**.
2. Dentro do modelo, revise os **templates de regras** disponíveis e dê um **Nome** e uma **Descrição** à nova regra.
3. Selecione o template que corresponde ao controle que você quer aplicar.
4. Crie uma **regra específica** a partir do template clicando em **Confirmar**.
ref: P13_Imagen4.png | compact
6. Decida **a quais tipos de turno cada regra se aplica**. Nem todas as regras devem se aplicar a todos os tipos.
7. Insira os parâmetros concretos da regra.
8. Salve a regra.
9. Repita apenas para as regras que o seu caso realmente precisa.
10. Verifique se as regras que você precisa estão ativas. Para ativar uma regra, ela deve ter sido atribuída a pelo menos um tipo de turno.
ref: P13_Imagen5.png | compact

Para o caso de referência, pense em exemplos como:
1. O turno da manhã deve começar dentro de uma janela específica.
2. Um turno partido não deveria exceder um nível de amplitude.
3. Uma sequência pouco desejável pode ser penalizada em vez de proibida.

Quando você terminar esta seção, deverá ter um conjunto inicial de regras que reflita limites obrigatórios e preferências operacionais.

## Revisando se as regras estão atribuídas ao tipo de turno correto

Depois de ativar as regras, você precisa revisar **a quais tipos de turno cada uma se aplica**. Algumas regras podem ser globais, outras devem ser específicas (manhã, tarde, partido).

Antes de continuar, certifique-se de que:
1. Você já ativou pelo menos uma regra dentro do modelo.
2. Você já definiu os tipos de turno que participam do caso.
3. Você sabe se a regra deve ser global ou específica.

Para revisar corretamente o escopo:
1. Selecione cada regra que você criou.
2. Revise a seção **Tipos de turnos aplicáveis**.
3. Selecione os tipos específicos aos quais a regra deve se aplicar.
4. Se a regra deve afetar todos os tipos do cenário, configure-a como global selecionando **todos os tipos de turno**.
5. Verifique se não existem duas regras ativas do mesmo template aplicadas ao mesmo tipo de turno, caso isso gere conflito lógico.
6. Salve a configuração.
7. Repita para cada regra do modelo.

Para o caso de referência:
1. Uma janela de início cedo pode se aplicar apenas ao **Turno manhã**.
2. Uma regra de descanso pode se aplicar a vários tipos.
3. Uma preferência geral pode ser global.

Quando você terminar esta seção, deverá ter regras com escopo claro e sem conflitos lógicos entre si, similar à imagem a seguir:
ref: P13_Imagen6.png | full

## Verificando que a lógica de turnos continua compatível com o serviço

O último passo é verificar se os tipos de turno e as regras que você definiu continuam compatíveis com a oferta validada e com a lógica de veículos que você já fechou. Não adianta ter regras “bonitas” se o resultado deixar o serviço sem uma forma realista de ser programado.

Antes de terminar, certifique-se de que:
1. Você já criou os tipos de turno necessários.
2. Você já ativou e atribuiu as regras correspondentes.
3. Você sabe qual serviço será a entrada do cenário de Scheduling.

Para validar que o caso continua calculável:
1. Revise o serviço validado que você vai usar como referência.
2. Verifique que os tipos de turno que você criou conseguem organizar esse trabalho.
3. Revise se alguma regra deixa o caso rígido demais.
4. Verifique que não existe contradição forte com as regras de veículos já ativadas.
5. Pergunte-se se o sistema já poderia construir tarefas legais e operacionalmente coerentes com essa base.
6. Se a resposta for sim, continue com o próximo quick start.
7. Se a resposta for não, corrija os tipos ou as regras antes de seguir.

Para o caso de referência, não prossiga até poder afirmar:
1. A oferta validada da L1 continua compatível com os tipos de turno definidos.
2. As regras não bloqueiam o caso desnecessariamente.
3. O modelo já está pronto para entrar no cenário de Scheduling.

Quando você terminar esta seção, deverá ser capaz de afirmar que a lógica de turnos está suficientemente fechada para passar à criação do cenário de Scheduling.

## Leituras adicionais

- [Criando o primeiro cenário de Scheduling](P14_Criando_o_primeiro_cenario_de_scheduling.md)

