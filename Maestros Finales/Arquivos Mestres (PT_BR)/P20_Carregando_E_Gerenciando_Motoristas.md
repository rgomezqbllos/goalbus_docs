---
title: Carregando e gerenciando Motoristas
shortTitle: Motoristas
intro: Saiba como criar, importar e manter a base Motorista no GoalBus, rever seu
  perfil operacional e deixar um modelo confiável antes de se mover para o destacamento,
  regras e cálculo do Alocação.
contentType: how-tos
versions:
- '*'
---
## Criação ou importação de modelo Motorista

Antes de falar sobre regras Alocação, Ausências ou Turno atribuição, você precisa ter uma base Motorista confiável. Em GoalBus, Gestão de motoristas atua como a principal fonte de verdade para a operatividade humana: permite combinar criação manual e carregamento em massa, e concentra identidade, afiliação de depósito e disponibilidade no mesmo diretório. fileciteturn38file2L1-L24

Use este início rápido quando estiver claro sobre a transição de Programação para Alocação e precisa preparar o verdadeiro grupo de pessoas que participarão da atribuição.

Antes de começar, certifique-se de que:
1. Você já fechou a transição de Programação no P19.
2. É claro para você que coletivo de Motoristas irá participar no cálculo.
3. Você sabe se você vai descarregar alguns Motoristas manualmente ou se você precisa de uma carga enorme.
4. Você tem acesso ao ambiente com permissões para gerenciar pessoal.

Para este início rápido, use este caso de referência:

> **Vou carregar e rever o modelo Motorista que pode cobrir a solução L1 antes de entrar em destacamento, regras e disponibilidade.**

Para criar ou importar o modelo Motorista:
1. Em GoalBus, vá para o módulo **Configuração** > **Pessoal** > **Gestão de motoristas**.
ref: P20_Imagen1.png | compact
2. Verifique se o caso Motoristas já existe na lista geral.
3. Se você precisar criar poucos Motoristas, clique em **Novo Motorista**.
ref: P20_Imagen2.png | compact(2x)
4. Se você precisar carregar muitos Motoristas, faça uma importação maciça usando arquivo CSV do **Carga pessoal**.
ref: P20_Imagen3.png | compact
5. Se escolher a importação em massa, prepare o ficheiro com os dados mínimos necessários para identificar corretamente cada pessoa. A janela de importação ajudará a preparar a carga CSV.
ref: P20_Imagen4.png
6. Execute a carga e verifique o resultado.
7. Volte para a lista geral e verifique se o Motoristas aparece corretamente.
8. Se detectar duplicados ou registros incompletos, corrija-os antes de continuar.

Para o caso de referência, termine este Seção apenas quando puder dizer:
1. O L1 Motoristas já é descarregado ou importado.
2. A lista geral reflecte um único modelo de referência.
3. Agora você pode abrir o perfil de cada Motorista para rever seu contexto operacional.

Quando você terminar este Seção, você deve ter um modelo Motorista carregado e visível no sistema. fileciteturn38file0L1-L7 fileciteturn38file2L1-L24

## Verificação do Perfil do motorista e dados estruturais

Uma vez que o modelo é criado, você precisa rever o **Perfil do motorista**. O perfil não é apenas uma folha de contato: é o arquivo digital completo do empregado dentro da operação. Ali eles coexistem dados estáticos, contexto operacional e atributos que o sistema usará mais tarde para raciocinar sobre sua elegibilidade. fileciteturn38file0L8-L20 fileciteturn38file2L25-L40

Antes de iniciar este Seção, certifique-se de que:
1. Você já tem Motoristas visível na lista geral.
2. Você sabe qual Motorista ou grupo você vai usar como uma amostra.
3. Você quer validar que o registro não é apenas administrativo, mas operacional.

Para verificar o Perfil do motorista:
1. Na lista geral, clique no nome de um Motorista.
ref: P20_Imagen5.png | full
2. Verifique a barra lateral de dados estáticos.
3. Verifique pelo menos estes grupos de informação:
   1. dados de base, tais como nome e código,
   2. dados operacionais, tais como a convenção colectiva ou o tipo de contrato,
   3. ligações operacionais, tais como armazém principal, Grupo de trabalho, área ou tipos de Aprovado Veículos.
4. Se faltar algum dado estrutural chave, preencha-o antes de prosseguir.
5. Guarde qualquer mudança necessária.
6. Repita a revisão sobre vários Motoristas para confirmar a consistência no modelo.

Para o caso de referência, verifique pelo menos:
1. O código do Motorista.
2. O seu armazém principal.
3. A sua força Tarefa.
4. As propriedades operacionais que irão condicionar a sua subsequente atribuição.

Quando você terminar este Seção, você deve estar claro que cada Motorista tem um arquivo de operação consistente e utilizável. fileciteturn38file0L8-L20

## Revisão do contexto operacional e dados dinâmicos Motorista

Além dos dados estruturais, o Perfil do motorista inclui dados dinâmicos que afetam diretamente como o sistema raciocina sobre a pessoa. Na guia de administração você pode rever contadores e padrões de trabalho, que fazem parte do contexto operacional usado posteriormente pela lógica de mapeamento. fileciteturn38file0L12-L17

Antes de iniciar este Seção, certifique-se de que:
1. Já verificou os dados estáticos do perfil.
2. Você sabe se sua operação usa contadores ou padrões cíclicos.
3. Você quer verificar que o Motorista não só existe, mas tem um contexto operacional interpretável.

Revisão do contexto operacional dinâmico:
1. Dentro do Perfil do motorista, abra a aba **Detalhes da administração**.
2. Verifique o **contadores** ou o KPI associado ao Motorista se eles existirem.
3. Verifique se o Motorista está ligado a qualquer **Padrão de trabalho**.
4. Se a sua operação usar padrões cíclicos, verifique também a lag ou posição do Motorista atual dentro do padrão.
5. Confirma que estes dados fazem sentido para o contexto real.
6. Se a informação dinâmica não estiver correta, ajuste-a antes de se mover para regras ou cálculo.

Para o caso de referência, pergunte-se:
1. Este Motorista tem o padrão que devia ter?
2. Seus contadores ou KPIs estão disponíveis se o processo precisar deles?
3. Poderia o sistema raciocinar corretamente sobre essa pessoa num cálculo de atribuição?

Quando você terminar este Seção, você deve ter Validado não só a identidade do Motorista, mas também o seu contexto operacional dinâmico. fileciteturn38file0L12-L17

## Validar as classificações antes de usar o Motorista no Alocação

Antes de considerar um Motorista como elegível, você precisa rever o seu **notações**. Essas classificações respondem à pergunta: "Pode esta pessoa trabalhar legalmente ou tecnicamente neste depósito, grupo ou unidade? " Eles são gerenciados em um tempo Linha com início e Data de fim, e o sistema mostra estados como ativos, futuros, expirados ou próximos de expirar para facilitar a leitura. Se uma pessoa não está habilitada para o contexto necessário, o motor gera um erro ao tentar atribui-lo. fileciteturn38file0L17-L34

Antes de iniciar este Seção, certifique-se de que:
1. Você já verificou o perfil do Motorista.
2. Você sabe que depósito, grupo ou unidade você vai precisar para o seu caso.
3. Você entende que um empoderamento não é o mesmo que uma designação temporária ou destacamento.

Para rever e validar as classificações:
1. Dentro do Perfil do motorista, abra a aba **Activação/qualificação**.
2. Verificar se existem registos para:
   1. depósitos,
   2. grupos de trabalho,
   3. Unidades de negócios.
3. Verifique o estado visual de cada classificação:
   1. ativo,
   2. futuro,
   3. próximo de expirar,
   4. Expirou.
4. Se faltar uma classificação necessária, adicione-a com as datas corretas.
5. Se uma habilitação tiver expirado e não deve ser usada, deixe-a como histórica sem tentar reescrever o passado.
6. Salve as mudanças.
7. Confirme que o Motorista já está ativado para o contexto onde você espera usá-lo.

Para o caso de referência, não continue até poder dizer:
1. O Motorista está habilitado para o depósito correto.
2. O Grupo de trabalho necessário está coberto.
3. Não há expirações que quebrem a elegibilidade atual.

Quando você terminar este Seção, você deve ter Motoristas que não só existem no modelo, mas também são elegíveis de um ponto de vista operacional e regulatório. fileciteturn38file0L17-L34

## Confirmando que o modelo já está pronto para a próxima camada de Alocação

O último passo é verificar se a base Motorista está pronta para entrar na seguinte camada: destacamento operacional, regras, Ausências e cálculo. Aqui o objetivo não é apenas ter nomes carregados, mas um modelo coerente, rastreável e utilizável pelo motor.

Antes de terminar, certifique-se de que:
1. Você já carregou ou importou o modelo.
2. Já verificou os perfis principais.
3. Você já verificou dados estruturais e dinâmicos.
4. Você já tem classificações essenciais Validado.

Para confirmar que o modelo já está pronto:
1. Volte para a lista geral de Motoristas.
2. Verifique se o coletivo necessário para o seu caso está presente.
3. Verifique se os perfis críticos não apresentam lacunas importantes em matéria de informação.
4. Certifique-se de que as pessoas que você espera usar estão habilitadas para o contexto certo.
5. Pergunte-se se o sistema já poderia usar esta base como ponto de partida para:
   1. destacamento operacional,
   2. Regras Alocação,
   3. e a disponibilidade real.
6. Se a resposta for sim, continue com o próximo início rápido.
7. Se a resposta for não, corrija a base Motorista antes de continuar.

Para o caso de referência, termine este início rápido apenas quando puder dizer:
1. O modelo L1 Motorista já está carregado.
2. Os perfis-chave já foram revistos.
3. As avaliações essenciais já estão em vigor.
4. A base está pronta para o destacamento operacional.

Quando você terminar este Seção, você deve ter um modelo Motorista suficientemente forte para continuar com a próxima camada de Alocação.

## Lecturas adicionais

- [Gestão do destacamento operacional do Motorista](P21_Gestão_Do_Destacamento_Operacional_Do_Motorista.md)
