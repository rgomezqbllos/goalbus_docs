---
title: Preparação de lotes e armazéns Garagem para a operação
shortTitle: Carro Entrada na garagems e armazéns
intro: Saiba como configurar os espaços e armazéns da Garagem de forma consistente
  para que a Programação possa usar uma infraestrutura física realista, minimizar
  a quilometragem vazia e respeitar a hierarquia de dados correta.
contentType: how-tos
versions:
- '*'
---
## Configurar o depósito como estrutura operacional e de relé

Antes de criar o Garagem, você precisa verificar o **depósito**. No GoalBus, o depósito é a base operacional da organização e é o link obrigatório para o Veículos e o Motoristas. Além disso, o seu Configuração não serve apenas para identificar a unidade, mas também para definir onde o Turnos pode começar ou terminar, incluindo cabeçalhos ou terminais autorizados que permitem relés eficientes e reduzir a quilometragem a vácuo.

Antes de iniciar este Seção, certifique-se de que:
1. Você sabe que depósito é responsável pelo Linha ou serviço que você está preparando.
2. Você entende que o depósito é a entidade principal e que o Garagem depende disso.
3. Você já criou todos os tipos de Veículos necessários para a operação.

Para criar ou validar o seu depósito de caso:
1. Em GoalBus, abra o módulo **Depósitos**.
ref: P5_Imagen3.png | full
2. Veja se o depósito que você precisa já existe.
3. Se o depósito já existir, abra-o e verifique o seu Configuração.
4. Se não existir, crie um novo.
ref: P5_Imagen4.png | compact(2x)
5. Define ou valida estes campos:
   1. **Código** como um Identificador único.
   2. **Denominação curta** para visões compactas.
   3. **Porcentagem** como parte de depósito no total das operações. Entre todos os depósitos deve adicionar 100%.
   4. **Nome longo** como o nome principal do depósito.
   5. **Identificação externa**, se o cliente trabalhar com integrações ERP ou HR.
6. Adicionar o **Início e fim autorizados Paradas** como cabeçalhos ou terminais onde relés ou fim de Turno são permitidos.
7. Guarde o depósito.
ref: P5_Imagen5.png | compact(8.5x)
8. Confirma que o depósito já pode sustentar operacionalmente o caso que você tem construído.

Para o caso de referência, verifique que:
1. O Depósito Norte é o depósito organizacional correto.
2. Os cabeçalhos ou terminais L1 relevantes são autorizados como locais iniciais ou finais quando se aplicam.

Quando você terminar este Seção, você deve ter um depósito corretamente identificado ligado a seus locais de operação autorizados.

## Configurando o Garagem como um nó físico da rede

Depois de ter definido o depósito e antes de ir em vazio Viagems, Frota ou Programação regras, você precisa deixar o **Garagem** bem configurado que irá segurar o seu caso. Em GoalBus, um lote Garagem não é apenas uma tag administrativa. É um nó físico geolocalizado da rede, e quando você cria-o o sistema gera automaticamente um Parada associado nessas coordenadas para que o motor possa calcular Distâncias, tempos de entrada e tempos de saída consistentemente. Além disso, cada Garagem deve ser ligado a um depósito organizacional.

Use este início rápido quando você já tiver criado a rede base e precisar conectar essa rede à infraestrutura física real antes de avançar e Programação.

Antes de começar, certifique-se de que:
1. Você está claro que Linha ou serviço você vai usar como um caso de referência.
2. Você sabe de que base física essa operação deve sair.
3. Já arranjaste os depósitos operacionais.
4. Você já criou todos os tipos necessários de Veículos.

Para este início rápido, use este caso de referência:

> **Vou preparar o lote North Garagem Garagem e validar que sua relação com o depósito e Linha L1 é consistente antes de continuar com Viagems vazio e Programação.**

Para criar ou validar o seu caso Garagem:
1. Em GoalBus, abra o módulo **Lotes Garagem** ou **Lotes Garagem** dentro da infraestrutura de rede.
ref: P5_Imagen1.png | full
2. Veja se o Garagem que você precisa já existe.
3. Se o Garagem já existir, abra-o e verifique o seu Configuração.
4. Se o Garagem não existir, crie um novo.
ref: P5_Imagen2.png | compact(2x)
5. Define ou valida estes campos:
   1. **Código** como um curto Identificador para visões compactas.
   2. **Denominação curta** para visões compactas.
   3. **Nome longo** como um nome descritivo da garagem ou pátio.
   4. **Coordenadas** para localizar corretamente o Garagem no mapa.
   5. **Identificação externa**, se o cliente trabalhar com integrações ERP ou HR.
6. Verifique se o Garagem está ligado ao **depósito** correto previamente criado.
ref: P5_Imagen6.png | compact(8.5x)
7. Clique no **Próxima** para configurar a capacidade Garagem e os tipos Veículo permitidos. Isto pode ser editado no futuro à medida que as condições mudarem.
ref: P5_Imagen7.png | compact(8.5x)
8. Verifique visualmente o mapa que sua localização faz sentido para a operação real.
9. Confirma que o sistema já pode tratar que Garagem como a fonte ou destino logístico da operação.

Quando você terminar este Seção, você deve ter um espaço de Garagem adequadamente geolocalizado e devidamente subordinado para o armazém adequado.

## Validando a consistência entre Garagem, depósito e Linha

Agora que você já configurou o Garagem e armazenamento, você precisa verificar que esta infraestrutura se encaixa na lógica e eficiência logística do Linha que o GoalBus espera. O próprio modelo Linha permite definir o **lotes ou armazéns Garagem permitidos** para forçar o sistema a iniciar o serviço a partir das bases geograficamente corretas e minimizar a quilometragem vazia. Esta não é uma preferência cosmética: guiar o programador diretamente na construção de soluções.

Antes de continuar, certifique-se de que:
1. O Garagem já está ligado ao depósito correto.
2. O armazém já tem os seus locais autorizados.

Para validar a coerência completa da infraestrutura (se você já tiver um Linha):
1. Abra o **Linha** Configuração que irá usar como referência.
2. Verifique o **espaços Garagem permitidos** ou **Depósitos autorizados** Seção.
3. Verifique se o depósito correto está autorizado a iniciar serviços no Linha.
4. Se o depósito correto não for autorizado, adicione-o.
5. Confirme que você não está deixando depósitos habilitados que não têm significado geográfico para esse Linha.
6. Verifique se a relação entre Linha, depósito e Garagem minimiza Dirigindo sem renda.
7. Confirme que a infraestrutura física que você acaba de preparar poderia suportar o serviço que você irá criar ou calcular mais tarde.
8. Se detectar inconsistências, corrija-as antes de continuar.

Para o caso de referência, pergunte-se:
1. A Linha L1 está autorizada a sair do Norte da Garagem?
2. Esse armazém usa o North Garagem como base física?
3. Será que a lógica resultante reduz milhas em um vácuo em vez de aumentá-las?

Quando você terminar este Seção, você deve ser capaz de dizer que o Linha, o depósito e o Garagem formam a mesma lógica operacional e logística.

## Lecturas adicionais

- [Rede de mestrado](P6_Preparar_A_Rede_Mestre_Com_Paradas_Linhas_E_Rotas.md)
