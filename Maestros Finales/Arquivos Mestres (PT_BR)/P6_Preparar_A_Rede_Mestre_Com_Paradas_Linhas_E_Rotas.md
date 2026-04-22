---
title: Preparar a rede mestre com Paradas, Linhas e Rotas
shortTitle: Rede de mestrado
intro: Saiba como criar e validar a base de rede que irá usar o seu planejamento,
  incluindo Paradas, Linhas e Rotas, de modo que os próximos passos nos tempos, serviços
  e Programação partem de uma estrutura coerente.
contentType: how-tos
versions:
- '*'
---
## Criando ou validando o Paradas sua rede irá usar

Antes de criar Linhas ou Rotas, você precisa ter certeza de que o **Paradas** que você vai usar já existe e está correctamente definido. Em GoalBus, um Parada não é apenas um ponto geográfico. É também uma entidade com identidade operacional e várias camadas de nomes que servem diferentes públicos, como planejadores, passageiros e dispositivos internos. Além disso, o sistema permite que você desactive Paradas em vez de removê-los abruptamente, para não quebrar Rotas ativo ou Viagems.

Use este início rápido quando você já tiver fechado a base de tempo em P2 e P3, e você precisa começar a construir a rede de base na qual você irá então definir Rotas, tempos de viagem e serviços.

Antes de começar, certifique-se de que:

1. Você já configurou os tipos de feriados e dias em P2.
2. Você já tem Validado o ano de operação em P3.
3. Você tem acesso ao ambiente com permissões para consultar ou editar infraestrutura de rede.
4. Você está claro o que Linha ou corredor que você quer preparar como um primeiro caso.

Para este início rápido, use este caso de referência:

> **Vou preparar Linha L1, criar ou validar a sua base Paradas e listar a sua para trás e para frente Rotas para uso posterior no meu primeiro caso de Programação.**

Para criar ou validar o Paradas do seu caso:

1. Em GoalBus, vá para o módulo **Parada Configuração** dentro do serviço Configuração.
ref: P6_Imagen1.png
2. Descubra se a base Paradas no seu caso já existe.
3. Se um Parada já existir, abra-o e confirme que sua identidade está correta.
4. Se um Parada não existir, clique em **Novo Parada**.
5. Digite ou valide estes campos:
   1. **Código** como um Identificador único.
   2. **Denominação comercial** como um nome de passageiro visível.
   3. **Nome longo** como referência descritiva interna.
   4. **Denominação curta** se você precisar dele para visões compactas.
6. Defina a localização do Parada por coordenadas ou direcção.
7. Adicionar um **Identificação externa** se você quiser um Identificador extra.
8. Salve o Parada.
ref: P6_Imagen2.png | compact(20x)
9. Repita o processo até ter o mínimo de Paradas necessário para o seu caso.
10. Se você detectar um Parada antigo que não deve continuar a ser usado em novo planejamento, mude-o para **Inativos** em vez de apagá-lo.

Para o caso de referência, use uma lógica como esta:

1. Terminal Norte
2. Centro
3. Hospital
4. Universidade
5. Terminal Sul

Quando você terminar este Seção, você deve ter a base Paradas pronta e em um estado consistente para construir o Linha e Rotas.

## Criando ou validando o Linha como um contentor operacional

Depois de ter a base Paradas, você precisa verificar o **Linha**. Em GoalBus, um Linha é mais do que apenas um número de serviço. É um contêiner de lógica operacional. Ao configurá-lo adequadamente, você define limites físicos e logísticos do serviço, tais como o tipo de Frota permitido ou a geografia operacional de depósitos e Garagems que irá então influenciar a otimização.

Antes de iniciar este Seção, certifique-se de que:

1. Você já verificou ou criou a base Paradas no seu caso.
2. Sabes que serviço que queres representar.
3. Você está claro que o Linha é o contêiner administrativo e ainda não o caminho físico detalhado.

Para criar ou validar o seu caso Linha:

1. Em GoalBus, vá para o módulo **Rede Configuração**.
ref: P6_Imagen3.png
2. Veja se o Linha que você precisa já existe.
3. Se o Linha já existir, abra-o e verifique o seu Configuração.
4. Se não existir, crie um novo Linha clicando em **Criar Linha**.
5. Define ou valida:
   1. **Nome do Linha** para nome interno.
   2. **Denominação curta** para visões compactas.
   3. **Denominação comercial**, se aplicável.
   4. **Garagem** associado ao Linha. **EYE: a criação anterior de Garagems é necessária.**
   5. **Tipos Veículo** para associar os tipos de Veículos disponíveis para o Linha. **EYE: A pré-criação dos tipos Veículo é necessária.**
   6. **Identificação externa** para adicionar um Identificador extra.
   7. **Cor** para atribuir uma certa cor ao Linha.
6. Verifique se o Linha realmente representa o serviço certo.
7. Salve o Linha.
ref: P6_Imagen4.png | compact(8.5x)8. Confirma que la línea ya puede usarse como contenedor para crear rutas específicas.

Para o caso de referência, você pode pensar em um Linha como:

- **Avaliação do risco de crédito e do risco de crédito**
- **L1: Terminal Norte - Terminal Sul**

Quando você terminar este Seção, você deve ter um Linha claro e utilizável sobre o qual você pode definir caminhos por significado.

## Criando ou validando o Rotas de ida e volta

Com o Linha já pronto, você pode agora trabalhar com o **Rotas**. Em GoalBus, um Rota é o caminho físico real que viaja um Veículo. O mesmo Linha pode ter vários Rotas válidos, por exemplo, curtas voltas, desvios ou entradas de armazém. O sistema organiza essas variações por direção ou sentido, e protege o Rotas em uso para evitar alterações perigosas em serviços já ativos.

Antes de iniciar este Seção, certifique-se de que:

1. Você já tem o Linha criado ou Validado.
2. Você já tem a base Paradas que você vai usar na sequência.
3. Você sabe se você vai criar um único caminho pelo significado ou se seu caso já precisa de variantes.

Para criar ou validar o Rotas do seu caso:

1. Na tabela principal Linha, clique no Linha que você acabou de criar ou Validado para aceder à vista do caminho.
ref: P6_Imagen5.png
2. Use as abas ou controles de direcção para trabalhar com **Sentido 1** e **Sentido 2**.
3. Verifique se já existe um caminho adequado para o sentido que você precisa.
4. Se o Rota não existir, crie uma nova variação Rota para esse sentido.
5. Define a sequência de Paradas na ordem correta.
6. Confirma o cabeçalho inicial e o cabeçalho final.
7. Salve o Rota.
8. Repita a lógica para o sentido oposto.
9. Se encontrar um caminho marcado como **Em uso**, não tente alterar a sua geometria básica sem primeiro verificar se existe uma alternativa desbloqueada.


Para o caso de referência:
1. Define o Rota de sentido único:
   1. Terminal Norte
   2. Centro
   3. Hospital
   4. Universidade
   5. Terminal Sul
2. Define o caminho de volta:
   1. Terminal Sul
   2. Universidade
   3. Centro
   4. Terminal Norte

Quando você terminar este Seção, você deve ter um Linha com seu principal Rotas por direção, pronto para você revisar sequências, pontos relevantes e lógica operacional no próximo início rápido.

## Lecturas adicionais

- [Revisão da rede operacional: sequências, permissões Parada e pontos de relé]
