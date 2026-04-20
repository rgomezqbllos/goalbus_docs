---
title: Executando o primeiro cálculo de Rostering
shortTitle: Calcular Rostering
intro: 'Aprenda a preparar e executar o primeiro cálculo de Rostering, revisar se a solução de pessoal é viável e detectar se os problemas pertencem a regras, disponibilidade ou adscrição antes de validar.'
contentType: how-tos
versions:
  - '*'
---

## Preparando a base antes de executar o cálculo de Rostering

Antes de executar o cálculo, você precisa verificar que a base de pessoal está suficientemente madura. O Rostering não deve ser usado para descobrir dados mestres faltando de última hora. Se a base, a adscrição, as regras ou a disponibilidade não estiverem bem preparadas, o cálculo falhará ou produzirá uma solução enganosa.

Use este quick start quando você já tiver uma solução de Scheduling estável e tiver preparado toda a camada de pessoal necessária para atribuir trabalho real a motoristas reais.

Antes de começar, certifique-se de que:
1. Você já fechou a transição desde Scheduling no P19.
2. Você já carregou e revisou motoristas no P20.
3. Você já validou a adscrição operativa no P21.
4. Você já configurou regras de Rostering no P22.
5. Você já registrou ausências, inatividades e disponibilidade no P23.
6. Você já registrou cessões/transferências/mudanças de adscrição no P24.
7. Você sabe qual solução de Scheduling será a entrada do cálculo.

Para este quick start, use este caso de referência:

> **Vou executar o primeiro cálculo de Rostering para a linha L1, usando uma solução de Scheduling estável e uma base de motoristas corretamente preparada.**

Para preparar a base:
1. Abra o módulo/ambiente de **Rostering**.
ref: P25_Imagen1.png | compact
2. Revise qual solução de Scheduling será a entrada.
3. Confirme que o coletivo de motoristas está disponível e no contexto correto.
4. Revise que as regras ativas respondem ao caso real.
5. Verifique que ausências e inatividades principais já estão registradas.
6. Confirme que cessões/transferências relevantes já estão refletidas.
7. Se detectar um problema de dados mestres, corrija antes de calcular.

Para o caso de referência, não prossiga até poder afirmar:
1. A solução da L1 já não precisa de mudanças estruturais.
2. O coletivo de motoristas existe e está pronto.
3. Regras e disponibilidade representam a realidade do período.
4. Você pode tentar uma alocação real de trabalho.

Quando você terminar esta seção, deverá ter uma base suficientemente estável para executar o Rostering.

## Selecionando a entrada correta do Scheduling

O Rostering precisa de uma entrada de trabalho clara. Essa entrada não deve ser uma mistura ambígua, e sim uma solução de Scheduling conhecida e utilizável. Aqui o importante é confirmar que você vai atribuir pessoas ao trabalho correto.

Antes de começar esta seção, certifique-se de que:
1. Você sabe qual cenário/solução de Scheduling vai usar.
2. Você sabe qual linha, tipo de dia ou contexto vai cobrir.
3. Você consegue distinguir a solução vigente de uma iteração ainda não consolidada.

Para selecionar corretamente a entrada:
1. No módulo de Rostering, abra a configuração do cálculo/cenário de alocação.
2. Selecione a **solução de Scheduling** que atuará como entrada (publicada para um intervalo de datas).
3. Verifique que o tipo de dia coincide com o cálculo que você quer fazer.
4. Confirme que a(s) linha(s) correspondem ao caso.
5. Se houver várias versões, escolha apenas a que você quer usar como base.
6. Salve a seleção.
7. Verifique que o sistema mostra com clareza qual trabalho será atribuído.

Para o caso de referência, garanta que:
1. A entrada corresponde à L1 dia útil.
2. Você não está misturando uma versão publicada com uma iteração não aprovada.
3. O trabalho que chega ao Rostering é exatamente o que você quer cobrir.

Quando você terminar esta seção, deverá ter uma entrada bem definida para o cálculo de pessoal.

## Configurando o cálculo de Rostering com regras e coletivo corretos

Depois de escolher a entrada, você precisa revisar se o cálculo usa o coletivo e as regras corretas. No Rostering, uma combinação ruim entre coletivo, regras e disponibilidade pode tornar inviável uma solução.

Antes de começar esta seção, certifique-se de que:
1. Você já selecionou a entrada do Scheduling.
2. Você sabe qual coletivo participará.
3. Você definiu se usará regras básicas, avançadas ou combinação controlada.

Para configurar o cálculo de Rostering:
1. Inicie a configuração criando um novo cenário de rostering.
2. Selecione:
   1. os **Depósitos** que participarão,
   2. as **datas** do novo cenário,
   3. o **modelo de regras** aplicado ao cálculo (confirme que corresponde ao grupo correto),
   4. uma **descrição** (opcional).
3. Salve a configuração.
ref: P25_Imagen2.png | compact
4. Verifique se o cálculo considera:
   1. ausências,
   2. inatividades,
   3. cessões,
   4. restrições de disponibilidade.
5. Confirme que o cálculo já tem:
   1. trabalho de entrada,
   2. coletivo elegível,
   3. regras aplicáveis.

Para o caso de referência, confirme que:
1. O grupo de motoristas da L1 é o que será usado.
2. As regras ativas correspondem a esse grupo.
3. A configuração não está trazendo restrições de outro contexto.

Quando você terminar esta seção, deverá ter o cálculo de Rostering parametrizado corretamente antes de executar.

## Executando o primeiro cálculo de alocação

Agora sim você pode executar o cálculo. Neste ponto, o sistema tentará atribuir pessoas reais ao trabalho herdado do Scheduling, respeitando regras, adscrição e disponibilidade.

Antes de começar esta seção, certifique-se de que:
1. Você já escolheu a entrada correta.
2. Você já configurou o coletivo e as regras.
3. Você já revisou disponibilidade e mudanças de contexto.
4. Não faltam dados mestres essenciais.

Para executar o cálculo de Rostering:
1. No cenário/módulo de Rostering, execute **Calcular** / **Iniciar cálculo**.
ref: P25_Imagen3.png | compact
2. Verifique que o sistema inicia o processamento.
3. Aguarde o cálculo terminar.
4. Verifique se o sistema devolve:
   1. solução atribuída,
   2. solução parcial,
   3. ou um sinal claro de conflito.
5. Se não gerar solução utilizável, não assuma imediatamente falta de pessoal. Revise primeiro:
   1. regras muito restritivas,
   2. adscrição incorreta,
   3. ausências carregadas incorretamente,
   4. cessões e habilitações inconsistentes.

Para o caso de referência, confirme que:
1. O cálculo da L1 roda sobre o coletivo esperado.
2. O sistema tenta atribuir trabalho real a pessoas reais.
3. O resultado permite revisar viabilidade ou detectar conflitos concretos.

Quando você terminar esta seção, deverá ter uma primeira solução de Rostering ou um sinal claro de onde está o bloqueio.

## Interpretando se o problema é de regras, disponibilidade ou adscrição

Depois do cálculo, você precisa interpretar corretamente o resultado. Nem todas as falhas significam a mesma coisa. Se você não distinguir a causa, pode corrigir na camada errada.

Antes de continuar, certifique-se de que:
1. Você já executou o cálculo.
2. Você já viu se a solução saiu completa, parcial ou com conflito.
3. Você está disposto a diagnosticar antes de alterar dados.

Para interpretar o resultado:
1. Se faltarem muitas atribuições, revise primeiro a **disponibilidade**.
2. Se o sistema deixar de fora pessoas que deveriam ser válidas, revise **adscrição** e **habilitações**.
3. Se a alocação parecer rígida demais, revise as **regras de Rostering**.
4. Se o trabalho herdado parecer inviável, verifique se o problema vem do **Scheduling**.
5. Não corrija por intuição: localize se o problema pertence a:
   1. regras,
   2. disponibilidade,
   3. adscrição,
   4. ou estrutura herdada.

Para o caso de referência, pergunte-se:
1. Faltam pessoas de fato ou estão mal configuradas?
2. A regra ativada tornou impossível a alocação?
3. Estou tentando usar um motorista em um contexto em que não pertence ou não está habilitado?
4. O problema já existia antes de entrar no Rostering?

Quando você terminar esta seção, deverá ter uma primeira leitura diagnóstica do resultado.

## Deixando a solução pronta para revisão funcional

O objetivo deste quick start ainda não é aprovar definitivamente a solução. O objetivo é executar o primeiro cálculo e deixar uma base pronta para revisão funcional: cobertura, conflitos, equilíbrio e viabilidade.

Antes de terminar, certifique-se de que:
1. Você já executou o cálculo.
2. Você já revisou se a solução é completa ou parcial.
3. Você já identificou se os problemas pertencem a regras, disponibilidade, adscrição ou Scheduling.

Para fechar este primeiro cálculo:
1. Preserve o resultado como base de revisão.
2. Evite mudanças massivas sem identificar a causa.
3. Decida se o próximo passo será:
   1. revisar conflitos de cobertura,
   2. ajustar regras,
   3. corrigir dados de pessoal,
   4. ou voltar ao Scheduling se o problema for estrutural.
4. Trate esta primeira execução como validação do modelo completo de alocação.
5. Se a base for razoável, continue com revisão de cobertura e conflitos.

Para o caso de referência, finalize este quick start apenas quando puder afirmar:
1. Você executou o primeiro cálculo de Rostering para L1.
2. Você sabe se a solução é viável ou parcial.
3. Você tem uma hipótese clara sobre os principais conflitos.
4. Você está pronto para revisar cobertura e conflitos com mais detalhe.

Quando você terminar esta seção, deverá ter executado o primeiro cálculo de Rostering e ter uma base clara para a próxima fase.

## Leituras adicionais

- [Revisando conflitos, cobertura e viabilidade de pessoal](P26_Revisando_conflitos_cobertura_e_viabilidade_de_pessoal.md)

