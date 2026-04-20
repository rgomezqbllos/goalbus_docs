---
title: Carregando viagens em vazio e deslocamentos
shortTitle: Viagens em vazio
intro: "Aprenda a configurar matrizes de viagens em vazio e deslocamentos de motoristas para que o GoalBus use tempos logísticos reais, minimize custos não produtivos e construa horários e turnos mais realistas."
contentType: how-tos
versions:
  - "*"
---

## Criando a matriz adequada para o tipo de dia correto

Antes de calcular o Scheduling, você precisa definir como a operação se move fisicamente quando não está gerando receita. No GoalBus, este módulo cobre duas coisas diferentes:

1. **Viagens em vazio**, que representam o movimento de um ônibus com motorista entre o depósito, o parking, o início de uma linha ou entre linhas.
2. **Deslocamentos de motoristas**, que representam o deslocamento do motorista sem veículo, por exemplo a pé, de táxi ou em van/shuttle.

O GoalBus não trata esses movimentos como uma lista única e fixa. A ferramenta deixa claro que eles devem ser organizados em **matrizes por tipo de dia**, porque o trânsito muda conforme o contexto operacional. Um trajeto pode durar 15 minutos em um domingo e 45 minutos em uma segunda-feira de manhã, então a mesma conexão não deveria reutilizar sempre o mesmo tempo.

Use este quick start quando você já tiver configurado parkings e depósitos e precisar preparar a logística “invisível” que torna o planejamento realista possível.

Antes de começar, certifique-se de que:
1. Você já preparou os parkings e depósitos no P5.
2. Você sabe qual linha ou serviço vai usar como referência.
3. Você sabe qual tipo de dia está modelando.
4. Você entende a diferença entre uma viagem em vazio e um deslocamento de motorista.

Para este quick start, use este caso de referência:

> **Vou preparar a matriz de viagens em vazio para um dia útil da linha L1, conectando o Parking Norte ao Terminal Norte, e também a matriz de deslocamentos de motoristas quando necessário para relevos.**

Para criar a matriz correta para o seu caso:
1. No GoalBus, abra o módulo de **viagens em vazio e deslocamentos**.
ref: P8_Imagen1.png | full
2. Primeiro decida se você vai criar uma matriz de **viagens em vazio**, uma matriz de **deslocamentos de motoristas** ou ambas.
3. Clique em **Criar novo**.
ref: P8_Imagen2.png | compact
4. Informe um **nome** claro para a matriz.
5. Adicione uma **descrição** que ajude a reconhecer o contexto operacional.
6. Atribua os **tipos de dia** aos quais essa matriz se aplicará.
7. Salve a matriz.
ref: P8_Imagen3.png | compact
8. Verifique se a matriz ficou claramente associada ao contexto correto e não a uma lógica genérica.

Para o caso de referência, uma matriz válida poderia se chamar:
- **Vazios - Janeiro de 2026**
- **Deslocamentos de motoristas - Dias úteis**

Quando você terminar esta seção, deverá ter uma matriz criada e vinculada ao tipo de dia adequado.

## Carregando conexões por importação em massa ou edição manual

Depois de criar a matriz, você precisa preenchê-la com as conexões reais entre origens e destinos. O GoalBus permite duas formas de trabalho:

1. **Importação em massa via CSV**, recomendada para redes grandes.
2. **Entrada manual**, útil para casos pequenos ou ajustes pontuais.

Antes de começar esta seção, certifique-se de que:
1. Você já criou a matriz correta.
2. Você já identificou as origens e destinos relevantes.
3. Você sabe se o seu caso pode ser carregado manualmente ou se vale mais a pena importar em massa.

Para carregar dados por importação em massa:
1. Prepare um arquivo CSV no formato padrão do GoalBus.
2. Garanta incluir pelo menos:
   1. Origens
   2. Destinos
   3. Distâncias
   4. Faixas horárias, quando aplicável
   5. Durações
3. No GoalBus, selecione a opção de **carga/importação**.
ref: P8_Imagen4.png | compact
4. Escolha o arquivo CSV.
5. Revise a **validação prévia** do sistema.
6. Verifique se o sistema:
   1. detecta erros,
   2. indica quantos registros serão criados.
ref: P8_Imagen5.png |compact
7. Se a validação estiver correta, confirme a carga.
8. Verifique se a grade ficou preenchida com os registros esperados.

Se estiver tudo correto, a matriz será visualizada de forma semelhante à imagem a seguir:
ref: P8_Imagen6.png |full

Para carregar dados manualmente:
1. Abra a grade da matriz.
2. Adicione um novo registro clicando em **Nova relação**.
ref: P8_Imagen7.png | compact
3. Defina a **origem**.
4. Defina o **destino**.
5. Insira o tempo ou a distância correspondente.
6. Se aplicável, defina a faixa horária.
ref: P8_Imagen8.png | compact
7. Salve o registro.
8. Repita até completar as conexões mínimas necessárias para o seu caso.

Para o caso de referência, comece com conexões como:
1. Parking Norte → Terminal Norte
2. Terminal Sul → Parking Norte

Quando você terminar esta seção, deverá ter uma matriz com conexões reais, seja por arquivo ou por entrada manual.

## Diferenciando viagens em vazio de deslocamentos de motoristas

Agora você precisa confirmar que não está misturando duas lógicas diferentes. O GoalBus trata **viagens em vazio** e **deslocamentos de motoristas** de forma parecida na configuração, mas com um propósito de negócio diferente:

1. A viagem em vazio usa **ônibus + motorista** e modela a logística de mover um veículo para onde ele é necessário.
2. O deslocamento usa **apenas o motorista** e modela o tempo que uma pessoa precisa para chegar a um ponto de relevo ou início sem mover frota.

Antes de continuar, certifique-se de que:
1. Você já carregou pelo menos as conexões essenciais do seu caso.
2. Você consegue identificar se cada conexão corresponde a um veículo ou apenas a uma pessoa.
3. Você não misturou as duas lógicas na matriz errada.

Para validar que cada matriz representa o recurso correto:
1. Revise uma conexão de **viagem em vazio** e confirme que a lógica responde a:
   1. mover um veículo do depósito/parking para a linha, ou
   2. mover um veículo entre linhas.
2. Revise uma conexão de **deslocamento** e confirme que a lógica responde a:
   1. deslocar um motorista sem veículo, ou
   2. permitir um relevo em um terminal.
3. Verifique se a matriz de viagens em vazio está modelando tempos dependentes do trânsito.
4. Verifique se a matriz de deslocamentos de motoristas reflete o modo real de deslocamento, como caminhar, táxi ou shuttle.
5. Corrija qualquer conexão colocada no lugar errado antes de seguir.

Para o caso de referência, pergunte-se:
1. Estou modelando aqui um ônibus saindo do parking ou apenas um motorista indo a um terminal?
2. O tempo que coloquei corresponde ao trânsito real ou ao modo de deslocamento do motorista?
3. O motor usaria essa informação corretamente ao construir o horário e os turnos?

Quando você terminar esta seção, deverá estar claro qual parte da configuração pertence à logística do veículo e qual pertence à logística do motorista.

## Verificando que a matriz está pronta para Scheduling

O objetivo final deste quick start não é apenas preencher uma tabela, mas preparar uma base logística que o Scheduling possa consumir. Um modelado preciso melhora:

1. a **transparência de custos**,
2. a **criação realista de turnos**,
3. a **precisão da otimização**.

Antes de terminar, certifique-se de que:
1. A matriz correta existe.
2. Ela está associada ao tipo de dia correto.
3. As conexões mínimas do caso já estão carregadas.
4. Você separou corretamente viagens em vazio e deslocamentos de motoristas.

Para validar que a matriz já está pronta para o próximo passo:
1. Revise o caso de referência que você está construindo.
2. Confirme que o GoalBus já sabe:
   1. de onde o veículo sai fisicamente,
   2. por onde ele entra na linha,
   3. como ele volta quando necessário,
   4. e como um motorista se deslocaria para um relevo, se aplicável.
3. Pergunte-se se o sistema já poderia minimizar tempos e distâncias não produtivas nesse caso.
4. Se a resposta for sim, continue com o próximo quick start.
5. Se a resposta for não, volte e adicione ou corrija conexões antes de seguir.

Quando você terminar esta seção, deverá ser capaz de afirmar que a sua base logística já é realista o suficiente para sustentar tempos, serviços e Scheduling.

## Leituras adicionais

- [Definindo tipos de veículo e frota permitida por linha](P4_Definindo_tipos_de_veiculo_e_frota_permitida_por_linha.md)

