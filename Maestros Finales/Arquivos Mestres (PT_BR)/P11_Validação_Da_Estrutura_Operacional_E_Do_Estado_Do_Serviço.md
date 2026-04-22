---
title: Validação da estrutura operacional e do estado do serviço
shortTitle: Estrutura operacional
intro: Saiba como revisar depósitos, unidades e grupos operacionais, e validar o serviço
  criado para torná-lo realmente elegível para o Programação antes de passar às regras
  e cálculos.
contentType: how-tos
versions:
- '*'
---
## Revisão da estrutura operacional que suporta o seu serviço

Antes de passar às regras e ao Programação Cenário, você precisa verificar que sua oferta não só existe, mas é suportada por uma estrutura operacional coerente. Nesta fase, você precisa verificar se o Linha, depósito, unidade operacional e grupos relacionados pertencem ao mesmo contexto de negócio e de operação.

Use este início rápido quando você já criou a oferta de serviço base e precisa confirmar que o ambiente organizacional que o suporta está correto antes de calcular.

Antes de começar, certifique-se de que:
1. Você já criou a oferta de serviço na P10.
2. Você já configurou lotes Garagem e armazéns em P6.
3. Você já definiu restrições Frota e base Linha em P8.
4. Você está claro o que Linha e serviço que você vai usar como referência.

Para este início rápido, use este caso de referência:

> **Vou validar que o Linha L1, o Norte Garagem, a unidade operacional associada e os grupos relacionados formam uma base coerente antes de levar o serviço para o Programação.**

Para rever a estrutura operacional do seu caso:
1. Abre a vista Configuração ou operacional relacionada com o serviço que você acabou de criar.
2. Identifique qual **depósito** suporta o serviço.
3. Verifique se o depósito corresponde à base física que definiu anteriormente.
4. Verifique a qual **Unidade operacional** pertence o Linha ou serviço.
5. Verifique se essa unidade se encaixa na infraestrutura, geografia e organização do caso.
6. Verifique o **grupos** relacionado que afeta esse contexto, se eles existirem.
7. Confirma que o Linha, unidade e depósito não pertencem a estruturas incompatíveis.
8. Se detectar uma inconsistência, corrija-a antes de continuar.

Para o caso de referência, verifique:
1. Que Linha L1 está associado ao North Garagem.
2. Esse depósito pertence à unidade certa.
3. Esses grupos ligados não apontam para outra área operacional.

Quando você terminar este Seção, você deve ser claro que a oferta de serviço vive dentro de uma estrutura operacional consistente.

## Confirmando que o serviço já está Validado e pronto para programação

Depois de rever a estrutura operacional, você precisa confirmar algo crítico: que o serviço criado em P10 já está em estado **Validação**. Não é suficiente ter criado Viagems, intervalos e Rotas. Para que Programação possa ler o serviço e considerá-lo elegível, o serviço deve ter passado pela ação de validação.

Antes de iniciar este Seção, certifique-se de que:
1. Você já verificou o serviço comercial e seu P10 Viagems.
2. Você já verificou intervalos, Rotas e duraçãos.
3. Você não precisa mais editar o serviço neste estágio.

Para confirmar que o serviço está pronto para programação:
1. Abra o serviço comercial que irá usar como referência.
2. Verifique o seu **Situação** atual.
3. Se o status já for **Validação**, confirme que não há nada pendente antes de continuar.
4. Se o serviço ainda estiver em edição ou em um estado anterior, execute a ação **Validar**.
5. Verifique se o estado muda corretamente.
6. Verifique isso:
   1. o serviço já não é um Rascunho,
   2. a viagem está protegida contra alterações acidentais,
   3. e o serviço já pode ser consumido pela Programação.
7. Se detectar um erro de estrutura, corrija-o antes de revalidá-lo.

Para o caso de referência, não continue até poder dizer:
1. A Linha L1 já tem a sua oferta operacional revista.
2. O serviço já mudou para o estado **Validação**.
3. O sistema agora pode ser usado como uma entrada de programação.

Quando você terminar este Seção, você deve ter um serviço realmente preparado para ser lido pelo motor.

## Verificar a coerência entre estrutura, serviço e elegibilidade

Agora você precisa fazer uma revisão conjunta final. O objetivo não é apenas ter um serviço Validado, mas para confirmar que o serviço Validado vive na estrutura correta e não arrasta inconsistências organizacionais que depois complicam o cálculo.

Antes de continuar, certifique-se de que:
1. Já verificaram armazém, unidade e grupos.
2. Você já Validado o serviço ou confirmou sua validação.
3. Sabes qual é o próximo caso que vais aceitar.

Para validar a elegibilidade completa antes do Programação:
1. Verifique o serviço Validado e confirme qual Linha você usa.
2. Verifique que o Linha ainda está ligado ao depósito correto.
3. Verifique se a unidade operacional e os grupos não contradizem o contexto do serviço.
4. Pergunte-se se o sistema já poderia tomar esse serviço como uma entrada válida e consistente para o cálculo.
5. Se a resposta for sim, continue com o próximo início rápido.
6. Se a resposta for não, corrija a estrutura ou devolva o serviço à edição apenas se precisar reformular parte da base antes de revalidá-la.

Para o caso de referência, certifique-se de que:
1. L1 pertence ao contexto organizacional correto.
2. O Depósito do Norte é realmente a base para o serviço.
3. O serviço utilizável já é Validado e não tem contradições com sua estrutura.

Quando você terminar este Seção, você deve ser capaz de afirmar que a oferta não só é criada, mas também estruturalmente alinhado e elegível para Programação.

## Lecturas adicionais

- [Definição das Regras Veículo para Programação](P12_Definição_Das_Regras_Veículo_Para_Programação.md)
