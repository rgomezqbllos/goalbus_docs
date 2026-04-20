---
title: Criando a oferta de serviço base com viagens e horários
shortTitle: Oferta de serviço
intro: "Aprenda a criar um serviço comercial, revisar suas viagens por linha e sentido e deixar uma oferta validada e executável antes de passar para Scheduling no GoalBus."
contentType: how-tos
versions:
  - "*"
---

## Criando o serviço comercial que atuará como contêiner da oferta

Antes de revisar viagens individuais, você precisa criar o **serviço comercial** que atuará como contêiner da sua oferta. No GoalBus, os serviços comerciais são a camada de governança da oferta: vinculam linhas e rotas, tipos de dia e lógica de calendário, e as viagens que definem o serviço real. Essa estrutura evita que horários incompletos ou não revisados cheguem a ser usados operacionalmente.

Use este quick start quando você já tiver uma rede validada, uma base temporal definida e precisar transformar essa estrutura em uma oferta real que depois possa ser validada, medida e consumida no Scheduling.

Antes de começar, certifique-se de que:
1. Você já configurou tipos de dia e feriados no P2.
2. Você já validou o ano operacional no P3.
3. Você já preparou a rede mestra e a rede operacional no P6 e no P7.
4. Você já preparou parkings e depósitos no P5.
5. Você já definiu tipos de veículo permitidos no P4.
6. Você já carregou viagens em vazio e deslocamentos no P8.
7. Você já criou a versão de tempo e os tempos de percurso no P9.
8. Você sabe qual linha, tipo de dia e sentido vai usar como caso de referência.

Para este quick start, use este caso de referência:

> **Vou criar o serviço comercial de dias úteis da linha L1, revisar suas viagens de ida e volta e deixar a oferta validada antes de passar para Scheduling.**

Para criar o serviço comercial do seu caso:
1. No GoalBus, vá para a visão **Serviços**.
ref: P10_Imagen1.png | compact
2. Verifique se já existe um serviço comercial adequado para o seu caso.
3. Se o serviço já existir, abra-o e confirme que ele corresponde ao tipo de dia e à oferta que você quer preparar.
4. Se não existir, crie um novo.
ref: P10_Imagen2.png | compact
5. Defina:
   1. Um **nome** claro para o serviço,
   2. O **tipo de dia** que se aplicará,
   3. As **linhas** que farão parte desse serviço,
   4. A **descrição** do serviço, se você quiser adicionar mais detalhe (opcional).
6. Salve o serviço.
ref: P10_Imagen3.png | compact
7. Confirme que você já consegue entrar na visão de horários ou na grade de viagens.

Para o caso de referência, uma opção válida poderia ser:
- **Dia útil padrão - L1**

Também é possível criar o novo serviço a partir da importação de arquivos GTFS. Para isso:
1. No GoalBus, vá para a visão **Serviços**.
ref: P10_Imagen1.png | compact
2. Importe os arquivos GTFS em **Importar serviços**.
ref: P10_Imagen11.png | compact
3. Se não houver erros na carga, o serviço terá sido criado corretamente.
4. Ao abrir o serviço, é possível ver todas as viagens criadas com a importação.

Quando você terminar esta seção, deverá ter um serviço comercial que atua como contêiner estruturado da oferta.
ref: P10_Imagen4.png  | full

## Acessando a grade de viagens e mudando de contexto

Depois de criar o serviço, o próximo passo é entrar na grade de viagens. Essa visão é uma “torre de controle” centralizada para todas as viagens programadas dentro do serviço. A partir daqui você pode mudar de linha, mudar de serviço e alternar entre **Sentido 1** e **Sentido 2** sem perder o contexto operacional.

Antes de começar esta seção, certifique-se de que:
1. Você já criou ou validou o serviço comercial.
2. Você sabe qual linha quer revisar primeiro.
3. Você sabe qual sentido/direção vai usar como ponto de partida.

Para acessar e mudar de contexto na grade de viagens:
1. Na lista de serviços, clique no identificador do serviço ou no ícone **Ver horários**.
2. Uma vez dentro, use o seletor de linha para alternar entre as linhas incluídas no serviço.
3. Use o menu suspenso de serviços se quiser comparar com outro serviço comercial.
4. Alterne entre **Sentido 1** e **Sentido 2** para revisar separadamente as viagens de ida e volta.
5. Mantenha o foco em uma única linha e em um único sentido enquanto constrói o seu caso base.

Para o caso de referência:
1. Abra o serviço **Dia útil padrão - L1**.
2. Entre primeiro em **Sentido 1**.
3. Depois revise **Sentido 2**.
ref: P10_Imagen5.png  | full

Quando você terminar esta seção, deverá conseguir navegar pela oferta sem perder o contexto de linha, serviço e direção.

## Criando ou revisando as viagens do serviço

Agora sim, entre no detalhe das **viagens**. Um horário é uma sequência de eventos, e cada viagem deve estar vinculada a:
1. uma variação específica de rota,
2. uma sequência de paradas,
3. e uma referência temporal.

Isso garante que saídas e chegadas sejam fisicamente executáveis. A grade mostra por padrão apenas as paradas principais/pontos temporais para manter uma visão clara, embora você possa ampliar para ver todas as intermediárias.

Antes de começar esta seção, certifique-se de que:
1. Você já tem uma versão de tempo válida no P9.
2. Você sabe qual variação de rota corresponde à viagem que quer criar ou revisar.
3. Você sabe qual linha e qual sentido está editando.

Para criar ou revisar as viagens do serviço:
1. Dentro do serviço, selecione uma linha e um sentido.
2. Revise as viagens que já existem na grade.
3. Se precisar criar uma nova viagem, use a ação correspondente para adicionar uma nova saída.
ref: P10_Imagen9.png | compact
4. Atribua à viagem:
   1. a **rota/variação** correta,
   2. a **hora de saída**,
   3. e a **referência temporal** coerente com a versão criada no P9.
   ref: P10_Imagen10.png
5. Se a viagem já existir, passe o cursor sobre o identificador para verificar qual variação de rota ela está usando.
6. Verifique se a duração total calculada faz sentido em relação aos tempos de percurso definidos.
7. Amplie a sequência se precisar revisar todas as paradas intermediárias.
8. Repita até ter uma base mínima de viagens por sentido.

Para o caso de referência, você pode começar com uma estrutura mínima assim:
1. L1 - Sentido 1
   1. Viagem 1: saída 06:00
   2. Viagem 2: saída 06:20
2. L1 - Sentido 2
   1. Viagem 1: saída 06:10
   2. Viagem 2: saída 06:30

Quando você terminar esta seção, deverá ter uma oferta básica de viagens já vinculada a rota, sentido e referência temporal.

## Revisando intervalos, duração total e equilíbrio da oferta

Depois de criar ou revisar viagens, você precisa confirmar que a oferta faz sentido como conjunto. A grade permite acompanhar continuamente:
1. a **duração total** de cada viagem,
2. o **intervalo** em relação à viagem anterior,
3. e os KPIs globais por linha, como quantidade de viagens, distância total e tempo total de condução.

Isso permite avaliar se a oferta é equilibrada, simétrica e economicamente viável.

Antes de continuar, certifique-se de que:
1. Você já tem algumas viagens criadas ou revisadas.
2. Você já consegue ver a duração total dessas viagens.
3. Você já consegue comparar sentidos e frequências.

Para validar o equilíbrio da oferta:
1. Na grade, revise a **duração total** de cada viagem.
2. Verifique se ela coincide razoavelmente com os tempos de percurso esperados.
3. Revise o **intervalo** em relação à viagem anterior e detecte lacunas excessivas ou saídas muito próximas.
4. Compare o número de viagens do **Sentido 1** com o do **Sentido 2**.
5. Revise os KPIs globais da linha:
   1. **Quantidade de viagens**,
   2. **Distância total**,
   3. **Tempo total**.
ref: P10_Imagen6.png | compact
6. Corrija qualquer desequilíbrio evidente antes de considerar o serviço pronto.

Para o caso de referência, pergunte-se:
1. Ida e volta estão equilibradas?
2. Os intervalos entre viagens correspondem ao nível de oferta que você quer construir?
3. A duração total de cada viagem é coerente com a referência temporal?
4. A oferta parece economicamente razoável ou está superdimensionada?

Quando você terminar esta seção, deverá ter uma oferta não apenas criada, mas também revisada do ponto de vista de frequência, duração e equilíbrio.

## Validando o serviço para deixá-lo pronto para cálculo

O último passo é **validar** o serviço. Validar bloqueia os dados das viagens e habilita o serviço para programação, enquanto um serviço não validado continua em edição e não está pronto para cálculo. Um serviço validado passa a estar restrito para edição, deixa de ser excluível e fica pronto para uso na programação.

Antes de terminar, certifique-se de que:
1. Você já revisou as viagens do serviço.
2. Você já conferiu rotas, durações e intervalos.
3. Você já confirmou que a oferta atende ao caso que você quer construir.

Para validar o serviço e deixá-lo pronto para Scheduling:
1. Revise uma última vez a grade de viagens do serviço.
2. Confirme que você não precisa continuar editando o serviço.
3. Execute a ação **Validar** no serviço (ou no conjunto de viagens correspondente).
ref: P10_Imagen7.png | full
4. Verifique se o status do serviço muda para **Validado**.
ref: P10_Imagen8.png | compact
5. Confirme que:
   1. as viagens ficam bloqueadas contra alterações acidentais,
   2. o serviço já está **pronto para cálculo**,
   3. e o Scheduling poderá lê-lo nos próximos passos.
6. Se você ainda precisar de alterações, use **Não validar** apenas para devolver o serviço à edição, finalizar os ajustes e validar novamente.

Para o caso de referência, não prossiga para Scheduling até conseguir afirmar:
1. A linha L1 tem uma oferta de dias úteis coerente.
2. As viagens estão associadas à variação de rota correta.
3. A duração total e os intervalos fazem sentido.
4. O serviço está em status **Validado**.

Quando você terminar esta seção, deverá ter uma oferta comercial estruturada, revisada e validada, pronta para que o Scheduling a consuma.

## Leituras adicionais

- [Validando a estrutura operacional e o status do serviço](P11_Validando_a_estrutura_operacional_e_o_status_do_servico.md)

