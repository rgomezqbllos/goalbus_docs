---
title: Carregando viagens vazias e viagens
shortTitle: Viagem vazia
intro: Saiba como configurar viagens vazias e matrizes de viagens Motorista para que
  GoalBus use tempos de logística reais, minimize custos não produtivos e constrói
  Escalas e Turnos mais realistas.
contentType: how-tos
versions:
- '*'
---
## Criando a matriz certa para o tipo de dia certo

Antes de calcular Programação, você precisa definir como a operação se move fisicamente quando não está gerando receita. No GoalBus, este módulo cobre duas coisas diferentes:

1. **Viagem vazia**, representando o movimento de um ônibus com um Motorista entre o tanque, o lote Garagem, o início do Linha ou entre Linhas.
2. **Deslocamentos Motorista**, representando o movimento do Motorista sem um Veículo, por exemplo, a pé, táxi ou nave auxiliar.

GoalBus não trata estes movimentos como uma lista única e fixa. A Ferramenta deixa claro que eles devem ser organizados em **Matrizes por tipo de dia**, porque o tráfego muda de acordo com o contexto operacional. Uma viagem pode durar 15 minutos em um domingo e 45 minutos em uma manhã de segunda-feira, por isso o mesmo Conexão nem sempre deve reutilizar o mesmo tempo.

Use este início rápido quando você já tiver configurado lotes e armazéns Garagem, e você precisa preparar a logística invisível que tornará o planejamento realista possível.

Antes de começar, certifique-se de que:

1. Você já preparou os lotes Garagem e armazéns na P5.
2. Você já está claro sobre o Linha ou serviço que você vai usar como referência.
3. Sabes que tipo de dia estás a modelar.
4. Você entende a diferença entre um passeio vazio e um passeio Motorista.

Para este início rápido, use este caso de referência:

> **Vou preparar a matriz de viagem vazia para um dia útil de Linha L1, conectando o Norte Garagem com o Terminal Norte, e também a matriz de viagem Motorista quando necessário para relés.**

Para criar a matriz correta para o seu caso:

1. Em GoalBus, abra o módulo **Viagens sem carga e viagens**.
ref: P8_Imagen1.png | full
2. Decida primeiro se criar uma matriz **Viagems vazio**, uma matriz **Movimentos Motorista**, ou ambos.
3. Clique em **Criar Novo**.
ref: P8_Imagen2.png | compact(2x5)
4. Digite um **nome** claro para a matriz.
5. Adicione um **Descrição** para permitir que você reconheça o contexto operacional.
6. Atribui o **tipos de dia** ao qual se aplica essa matriz.
7. Salve a matriz.
ref: P8_Imagen3.png | compact(x8)
8. Verifique se a matriz está claramente associada ao contexto correto e não a uma lógica genérica.

Para o caso de referência, uma matriz válida pode ser chamada:

- **Vazio - Janeiro 2026**
- **Dirigindo deslocamentos - dias úteis**

Quando você terminar este Seção, você deve ter uma matriz adequadamente criada ligada ao tipo de dia certo.

## Carregando Conexãos por importação em massa ou edição manual

Uma vez que a matriz é criada, você precisa preenchê-la com o Conexãos real entre origens e destinos. O documento indica que GoalBus permite duas formas de trabalho:

1. **Importação em massa CSV**, recomendado para redes grandes.
2. **Input manual**, útil para pequenos casos ou para completar ajustes de pontos.

Antes de iniciar este Seção, certifique-se de que:

1. Você já criou a matriz certa.
2. Você já identificou as origens e destinos relevantes.
3. Você sabe se o seu caso pode ser carregado manualmente ou se uma importação maciça é desejável.

Para carregar dados por importação em massa:

1. Prepare um arquivo CSV com o formato padrão GoalBus.
2. Certifique-se de incluir pelo menos:
   1. Origens
   2. Destinos
   3. Distâncias
   4. Fases de tempo, quando aplicadas.
   5. Durações
3. No GoalBus, selecione a opção **carga** ou **importação**.
ref: P8_Imagen4.png | compact
4. Escolha o arquivo CSV.
5. Verifique o **pré- validação** que faz o sistema.
6. Verificar se o sistema:
   1. detecta erros,
   2. indica quantos registros serão criados.
ref: P8_Imagen5.png |compact
7. Se a validação estiver correta, confirme a carga.
8. Verifique se a grade está preenchida com os registros esperados.

Se tudo estiver correto, o array será exibido de uma forma semelhante à da seguinte imagem:
ref: P8_Imagen6.png |full

Para carregar manualmente os dados:

1. Abra a grade da matriz.
2. Adicione um novo registro clicando em **Nova relação**.
ref: P8_Imagen7.png | compact
3. Defina o **origem**.
4. Defina o **destino**.
5. Digite o tempo correspondente ou Distância.
6. Se aplicável, definir o intervalo de tempo.
ref: P8_Imagen8.png | compact(15x)
7. Mantém o registo.
8. Repita o processo até completar o mínimo de Conexãos necessário para o seu caso.

Para o caso de referência, comece com Conexãos como este:

1. Norte Garagem → Terminal Norte
2. Terminal Sul → Norte Garagem

Quando você terminar este Seção, você deve ter uma matriz com Conexãos real, carregado por arquivo ou introduzido manualmente.

## Diferenciando a viagem vazia da viagem Motorista

Agora você precisa verificar que você não está misturando duas lógicas diferentes. O documento destaca que GoalBus trata **Viagems vazio** e **Movimentos Motorista** da mesma forma em Configuração, mas com um propósito de negócio diferente:

1. A viagem vazia usa **autocarro + Motorista** e modela a logística de mover um Veículo onde é necessário.
2. O pergaminho usa **apenas Motorista** e modela o tempo que uma pessoa precisa para alcançar um relé ou ponto de partida sem mover Frota.

Antes de continuar, certifique-se de que:

1. Você já carregou pelo menos o Conexãos essencial para o seu caso.
2. Você pode identificar se cada Conexão corresponde a um Veículo ou apenas uma pessoa.
3. Você não misturou ambas as lógicas na mesma matriz errada.

Para validar que cada matriz representa o recurso correto:

1. Verifique um **viagem vazia** Conexão e confirme que a sua lógica responde a:
   1. Mover um Veículo de um tanque ou lote Garagem para o Linha; ou
   2. mover um Veículo entre Linhas.
2. Verifique um **deslocamento** Conexão e confirme que a sua lógica responde a:
   1. Mover um Motorista sem um Veículo; ou
   2. permitir um relé em um terminal ou cabeçalho.
3. Verifique que a matriz de viagem vazia está modelando tempos dependentes do tráfego.
4. Verifique se a matriz de viagem Motorista reflete o modo de transferência real, como caminhada, táxi ou transporte.
5. Corrija qualquer Conexão perdido antes de continuar.

Para o caso de referência, pergunte-se:

1. Estou modelando aqui um ônibus saindo do lote Garagem ou apenas um Motorista indo para um cabeçalho?
2. Será que o tempo que eu configurei corresponde ao tráfego real ou ao modo de viagem do Motorista?
3. O motor usaria esta informação corretamente ao construir o Escala e o Turnos?

Quando você terminar este Seção, você deve estar claro qual parte do seu Configuração pertence à logística Veículo e qual parte pertence à logística do Motorista.

## Verificando que a matriz está pronta para Programação

O objetivo final deste início rápido não é apenas preencher uma tabela, mas preparar uma base logística que Programação pode consumir. O documento explica que uma modelagem precisa dessas matrizes melhora três coisas:

1. o **transparência dos custos**,
2. o **Criação realista de Turnos**,
3. e o **Precisão de otimização**.

Antes de terminar, certifique-se de que:

1. A matriz correta existe.
2. Está associado ao dia certo.
3. O mínimo Conexãos no caso já está carregado.
4. Você separou corretamente a viagem vazia e a viagem Motorista.

Para validar que a matriz já está pronta para o próximo passo:

1. Vejam o caso de referência que estão a construir.
2. Confirma que o GoalBus já sabe:
   1. de onde o Veículo sai fisicamente,
   2. onde entra no Linha,
   3. Como é que volta quando é devido,
   4. e como um Motorista se moveria para um relé se aplicado.
3. Pergunte-se se o sistema já poderia minimizar tempos não produtivos e Distâncias nesse caso.
4. Se a resposta for sim, continue com o próximo início rápido.
5. Se a resposta for não, volte atrás e adicione ou corrija Conexãos antes de continuar.

Quando você terminar este Seção, você deve ser capaz de afirmar que sua base logística é realista o suficiente para sustentar tempos, serviços e Programação.

## Lecturas adicionais

- [Definir os tipos Veículo e Frota permitidos por Linha](P4_Definir_Os_Tipos_Veículo_E_Frota_Permitidos_Por_Linha.md)
