---
title: Executando o primeiro cálculo Alocação
shortTitle: Calcular Alocação
intro: Saiba como preparar e executar o primeiro cálculo do Alocação, verifique se
  a solução de pessoal é viável e detecte quais os problemas pertencem a regras, disponibilidade
  ou destacamento antes de validar a atribuição.
contentType: how-tos
versions:
- '*'
---
## Preparar a base antes de lançar o cálculo Alocação

Antes de executar o cálculo, você precisa verificar que a base de pessoal está madura o suficiente. Alocação não deve ser usado para descobrir dados mestre faltando no último minuto. Se o modelo, destacamento, regras ou disponibilidade não estão bem preparados, o cálculo falhará ou produzirá uma solução enganosa.

Use este início rápido quando você já tiver uma solução estável Programação e tenha preparado todo o pessoal necessário para atribuir o trabalho real ao Motoristas.

Antes de começar, certifique-se de que:
1. Você já fechou a transição de Programação no P19.
2. Você já carregou e verificou o Motoristas no P20.
3. Você já tem Validado o destacamento operacional para P21.
4. Você já definiu as regras Alocação para P22.
5. Você já registrou Ausências, inatividade e disponibilidade no P23.
6. Você já registou atribuições, transferências ou mudanças de destacamento no P24.
7. Você está claro que solução Programação atuará como entrada para o cálculo.

Para este início rápido, use este caso de referência:

> **Vou executar o primeiro cálculo Alocação para Linha L1, usando uma solução Programação já estável e uma base Motorista adequadamente preparada.**

Preparar a base antes do cálculo:
1. Abre o ambiente ou módulo **Alocação**.
ref: P25_Imagen1.png | compact
2. Verifique qual solução Programação será a entrada do cálculo.
3. Confirma que o coletivo de Motoristas que participará está disponível e pertence ao contexto correto.
4. Verifique se as regras ativas do Alocação respondem ao caso real.
5. Verifica que os principais Ausências e inatividades já estão registrados.
6. Confirma que as atribuições ou transferências relevantes já estão refletidas.
7. Se você detectar um problema de dados mestre, corrija-o antes de calcular.

Para o caso de referência, não continue até poder dizer:
1. A solução L1 já não necessita de alterações estruturais.
2. O coletivo de Motoristas já existe e está pronto.
3. As regras e a disponibilidade já representam a realidade do período.
4. Podes tentar um emprego a sério agora.

Quando você terminar este Seção, você deve ter uma base estável suficiente para lançar Alocação.

## Selecionar a entrada correta do Programação

Alocação precisa de uma entrada de trabalho clara. Essa entrada não deve ser uma mistura ambígua de Cenários, mas uma solução Programação bem conhecida e utilizável. Nesta fase, o importante é confirmar que você vai atribuir as pessoas para o trabalho certo.

Antes de iniciar este Seção, certifique-se de que:
1. Você sabe o que Programação Cenário ou solução que você irá usar.
2. Você sabe o que Linha, tipo de dia ou contexto você vai cobrir.
3. Agora você pode distinguir entre a solução atual e uma iteração não consolidada.

Para selecionar corretamente a entrada do cálculo:
1. No módulo Alocação, abra o cálculo Configuração ou o mapeamento Cenário.
2. Selecione o **Solução Programação** que irá agir como uma entrada, ou seja, qual solução é Publicado para um Intervalo de datas.
3. Verifique se o tipo de dia corresponde ao cálculo que deseja fazer.
4. Verifique se o Linha ou o conjunto de Linhas correspondem ao caso.
5. Se houver vários Versãos possíveis, escolha apenas aquele que realmente deseja usar como base.
6. Salve a selecção.
7. Verifique se o sistema já mostra claramente o trabalho que será atribuído.

Para o caso de referência, certifique-se de que:
1. A entrada corresponde a L1 utilizável.
2. Você não está misturando um Publicado Versão com uma iteração não aprovada.
3. O trabalho que vem para Alocação é exatamente o que você quer cobrir.

Quando você terminar este Seção, você deve ter uma entrada Programação bem definida para o cálculo da equipe.

## Configurando o cálculo Alocação com as regras corretas e coletivas

Uma vez que a entrada é escolhida, você precisa verificar que o cálculo usa o coletivo e as regras corretas. No Alocação, uma combinação ruim de coletivo, regras e disponibilidade pode tornar uma solução que no Programação estava correto inviável.

Antes de iniciar este Seção, certifique-se de que:
1. Você já selecionou a entrada do Programação.
2. Você sabe que grupo de pessoal vai participar.
3. Você já definiu se você vai usar regras básicas, avançadas ou uma combinação controlada.

Para configurar o cálculo do Alocação:
1. Começa o Configuração do cálculo de mapeamento criando uma nova torrefação Cenário.
2. Selecione os seguintes dados de entrada:
   1. O **Depósitos** que vai participar.
   2. Selecione o **datas** da nova torrefação Cenário.
   3. Verifique se o **Regras-modelo** se aplicará ao cálculo. Confirme que as regras ativas correspondem ao grupo correto.
   4. Adicione um **Descrição** se quiser dar mais detalhes.
3. Salve o Configuração.
ref: P25_Imagen2.png | compact(x10)
4. Verifique se o cálculo terá em conta:
   1. Ausências,
   2. inatividade,
   3. atribuições,
   4. e restrições de disponibilidade.
5. Verifique se o cálculo já tem:
   1. trabalho de entrada,
   2. coletivo elegível,
   3. Regras aplicáveis.

Para o caso de referência, confirma que:
1. O grupo L1 Motorista é o que deve ser utilizado.
2. As regras ativas correspondem a esse grupo.
3. O Configuração não está arrastando restrições de outro contexto.

Quando você terminar este Seção, você deve ter o cálculo Alocação parametrizado corretamente antes de executá-lo.

## Executar o primeiro cálculo de atribuição

Agora você pode iniciar o cálculo. Neste ponto, o sistema tentará atribuir pessoas reais para trabalhar herdadas do Programação, respeitando regras, destacamento e disponibilidade.

Antes de iniciar este Seção, certifique-se de que:
1. Já escolheu a entrada certa.
2. Você estabeleceu o coletivo e as regras.
3. Você já revisou a base de disponibilidade e as mudanças de contexto.
4. Já não faltam dados mestrais essenciais.

Para executar o cálculo do Alocação:
1. A partir do estágio ou módulo Alocação, lança a ação **Calcular** ou **Início do cálculo**.
ref: P25_Imagen3.png | compact(3x)
2. Verifique se o sistema começa a processar a atribuição.
3. Espere até o cálculo acabar.
4. Verifique se o sistema retorna:
   1. uma solução atribuída,
   2. uma solução parcial,
   3. ou um sinal claro de conflito.
5. Se o cálculo não gerar uma solução utilizável, não assuma imediatamente que você está faltando pessoal. Verifique primeiro:
   1. regras demasiado restritivas,
   2. Despacho incorreto,
   3. Ausências mal carregado,
   4. o atribuições e audiências divergentes.

Para o caso de referência, confirma que:
1. O cálculo de L1 é executado no coletivo esperado.
2. O sistema tenta atribuir trabalho real a pessoas reais.
3. O resultado permite revisar a viabilidade ou detectar conflitos específicos.

Quando você terminar este Seção, você deve ter uma primeira solução Alocação ou um sinal claro de onde o bloqueio está.

## Interpretar se o problema é regras, disponibilidade ou destacamento

Após o cálculo, você precisa interpretar corretamente o resultado. Nem todas as falhas significam a mesma coisa. Se você não distinguir bem a causa, você pode corrigi-lo na camada errada.

Antes de continuar, certifique-se de que:
1. Já controlaste o cálculo.
2. Viu se a solução estava completa, parcial ou em conflito.
3. Está disposto a diagnosticar antes de tocar nos dados.

Para interpretar corretamente o resultado:
1. Se faltarem muitas tarefas, verifique primeiro a equipe **disponibilidade**.
2. Se o sistema deixar fora as pessoas que devem ser válidas, verifique seu **destacamento** e seu **notações**.
3. Se a atribuição parecer muito rígida ou impossível, verifique o **Regras Alocação**.
4. Se o trabalho de legado parecer impraticável para qualquer grupo, verifique novamente se o problema vem do **Programação**.
5. Não corrija por intuição. Descubra primeiro se o problema pertence a:
   1. regras,
   2. disponibilidade,
   3. destacamento,
   4. ou estrutura herdada.

Para o caso de referência, faça-se estas perguntas:
1. As pessoas estão mesmo desaparecidas ou mal configuradas?
2. A regra que eu ativei tornou a missão impossível?
3. Estou tentando usar um Motorista em um contexto onde ele não pertence ou não está habilitado?
4. O problema já existia antes de entrar no Alocação?

Quando você terminar este Seção, você deve ter uma primeira leitura diagnóstica do resultado do cálculo.

## Deixando a solução pronta para revisão funcional

O objetivo deste início rápido ainda não é aprovar definitivamente a solução. O objetivo é executar o primeiro cálculo e deixar uma base pronta para revisão funcional: cobertura, conflitos, equilíbrio e viabilidade.

Antes de terminar, certifique-se de que:
1. Já controlaste o cálculo.
2. Você já verificou se a solução é completa ou parcial.
3. Você já identificou se os problemas pertencem a regras, disponibilidade, destacamento ou Programação.

Para fechar este primeiro cálculo útilmente:
1. Mantém o resultado do cálculo como base de reexame.
2. Não faça mudanças maciças sem primeiro identificar a causa do problema.
3. Decide se o próximo passo será:
   1. analisar os conflitos de cobertura,
   2. ajustar as regras,
   3. corrigir os dados do pessoal,
   4. ou retorne para Programação se o problema for estrutural.
4. Trata esta primeira execução como uma validação de todo o modelo de mapeamento.
5. Se a base for razoável, continuar com a revisão da cobertura e dos conflitos.

Para o caso de referência, termine este início rápido apenas quando puder dizer:
1. Você já executou o primeiro cálculo Alocação para L1.
2. Sabe se a solução é viável ou parcial.
3. Você já tem uma hipótese clara sobre onde estão os principais conflitos.
4. Você está pronto para rever cobertura e conflitos em mais detalhes.

Quando você terminar este Seção, você deve ter executado o primeiro cálculo Alocação e uma base clara para a próxima fase de revisão.

## Lecturas adicionais

- [Revisão de conflitos, cobertura e viabilidade do pessoal](P26_Revisão_De_Conflitos_Cobertura_E_Viabilidade_Do_Pessoal.md)
