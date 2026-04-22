---
title: Gerenciando Ausências, inatividade e disponibilidade de pessoal
shortTitle: Disponibilidade pessoal
intro: Saiba como registrar o Ausências, restrições de inatividade e disponibilidade
  para que o Alocação atribua apenas a pessoas realmente elegíveis e não tente cobrir
  o trabalho com o Motoristas indisponível.
contentType: how-tos
versions:
- '*'
---
## Compreender a diferença entre Ausência, inatividade e disponibilidade

Antes de calcular o Alocação, você precisa controlar quais pessoas estão realmente disponíveis para trabalhar. Nesta camada já não é suficiente para que o Motorista exista, esteja ligado ao contexto correto e tenha regras aplicáveis. Você também precisa dizer ao sistema se essa pessoa:
1. está disponível,
2. está ausente,
3. Está inativo.
4. ou tem uma disponibilidade parcial ou restrita.

Use este início rápido quando você já tiver carregado o Motoristas, revise seu destacamento operacional e prepare a base de regra Alocação, e você precisa evitar que o cálculo tente atribuir trabalho a pessoas inelegíveis.

Antes de começar, certifique-se de que:
1. Você já carregou e verificou o Motoristas no P20.
2. Você já tem Validado seu destacamento operacional para P21.
3. Você já definiu a base de regras do Alocação em P22.
4. É claro para si que grupo de pessoal irá participar no cálculo.
5. Você sabe se em sua operação você precisa registrar férias, baixas, licenças, parciais Indisponibilidades ou estados não operacionais.

Para este início rápido, use este caso de referência:

> **Vou gravar a Ausências, restrições de inatividade e disponibilidade na Motoristas que cobrirá a Linha L1 para garantir que a Alocação apenas atribui trabalho a pessoas realmente elegíveis.**

Compreender corretamente esses conceitos:
1. Use um **Ausência** quando a pessoa existir e pertencer ao coletivo, mas não está disponível para um período específico.
2. Use um **inatividade** quando a pessoa deve ser deixada fora de operação por um período mais estrutural ou não deve participar no cálculo.
3. Use um **Restrição da disponibilidade** quando a pessoa puder trabalhar, mas não em todo momento ou não em todas as condições.
4. Não misture esses conceitos como se fossem os mesmos.
5. Use esta regra de leitura:
   1. **Ausência** = não pode funcionar durante um período específico,
   2. **inatividade** = não deve ser tratado como um recurso operacional nesse contexto ou período,
   3. **disponibilidade restrita** = pode funcionar, mas com limites.

Para gravar os tipos de Ausências, inatividades ou Indisponibilidades:
1. Em GoalBus, você deve abrir **Configuração** > **Pessoal** > **Ausência Configuração**.
ref: P23_Imagen1.png | compact
2. Verifique se todos os tipos de Ausência que você precisa são criados.
3. Se não houver Ausência ou você precisar criar um novo, clique no botão **Criar um novo Ausência**.
ref: P23_Imagen2.png | compact(2x)
4. Para criar um novo tipo de Ausência, os seguintes campos devem ser preenchidos:
   1. **Nome do Ausência**: nome do Tipo de ausência a ser criado.
   2. **Denominação curta**: para visões compactas.
   3. **ID do ObjectivoDriver**: código interno se você trabalhar com integrações.
   4. **Categoria Ausência**: Pode ser **Pura**, **Grátis** ou **Trabalho**. Dependendo do que escolher, uma duração (**Tempo** ou **Dia inteiro**), uma duração de **Tempo de trabalho** ou **Dias máximos** deve ser atribuído.
   5. **Elegibilidade para atribuir o trabalho**: Se você pode escolher o Motorista para atribuir-lhe trabalho ou não, apesar do seu Ausência.
   6. Selecione se este tipo de Ausência será **Requerível pelo Motorista**.
5. Salve o novo tipo de Ausência.
ref: P23_Imagen3.png | compact(x10)
6. Continua a gravar todos os tipos necessários de Ausência.
7. Confirme que você tem todos os tipos de Ausência necessários para o seu planejamento.

Quando você terminar este Seção, você deve ter uma visão clara de que tipo de Ausências você será capaz de usar no seu planejamento de torrefação e que você será capaz de atribuir para Motoristas diferente. fileciteturn22file3L1-L20 fileciteturn22file2L1-L18

## Gravação Planejado Motorista Ausências

Planejado Ausências são um dos primeiros itens a carregar antes do cálculo Alocação. Aqui vêm férias, licenças, deficiências, licenças ou qualquer outro período em que uma pessoa não deve receber um emprego.

Antes de iniciar este Seção, certifique-se de que:
1. Você sabe que Motoristas terá Ausências dentro do horizonte de cálculo.
2. Você sabe as datas exatas ou aproximadas daqueles Ausências.
3. Você quer deixar o sistema inequívoco sobre que dias uma pessoa não pode ser usada.
4. Você já criou todos os tipos necessários de Ausência.

Para gravar o Ausências do Perfil do motorista:
1. Em GoalBus, você deve abrir **Configuração** > **Pessoal** > **Gestão de motoristas**.
ref: P23_Imagen4.png | compact
2. Clique no botão na barra superior para carregar os dados Ausências.
ref: P23_Imagen5.png | compact(3x)
3. Selecione a ação **Pessoal de carga Ausências**.
ref: P23_Imagen6.png | compact
4. Carregue o arquivo Ausências na janela pop-up. Nesta janela você pode rever o formato do arquivo Ausências, lendo as instruções ou baixando um modelo de exemplo.
ref: P23_Imagen7.png | full
5. Confirma a carga de ficheiros.
6. Mantém o registo.
7. Agora você pode verificar o Ausências carregado no perfil de cada Motorista.

Para o caso de referência, uma lógica mínima poderia ser:
1. Motorista A: férias de 10 a 20
2. Motorista B: Permissão no dia 14
3. Motorista C: Incapacidade por uma semana específica

Quando você terminar este Seção, você deve ter gravado o Ausências principal que afeta o cálculo Alocação.

## Verificar que o Alocação já vê corretamente a elegibilidade real

O último passo é validar que a combinação entre Motoristas, destacamento, regras e disponibilidade já reflete a realidade do cálculo. Aqui o objetivo é garantir que Alocação não tentará atribuir trabalho a pessoas ausentes, inativas ou mal restritas, nem deixará fora pessoas que devem ser elegíveis.

Antes de terminar, certifique-se de que:
1. Você já registou Ausências relevante.
2. Você já configurou disponibilidades parciais se necessário.
3. Você sabe que coletivo vai usar o seguinte cálculo.

Para verificar se a disponibilidade real já está bem modelada:
1. Volte para a lista geral de Motoristas.
2. Revisar vários perfis representativos do coletivo.
3. Confirma que os ausentes têm os seus períodos corretamente registrados.
4. Confirma que as restrições parciais não são modeladas como total Ausências por engano.
5. Pergunte-se se o sistema já poderia:
   1. exclui os que não devem trabalhar,
   2. incluindo aqueles que podem trabalhar,
   3. e respeitar restrições parciais sem quebrar o cálculo.
6. Se a resposta for sim, continue com o próximo início rápido.
7. Se a resposta for não, corrija os registros antes de continuar.

Para o caso de referência, não continue até poder dizer:
1. L1 Motoristas já tem sua disponibilidade real bem refletida.
2. Os Ausências estão carregados.
3. A inatividade é diferenciada.
4. Restrições parciais não foram confundidas com Ausências completo.

Quando você terminar este Seção, você deve ter uma base de disponibilidade suficientemente confiável para mudar para tarefas, transferências e mudanças de destacamento.

## Lecturas adicionais

- [Gestão de transferências, atribuições e alterações de destacamento](P24_Gestão_De_Transferências_Atribuições_E_Alterações_De_Destacamento.md)
