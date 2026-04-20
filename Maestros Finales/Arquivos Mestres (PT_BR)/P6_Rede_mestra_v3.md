---
title: Preparando a rede mestra com paradas, linhas e rotas
shortTitle: Rede mestra
intro: "Aprenda a criar e validar a base de rede que o seu planejamento vai usar, incluindo paradas, linhas e rotas, para que os próximos passos de tempos, serviços e Scheduling partam de uma estrutura coerente."
contentType: how-tos
versions:
  - "*"
---

## Criando ou validando as paradas que a sua rede vai usar

Antes de criar linhas ou rotas, você precisa garantir que as **paradas** que vai usar já existem e estão corretamente definidas. No GoalBus, uma parada não é apenas um ponto geográfico. Ela também é uma entidade com identidade operacional e com várias camadas de nome que servem a públicos diferentes, como planejadores, passageiros e dispositivos internos. Além disso, o sistema permite desativar paradas em vez de excluí-las de forma abrupta, para não quebrar rotas ou viagens ativas.

Use este quick start quando você já tiver fechado a base temporal no P2 e no P3 e precisar começar a construir a rede base sobre a qual depois você vai definir rotas, tempos de percurso e serviços.

Antes de começar, certifique-se de que:
1. Você já configurou os tipos de dia e feriados no P2.
2. Você já validou o ano operacional no P3.
3. Você tem acesso ao ambiente com permissões para consultar ou editar infraestrutura de rede.
4. Você já sabe qual linha ou corredor quer preparar como primeiro caso.

Para este quick start, use este caso de referência:

> **Vou preparar a linha L1, criar ou validar suas paradas base e deixar prontas suas rotas de ida e volta para usá-las mais adiante no meu primeiro caso de Scheduling.**

Para criar ou validar as paradas do seu caso:
1. No GoalBus, vá ao módulo de **Configuração de Paradas** dentro da configuração de serviços.
ref: P6_Imagen1.png
2. Verifique se as paradas base do seu caso já existem.
3. Se uma parada já existir, abra-a e confirme que a identidade está correta.
4. Se uma parada não existir, clique em **Nova Parada**.
5. Insira ou valide estes campos:
   1. **Código** como identificador único.
   2. **Nome comercial** como nome visível para o passageiro.
   3. **Nome longo** como referência descritiva interna.
   4. **Nome curto**, se você precisar para visualizações compactas.
6. Defina a localização da parada por coordenadas ou endereço.
7. Adicione um **ID Externo** se quiser um identificador extra.
8. Salve a parada.
ref: P6_Imagen2.png | compact
9. Repita até ter as paradas mínimas necessárias para o seu caso.
10. Se você identificar uma parada antiga que não deveria continuar sendo usada em novo planejamento, altere para **Inativa** em vez de excluir.

Para o caso de referência, use uma lógica como:
1. Terminal Norte
2. Centro
3. Hospital
4. Universidade
5. Terminal Sul

Quando você terminar esta seção, deverá ter as paradas base prontas e em um estado coerente para construir a linha e as rotas.

## Criando ou validando a linha como contêiner operacional

Depois de ter as paradas base, você precisa revisar a **linha**. No GoalBus, uma linha é mais do que um simples número de serviço. Ela é um contêiner de lógica operacional. Ao configurá-la corretamente, você define limites físicos e logísticos do serviço, como o tipo de frota permitido ou a geografia operacional de depósitos e parkings, que depois influenciará a otimização.

Antes de começar esta seção, certifique-se de que:
1. Você já revisou ou criou as paradas base do seu caso.
2. Você sabe qual serviço quer representar.
3. Você entende que a linha é o contêiner administrativo e ainda não o trajeto físico detalhado.

Para criar ou validar a linha do seu caso:
1. No GoalBus, vá ao módulo de **Configuração da Rede**.
ref: P6_Imagen3.png
2. Verifique se a linha de que você precisa já existe.
3. Se a linha já existir, abra-a e revise a configuração.
4. Se não existir, crie uma nova linha clicando em **Criar linha**.
5. Defina ou valide:
   1. **Nome da Linha** para nome interno.
   2. **Nome curto** para visualizações compactas.
   3. **Nome comercial**, se aplicável.
   4. **Parkings** associados à linha. **Atenção: é necessária a criação prévia de Parkings.**
   5. **Tipos de veículos** para associar os tipos de veículos disponíveis para a linha. **Atenção: é necessária a criação prévia dos tipos de veículo.**
   6. **ID Externo** para adicionar um identificador extra.
   7. **Cor** para atribuir uma cor específica à linha.
6. Verifique se a linha realmente representa o serviço correto.
7. Salve a linha.
ref: P6_Imagen4.png
8. Confirme que a linha já pode ser usada como contêiner para criar rotas específicas.

Para o caso de referência, você pode pensar em uma linha como:
- **L1**
- **L1: Terminal Norte - Terminal Sul**

Quando você terminar esta seção, deverá ter uma linha clara e utilizável sobre a qual depois você poderá definir rotas por sentido.

## Criando ou validando as rotas de ida e volta

Com a linha pronta, agora sim você pode trabalhar com as **rotas**. No GoalBus, uma rota é o trajeto físico real que um veículo percorre. Uma mesma linha pode ter várias rotas válidas, por exemplo, retornos curtos, desvios ou entradas em depósito. O sistema organiza essas variações por direção/sentido e protege as rotas “em uso” para evitar mudanças perigosas em serviços já ativos.

Antes de começar esta seção, certifique-se de que:
1. Você já criou ou validou a linha.
2. Você já tem as paradas base que usará na sequência.
3. Você sabe se vai criar uma única rota por sentido ou se o seu caso já precisa de variantes.

Para criar ou validar as rotas do seu caso:
1. Na tabela principal de linhas, clique na linha que você acabou de criar ou validar para acessar a visão de rotas.
ref: P6_Imagen5.png
2. Use as abas/controles de direção para trabalhar por **Sentido 1** e **Sentido 2**.
3. Verifique se já existe uma rota adequada para o sentido de que você precisa.
4. Se a rota não existir, crie uma nova variação de rota para esse sentido.
5. Defina a sequência de paradas na ordem correta.
6. Confirme a parada de início e a parada de fim.
7. Salve a rota.
8. Repita a lógica para o sentido contrário.
9. Se você encontrar uma rota marcada como **Em uso**, não tente alterar a geometria básica sem antes verificar se existe uma alternativa desbloqueada.

Para o caso de referência:
1. Defina a rota de ida:
   1. Terminal Norte
   2. Centro
   3. Hospital
   4. Universidade
   5. Terminal Sul
2. Defina a rota de volta:
   1. Terminal Sul
   2. Universidade
   3. Centro
   4. Terminal Norte

Quando você terminar esta seção, deverá ter uma linha com suas rotas principais por sentido, pronta para que no próximo quick start você valide com mais detalhe sequências, permissões de parada e lógica operativa.

## Leituras adicionais

- [Revisando a rede operacional com sequências e pontos-chave](P7_Revisando_a_rede_operacional.md)

