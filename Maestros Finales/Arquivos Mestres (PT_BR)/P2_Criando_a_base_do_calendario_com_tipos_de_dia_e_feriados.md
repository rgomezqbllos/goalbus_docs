---
title: Criando a base do calendário com tipos de dia e feriados
shortTitle: Tipos de dia e feriados
intro: 'Aprenda a configurar os tipos de dia e os feriados para que a lógica de planejamento aplique o padrão operacional correto antes de passar para rotas, tempos de percurso e criação de serviços.'
contentType: how-tos
versions:
  - '*'
---

## Criando o tipo de dia que você vai usar para planejar

Antes de criar serviços ou executar cálculos de planejamento, você precisa definir a lógica de calendário que diz ao sistema com que tipo de dia ele está trabalhando. No GoalBus, os tipos de dia são categorias operacionais que agrupam dias como dias úteis padrão, sextas-feiras, fins de semana ou dias especiais, para que você não precise construir a lógica de planejamento data a data.

Use este quick start quando você estiver preparando o seu primeiro caso de planejamento, quando precisar criar ou validar o tipo de dia que o seu cenário vai usar, ou quando quiser garantir que a lógica de feriados está pronta antes de continuar.

Antes de começar, certifique-se de que:
1. Você tem acesso ao ambiente com permissões para ver ou editar a configuração de calendário.
2. Você já sabe qual caso de planejamento quer construir.
3. Você já sabe qual período quer preparar, por exemplo janeiro de 2026.
4. Você já revisou o seu papel de planejador e o fluxo geral no P1.

Para este quick start, use este caso de referência:

> **Estou preparando a base do calendário para um cenário de dias úteis de janeiro de 2026, incluindo o comportamento correto de feriados.**

Para criar ou validar o tipo de dia do seu caso:
1. No GoalBus, vá em **Configuração** > **Gestão de Tempo** > **Gestão de tipos de dia**.
ref: P2_Imagen1.png | compact
2. Revise os tipos de dia existentes e verifique se já existe um que represente a lógica operacional que você precisa.
3. Se já existir um tipo de dia adequado, confirme que:
   1. O nome é claro.
   2. O nome curto é claro.
   3. Ele realmente representa o padrão operacional que você precisa.
4. Se não existir um tipo de dia adequado, clique em **Criar tipo de dia**.
ref: P2_Imagen2.png | full
5. Defina o **nome** e o **nome curto** do novo tipo de dia.
ref: P2_Imagen3.png | compact
6. Selecione os dias da semana que se aplicam a esse tipo de dia.
ref: P2_Imagen4.png | compact
7. Se o tipo de dia também deve se aplicar a feriados, ative a opção para aplicar o tipo de dia a feriados.
ref: P2_Imagen5.png | compact
8. Salve o tipo de dia.
9. Revise o resultado e confirme que o tipo de dia agora representa claramente o caso que você está preparando.

Quando você terminar esta seção, deverá ter um tipo de dia que o sistema possa usar como categoria operacional para o seu caso de planejamento.

## Registrando os feriados que alteram a lógica normal do calendário

Depois de definir o tipo de dia geral, você precisa indicar ao sistema o que fazer com as datas excepcionais. Os feriados são importantes porque o calendário pode dizer que uma data é terça-feira, enquanto a operação deveria se comportar como um domingo ou como outro padrão especial. Se você não registrar corretamente os feriados, o sistema pode aplicar o plano errado quando, mais adiante, você publicar ou calcular cenários.

Antes de começar esta seção, certifique-se de que:
1. Você já criou ou confirmou o tipo de dia que o seu caso vai usar.
2. Você sabe se o período de planejamento inclui feriados ou datas especiais.
3. Você está pronto para decidir qual padrão operacional cada feriado deve seguir.

Para registrar e validar os feriados do seu caso:
1. Na mesma seção de gestão de tipos de dia, mude para a aba **Dias feriados**.
ref: P2_Imagen6.png | compact
2. Verifique se o feriado de que você precisa já existe no sistema.
3. Se o feriado não existir, crie um novo registro de feriado.
4. Se o feriado já existir, abra-o e revise a configuração.
5. Insira ou confirme o **nome** do feriado.
6. Atribua o **tipo de dia** correto a esse feriado.
ref: P2_Imagen7.png | compact
7. Salve o registro do feriado.
8. Repita este processo para qualquer outro feriado que afete o período que você está preparando.
9. Revise a lista de feriados e confirme que cada data excepcional aponta para o padrão operacional correto.

Para o caso de referência, faça estas perguntas:
1. Janeiro de 2026 inclui algum feriado que deva se comportar de forma diferente de um dia útil padrão?
2. Esse feriado deveria se comportar como domingo, como sábado ou como outro tipo de dia especial?
3. Se você publicasse um cenário para este período, o sistema saberia exatamente qual padrão aplicar nessa data?

Quando você terminar esta seção, o sistema deverá conseguir substituir o comportamento normal do calendário nas datas de feriado que importam para o seu caso.

## Verificando se a sua base de calendário está pronta para planejar

Agora que você já definiu o tipo de dia geral e as exceções por feriados, você precisa confirmar que a base de calendário realmente é utilizável. Este é o passo em que você verifica se a estrutura que criou consegue sustentar os próximos quick starts sem introduzir erros evitáveis.

Antes de continuar, certifique-se de que:
1. O tipo de dia existe e tem a lógica semanal correta.
2. Os feriados relevantes estão registrados.
3. Cada feriado está vinculado ao tipo de dia correto.
4. O seu caso de planejamento continua claro e específico.

Para validar a sua base de calendário antes de passar para o próximo quick start:
1. Revise o caso de planejamento que você definiu no início deste artigo.
2. Confirme que o tipo de dia que você criou ou validou coincide com esse caso.
3. Confirme que qualquer feriado dentro do período de planejamento foi registrado e associado ao tipo de dia correto.
4. Verifique se a opção de aplicação a feriados que você ativou no tipo de dia realmente reflete o comportamento que você quer.
5. Pergunte-se se o sistema já conseguiria distinguir:
   1. os dias normais do período, e
   2. as datas excepcionais que devem seguir outro padrão operacional.
6. Se a resposta for sim, continue com o próximo quick start.
7. Se a resposta for não, volte e corrija o tipo de dia ou a associação de feriados antes de seguir.

Ao terminar esta seção, você deverá ser capaz de afirmar que o seu caso de planejamento tem uma base de calendário confiável e que os próximos quick starts poderão se apoiar nela sem herdar um erro de lógica temporal.

## Leituras adicionais

- [Validando o ano operacional antes de planejar](P3_Validando_o_ano_operacional_antes_de_planejar.md)

