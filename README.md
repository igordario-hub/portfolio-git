# Portfólio Git — Controle de Versão na Prática

Repositório criado como exercício prático de Git e GitHub. O objetivo é demonstrar, na prática, o uso de commits semânticos, branches, pull requests, resolução de conflitos e reflexão sobre o aprendizado.

## Estrutura

```text
portfolio-git/
├── README.md
├── REFLEXAO.md
├── exercicios/
│   ├── ex01-commits/notas.md
│   ├── ex02-branches/notas.md
│   └── ex03-conflito/REGISTRO.md
└── projeto/
    └── hello-world/
        ├── main.py
        ├── estudos.py
        └── resumo.py

Projeto: Agenda de Estudos

Mini-aplicativo em Python que simula uma agenda de estudos. Ele permite listar sessões cadastradas, buscar sessões por disciplina e calcular o total de horas estudadas por matéria. O projeto foi usado como base prática para os exercícios de Git e GitHub.

Modulos

| Arquivo      | Responsabilidade                                                |
| ------------ | --------------------------------------------------------------- |
| `main.py`    | Executa o fluxo principal do programa                           |
| `estudos.py` | Armazena as sessões de estudo e permite cadastrar novas sessões |
| `resumo.py`  | Realiza busca por disciplina e cálculo de carga horária         |

Como executar

python projeto/hello-world/main.py
