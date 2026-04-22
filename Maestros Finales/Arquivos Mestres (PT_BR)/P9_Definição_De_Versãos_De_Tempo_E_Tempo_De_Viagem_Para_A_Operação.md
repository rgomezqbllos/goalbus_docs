---
title: Definição de Versãos de tempo e tempo de viagem para a operação
shortTitle: Versãos e Tempos
intro: Saiba como criar tempo Versãos, definir tempos de viagem e permanência por
  tipo de dia e espaço de tempo, e deixar uma referência de tempo confiável antes
  de criar ou ajustar serviços no GoalBus.
contentType: how-tos
versions:
- '*'
---
## Criando o Versão do tempo que o seu caso irá usar

Antes de definir os tempos de viagem, você precisa criar um **tempo Versão**. Em GoalBus, um Versão não é apenas uma tag: é a biblioteca do tempo que agrupa a lógica do tempo que se aplicará a tipos específicos de dia Rotas. Isto é importante porque numa segunda-feira de manhã não se comporta como um domingo de manhã, e o sistema não deve reutilizar um único conjunto de tempos para o ano inteiro.

Use este início rápido quando você já tiver um Linha e seu definido Rotas, e você precisa construir a base de tempo que será então usada para calcular a viagem, validar duraçãos e comparar desvios com o padrão.

Antes de começar, certifique-se de que:
1. Você já preparou a rede mestre na P6.
2. Já verificou a rede operacional na P7.
3. Você já definiu a base de tempo dos tipos de dia para P2.
4. Você já tem Validado o ano de operação em P3.
5. Você sabe o que Linha, que Rotas e que tipo de dia você vai usar como referência.

Para este início rápido, use este caso de referência:

> **Vou criar um tempo Versão para o L1 Linha em dias úteis e usá-lo como referência temporária antes de criar ou ajustar serviços.**

Para criar o tempo Versão do seu caso:
1. No GoalBus, abra o **Visualização de Caminhos** do Linha que irá usar como referência.
2. Selecione o ícone ou opção **Gestão de viagens e Parada vezes**.
ref: P9_Imagen1.png | compact
3. No topo da vista, crie um novo Versão selecionando **Novo conjunto de Escalas**.
ref: P9_Imagen2.png | compact
4. Define um **nome** claro para o Versão.
5. Adicione um **Descrição** para ajudá-lo a distinguir o contexto operacional.
6. Selecione o **tipos de dia** ao qual se aplica esse Versão, por exemplo **Dias úteis**.
7. Ligar o **Variações Rota** ou sequências específicas que serão parte desse Versão temporário.
8. Salve o Versão.
ref: P9_Imagen3.png | compact(x8)
9. Verifique se o Versão já está disponível como referência temporária para esse Linha.

Para o caso de referência, um Versão válido pode ser chamado:
- **Dias úteis de inverno**
- **Base de trabalho L1**

Quando você terminar este Seção, você deve ter criado um tempo Versão que o sistema pode usar como uma referência temporária para os serviços desse Linha semelhante ao da imagem abaixo.
ref: P9_Imagen4.png | full

## Definir os tempos de viagem entre os principais Paradas

Após a criação do Versão, você precisa entrar no **tempos de viagem**. No GoalBus, estes tempos são principalmente definidos entre **Principal Paradas** ou **pontos de tempo**, não entre todos os Paradas intermediários. Os cabeçalhos são os principais por padrão, e a partir de lá você constrói a lógica temporária que irá alimentar os serviços.

Além disso, GoalBus não funciona com um único valor por segmento. O motor usa uma lógica **mínimo, óptimo e máximo** para dar flexibilidade de controle ao cálculo:
1. **Mínimo**: o tempo mais rápido possível.
2. **Óptima**: o tempo de alvo que o motor irá definir.
3. **Máximo**: o tempo mais lento aceitável.

Antes de iniciar este Seção, certifique-se de que:
1. Você já criou o tempo Versão.
2. Você sabe que maior Paradas você vai usar como referência.
3. Você já identificou a direção que deseja configurar primeiro.

Para definir os tempos de viagem do seu caso:
1. Dentro da grade de tempo, selecione o **segmento** entre dois principais Paradas.
ref: P9_Imagen5.png | full
2. Crie um ou mais **ranhuras** para refletir a realidade operacional.
3. Para cada faixa, insira:
   1. a hora **Mínimo**,
   2. a hora **óptimo**,
   3. Tempo **Máximo**.
ref: P9_Imagen6.png | compact
4. Salve o segmento.
5. Repita o processo para o próximo segmento principal.
6. Quando você terminar um sentido, repita a mesma lógica para o sentido oposto.

As tiras criadas não devem ter lacunas ou sobreposições entre elas. No caso de haver, não será possível salvar os tempos.

Para o caso de referência, uma lógica básica poderia ser:
1. **Terminal Norte → Centro**
   1. 07:00–09:00
      1. Mínimo: 12 min
      2. Otimizado: 15 min
      3. Máximo: 18 min
   2. 09:00-22:00
      1. Mínimo: 5 min
      2. Otimista: 5 min
      3. Máximo: 5 min
   3. 22:00–06:00
      1. Mínimo: 8 min
      2. Otimista: 10 min
      3. Máximo: 12 min
2. **Centro → Hospital**
3. **Hospital → Universidade**
4. **Universidade → Terminal Sul**

Quando você terminar este Seção, você deve ter definido Dirigindo elástico vezes entre os principais pontos de tempo do Rota.

## Definir os tempos de retenção para a regulação e recuperação

Além do tempo Dirigindo, GoalBus precisa saber quanto tempo um Veículo pode ficar em um Parada principal. Estes **Escala tempos** são importantes porque permitem regular a saída, absorver chegadas precoces e deixar espaço para recuperação em terminais ou pontos Conexão.

Antes de iniciar este Seção, certifique-se de que:
1. Você já definiu tempos de viagem entre os segmentos principais.
2. Sabem que terminais ou pontos importantes necessitam de regulação.
3. Já identificaste onde é necessário um espaço operacional real.

Para definir os tempos de escala:
1. Na grade de tempo, selecione o **coluna** a partir de um Parada principal.
ref: P9_Imagen7.png | full
2. Escolha um terminal importante, cabeçalho ou ponto Conexão.
3. Definir:
   1. **Mínimo**, como tempo de espera obrigatório.
   2. **Máximo**, como margem permitida para regulação ou sincronização.
4. Salve o Configuração.
5. Repita o processo para outro Paradas principal onde você precisa de permanência controlada.

Para o caso de referência, uma possível lógica seria:
1. **Terminal Norte**
   1. Mínimo: 4 min
   2. Máximo: 10 min
2. **Terminal Sul**
   1. Mínimo: 5 min
   2. Máximo: 12 min

Quando você terminar este Seção, você deve ter definido as margens que o motor pode usar para recuperar ou regular sem deformar a lógica do Escala.

## Verificação de fendas, visão estendida e consistência visual

Uma vez que você já tem tempos de viagem e permanência, você precisa verificar se a grade reflete uma lógica realista. O documento destaca que o GoalBus inclui ajudas visuais para detectar erros quando você manipula muitos pontos de dados, muitas tiras, ou vários caminhos.

Antes de continuar, certifique-se de que:
1. Arranjaste pelo menos uma vaga.
2. Você já introduziu valores mínimos, ótimos e máximos.
3. Você já adicionou tempos de retenção nos pontos relevantes.

Para rever visualmente a consistência do Configuração:
1. Verifique a grade e confirme que cada segmento principal tem um intervalo de tempo válido.
2. Use as ajudas visuais disponíveis para detectar valores anormais.
3. Verifique se as horas de pico mostram horas superiores às horas do vale.
4. Expanda a visão se você precisar ver mais detalhes ou mais intermediário Paradas.
5. Correge qualquer valor anómalo diretamente da vista ou do painel de edição.
6. Repita a revisão até a lógica do tempo refletir uma operação credível.

Para o caso de referência, pergunte-se:
1. A hora de ponta aparece com tempos mais altos do que a noite?
2. Os tempos mínimos, ótimos e máximos têm uma relação lógica?
3. Os terminais têm um espaço regulamentar realista?
4. A grelha já representa um dia de trabalho completo?

Quando você terminar este Seção, você deve ter uma base de tempo visualmente revisado livre de inconsistências importantes.

## Aplicando o tempo Versão como referência para serviços

O objetivo final deste início rápido não é apenas criar dados temporários, mas deixar uma referência que pode então ser usada ao criar ou modificar serviços. O documento indica que cada Viagem deve ser medido contra um **referência temporária Versão**, e que esta referência é usada automaticamente quando você cria novo Viagems ou alterar o Rota de um Viagem. Também permite detectar desvios se um Viagem foi importado ou modificado fora do padrão.

Antes de terminar, certifique-se de que:
1. Você já criou um Versão temporário válido.
2. Já definiste tempos de viagem e de permanência.
3. Já verificaste a consistência da grade.
4. Você sabe o que Linha e caso você vai usar para criar serviços.

Para verificar se a sua base temporária está pronta para os serviços:
1. Verifique o Versão do tempo que acabou de criar.
2. Confirma que está ligado ao tipo de dia correto.
3. Confirme que ele inclui o Rotas ou variações que você vai usar.
4. Verifica que tal Versão já poderia atuar como referência temporária para:
   1. criar um novo Viagems,
   2. recalcular os horários de chegada e de partida,
   3. as discrepâncias de auditoria em relação à norma.
5. Se a resposta for sim, continue com o próximo início rápido.
6. Se a resposta for não, volte atrás e corrija o Versão ou seus tempos antes de continuar.

Quando você terminar este Seção, você deve ser capaz de dizer que o Linha já tem um tempo de referência Versão suficiente para criar serviços de uma forma coerente.

## Lecturas adicionais

- [Criando a oferta de serviço básico: grupos de viagem ou serviço por Linha, Rota e significado](P10_Criando_A_Oferta_De_Serviço_Básico_Com_Viagems_E_Escalas.md)
