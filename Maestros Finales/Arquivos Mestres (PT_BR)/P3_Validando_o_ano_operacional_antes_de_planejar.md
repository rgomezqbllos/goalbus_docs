---
title: Validando o ano operacional antes de planejar
shortTitle: Ano operacional
intro: 'Aprenda a validar o ano operacional que sustentará o seu caso de planejamento para evitar lacunas, sobreposições ou cortes artificiais nos dados antes de passar para rede, infraestrutura e serviços.'
contentType: how-tos
versions:
  - '*'
---

## Criando ou validando o ano operacional que o seu planejamento vai usar

Antes de seguir com rede, tempos, serviços ou regras, você precisa verificar se o período que quer planejar está dentro do **ano operacional correto**. No GoalBus, o ano operacional existe para adaptar a lógica temporal do sistema à realidade do negócio. Isso é importante porque muitas operações não seguem o ano natural de janeiro a dezembro. Por exemplo, uma operação escolar pode trabalhar de setembro a agosto, e um contrato fiscal ou sindical pode exigir outro intervalo.

Use este quick start quando você já tiver definido a lógica de tipos de dia e feriados, quando quiser preparar o seu primeiro caso real de planejamento, ou quando precisar confirmar que o período que você vai usar é suportado por uma linha do tempo válida.

Antes de começar, certifique-se de que:
1. Você já revisou o papel do planejador no P1.
2. Você já configurou ou validou os tipos de dia e feriados no P2.
3. Você sabe exatamente qual período quer planejar.
4. Você tem acesso ao ambiente com permissões para consultar ou editar a configuração temporal.

Para este quick start, use este caso de referência:

> **Vou planejar janeiro de 2026 e preciso confirmar que esse período está dentro do ano operacional correto antes de seguir com o meu primeiro planejamento.**

Para criar ou validar o ano operacional do seu caso:
1. No GoalBus, vá em **Configuração**.
2. Abra **Gestão de Tempo** > **Anos operacionais**.
ref: P3_Imagen1.png | compact
3. Revise os anos operacionais existentes e identifique qual deve cobrir o período que você quer planejar.
4. Se não existir um ano operacional adequado, clique na opção de criar um novo selecionando **Criar Ano Operacional**.
ref: P3_Imagen2.png | full
5. Defina um **Nome Único** e, se necessário, uma **Descrição**.
6. Ajuste a **Data de início** e a **Data de fim** para que se adaptem à realidade operacional ou fiscal do seu caso.
7. Associe as **Unidades de Negócio**, se houver.
8. Salve o ano operacional.
ref: P3_Imagen3.png | compact
9. Confirme que o período que você quer planejar fica completamente coberto por esse ano.
10. Se o ano já existia, ainda assim verifique se ele continua sendo o correto para o seu caso e se as datas não geram dúvidas.

Quando você terminar esta seção, deverá ter identificado ou criado o ano operacional que realmente sustenta o seu caso de planejamento.

## Revisando a continuidade temporal e evitando lacunas ou sobreposições

Depois de identificar o ano operacional correto, você precisa verificar se a sequência temporal é coerente. No GoalBus, a continuidade entre anos operacionais não é opcional. O sistema é projetado para evitar **lacunas** ou **sobreposições** entre anos, porque esses erros acabam afetando métricas acumuladas, KPIs anuais e cálculos posteriores.

Antes de começar esta seção, certifique-se de que:
1. Você já encontrou o ano operacional que deve cobrir o seu caso.
2. Você já conhece a data de início e a data de fim.
3. Você sabe se há anos anteriores ou posteriores que fazem parte da mesma sequência.

Para revisar a continuidade temporal do ano operacional:
1. Abra o detalhe do ano operacional que você usará como referência.
2. Revise a **Data de início** e a **Data de fim**.
3. Verifique se o período que você quer planejar está dentro desse intervalo sem ambiguidade.
4. Revise o ano operacional anterior ou posterior, se existir, para garantir que não há:
   1. lacunas entre um ano e outro, ou
   2. sobreposições entre dois intervalos temporais.
5. Se você precisar criar um novo ano no final da sequência, adicione-o apenas no final e verifique se ele continua exatamente de onde o anterior termina.
6. Se você detectar uma inconsistência, corrija as datas antes de continuar.
7. Confirme que o sistema permite salvar a sequência sem bloquear por erros de continuidade.

Para o caso de referência, faça estas perguntas:
1. Janeiro de 2026 está completamente dentro de um ano operacional válido?
2. Esse ano se conecta corretamente com o anterior e o seguinte?
3. O sistema conseguiria acumular dados sem quebrar a continuidade do período?

Quando você terminar esta seção, deverá ter segurança de que não existem lacunas nem sobreposições que afetem o seu caso.

## Verificando a relação entre o ano operacional e a lógica de calendário

Agora que você validou o ano operacional e a continuidade, você precisa conectá-lo ao que definiu no P2. Não adianta ter tipos de dia e feriados bem configurados se o marco temporal em que esses dados existirão não está bem construído.

Antes de continuar, certifique-se de que:
1. O ano operacional correto já está identificado.
2. Os tipos de dia e feriados do caso já estão configurados.
3. O período que você vai planejar continua claro e delimitado.

Para verificar que o ano operacional já está pronto para sustentar o planejamento:
1. Revise o caso de planejamento que você definiu no início deste artigo.
2. Confirme que esse período está dentro do ano operacional correto.
3. Verifique que a lógica de calendário definida no P2 também se aplica dentro desse mesmo marco temporal.
4. Pergunte-se se o sistema já poderia usar simultaneamente:
   1. a categoria correta de tipo de dia,
   2. os feriados corretos, e
   3. o ano operacional correto.
5. Se a resposta for sim, continue com o próximo quick start.
6. Se a resposta for não, corrija o ano operacional ou revise a coerência com o calendário antes de seguir.

Ao terminar esta seção, você deverá ser capaz de afirmar que o seu caso tem uma base temporal completa: calendário correto e ano operacional correto.

## Leituras adicionais

- [Definindo tipos de veículo e frota permitida por linha](P4_Definindo_tipos_de_veiculo_e_frota_permitida_por_linha.md)

