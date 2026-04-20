---
title: Preparando parkings e depósitos para a operação
shortTitle: Parkings e depósitos
intro: 'Aprenda a configurar parkings e depósitos de forma coerente para que o Scheduling possa usar uma infraestrutura física realista, minimizar a quilometragem em vazio e respeitar a hierarquia correta de dados.'
contentType: how-tos
versions:
  - '*'
---

## Configurando o depósito como estrutura operativa e de relevo

Antes de criar o parking, você precisa revisar o **depósito**. No GoalBus, o depósito é a base operativa da organização e é o vínculo obrigatório para veículos e motoristas. Além disso, a configuração do depósito não serve apenas para identificar a unidade, mas também para definir de onde os turnos podem começar ou terminar, incluindo terminais autorizados que permitem relevos eficientes e reduzem a quilometragem em vazio.

Antes de começar esta seção, certifique-se de que:
1. Você sabe qual depósito é responsável pela linha ou serviço que está preparando.
2. Você entende que o depósito é a entidade principal e que o parking depende dele.

Para criar ou validar o depósito do seu caso:
1. No GoalBus, abra o módulo de **depósitos**.
ref: P5_Imagen3.png | full
2. Verifique se o depósito de que você precisa já existe.
3. Se o depósito já existir, abra-o e revise a configuração.
4. Se não existir, crie um novo.
ref: P5_Imagen4.png | compact
5. Defina ou valide estes campos:
   1. **Código** como identificador único.
   2. **Nome curto** para visualizações compactas.
   3. **Percentual de participação %** como participação do depósito no total de operações. Entre todos os depósitos, deve somar 100%.
   4. **Nome longo** como nome principal do depósito.
   5. **ID externo**, se o cliente trabalha com integrações ERP ou de RH.
6. Adicione as **paradas de início e fim autorizadas**, como terminais onde sejam permitidos relevos ou finais de turno.
7. Salve o depósito.
ref: P5_Imagen5.png | compact
8. Confirme que o depósito já pode sustentar operacionalmente o caso que você está construindo.

Para o caso de referência, verifique que:
1. O Depósito Norte é o depósito organizacional correto.
2. Os terminais relevantes da linha L1 estão autorizados como locais de início ou fim quando aplicável.

Quando você terminar esta seção, deverá ter um depósito corretamente identificado e vinculado às suas localizações operacionais autorizadas.

## Configurando o parking como nó físico da rede

Depois de definir o depósito e antes de passar para viagens em vazio, frota ou regras de Scheduling, você precisa deixar bem configurado o **parking** que sustentará o seu caso. No GoalBus, um parking não é apenas um rótulo administrativo. Ele é um nó físico geolocalizado da rede e, ao criá-lo, o sistema gera automaticamente uma parada associada nessas coordenadas para que o motor possa calcular distâncias e tempos de entrada/saída de forma coerente. Além disso, cada parking deve estar vinculado obrigatoriamente a um depósito organizacional.

Use este quick start quando você já criou a rede base e precisa conectá-la à infraestrutura física real antes de seguir com deslocamentos e Scheduling.

Antes de começar, certifique-se de que:
1. Você já preparou paradas, linhas e rotas no P6.
2. Você já revisou a rede operacional no P7.
3. Você sabe qual linha ou serviço vai usar como caso de referência.
4. Você sabe de qual base física essa operação deve sair.
5. Você já configurou o(s) depósito(s) operacionais.

Para este quick start, use este caso de referência:

> **Vou preparar o parking do Depósito Norte e validar que a relação com o depósito e com a linha L1 é coerente antes de seguir com viagens em vazio e Scheduling.**

Para criar ou validar o parking do seu caso:
1. No GoalBus, abra o módulo de **parkings** (ou **aparcamentos**) dentro da infraestrutura de rede.
ref: P5_Imagen1.png | full
2. Verifique se o parking de que você precisa já existe.
3. Se o parking já existir, abra-o e revise a configuração.
4. Se o parking não existir, crie um novo.
ref: P5_Imagen2.png | compact
5. Defina ou valide estes campos:
   1. **Código** como identificador breve para visualizações compactas.
   2. **Nome curto** para visualizações compactas.
   3. **Nome longo** como nome descritivo da garagem ou pátio.
   4. **Coordenadas** para posicionar corretamente o parking no mapa.
   5. **ID externo**, se o cliente trabalha com integrações ERP ou de RH.
6. Verifique se o parking está vinculado ao **depósito** correto criado previamente.
ref: P5_Imagen6.png | compact
7. Clique em **Próximo** para configurar a capacidade do parking e os tipos de veículos permitidos. Isso pode ser editado no futuro conforme as condições mudem.
ref: P5_Imagen7.png | compact
8. Revise visualmente no mapa se a localização faz sentido para a operação real.
9. Confirme que o sistema já pode tratar esse parking como origem ou destino logístico da operação.

Quando você terminar esta seção, deverá ter um parking corretamente geolocalizado e corretamente subordinado ao depósito adequado.

## Validando a coerência entre parking, depósito e linha

Agora que você já configurou parking e depósito, você precisa verificar se essa infraestrutura se encaixa na lógica da linha e na eficiência logística que o GoalBus espera. O próprio modelo de linha permite definir **parkings ou depósitos permitidos** para obrigar o sistema a iniciar o serviço a partir das bases geograficamente corretas e minimizar quilometragem em vazio. Isso não é uma preferência cosmética: guia diretamente o programador ao construir soluções.

Antes de continuar, certifique-se de que:
1. O parking já está vinculado ao depósito correto.
2. O depósito já tem suas localizações autorizadas.
3. A linha que você vai usar no seu caso já existe e está validada.

Para validar a coerência completa da infraestrutura:
1. Abra a configuração da **linha** que você vai usar como referência.
2. Revise a seção de **parkings permitidos** ou **depósitos permitidos**.
3. Verifique se o depósito correto está autorizado a iniciar os serviços dessa linha.
4. Se o depósito correto não estiver autorizado, adicione-o.
5. Confirme que você não está deixando habilitados depósitos que não façam sentido geográfico para essa linha.
6. Revise se a relação entre linha, depósito e parking minimiza condução sem receita.
7. Confirme que a infraestrutura física que você acabou de preparar poderia sustentar o serviço que você criará ou calculará depois.
8. Se detectar incoerências, corrija antes de seguir.

Para o caso de referência, pergunte-se:
1. A linha L1 está autorizada a sair do Depósito Norte?
2. Esse depósito usa como base física o Parking Norte?
3. A lógica resultante reduz quilômetros em vazio em vez de aumentá-los?

Quando você terminar esta seção, deverá ser capaz de afirmar que a linha, o depósito e o parking formam uma mesma lógica operativa e logística.

## Leituras adicionais

- [Carregando viagens em vazio e deslocamentos](P8_Carregando_viagens_em_vazio_e_deslocamentos.md)

