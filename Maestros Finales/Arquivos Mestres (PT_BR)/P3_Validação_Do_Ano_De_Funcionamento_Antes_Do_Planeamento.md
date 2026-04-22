---
title: Validação do ano de funcionamento antes do planeamento
shortTitle: Ano operacional
intro: Saiba como validar o ano de operação que irá sustentar seu caso de planejamento
  para evitar lacunas, sobreposições ou cortes artificiais em dados antes de mudar
  para rede, infraestrutura e serviços.
contentType: how-tos
versions:
- '*'
---
## Criar ou validar o ano de operação que irá usar o seu planejamento

Antes de continuar com rede, horários, serviços ou regras, você precisa verificar que o período que você deseja planejar se insere no **Exercício de exploração correto**. Em GoalBus, o ano de operação existe para adaptar a lógica temporal do sistema à realidade do negócio. Isto é importante porque muitas operações não seguem o ano calendário de janeiro a dezembro. Por exemplo, uma operação escolar pode funcionar de setembro a agosto, e um contrato fiscal ou sindical pode precisar de outra classificação.

Use este início rápido quando já tiver definido a lógica dos tipos de dia e férias, quando quiser preparar o seu primeiro caso de planejamento real, ou quando precisar confirmar que o período que vai usar é suportado por uma linha de tempo válida.

Antes de começar, certifique-se de que:
1. Já revisou o papel do planejador em P1.
2. Você já definiu ou Validado os tipos de feriados e dias em P2.
3. Sabes exactamente que período queres planear.
4. Você tem acesso ao ambiente com permissões para consultar ou editar o Configuração temporário.

Para este início rápido, use este caso de referência:

> **Vou planear Janeiro de 2026 e preciso confirmar que esse período se insere no ano de funcionamento correto antes de prosseguir o meu primeiro planejamento.**

Para criar ou validar o ano de operação do seu caso:
1. Em GoalBus, vá para **Configuração**.
2. Abre o **Gestão do Tempo** Seção > **Exercícios operacionais**.
ref: P3_Imagen1.png | compact
3. Verifique os anos de funcionamento existentes e encontre qual deve cobrir o período que você deseja planejar.
4. Se não houver um ano de operação adequado, clique na opção para criar um novo clicando em **Criar o Ano Operacional**.
ref: P3_Imagen2.png | full
5. Defina um **Denominação única** e, se precisar, um **Designação das mercadorias**.
6. Ajuste o **Data de início** e o **Data de fim** para se adaptar à realidade operacional ou fiscal do seu caso.
7. Associar o **Unidades de Negócios** se houver algum.
8. Salve o ano de operação.
ref: P3_Imagen3.png | compact(x10)
9. Confirme que o período que deseja planear está totalmente coberto para esse ano.
10. Se o ano já existiu, verifique também que continua a ser o ano certo para o seu caso e que as suas datas não suscitam dúvidas.

Quando você terminar este Seção, você deve ter identificado ou criado o ano de operação que realmente suporta o seu caso de planejamento.

## Revisar a continuidade do tempo e evitar lacunas ou sobreposições

Depois de identificar o ano de operação correto, você precisa verificar que sua sequência de tempo é consistente. No GoalBus, a continuidade entre anos de operação não é opcional. O sistema é projetado para evitar que o **Lacunas** ou **sobreposições** exista entre anos, porque esses erros acabariam afetando as métricas acumuladas, os KPIs anuais e cálculos posteriores.

Antes de iniciar este Seção, certifique-se de que:
1. Já encontraste o ano de operação que deve cobrir o teu caso.
2. Conheces o Data de início e o Data de fim.
3. Você sabe se há anos anteriores ou posteriores que fazem parte da mesma sequência.

Revisar a continuidade temporal do ano de funcionamento:
1. Abra o detalhe do ano de operação que você irá usar como referência.
2. Verifique o **Data de início** e o **Data de fim**.
3. Verifique se o período que você deseja planejar está dentro desse intervalo inequívoco.
4. Revisar o ano de funcionamento anterior ou subsequente, se for caso disso, para garantir que não existe:
   1. Lacunas entre um ano e outro; ou
   2. sobreposições entre dois intervalos de tempo.
5. Se você precisar criar um novo ano no final da sequência, adicione-o apenas no final e verifique para continuar exatamente onde o anterior termina.
6. Se você notar uma inconsistência, corrigir as datas antes de continuar.
7. Confirma que o sistema permite salvar a sequência sem bloquear o salvamento devido a erros de continuidade.

Para o caso de referência, faça-se estas perguntas:
1. Janeiro de 2026 está totalmente em um ano de operação válido?
2. Será que esse ano se conecta corretamente com o ano anterior e com o ano seguinte?
3. Poderia o sistema acumular dados sem quebrar a continuidade do período?

Quando você terminar este Seção, você deve ter certeza de que não há lacunas ou sobreposições que afetam o seu caso.

## Verificação da relação entre o ano de funcionamento e a lógica do calendário

Agora que você tem Validado o ano de operação e sua continuidade, você precisa conectá-lo ao que você definiu em P2. Não é útil ter tipos bem configurados de feriado e de dia se o período em que esses dados vão viver não for bem construído.

Antes de continuar, certifique-se de que:
1. O ano de funcionamento correto já está identificado.
2. Os tipos de dias e feriados do caso já estão configurados.
3. O período que você planeia ainda está claro e limitado.

Para verificar se o ano de operação está pronto para sustentar o planejamento:
1. Revise o caso de planejamento que definiu no início deste artigo.
2. Confirma que este período vive dentro do ano de operação correto.
3. Verifica que a lógica do calendário definida em P2 também se aplica no mesmo intervalo de tempo.
4. Pergunte a si mesmo se o sistema já poderia usar simultaneamente:
   1. a categoria correcta do tipo de dia,
   2. As férias corretas; e
   3. O ano de funcionamento correto.
5. Se a resposta for sim, continue com o próximo início rápido.
6. Se a resposta for não, corrigir o ano de funcionamento ou rever a coerência com o calendário antes de continuar.

No final deste Seção, você deve ser capaz de afirmar que o seu caso tem uma base de tempo integral: calendário correto e ano de operação correto.

## Lecturas adicionais

- [Preparação da rede principal: Paradas, Linhas e Rotas](P4_Definir_Os_Tipos_Veículo_E_Frota_Permitidos_Por_Linha.md)
