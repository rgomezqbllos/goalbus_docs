---
title: Validando e consolidando a solução de Rostering
shortTitle: Validar Rostering
intro: 'Aprenda a encerrar a revisão da solução de Rostering, validar a alocação quando já é confiável operacionalmente e consolidá-la como referência aprovada para uso posterior ou integração com a operação.'
contentType: how-tos
versions:
  - '*'
---

## Confirmando que a solução já está pronta para validar

Depois de revisar cobertura, conflitos e viabilidade, o próximo passo é decidir se a solução de Rostering já pode ser considerada suficientemente sólida. Validar não é apenas um “ok” administrativo. É declarar que a alocação já é coerente, entendível e utilizável como base aprovada.

Use este quick start quando você já executou o cálculo de Rostering, analisou o resultado e precisa encerrar formalmente a solução antes de consolidá-la.

Antes de começar, certifique-se de que:
1. Você já executou o cálculo de Rostering no P25.
2. Você já revisou conflitos, cobertura e viabilidade no P26.
3. Você já corrigiu os principais problemas ou entende por que conflitos restantes são aceitáveis.
4. Você sabe qual solução específica vai validar.

Para este quick start, use este caso de referência:

> **Vou validar a solução de Rostering da linha L1 porque a alocação já cobre o trabalho de forma confiável e quero consolidá-la como referência aprovada.**

Para confirmar que a solução está pronta:
1. Abra a solução de Rostering que você vai usar como referência.
2. Revise uma última vez a cobertura do trabalho.
3. Confirme que conflitos principais já foram resolvidos ou diagnosticados.
4. Verifique se a alocação resultante continua coerente com:
   1. regras de Rostering,
   2. disponibilidade real,
   3. adscrição operativa,
   4. solução herdada do Scheduling.
5. Se detectar um problema importante não resolvido, não valide ainda.
6. Se a base estiver estável, prossiga para validação.

Para o caso de referência, não prossiga até poder afirmar:
1. O trabalho da L1 está coberto ou lacunas restantes estão entendidas.
2. A solução é defensável operacionalmente.
3. Você não precisa de mudanças estruturais antes de aprovar.

Quando você terminar esta seção, deverá ter claro se a solução merece validação formal.

## Executando a validação da solução de pessoal

Depois que a solução estiver estável o suficiente, você precisa executar a validação. Este passo fecha cálculo e revisão e converte a solução em referência aprovada no fluxo.

Antes de começar esta seção, certifique-se de que:
1. Você decidiu que a solução é válida.
2. Você não precisa recalcular nem ajustar regras antes de aprovar.
3. Você sabe que validar congela a solução como referência aprovada.

Para validar a solução de Rostering:
1. Na visão da solução ou na tabela principal, abra o menu de ações correspondente.
ref: P27_Imagen1.png | full
2. Selecione **Validar**.
3. Revise o resumo final antes de confirmar.
4. Confirme a validação quando o sistema solicitar.
5. Verifique que o status muda para o status de aprovação correspondente.
6. Confirme que a solução deixa de ser tratada como versão provisória.
7. Se o seu fluxo usa permissões de aprovação, confirme que a validação foi registrada corretamente.

Para o caso de referência, garanta que:
1. A solução da L1 muda de status após validar.
2. O sistema a reconhece como versão aprovada.
3. A solução deixa de ser tratada como iteração aberta.

Quando você terminar esta seção, deverá ter uma solução de Rostering formalmente validada.

## Consolidando a solução como referência operacional

Depois de validar, você precisa consolidar a solução. Consolidar significa tratar essa versão como a referência aprovada para o próximo nível do processo. A partir daqui, não deve ser gerida como teste, e sim como base séria e rastreável de alocação.

Antes de começar esta seção, certifique-se de que:
1. A solução já está validada.
2. Você sabe se ela será a referência vigente ou uma versão aprovada para uso posterior.
3. Você consegue diferenciar uma solução aprovada de uma solução em revisão.

Para consolidar a solução validada:
1. Revise nome e descrição.
2. Se necessário, atualize a descrição para deixar claro:
   1. que contexto cobre,
   2. que período representa,
   3. por que foi aprovada.
3. Verifique que a solução validada se distingue claramente de rascunhos, testes e iterações anteriores.
4. Se o processo interno exigir, registre que esta versão vira referência para o próximo passo.
5. Mantenha versões anteriores como histórico, mas evite tratá-las como equivalentes.

Para o caso de referência, garanta que:
1. A solução validada da L1 se distingue de versões intermediárias.
2. A equipe consegue identificá-la como referência correta.
3. A rastreabilidade da aprovação está clara.

Quando você terminar esta seção, deverá ter uma solução aprovada e reconhecível como referência de Rostering.

## Revisando o que fica bloqueado e o que exigiria nova iteração

Antes de encerrar, tenha claro que validar não elimina a possibilidade de melhorar. Significa que aquela versão está fechada. Se mais adiante você precisar de uma melhoria de fundo, o correto é abrir nova iteração (ou novo ciclo), não alterar a versão aprovada sem controle.

Antes de continuar, certifique-se de que:
1. A solução já está validada.
2. Você sabe quais partes ficaram fechadas.
3. Você tem claro que melhorias futuras devem ser rastreadas como novas iterações.

Para manter governança após validar:
1. Trate a solução validada como referência fechada.
2. Evite modificá-la diretamente como se fosse rascunho.
3. Se detectar melhoria futura:
   1. crie nova iteração,
   2. ou abra novo ciclo de cálculo e revisão.
4. Mantenha a versão validada como base histórica de comparação.
5. Se a equipe audita decisões, use esta solução como referência aprovada.

Para o caso de referência, finalize esta seção apenas quando puder afirmar:
1. A versão validada da L1 está fechada.
2. Qualquer melhoria futura será feita por nova iteração.
3. A rastreabilidade entre cálculo, revisão e aprovação está preservada.

Quando você terminar esta seção, deverá ter claro o que significa consolidar uma solução e como manter controle de versões.

## Deixando a solução pronta para o próximo nível do processo

O último passo é preparar a transição. A partir daqui, a solução de Rostering já não está em fase de cálculo técnico, e sim em fase de uso, consolidação ou transferência para o próximo processo operacional.

Antes de terminar, certifique-se de que:
1. Você já validou a solução.
2. Você já a tratou como referência consolidada.
3. Você sabe se o próximo passo será:
   1. comunicar,
   2. integrar,
   3. auditar,
   4. ou preparar nova iteração futura.

Para encerrar este quick start:
1. Revise uma última vez o status da solução.
2. Confirme que não é mais um cálculo provisório.
3. Verifique que a equipe conseguiria identificar esta versão como a aprovada.
4. Se necessário, registre a transição para o próximo nível operacional.
5. Mantenha a solução como referência estável para comparação futura.

Para o caso de referência, finalize este quick start apenas quando puder afirmar:
1. A solução de Rostering da L1 está validada.
2. Está consolidada como referência aprovada.
3. O próximo passo já não é calcular, e sim usar/revisar/evoluir de forma controlada.

Quando você terminar esta seção, deverá ter uma solução de Rostering validada, consolidada e pronta para servir como referência estável.

## Leituras adicionais

- [Atribuindo tarefas lógicas a veículos reais](P28_Atribuindo_tarefas_logicas_a_veiculos_reais.md)

