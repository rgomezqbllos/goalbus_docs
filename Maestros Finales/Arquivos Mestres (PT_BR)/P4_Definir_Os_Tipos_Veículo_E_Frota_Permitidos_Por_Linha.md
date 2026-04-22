---
title: Definir os tipos Veículo e Frota permitidos por Linha
shortTitle: Frota por Linha
intro: Saiba como configurar os tipos Veículo e as restrições Frota permitidas por
  Linha para que GoalBus bloqueie atribuições inviáveis, respeite os limites físicos
  e ambientais e prepare uma base coerente antes de definir tempos e serviços.
contentType: how-tos
versions:
- '*'
---
## Definição dos tipos Veículo permitidos para um Linha

Como um primeiro passo, você precisa deixar claro qual **Tipos Veículo** pode operar cada Linha. Em GoalBus, esta restrição não é decorativa: atua como um filtro de segurança, conformidade e viabilidade física. O objetivo é evitar que o sistema proponha um Veículo que não se encaixe em uma rua, que não cumpra com uma restrição ambiental, ou que não deve circular nesse serviço.

Use este início rápido quando você precisar fechar a base Frota que seu caso irá usar antes de definir tempos e oferta de serviço.

Antes de começar, certifique-se de que:
1. Você está claro o que Linha você vai usar como um caso de referência.
2. Você sabe, pelo menos no nível básico, que restrições físicas ou ambientais afetam que Linha.

Para este início rápido, use este caso de referência:

> **Vou definir que tipos de Veículo podem operar o L1 Linha para garantir que meu primeiro planejamento use apenas um Frota compatível com a realidade física e regulamentar do serviço.**

Para definir os tipos Veículo permitidos do seu caso:
1. No GoalBus, se algum Linha já existir, abra o **Linha** Configuração que você vai usar como referência.
2. Encontre o **Tipos de Veículos permitidos** Seção.
3. Verifique se o Linha já tem tipos atribuídos.
4. Se o Linha já tem tipos definidos, ele confirma que eles ainda estão corretos para o caso.
5. Se ainda não estiverem definidos, verifique primeiro se o **Tipo de Veículo** que você precisa já existe no Veículo Configuração geral.
6. Se digitar **Sim, existe.**, selecione-o como permitido para esse Linha.
7. Se digitar **não existe**, saia do Linha Configuração e vá para o **Veículos** Configuração geral para criar ou completar primeiro o catálogo do tipo disponível a partir do painel **Tipos Veículo**.
ref: P4_Imagen1.png | full
8. Crie o tipo de Veículo que você precisa usando uma categoria clara e compreensível para o negócio, por exemplo:
   1. Minibús
   2. Padrão eléctrico
   3. Diesel articulado
ref: P4_Imagen2.png | compact(2x5)
9. Salvar o novo tipo de Veículo.
ref: P4_Imagen3.png | compact(x9)
10. Volte para o Linha Configuração.
11. Marque os tipos específicos de Veículo que são autorizados a operar nesse Linha.
ref: P4_Imagen4.png | compact(8x)
12. Deixar sem marcar os tipos que não têm de operar esse serviço.
13. Salve o Configuração.
14. Verifique novamente o Linha (se já existir) e confirme que o filtro já representa corretamente a realidade operacional.

Para o caso de referência, pergunte-se:
1. O Linha L1 suporta um ônibus padrão, um minibus ou ambos?
2. Existe um tipo de Veículo a ser excluído por tamanho ou ambiente?
3. Se não havia o cara que você precisava, você criou antes de tentar atribui-lo ao Linha?
4. O sistema deve bloquear um mapeamento manual se você tentar usar um Veículo não autorizado?

Quando você terminar este Seção, você deve ter definido uma restrição Frota-por-Linha que já serve de base para cálculos adicionais.

## Relacionando o Linha aos armazéns autorizados ou espaços Garagem

Depois de definir qual Frota se encaixa ou não se encaixa no Linha, você precisa verificar a partir de quais bases físicas esse serviço pode sair. GoalBus permite definir **lotes ou armazéns Garagem permitidos** por Linha para forçar o sistema a iniciar o serviço a partir de locais geograficamente corretos e reduzir a quilometragem vazia.

Antes de iniciar este Seção, certifique-se de que:
1. Você já configurou os tipos Veículo permitidos do Linha.
2. Você sabe a partir de que base operacional o serviço deve realmente começar.

Para relacionar o Linha com os seus armazéns permitidos ou Garagem:
1. Dentro do mesmo Linha Configuração, localize o **Garagem permitido** ou **Depósitos admissíveis** Seção.
2. Verifique se o Linha já tem depósitos autorizados.
3. Selecione apenas os armazéns ou garagens que estão geograficamente autorizados a iniciar serviços no Linha.
4. Deixar de fora as bases que não fazem sentido operacional para aquele corretor.
5. Salve o Configuração.
6. Verifique que o Linha agora tem uma lógica coerente de saída da base mais razoável.

No caso de referência, considera que:
1. Linha L1 pode sair do Norte Garagem.
2. O principal associado Garagem é o direito.
3. Você não está permitindo um depósito distante que o força a viajar muitas milhas em um vácuo para iniciar o primeiro Viagem.

Quando você terminar este Seção, você deve ter o Linha (se ele já existe), o Frota permitido e a geografia de saída de serviço alinhada.

## Validando que o Linha já tem uma base Frota coerente

Agora que você já definiu os tipos Veículo permitidos e os armazéns autorizados ou espaços Garagem, você precisa fazer uma validação final.

Antes de continuar, certifique-se de que:
1. O Linha já tem os tipos Veículo permitidos.
2. Se o Tipo de veículo necessário não existisse, foi previamente criado no Configuração geral.
3. O Linha já tem armazéns autorizados ou Garagem.
4. O Configuração reflete a realidade do caso que você está construindo.

Para validar que a base Frota já está pronta:
1. Verifique o Linha Configuração completo novamente.
2. Confirma que os tipos Veículo selecionados representam o Frota que deve realmente operar esse serviço.
3. Confirma que os armazéns autorizados ou Garagems minimizam a quilometragem vazia.
4. Pergunte-se se o sistema, com este Configuração, já evitaria:
   1. atribuições fisicamente impossíveis,
   2. Incumprimentos ambientais,
   3. afastamentos de bases geograficamente ineficientes.
5. Se a resposta for sim, continue com o próximo início rápido.
6. Se a resposta for não, corrija o Linha ou crie o Tipo de veículo que falta antes de continuar.

Quando você terminar este Seção, você deve ser capaz de afirmar que você tem todos os tipos de Veículo e Frota necessários para o planejamento do seu Linha.

## Lecturas adicionais

- [Preparação de Garagem e armazéns](P5_Preparação_De_Lotes_E_Armazéns_Garagem_Para_A_Operação.md)
