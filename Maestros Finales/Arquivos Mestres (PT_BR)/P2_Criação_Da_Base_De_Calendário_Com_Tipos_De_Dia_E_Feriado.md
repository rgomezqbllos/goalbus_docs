---
title: Criação da base de calendário com tipos de dia e feriado
shortTitle: Tipos de dias e feriados
intro: Saiba como configurar os tipos de dia e feriados para que a lógica de planejamento
  aplique o padrão de operação correto antes de passar para Rotas, tempos de viagem
  e criação de serviços.
contentType: how-tos
versions:
- '*'
---
## Criando o tipo de dia que você vai usar para planejar

Antes de criar serviços ou lançar cálculos de planejamento, você precisa definir a lógica do calendário que diz ao sistema que tipo de dia você está trabalhando com. Na GoalBus, os tipos de dia são as categorias operacionais que agrupam dias como trabalhos padrão, sextas-feiras, fins de semana ou dias especiais, para que você não tenha que construir a data lógica de planejamento por data.

Use este início rápido quando você estiver preparando seu primeiro caso de planejamento, quando você precisa criar ou validar o tipo de dia que seu estágio vai usar, ou quando você quer ter certeza de que a lógica de férias está pronta antes de continuar.

Antes de começar, certifique-se de que:
1. Você tem acesso ao ambiente com permissões para ver ou editar o calendário Configuração.
2. Sabes qual é o caso de planeamento que queres construir.
3. Você sabe que período você quer preparar, por exemplo, Janeiro de 2026.
4. Você já revisou seu papel de planejamento e o fluxo global em P1.

Para este início rápido, use este caso de referência:

> **Estou preparando a base do calendário para um trabalho Cenário de janeiro de 2026, incluindo o comportamento correto dos feriados.**

Para criar ou validar o tipo de dia do seu caso:
1. Em GoalBus, vá para **Configuração** > **Gestão do Tempo** > **Gestão dos tipos de dia**.
ref: P2_Imagen1.png | compact
2. Verifique os tipos de dia existentes e veja se já existe um que represente a lógica operacional que você precisa.
3. Se já existir um tipo adequado de dia, confirma que:
   1. O nome dele está limpo.
   2. O nome curto dele é claro.
   3. Ele realmente representa o padrão de operação que você precisa.
4. Se não existir um tipo de dia adequado, clique em **Criar o Tipo de Dia**.
ref: P2_Imagen2.png | compact(2x)
5. Defina os **nome** e **Nome curto** para o novo tipo de dia.
ref: P2_Imagen3.png | compact(8.5x)
6. Selecione os dias da semana que se aplicam a esse tipo de dia.
ref: P2_Imagen4.png | compact(8.5x8)
7. Se o tipo de dia também se aplicar aos feriados, ativar a opção de aplicar o tipo de dia aos feriados.
ref: P2_Imagen5.png | compact(8.5x8)
8. Salve o gajo do dia.
9. Verifique o resultado e confirme que o tipo de dia agora representa claramente o caso que você está preparando.

Quando você terminar este Seção, você deve ter um tipo de dia que o sistema pode usar como uma categoria operacional para o seu caso de planejamento.

## Gravar feriados que alteram a lógica normal do calendário

Depois de definir o tipo de dia geral, você precisa dizer ao sistema o que fazer com as datas excepcionais. Férias são importantes porque o calendário pode dizer que uma data é terça-feira, enquanto a operação deve comportar-se como um domingo ou como outro padrão especial. Se você não registrar bem as férias, o sistema pode aplicar o plano errado quando você mais tarde publicar ou calcular Cenários.

Antes de iniciar este Seção, certifique-se de que:
1. Você criou ou confirmou o tipo de dia que o seu caso vai usar.
2. Você sabe se o período de planejamento inclui feriados ou datas especiais.
3. Você está pronto para decidir qual o padrão de operação que cada feriado deve seguir.

Para registrar e validar os feriados do seu caso:
1. No mesmo dia de gestão do tipo Seção, mude para a guia **Férias**.
ref: P2_Imagen6.png | compact
2. Verifique se o feriado que você precisa já existe no sistema.
3. Se as férias não existirem, crie um novo recorde de férias.
4. Se o feriado já existir, abra-o e verifique o seu Configuração.
5. Insira ou confirme o **nome** do feriado.
6. Atribua o **tipo de dia** correto para esse feriado.
ref: P2_Imagen7.png | compact
7. Mantenha o registo do feriado.
8. Repita este processo para qualquer outro feriado que afecte o período que você está preparando.
9. Verifique a lista de feriados e confirme que cada data excepcional aponta para o padrão de operação correto.

Para o caso de referência, faça-se estas perguntas:
1. Será que Janeiro de 2026 inclui um feriado que deve comportar-se diferente de um normal utilizável?
2. Deveria esse feriado comportar-se como domingo, como sábado, ou como outro tipo de dia especial?
3. Se você Publicado um Cenário para este período, o sistema saberia exatamente que padrão aplicar nessa data?

Quando você terminar este Seção, o sistema deve ser capaz de substituir o comportamento normal do calendário nas datas de feriado que importam para você.

## Verificando que a sua base de calendário está pronta para planejar

Agora que você já definiu o tipo de dia geral e exceções de feriado, você precisa confirmar que a base do calendário é realmente utilizável. Este é o passo em que você verifica que a estrutura que você criou pode segurar os seguintes inícios rápidos sem introduzir erros evitáveis.

Antes de continuar, certifique-se de que:
1. O tipo de dia existe e tem a lógica semanal correta.
2. Os feriados relevantes estão registados.
3. Cada feriado está ligado ao tipo de dia certo.
4. O seu caso de planeamento permanece claro e concreto.

Para validar a sua base de calendário antes de passar para o próximo início rápido:
1. Revise o caso de planejamento que definiu no início deste artigo.
2. Confirme que o tipo de dia que criou ou o Validado corresponde a esse caso.
3. Confirme que qualquer feriado dentro do período de planejamento foi registado e associado com o tipo de dia correto.
4. Verifique se a opção de aplicativo de férias que ativou no tipo de dia realmente reflete o comportamento que deseja.
5. Pergunte-se se o sistema já poderia distinguir:
   1. dias normais do período; e
   2. as datas excepcionais a seguir por outro padrão operacional.
6. Se a resposta for sim, continue com o próximo início rápido.
7. Se a resposta for não, volte atrás e corrija o tipo de dia ou a associação de férias antes de continuar.

No final deste Seção, você deve ser capaz de afirmar que seu caso de planejamento tem uma base de calendário confiável e que os seguintes inícios rápidos podem confiar nele sem herdar um erro lógico temporário.

## Lecturas adicionais

- [Validação do ano de funcionamento antes do planeamento](P3_Validação_Do_Ano_De_Funcionamento_Antes_Do_Planeamento.md)
