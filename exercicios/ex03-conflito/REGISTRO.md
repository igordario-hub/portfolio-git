# Registro de Resolução de Conflito

## Arquivo afetado
`projeto/hello-world/main.py`

## O que causou o conflito
O conflito aconteceu porque duas branches diferentes alteraram a mesma linha do arquivo `main.py`, responsável por exibir o título principal do programa.

## Branches envolvidas
- `feat/titulo-versao-a`
- `feat/titulo-versao-b`

## Como resolvi
Primeiro, fiz o merge da branch `feat/titulo-versao-a` na `main`.
Depois, ao tentar fazer o merge da branch `feat/titulo-versao-b`, o GitHub identificou conflito porque o mesmo trecho do arquivo já havia sido modificado.
Eu comparei as duas versões e escolhi uma frase final que reunisse as duas ideias.

## Versão final escolhida
`print("=== Agenda e Planejamento de Estudos ===")`

## Como marquei como resolvido
Usei a opção de resolver conflitos no próprio GitHub, editei manualmente o arquivo e depois marquei o conflito como resolvido antes de concluir o merge.
