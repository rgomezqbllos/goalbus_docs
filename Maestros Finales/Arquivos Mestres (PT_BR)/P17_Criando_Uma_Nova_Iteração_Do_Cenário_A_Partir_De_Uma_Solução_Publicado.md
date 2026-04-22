---
title: Criando uma nova iteração do Cenário a partir de uma solução Publicado
shortTitle: Nova Iteração
intro: Saiba como criar uma nova iteração de um Publicado Cenário já para testar melhorias,
  ajustar parâmetros ou introduzir alterações sem alterar o Versão que já está em
  operação.
contentType: how-tos
versions:
- '*'
---
## Baseado em uma solução Publicado sem alterar a atual Versão

Depois de uma solução Publicando, é normal que você precise continuar trabalhando nela. Você pode querer ajustar as regras, tentar outra lógica de viragem, incorporar alterações de oferta, ou preparar uma melhoria para um período futuro. Nesse caso, você não deve modificar diretamente o Publicado Versão já. A coisa correta é criar um **nova iteração** do Cenário para manter a rastreabilidade e proteger o Versão que já está no lugar.

Use este início rápido quando você já tiver um estágio com uma solução no status **Publicado** e precisa gerar uma nova variante sem perder a referência histórica da solução implantada.

Antes de começar, certifique-se de que:
1. Você já colocou o Cenário anterior no P16.
2. A solução Cenário que você tomará como sua base está em estado **Publicado**.
3. Sabes como é que queres parecer ou melhorar a próxima iteração.
4. É claro que a nova iteração não deve substituir automaticamente o atual Versão até que passe por cálculo, validação e publicação novamente.

Para este início rápido, use este caso de referência:

> **Vou criar uma nova iteração do Publicado L1 Cenário para testar melhorias na solução sem tocar o Versão que já está em operação.**

Para uma solução Publicado segura:
1. Em GoalBus, abra o módulo **Planejamento Cenários**.
2. Localiza o Cenário cuja solução está em estado **Publicado**.
3. Verifique seu nome, descrição, tipo de dia e associado Linhas.
4. Confirme que é realmente o Versão que deseja usar como referência.
5. Evite editar o Versão diretamente como se fosse um novo Rascunho.
6. Decida que mudança você quer fazer na nova iteração:
   1. regras,
   2. parâmetros,
   3. Oferta,
   4. ou ajustamentos estruturais permitidos.

Quando você terminar este Seção, você deve ter identificado claramente o Publicado Cenário que servirá de base para sua nova iteração.

## Criando a nova iteração a partir do Publicado Cenário

Uma vez que a base é identificada, o próximo passo é criar um **nova iteração**. O objetivo é preservar o Publicado Versão como referência histórica e abrir um novo ramo de trabalho controlado na mesma lógica operacional.

Antes de iniciar este Seção, certifique-se de que:
1. Você já identificou a solução Publicado correta.
2. Sabes porque precisas de uma nova iteração.
3. Você está claro que a nova iteração deve ser claramente diferenciada do Versão anterior.

Para criar a nova iteração:
1. A partir da tabela Cenário, abra o menu de ação do Publicado Cenário.
2. Selecione a opção para **criar uma nova iteração** clicando no **duplicado** o Cenário como base de trabalho.
ref: P17_Imagen1.png | compact
3. Digite um **novo nome** para a iteração.
4. Se aplicável, atualize o **Descrição** para refletir o alvo de alteração.
5. Salve a nova iteração.
ref: P17_Imagen2.png | compact
6. Verifica que o novo Cenário aparece como uma entidade separada do Publicado Cenário.
ref: P17_Imagen3.png | full
7. Verifique se o Publicado Versão original permanece intacto e diferenciado do novo.

Para o caso de referência, uma opção válida pode ser:
- **Cálculo clássico - L1 utilizável - Iteração 2**
- **L1 utilizável - melhoria das regras Turno**

Quando você terminar este Seção, você deve ter uma nova iteração criada sem perder a rastreabilidade do Publicado Versão.

## Definir quais as alterações que pertencem à nova iteração

Depois de criar a iteração, você precisa decidir o que você realmente vai mudar. Nem todas as iterações perseguem o mesmo objetivo. Alguns servem para ajustar regras, outros para melhorar a eficiência, outros para refletir uma nova oferta ou futura variação operacional.

Antes de iniciar este Seção, certifique-se de que:
1. Criaste a nova iteração.
2. Você sabe que aspecto da solução acima você quer rever.
3. Você está disposto a limitar o switch para um alvo específico para que você não misture muitas variáveis.

Definir o âmbito da iteração:
1. Abra o novo palco.
2. Verifique quais itens você quer manter exatamente o mesmo que no Publicado Versão.
3. Decidir qual item você vai mudar primeiro:
   1. **Regras Veículo**,
   2. **Regras de Turno**,
   3. **parâmetros do motor**,
   4. **oferta de serviços**,
   5. **Matrizes logísticas**.
4. Evite mudar muitas coisas ao mesmo tempo na primeira iteração, a menos que estritamente necessário.
5. Documentar no nome ou na descrição a finalidade da iteração.
6. Guarde as alterações descritivas antes de ir para o cálculo.

Para o caso de referência, use uma lógica como esta:
1. Mantenha a mesma oferta L1 funcional.
2. Ajuste apenas o modelo de regras Turno.
3. Recalcule para comparar a nova solução com a solução Publicado.

Quando você terminar este Seção, você deve ter uma nova iteração com um alvo claro, estreitado.

## Recalcular a iteração e compará-la com o Versão anterior

Uma vez definido o escopo, você precisa recalcular a iteração. Aqui a vantagem é que você já não sai do zero: partes de uma solução conhecida e você pode comparar melhor o impacto da mudança.

Antes de iniciar este Seção, certifique-se de que:
1. Criaste a nova iteração.
2. Você já definiu o objetivo da mudança.
3. Você já verificou quais regras, parâmetros ou entradas você vai modificar.

Para recalcular a nova iteração:
1. Revise o iterado Cenário e confirme que suas entradas permanecem consistentes.
2. Ajuste o item que deseja modificar.
3. Salve o Configuração.
4. Execute o cálculo do novo Cenário.
5. Espere até que o Cenário complete a fase de cálculo.
6. Verifique se a iteração passa para **Solução preparada** ou **Edição**.
7. Compare o resultado com o Versão anterior usando:
   1. KPI,
   2. estrutura geral,
   3. Lógica Tarefa,
   4. e a coerência operacional.
8. Se a mudança melhorar o resultado, continue com a revisão formal.
9. Se a alteração agravar o resultado, mantenha o Publicado Versão como referência e decida se deseja corrigir ou descartar esta iteração.

Para o caso de referência, comparar:
1. A solução Publicado L1.
2. A nova iteração com ajuste de regras.
3. O que mudou na qualidade, viabilidade ou equilíbrio.

Quando você terminar este Seção, você deve ter uma nova solução calculada e uma base clara para compará-lo com o já Publicado Versão.

## Decidir se a nova iteração substituirá o atual Versão

O último passo é decidir se esta iteração merece ser a nova operacional Versão. Uma nova iteração não substitui automaticamente a publicação anterior. Para chegar à produção, você deve voltar através da revisão, validação e publicação com sua própria vida Ciclo.

Antes de terminar, certifique-se de que:
1. Já calculaste a nova iteração.
2. Você já comparou o resultado com a solução Publicado.
3. Você sabe se a mudança traz uma real melhoria ou apenas uma variante sem valor operacional.

Para encerrar a decisão sobre a iteração:
1. Revisar a nova solução do ponto de vista técnico e operacional.
2. Se a iteração melhorar claramente a solução atual, prepare-a para:
   1. validação,
   2. e subsequente publicação.
3. Se a iteração não melhorar o resultado, ele mantém o atual Publicado Versão como referência atual.
4. Não exclua a publicação anterior apenas porque há uma nova iteração.
5. Mantenha tanto Versãos bem identificado para auditoria e comparação histórica.
6. Se você decidir seguir em frente, trate a iteração como um novo Cenário que deve viajar seu próprio fluxo até atingir **Publicado**.

Para o caso de referência, termine este início rápido apenas quando você puder afirmar uma destas duas coisas:
1. A nova iteração L1 melhora o Publicado Versão e merece continuar o seu Ciclo.
2. O atual Publicado Versão permanece melhor e a iteração permanecerá apenas como um teste ou referência.

Quando você terminar este Seção, você deve ter uma nova iteração calculada, comparada e pronta para se tornar um novo Versão ou para ser mantida como uma variante de análise.

## Lecturas adicionais

- [Executar e validar o primeiro cálculo do Programação](P15_Executar_E_Validar_O_Primeiro_Cálculo_Do_Programação.md)
