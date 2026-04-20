---
title: Revisando a rede operacional com sequências e pontos-chave
shortTitle: Rede operacional
intro: 'Aprenda a validar como a sua rede se comporta na operação real, revisando sequências, permissões de parada e pontos de relevo antes de passar para tempos e serviços.'
contentType: how-tos
versions:
  - '*'
---

## Revisando a sequência operativa das rotas

Agora que você já criou a rede base (paradas, linhas e rotas), o próximo passo é validar que essa rede funciona corretamente do ponto de vista operacional.

Neste ponto você não está mais criando estrutura — está validando como ela se comporta na prática.

Antes de começar:
1. Você já criou paradas, linhas e rotas no P6.
2. Você tem pelo menos uma rota por sentido.
3. Você sabe qual linha está preparando.

Caso:
> Validar que a rota L1 tem uma sequência coerente e operativa antes de definir tempos.

Passos:
1. Abra a linha em que você está trabalhando.
2. Acesse a visão de rotas.
ref: P7_Imagen1.png | full
3. Selecione um sentido.
4. Revise a sequência de paradas.
5. Verifique que:
   - Não faltam paradas-chave.
   - Não há duplicados desnecessários.
   - A ordem está correta.
6. Repita para o outro sentido.

Resultado esperado:
- Uma sequência limpa e lógica que represente o percurso real.

## Validando permissões de parada

Nem todas as paradas funcionam do mesmo jeito. Algumas permitem embarque, outras desembarque, e outras ambos.

Antes de continuar:
1. Você já validou a sequência.
2. Você sabe como cada parada funciona na realidade.

Passos:
1. Dentro da rota, revise cada parada.
2. Configure se permite:
   - Embarque
   - Desembarque
   - Ambos
ref: P7_Imagen2.png | compact
3. Garanta que:
   - Terminais permitem ambos.
   - Paradas intermediárias refletem a operação real.
4. Salve as alterações.

Resultado esperado:
- Cada parada tem um comportamento coerente com a operação.

## Definindo pontos de relevo

Os pontos de relevo são críticos para o Rostering e a operação.

Antes de começar:
1. Você já tem a sequência validada.
2. Você sabe onde ocorrem relevos na operação real.

Passos:
1. Identifique paradas onde ocorrem trocas de motorista.
2. Marque essas paradas como pontos de relevo.
ref: P7_Imagen3.png | compact
3. Verifique que:
   - Estão bem localizados.
   - São suficientes para a operação.
4. Salve.

Resultado esperado:
- A rede já contempla onde podem ocorrer trocas de motorista.

## Validação final da rede operacional

Antes de avançar:
1. Revise toda a rota novamente.
2. Confirme:
   - Sequência correta.
   - Permissões coerentes.
   - Relevos definidos.
3. Pergunte-se:
   - Essa linha poderia operar na vida real?
   - Falta algum detalhe operacional?

Se a resposta for sim, você pode continuar.

## Leituras adicionais

- [Preparando parkings e depósitos para a operação](P5_Preparando_parkings_e_depositos_para_a_operacao.md)

