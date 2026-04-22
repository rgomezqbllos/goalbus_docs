---
title: Criando a oferta de serviço básico com Viagems e Escalas
shortTitle: Oferta de serviço
intro: Aprenda a criar um serviço empresarial, revise suas viagens pela Linha e sinta,
  e deixe uma oferta válida e executável antes de se mudar para a Escala no GoalBus.
contentType: how-tos
versions:
- '*'
---
## Criação do serviço comercial que atuará como container da oferta

Antes de rever o Viagems individual, você precisa criar o **serviço comercial** que atuará como um container para sua oferta. Em GoalBus, os serviços de negócios são a camada de governança da oferta: eles ligam Linhas e Rotas, tipos de dia e lógica de calendário, e Viagems que definem o serviço real. A ferramenta deixa claro que esta estrutura impede que o Escalas incompleto ou não revisado seja utilizado operacionalmente.

Use este início rápido quando você já tiver uma rede Validado, uma base temporal definida, e precisa transformar essa estrutura em uma oferta real que pode então ser Validado, medida e consumida em Programação.

Antes de começar, certifique-se de que:

1. Você já configurou tipos de feriados e dias em P2.
2. Você já tem Validado o ano de operação em P3.
3. Você já preparou a base e a rede operacional em P4 e P5.
4. Você já definiu espaços Garagem, armazéns e Viagems em P6 e P7.
5. Você já definiu os tipos Veículo permitidos em P8.
6. Você já criou o tempo Versão e tempos de viagem em P9.
7. Você está claro o que Linha, que tipo de dia e que sentido você vai usar como um caso de referência.

Para este início rápido, use este caso de referência:

> **Vou criar o serviço de negócios L1, rever o seu retorno Viagems e deixar a oferta Validado antes de mudar para Escala.**

Para criar o serviço comercial do seu caso:

1. Em GoalBus, vá para a vista **Serviços**.
ref: P10_Imagen1.png | compact
2. Descubra se já existe um serviço comercial adequado para o seu caso.
3. Se o serviço já existir, abra-o e verifique se realmente corresponde ao tipo de dia e à oferta que deseja preparar.
4. Se não existir, crie um novo.
ref: P10_Imagen2.png | compact(2x)
5. Definir:
   1. Um **nome** claro para serviço,
   2. O **tipo de dia** a aplicar,
   3. O **Linhas** que fará parte desse serviço.
   4. O serviço **Descrição** se você quiser dar mais detalhes, embora este campo não seja obrigatório.
6. Salve o serviço.
ref: P10_Imagen3.png | compact(x8)
7. Confirme que você já pode inserir sua view Escala ou grelha de viagem.

Para o caso de referência, uma opção válida pode ser:

- **Dia normal de trabalho - L1**

Também é possível criar o novo serviço a partir da carga de arquivo GTFS. Para isso:
1. 1. Em GoalBus, vá para a vista **Serviços**.
ref: P10_Imagen1.png | compact
2. Importar arquivos GTFS do **Serviços de importação**.
ref: P10_Imagen11.png | compact
3. Se não houver erros no carregamento, o serviço terá sido criado corretamente.
4. Ao entrar no serviço, você pode ver todos os Viagems criados com a importação.

Quando você terminar este Seção, você deve ter um serviço comercial que atua como um recipiente estruturado da oferta.
ref: P10_Imagen4.png  | full



## Acesso à grelha de viagens e mudança de contexto

Uma vez criado o serviço, o próximo passo é entrar na grelha de viagem. Esta vista é uma torre de controle centralizada para todos os Viagems programados dentro do serviço. A partir daqui você pode alterar Linha, mudar de serviço e alternar entre **Sentido 1** e **Sentido 2** sem perder o contexto operacional.

Antes de iniciar este Seção, certifique-se de que:

1. Você já criou ou Validado o serviço comercial.
2. Você sabe o que Linha você quer verificar primeiro.
3. Você sabe que sentido ou direção você vai usar como um ponto de partida.

Para acessar e alterar o contexto na grelha de viagens:

1. Na lista de serviços, clique no serviço Identificador ou no ícone **Ver Escalas**.
2. Uma vez dentro, use o seletor Linha para alternar entre o Linhas incluído no serviço.
3. Use o menu suspenso do serviço se quiser comparar com outro serviço comercial.
4. Mude entre **Sentido 1** e **Sentido 2** para rever separadamente a rodada Viagems.
5. Mantenha o foco em um único Linha e um sentido ao construir seu caso base.

Para o caso de referência:

1. Abra o serviço **Dia normal de trabalho - L1**.
2. Digite o **Sentido 1** primeiro.
3. Verifique **Sentido 2** mais tarde.
ref: P10_Imagen5.png  | full

Quando você terminar este Seção, você deve ser capaz de navegar na oferta sem perder o contexto de Linha, serviço e endereço.

## Criação ou revisão de viagens de serviços

Agora sim, digite o detalhe do **viagem**. O documento explica que um Escala é uma sequência de eventos e que cada Viagem deve estar ligado a:

1. uma variação específica de Rota,
2. uma sequência de Paradas,
3. e uma referência temporária.

Isto garante que as saídas e chegadas são fisicamente executáveis. Além disso, a grade mostra por padrão apenas os principais pontos Paradas ou tempo para manter uma visão clara, embora você possa zoomar para ver todos os intermediários.

Antes de iniciar este Seção, certifique-se de que:

1. Você já tem um tempo válido Versão em P9.
2. Você sabe o que a variação Rota corresponde ao Viagem que você deseja criar ou revisar.
3. Você sabe o que Linha e que sentido você está editando.

Para criar ou revisar o serviço Viagems:

1. Dentro do serviço, selecione um Linha e um sentido.
2. Verifique o Viagems que já existe na grade.
3. Se você precisar criar um novo Viagem, use a ação correspondente para adicionar uma nova saída.
ref: P10_Imagen9.png | compact
4. Atribui o Viagem:
   1. o **trajeto ou variação** correcto,
   2. o **hora de partida**,
   3. e o **Referência temporária** consistente com o Versão criado em P9.
ref: P10_Image10.png
5. Se a jornada já existir, passe o cursor sobre o seu Identificador para verificar qual a variação Rota que você está usando.
6. Verifique se a duração total calculada faz sentido em comparação com os tempos de viagem definidos.
7. Expanda a sequência se você precisar verificar todos os intermediários Paradas.
8. Repita o processo até ter uma base mínima de viagens por sentido.

Para o caso de referência, você pode começar com uma estrutura mínima como esta:

1. L1 - Sentido 1
   1. Viagem 1: partida 06:00
   2. Viagem 2: saída 06:20
2. L1 - Sentido 2
   1. Viagem 1: saída 06:10
   2. Viagem 2: partida 06:30

Quando você terminar este Seção, você deve ter uma oferta de viagem básica já ligada ao Rota, sentido, e referência de tempo.

## Intervalos de revisão, duração total e balanço da oferta

Depois de criar ou rever Viagems, você precisa verificar que a oferta faz sentido como um todo. A grade permite que você fique de olho em:

1. o **duração total** para cada Viagem,
2. o **intervalo** em relação à viagem anterior,
3. KPIs globais por Linha, tais como contagem de viagens, total Distância e tempo total Dirigindo. Isso permite avaliar se a oferta é equilibrada, simétrica e economicamente viável.

Antes de continuar, certifique-se de que:

1. Você já tem pelo menos algum Viagems criado ou revisado.
2. Você já pode ver o comprimento total desses Viagems.
3. Você já pode comparar sentidos e frequências.

Para validar o saldo da oferta:

1. Na grade, verifique o **duração total** para cada Viagem.
2. Verifique se corresponde razoavelmente aos tempos de viagem esperados.
3. Verifique o **intervalo** em relação à viagem anterior e veja se há lacunas ou saídas excessivas muito próximas.
4. Compare o número de **Sentido 1** Viagems com o **Sentido 2**.
5. Verifique os KPI globais do Linha:
   1. **Conta de viagem**,
   2. **Total de Distância**,
   3. **Tempo total**.
ref: P10_Imagen6.png | compact
6. Corrige qualquer desequilíbrio óbvio antes de dar o serviço pronto.

Para o caso de referência, pergunte-se:

1. O redondo Viagem e o redondo Viagem estão equilibrados?
2. Os intervalos de viagem correspondem ao nível de oferta que você deseja construir?
3. A duração total de cada Viagem é consistente com a referência temporal?
4. Será que a oferta parece economicamente razoável ou é sobredimensionada?

Quando você terminar este Seção, você deve ter uma oferta não só criado, mas também revisto do ponto de vista da frequência, duração e equilíbrio.

## Validação do serviço para deixá-lo pronto para o cálculo

O último passo é o serviço **validar**. A validação bloqueia os dados de viagem e permite a programação, enquanto um serviço não validado ainda está em fase de edição e não está pronto para o cálculo. Também indica que um serviço Validado se torna restrito para a edição, deixa de ser removível e está pronto para o uso de programação.

Antes de terminar, certifique-se de que:

1. Você já verificou o serviço Viagems.
2. Você já verificou Rotas, duraçãos e intervalos.
3. Você já confirmou que a oferta responde ao caso que você quer construir.

Para validar o serviço e deixá-lo pronto para Programação:

1. Verifique a rede de viagens do serviço pela última vez.
2. Confirme que você não precisa mais editar o serviço.
3. Execute a ação **Validar** no serviço ou no conjunto de viagens correspondente.
ref: P10_Imagen7.png | full
4. Verifique se o estado do serviço muda para **Validação**.
ref: P10_Imagen8.png | compact(2x)
5. Confirma que:
   1. a viagem é bloqueada por alterações acidentais,
   2. o serviço é agora **Pronto para o cálculo**,
   3. e Programação pode lê-lo nos próximos passos.
6. Se você ainda precisar fazer alterações, use a lógica **Não validar** apenas para retornar o serviço à edição e terminá-lo ajustando-o antes de convalidá-lo novamente.

Para o caso de referência, não continue para Escala até poder dizer:

1. Linha L1 tem uma oferta consistente e viável.
2. As viagens estão associadas à variação correta de Rota.
3. A duração total e os intervalos fazem sentido.
4. O serviço já está em estado **Validação**.

Quando você terminar este Seção, você deve ter uma oferta de negócios já estruturado, revisado e Validado pronto para o Programação para consumir.

## Lecturas adicionais

- [Validação da estrutura operacional: armazéns, unidades e grupos](P11_Validação_Da_Estrutura_Operacional_E_Do_Estado_Do_Serviço.md)
