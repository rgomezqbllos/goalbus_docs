---
title: Mudança de Programação para Alocação
shortTitle: De Programação para Alocação
intro: Saiba o que deve estar pronto no Programação antes de entrar no Alocação, que
  informações herdam a tarefa da equipe e que problemas devem ser resolvidos antes
  de calcular o Motoristas real.
contentType: how-tos
versions:
- '*'
---
## Confirmando que deve ser fechado em Programação antes de se mover para Alocação

Antes de entrar em Alocação, você precisa verificar que Programação já deixou uma base suficientemente estável. Alocação não substitui Programação. Alocação parte do trabalho já construído e decide como atribui-lo a pessoas reais.

Use este início rápido quando você já tiver uma solução calculada e Validado Programação, e você precisa decidir se você pode começar a trabalhar com a equipe real.

Antes de começar, certifique-se de que:
1. Você já criou, calculou e Validado Programação Cenário.
2. Você já reviu a oferta de serviço e sua consistência global.
3. Você sabe o que Linhas, que tipo de dia e que solução você vai usar como referência.
4. Você está claro que Alocação não é o lugar para consertar uma base estrutural ruim para Programação.

Para este início rápido, use este caso de referência:

> **Vou confirmar que a solução Programação da Validado para a L1 Linha está madura o suficiente para mover para Alocação e começar a atribuir trabalho para Motoristas real.**

Para confirmar que o Programação está pronto:
1. Abra o Programação Cenário que irá usar como referência.
2. Verifique que sua condição já está correta para Parada tratá-lo como um trabalho Rascunho.
3. Verifique se a oferta utilizada ainda é a certa.
4. Verifique se a lógica de Veículos e a lógica de Turnos já foram aplicadas.
5. Confirma que não existem inconsistências estruturais óbvias na solução.
6. Se você ainda precisar reformular a base Veículo, horários, serviços ou regras, volte para Programação antes de seguir.
7. Se a solução já estiver estável, continue para o próximo passo.

Para o caso de referência, não continue até poder dizer:
1. A solução L1 já foi calculada.
2. Foi verificado.
3. Você já não precisa de correções estruturais de Programação.
4. Pode agora ser tratada como uma base de trabalho para o pessoal.

Quando você terminar este Seção, você deve estar claro se Programação já entregou uma base utilizável para Alocação.

## Entender o que Alocação herda de Programação

Uma vez que a base é confirmada, você precisa entender o que a informação acontece de Programação para Alocação. Aqui a chave é não pensar que Alocação começa do zero. Alocação herda o trabalho já estruturado e a partir de lá decide qual pessoa real pode assumir.

Antes de iniciar este Seção, certifique-se de que:
1. Você já identificou a solução Programação que você vai usar.
2. Sabes que parte dessa solução deve permanecer estável.
3. Você entende que a Alocação trabalha em trabalhos já construídos, não em uma oferta não estruturada.

Para entender o que o Alocação herda:
1. Verifique a solução Validado Programação.
2. Identifique o Tarefas, blocos ou estruturas de trabalho que servirão de base.
3. Verifique se a solução já tem uma forma operacionalmente reconhecível.
4. Tenha em mente que, ao se mover para Alocação, o sistema não está mais criando trabalho abstrato, mas tentando atribuir esse trabalho a pessoas reais.
5. Use esta regra de leitura:
   1. Programação define **o que o trabalho existe**.
   2. Alocação define **Quem vai fazer esse trabalho?**.

Para o caso de referência, pergunte-se:
1. A solução L1 já tem um trabalho claro suficiente para a atribuir?
2. Os blocos de trabalho são reconhecíveis e utilizáveis?
3. O problema que ainda está por resolver é de pessoas e não de estrutura?

Quando você terminar este Seção, você deve entender o que Alocação herda e o que não deve ser redefinido lá novamente.

## Distinguindo quais são os problemas resolvidos no Programação e quais no Alocação

Antes de finalmente passar para a camada de pessoal, você precisa separar muito bem as responsabilidades. Esta distinção é fundamental porque muitos erros aparecem quando você tenta corrigir no Alocação algo que deveria ter sido resolvido anteriormente no Programação.

Antes de continuar, certifique-se de que:
1. Você sabe que estágio Programação será na base.
2. Você entende que Alocação consome uma solução anterior.
3. Está preparado para distinguir problemas estruturais dos problemas de pessoal.

Para separar adequadamente ambos os domínios:
1. Trata como um problema **Programação** qualquer matéria relacionada com:
   1. estrutura do serviço,
   2. Lógica Frota,
   3. vezes,
   4. Regras Veículo,
   5. tipos de Turnos e sua construção de base.
2. Trata como um problema **Alocação** qualquer matéria relacionada com:
   1. Disponibilidade efectiva do Motorista,
   2. destacamento no depósito ou grupo,
   3. Ausências,
   4. inatividade,
   5. transferências ou transferências,
   6. Elegibilidade real para receber um Turno.
3. Se você detectar uma inconsistência de trabalho que afeta toda a estrutura, volte para Programação.
4. Se detectar a incoerência de uma pessoa, resolva-a em Alocação.

Para o caso de referência, utilize esta lógica:
1. Se o problema é que o trabalho de L1 foi mal construído, volte para Programação.
2. Se o problema é que você não sabe que Motorista real pode aceitar esse trabalho, você está entrando no Alocação corretamente.

Quando você terminar este Seção, você deve ser capaz de explicar claramente o que deve ser corrigido antes de passar para a equipe e o que pertence ao próximo módulo.

## Confirmando o que deve estar pronto do lado da equipe antes de calcular Alocação

Agora que você sabe o que Alocação recebe, você precisa verificar o que deve existir no lado da equipe para que o cálculo seguinte faça sentido. Não é suficiente para ter um bom Escala se você ainda não tiver uma base mínima de pessoas, destacamentos e disponibilidade.

Antes de iniciar este Seção, certifique-se de que:
1. Você já tem uma base válida do Programação.
2. Você sabe que grupos, depósitos ou contextos operacionais afetam as pessoas.
3. Estão prontos para verificar a camada de pessoal.

Para confirmar que a base de pessoal está pronta:
1. Verifica que já existe um grupo de pessoal que pode receber o trabalho.
2. Verifique se as pessoas estão ligadas ao contexto correto quando se aplicam.
3. Verifique que você não está inserindo Alocação sem informações mínimas de disponibilidade.
4. Verificar se a estrutura necessária já existe para:
   1. Regras Alocação,
   2. Ausências,
   3. inatividade,
   4. Transferências ou transferências, se for caso disso.
5. Se ainda não tiver esta base, não lance o cálculo da equipe.
6. Se a base já existe ou pelo menos está na pista, continue com o seguinte rápido começa a partir de Alocação.

Para o caso de referência, pergunte-se:
1. O pessoal já existe quem será capaz de receber a solução L1?
2. Esse bastão pertence ao reino certo?
3. A base de disponibilidade e de destacamento já está minimamente preparada?

Quando você terminar este Seção, você deve estar claro se o lado da equipe já está pronto para entrar em Alocação.

## Verificar o ponto de transição entre Programação e Alocação

O último passo é fechar mentalmente a transição. Este início rápido ainda não pretende calcular a tarefa da equipe. Tem por objetivo deixar muito claro quando o Programação termina e quando o Alocação começa para que você não misture ambos os domínios.

Antes de terminar, certifique-se de que:
1. Você já verificou a solução do Programação.
2. Você entende o que Alocação herda.
3. Já separaram problemas estruturais de problemas de pessoal.
4. Você já verificou para ver se há uma base mínima de pessoal.

Para fechar corretamente a transição:
1. Trata a solução Validado Programação como uma entrada formal Alocação.
2. Não continue a alterar essa base a menos que detecte um problema estrutural real.
3. Use os seguintes iniciais rápidos para se preparar:
   1. Regras Alocação,
   2. Ausências e inatividades,
   3. transferências, atribuições e alterações de destacamento.
4. Considera que o objetivo muda daqui:
   1. Já não se trata do trabalho de construção.
   2. Agora trata-se de a atribuir a pessoas reais.
5. Se você pode afirmar isso claramente, a transição está bem feita.

Para o caso de referência, termine este início rápido apenas quando puder dizer:
1. Programação já deixou uma solução L1 estável.
2. O próximo problema não é mais estrutural, mas a atribuição de pessoal.
3. Agora você pode digitar a camada de regra Alocação.

Quando você terminar este Seção, você deve ter uma transição clara e controlada entre Programação e Alocação.

## Lecturas adicionais

- [Definição de regras Alocação para a designação de pessoal](P20_Carregando_E_Gerenciando_Motoristas.md)
