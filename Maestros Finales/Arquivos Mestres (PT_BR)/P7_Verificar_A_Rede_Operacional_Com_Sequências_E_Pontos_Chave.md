---
title: Verificar a rede operacional com sequências e pontos-chave
shortTitle: Rede operacional
intro: Aprenda a validar como sua rede realmente se comporta em operação, revisando
  sequências, permissões Parada e pontos de retransmissão antes de passar aos horários
  e serviços.
contentType: how-tos
versions:
- '*'
---
## Verificando a sequência operacional do Rotas

Agora que você já criou a rede base (Paradas, Linhas e Rotas), o próximo passo é validar que essa rede funciona corretamente do ponto de vista operacional.

Neste ponto você não está mais criando estrutura, você está validando como ela se comporta na prática.

Antes de começar:
1. Você já criou Paradas, Linhas e Rotas no P6.
2. Você tem pelo menos um Rota por sentido.
3. Você sabe o que Linha você está preparando.

Processo:
> Validar que Rota L1 tem uma sequência coerente e operacional antes de definir os tempos.

Passos:
1. Abra o Linha em que está a trabalhar.
2. Acesse a vista Rota.
ref: P7_Imagen1.png | full
3. Selecione um sentido.
4. Verifique o Sequência de paradas.
5. Verifica que:
   - Não falta nenhuma chave Paradas.
   - Não há duplicados desnecessários.
   - A ordem está correta.
6. Repita para o outro sentido.

Resultado esperado:
- Uma sequência limpa e lógica que representa o Rota real.

## Validação de licenças Parada

Nem todos os Paradas funcionam do mesmo modo. Alguns permitem escalar, outros mais baixos, e outros ambos.

Antes de continuar:
1. Você tem Validado a sequência.
2. Você sabe como cada Parada na realidade funciona.

Passos:
1. Dentro do Rota, verifique todos os Parada.
2. Configurar se você permitir:
   - Levante-se
   - Abaixo
   - Ambos
ref: P7_Imagen2.png | compact
3. Certifique-se de que:
   - Os terminais permitem ambos.
   - O Paradas intermediário reflete a operação real.
4. Salve as mudanças.

Resultado esperado:
- Cada Parada tem um comportamento consistente com a operação.

## Definição de Pontos de Relação

Os pontos de relés são críticos para assamento e operação.

Antes de começar:
1. Você já tem uma sequência Validado.
2. Sabes onde os relés acontecem na operação.

Passos:
1. Identificar Paradas onde as alterações Motorista são feitas.
2. Marque os Paradas como pontos de relé.
ref: P7_Imagen3.png | compact
3. Verifica que:
   - Estão bem posicionados.
   - Já chega para a operação.
4. Guarda.

Resultado esperado:
- A rede já contempla onde as alterações Motorista podem ser feitas.

## Validação final da rede operacional

Antes de avançar:

1. Verifique o Rota inteiro novamente.
2. Confirma:
   - Sequência direita.
   - Permissões coerentes.
   - Relés determinados.
3. Pergunte a si mesmo:
   - Você poderia operar este Linha na vida real?
   - Falta algum detalhe operacional?

Se a resposta for sim, pode continuar.

## Lecturas adicionais

- P8 Carregando viagens vazias
