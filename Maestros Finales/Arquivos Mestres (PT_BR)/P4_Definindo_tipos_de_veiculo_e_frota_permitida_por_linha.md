---
title: Definindo tipos de veículo e frota permitida por linha
shortTitle: Frota por linha
intro: 'Aprenda a configurar os tipos de veículo e as restrições de frota permitida por linha para que o GoalBus bloqueie alocações inviáveis, respeite limites físicos e ambientais e prepare uma base coerente antes de definir tempos e serviços.'
contentType: how-tos
versions:
  - '*'
---

## Definindo os tipos de veículo permitidos para uma linha

Antes de passar para tempos de percurso, serviços ou regras de Scheduling, você precisa deixar claro quais **tipos de veículo** podem operar cada linha. No GoalBus, essa restrição não é decorativa: ela atua como um filtro de segurança, conformidade e viabilidade física. O objetivo é evitar que o sistema proponha um veículo que não cabe em uma rua, que viola uma restrição ambiental ou que não deveria circular naquele serviço.

Use este quick start quando você já tiver a rede, os parkings e os depósitos preparados e precisar fechar a base de frota que o seu caso vai usar antes de definir tempos e oferta de serviço.

Antes de começar, certifique-se de que:
1. Você já preparou a rede mestra no P6.
2. Você já revisou a rede operacional no P7.
3. Você já configurou parkings e depósitos no P5.
4. Você sabe qual linha vai usar como caso de referência.
5. Você sabe, pelo menos em nível básico, quais restrições físicas ou ambientais afetam essa linha.

Para este quick start, use este caso de referência:

> **Vou definir quais tipos de veículo podem operar a linha L1 para garantir que o meu primeiro planejamento use apenas uma frota coerente com a realidade física e normativa do serviço.**

Para definir os tipos de veículo permitidos do seu caso:
1. No GoalBus, abra a configuração da **linha** que você vai usar como referência.
2. Localize a seção **Tipos de veículos permitidos**.
3. Verifique se a linha já tem tipos atribuídos.
4. Se a linha já tiver tipos definidos, confirme que eles continuam corretos para o seu caso.
5. Se ainda não estiverem definidos, primeiro verifique se o **tipo de veículo** de que você precisa já existe na configuração geral de veículos.
6. Se o tipo **existir**, selecione-o como permitido para essa linha.
7. Se o tipo **não existir**, saia da configuração da linha e vá à configuração geral de **veículos** para criar ou completar primeiro o catálogo de tipos disponível no painel de **Tipos de Veículos**.
ref: P4_Imagen1.png | full
8. Crie o tipo de veículo que você precisa usando uma categoria clara e entendível para o negócio, por exemplo:
   1. Micro-ônibus
   2. Padrão elétrico
   3. Articulado a diesel
ref: P4_Imagen2.png | compact
9. Salve o novo tipo de veículo.
ref: P4_Imagen3.png | compact
10. Volte para a configuração da linha.
11. Marque os tipos de veículo específicos que estão autorizados a operar nessa linha.
ref: P4_Imagen4.png | compact
12. Deixe desmarcados os tipos que não devem operar esse serviço.
13. Salve a configuração.
14. Revise a linha novamente e confirme que o filtro já representa corretamente a realidade operacional.

Para o caso de referência, pergunte-se:
1. A linha L1 admite um ônibus padrão, um micro-ônibus ou ambos?
2. Existe algum tipo de veículo que deve ser excluído por tamanho ou pelo ambiente?
3. Se o tipo de que você precisa não existia, você já o criou antes de tentar atribuí-lo à linha?
4. O sistema deveria bloquear uma alocação manual se você tentasse usar um veículo não autorizado?

Quando você terminar esta seção, deverá ter definida uma restrição de frota por linha que já serve como base para o cálculo posterior.

## Relacionando a linha com os depósitos ou parkings permitidos

Depois de definir qual frota cabe ou não cabe na linha, você precisa revisar de quais bases físicas esse serviço pode sair. O GoalBus permite definir **parkings ou depósitos permitidos** por linha para obrigar o sistema a iniciar o serviço a partir de locais geograficamente corretos e reduzir a quilometragem em vazio.

Antes de começar esta seção, certifique-se de que:
1. Você já configurou os tipos de veículo permitidos da linha.
2. Você já preparou os parkings e depósitos do caso no P5.
3. Você sabe de qual base operacional o serviço deveria realmente começar.

Para relacionar a linha com seus depósitos ou parkings permitidos:
1. Na mesma configuração da linha, localize a seção **Aparcamientos permitidos** ou **Depósitos permitidos**.
2. Verifique se a linha já tem depósitos autorizados.
3. Selecione apenas os depósitos/garagens que estão geograficamente autorizados a iniciar os serviços dessa linha.
4. Deixe de fora as bases que não fazem sentido operacional para esse corredor.
5. Salve a configuração.
6. Verifique se a linha agora tem uma lógica coerente de saída a partir da base mais razoável.

Para o caso de referência, verifique que:
1. A linha L1 pode sair do Depósito Norte.
2. O parking principal associado é o correto.
3. Você não está permitindo um depósito distante que obrigue a percorrer muitos quilômetros em vazio para iniciar a primeira viagem.

Quando você terminar esta seção, deverá ter alinhado a linha, a frota permitida e a geografia de saída do serviço.

## Validando que a linha já tem uma base de frota coerente

Agora que você já definiu os tipos de veículo permitidos e os depósitos ou parkings autorizados, você precisa fazer uma validação final.

Antes de continuar, certifique-se de que:
1. A linha já tem tipos de veículo permitidos.
2. Se o tipo de veículo necessário não existia, ele já foi criado previamente na configuração geral.
3. A linha já tem depósitos ou parkings autorizados.
4. A configuração reflete a realidade do caso que você está construindo.

Para validar que a base de frota já está pronta:
1. Revise novamente a configuração completa da linha.
2. Confirme que os tipos de veículo selecionados representam a frota que realmente deveria operar esse serviço.
3. Confirme que os depósitos ou parkings autorizados minimizam a quilometragem em vazio.
4. Pergunte-se se o sistema, com essa configuração, já evitaria:
   1. alocações fisicamente impossíveis,
   2. descumprimentos ambientais,
   3. saídas de bases geograficamente ineficientes.
5. Se a resposta for sim, continue com o próximo quick start.
6. Se a resposta for não, corrija a linha ou crie o tipo de veículo faltante antes de seguir.

Quando você terminar esta seção, deverá ser capaz de afirmar que a linha já tem uma base de frota suficientemente madura para sustentar tempos de percurso, serviços e regras de Scheduling.

## Leituras adicionais

- [Definindo versões de tempo e tempos de percurso](P9_Definindo_versoes_de_tempo_e_tempos_de_percurso.md)

