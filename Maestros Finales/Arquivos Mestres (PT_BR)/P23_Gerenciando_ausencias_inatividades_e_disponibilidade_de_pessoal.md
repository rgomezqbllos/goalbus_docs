---
title: Gerenciando ausências, inatividades e disponibilidade de pessoal
shortTitle: Disponibilidade pessoal
intro: 'Aprenda a registrar ausências, inatividades e restrições de disponibilidade para que o Rostering atribua trabalho apenas a pessoas realmente elegíveis e não tente cobrir trabalho com motoristas indisponíveis.'
contentType: how-tos
versions:
  - '*'
---

## Entendendo a diferença entre ausência, inatividade e disponibilidade

Antes de calcular o Rostering, você precisa controlar quem está realmente disponível para trabalhar. Nesta camada não basta que o motorista exista, esteja adscrito ao contexto correto e tenha regras aplicáveis. Você também precisa dizer ao sistema se a pessoa:
1. está disponível,
2. está ausente,
3. está inativa,
4. ou tem disponibilidade parcial/restrita.

Use este quick start quando você já tiver motoristas carregados, adscrição operativa revisada e a base de regras de Rostering preparada, e precisar impedir que o cálculo atribua trabalho a pessoas não elegíveis.

Antes de começar, certifique-se de que:
1. Você já carregou e revisou motoristas no P20.
2. Você já validou a adscrição operativa no P21.
3. Você já definiu a base de regras de Rostering no P22.
4. Você sabe qual coletivo participará do cálculo.
5. Você sabe se precisa registrar férias, afastamentos, licenças, indisponibilidades parciais ou estados não operacionais.

Para este quick start, use este caso de referência:

> **Vou registrar ausências, inatividades e restrições de disponibilidade dos motoristas que cobrirão a linha L1 para garantir que o Rostering atribua trabalho apenas a pessoas realmente elegíveis.**

Para entender corretamente esses conceitos:
1. Use uma **ausência** quando a pessoa existe e pertence ao coletivo, mas não está disponível em um período específico.
2. Use uma **inatividade** quando a pessoa deve ficar fora da operação (ou do cálculo) por um período mais estrutural.
3. Use uma **restrição de disponibilidade** quando a pessoa pode trabalhar, mas não o tempo todo ou não em todas as condições.
4. Não misture esses conceitos.
5. Use esta regra:
   1. **ausência** = não pode trabalhar em um período específico,
   2. **inatividade** = não deve ser tratada como recurso operacional nesse contexto/período,
   3. **disponibilidade restrita** = pode trabalhar, mas com limites.

Para registrar tipos de ausências/inatividades/indisponibilidades:
1. No GoalBus, abra **Configuração** > **Pessoal** > **Configuração de Ausências**.
ref: P23_Imagen1.png | compact
2. Verifique se todos os tipos de ausência necessários já estão criados.
3. Se precisar criar um novo, clique em **Criar Nova Ausência**.
ref: P23_Imagen2.png | compact
4. Preencha ao menos:
   1. **Nome da ausência**
   2. **Nome curto**
   3. **GoalDriver ID** (se houver integrações)
   4. **Categoria de ausência** (e as regras de duração correspondentes)
   5. **Elegibilidade para atribuir trabalho**
   6. Se o tipo será **Solicitável pelo motorista**
5. Salve o novo tipo.
ref: P23_Imagen3.png | compact
6. Continue até registrar todos os tipos necessários.
7. Confirme que você tem os tipos necessários para o seu planejamento.

Quando você terminar esta seção, deverá ter clareza sobre quais tipos de ausências você poderá usar no planejamento de Rostering e atribuir aos diferentes motoristas.

## Registrando ausências planejadas do motorista

Ausências planejadas são um dos primeiros elementos que você deve carregar antes do cálculo de Rostering. Aqui entram férias, licenças, afastamentos e qualquer período em que a pessoa não deva receber trabalho.

Antes de começar esta seção, certifique-se de que:
1. Você sabe quais motoristas terão ausências no horizonte de cálculo.
2. Você conhece as datas exatas ou aproximadas.
3. Você quer deixar claro ao sistema em quais dias a pessoa não pode ser usada.
4. Você já criou os tipos de ausência necessários.

Para registrar ausências:
1. No GoalBus, abra **Configuração** > **Pessoal** > **Gestão de motoristas**.
ref: P23_Imagen4.png | compact
2. Clique no botão da barra superior para carregar dados de ausências.
ref: P23_Imagen5.png | compact
3. Selecione **Carregar ausências de pessoal**.
ref: P23_Imagen6.png | compact
4. Carregue o arquivo de ausências na janela. Você pode revisar o formato pelas instruções ou baixando um template.
ref: P23_Imagen7.png | full
5. Confirme a carga.
6. Salve o registro.
7. Revise as ausências carregadas no perfil de cada motorista.

Para o caso de referência, uma lógica mínima poderia ser:
1. Motorista A: férias de 10 a 20
2. Motorista B: licença no dia 14
3. Motorista C: afastamento por uma semana específica

Quando você terminar esta seção, deverá ter registradas as principais ausências que afetam o cálculo de Rostering.

## Verificando que o Rostering vê corretamente a elegibilidade real

O último passo é validar que a combinação entre motoristas, adscrição, regras e disponibilidade reflete a realidade do cálculo. O objetivo é garantir que o Rostering não tentará atribuir trabalho a pessoas ausentes/inativas/mal restringidas e também não deixará de fora pessoas que deveriam ser elegíveis.

Antes de terminar, certifique-se de que:
1. Você já registrou ausências relevantes.
2. Você configurou restrições parciais se necessário.
3. Você sabe qual coletivo o próximo cálculo vai usar.

Para verificar que a disponibilidade real está bem modelada:
1. Volte à lista geral de motoristas.
2. Revise alguns perfis representativos.
3. Confirme que pessoas ausentes têm seus períodos corretamente registrados.
4. Confirme que restrições parciais não foram modeladas como ausências totais.
5. Pergunte-se se o sistema já poderia:
   1. excluir quem não deve trabalhar,
   2. incluir quem pode trabalhar,
   3. e respeitar restrições parciais sem quebrar o cálculo.
6. Se a resposta for sim, continue com o próximo quick start.
7. Se a resposta for não, corrija os registros antes de seguir.

Para o caso de referência, não prossiga até poder afirmar:
1. Motoristas da L1 têm a disponibilidade real bem refletida.
2. Ausências estão carregadas.
3. Inatividades estão diferenciadas.
4. Restrições parciais não foram confundidas com ausências completas.

Quando você terminar esta seção, deverá ter uma base de disponibilidade suficientemente confiável para passar a cessões/transferências e mudanças de adscrição.

## Leituras adicionais

- [Gerenciando transferências, cessões e mudanças de adscrição](P24_Gerenciando_transferencias_cessoes_e_mudancas_de_adscricao.md)

