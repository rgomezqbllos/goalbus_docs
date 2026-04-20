---
title: Validando a estrutura operacional e o status do serviço
shortTitle: Estrutura operacional
intro: 'Aprenda a revisar depósitos, unidades e grupos operacionais e a validar o serviço criado para que ele fique realmente elegível para Scheduling antes de passar para regras e cálculo.'
contentType: how-tos
versions:
  - '*'
---

## Revisando a estrutura operacional que sustenta o seu serviço

Antes de passar para regras e para o cenário de Scheduling, você precisa verificar que a sua oferta não apenas existe, mas está apoiada em uma estrutura operacional coerente. Nesta fase você deve revisar se a linha, o depósito, a unidade operacional e os grupos relacionados pertencem ao mesmo contexto de negócio e de operação.

Use este quick start quando você já tiver criado a oferta de serviço base e precisar confirmar que o ambiente organizacional que a sustenta está correto antes de calcular.

Antes de começar, certifique-se de que:
1. Você já criou a oferta de serviço no P10.
2. Você já configurou parkings e depósitos no P5.
3. Você já definiu frota e restrições base da linha no P4.
4. Você sabe qual linha e qual serviço vai usar como referência.

Para este quick start, use este caso de referência:

> **Vou validar que a linha L1, o Depósito Norte, a unidade operacional associada e os grupos relacionados formam uma base coerente antes de levar o serviço ao Scheduling.**

Para revisar a estrutura operacional do seu caso:
1. Abra a configuração ou a visão operacional relacionada ao serviço que você acabou de criar.
2. Identifique qual **depósito** sustenta o serviço.
3. Verifique se esse depósito coincide com a base física definida anteriormente.
4. Revise a qual **unidade operacional** a linha ou o serviço pertence.
5. Confirme se essa unidade se encaixa com a infraestrutura, a geografia e a organização do caso.
6. Revise os **grupos** relacionados que afetam esse contexto, se existirem.
7. Confirme que a linha, a unidade e o depósito não pertencem a estruturas incompatíveis.
8. Se detectar uma incoerência, corrija antes de seguir.

Para o caso de referência, verifique:
1. A linha L1 está associada ao Depósito Norte.
2. Esse depósito pertence à unidade correta.
3. Os grupos vinculados não apontam para outro âmbito operacional.

Quando você terminar esta seção, deverá estar claro que a oferta de serviço vive dentro de uma estrutura operacional consistente.

## Confirmando que o serviço já está validado e pronto para programação

Depois de revisar a estrutura operacional, você precisa confirmar algo crítico: que o serviço criado no P10 já está em status **Validado**. Não basta ter criado viagens, intervalos e rotas. Para que o Scheduling consiga ler o serviço e considerá-lo elegível, o serviço precisa ter passado pela ação de validação.

Antes de começar esta seção, certifique-se de que:
1. Você já revisou o serviço comercial e suas viagens no P10.
2. Você já conferiu intervalos, rotas e durações.
3. Você não precisa continuar editando o serviço nesta fase.

Para confirmar que o serviço está pronto para programação:
1. Abra o serviço comercial que você vai usar como referência.
2. Revise o **status** atual.
3. Se o status já for **Validado**, confirme que não há nada pendente antes de seguir.
4. Se o serviço ainda estiver em edição ou em um status anterior, execute a ação **Validar**.
5. Verifique se o status muda corretamente.
6. Confirme que:
   1. o serviço não fica mais como rascunho,
   2. as viagens ficam protegidas contra alterações acidentais,
   3. e o serviço já pode ser consumido pelo Scheduling.
7. Se detectar um erro de estrutura, corrija antes de validar novamente.

Para o caso de referência, não prossiga enquanto não puder afirmar:
1. A linha L1 já tem a oferta de dias úteis revisada.
2. O serviço já mudou para status **Validado**.
3. O sistema já pode usá-lo como entrada de programação.

Quando você terminar esta seção, deverá ter um serviço realmente preparado para ser lido pelo motor.

## Verificando a coerência entre estrutura, serviço e elegibilidade

Agora você precisa fazer uma última revisão conjunta. O objetivo não é apenas ter um serviço validado, mas confirmar que o serviço validado vive na estrutura correta e que não carrega incoerências organizacionais que depois compliquem o cálculo.

Antes de continuar, certifique-se de que:
1. Você já revisou depósito, unidade e grupos.
2. Você já validou o serviço (ou confirmou a validação).
3. Você sabe qual caso levará para o próximo passo.

Para validar a elegibilidade completa antes do Scheduling:
1. Revise o serviço validado e confirme qual linha ele utiliza.
2. Verifique se essa linha continua vinculada ao depósito correto.
3. Revise se a unidade operacional e os grupos não contradizem o contexto do serviço.
4. Pergunte-se se o sistema já poderia tomar esse serviço como uma entrada válida e coerente para cálculo.
5. Se a resposta for sim, continue com o próximo quick start.
6. Se a resposta for não, corrija a estrutura ou devolva o serviço à edição apenas se você precisar refazer parte da base antes de validar novamente.

Para o caso de referência, certifique-se de que:
1. A L1 pertence ao contexto organizacional correto.
2. O Depósito Norte é realmente a base que sustenta o serviço.
3. O serviço de dias úteis já está validado e não tem contradições com sua estrutura.

Quando você terminar esta seção, deverá ser capaz de afirmar que a oferta não está apenas criada, mas também alinhada estruturalmente e elegível para Scheduling.

## Leituras adicionais

- [Definindo regras de veículos para Scheduling](P12_Definindo_regras_de_veiculos_para_scheduling.md)

