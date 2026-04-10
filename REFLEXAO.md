# Reflexão Pessoal

## O que foi difícil

A parte mais difícil deste exercício foi entender, na prática, como o Git organiza o histórico das mudanças e como isso se relaciona com branches, commits e merges. a parte de conflito foi a que eu mais demorei. Antes de fazer a atividade, eu via o Git mais como uma ferramenta para salvar versões do que como uma forma de organizar trabalho de maneira profissional. Quando comecei a usar branches separadas, percebi que o desafio não era só criar arquivos ou digitar comandos, mas entender em que branch eu estava, o que já tinha sido commitado e o que ainda não tinha sido enviado para o GitHub.

Outro ponto difícil foi criar commits realmente semânticos. No começo, minha tendência era escrever mensagens muito genéricas, como se eu só estivesse registrando que mexi em alguma coisa. Com a atividade, percebi que o commit precisa comunicar intenção. Pensar em mensagens como `feat`, `fix`, `docs` e `chore` parece simples quando se lê a definição, mas na hora de aplicar surgiram dúvidas sobre qual tipo usar em mudanças pequenas ou em alterações que misturavam código e documentação. Isso me fez prestar mais atenção no que realmente estava mudando em cada etapa.

A parte mais tensa foi a resolução de conflito. Eu já tinha ouvido falar em conflito de merge, mas nunca tinha entendido direito o que ele significava. Quando o Git mostrou duas versões diferentes do mesmo trecho do arquivo, com aquelas marcações no código, ficou mais claro que conflito não é um erro aleatório, e sim uma consequência de mudanças concorrentes no mesmo lugar. Mesmo assim, foi difícil no início interpretar o que estava acontecendo e decidir qual versão manter sem medo de apagar algo importante.

## O que ficou claro

O que ficou mais claro para mim foi a função de cada etapa do fluxo de trabalho com Git. Agora faz muito mais sentido separar o trabalho em branches, porque isso evita bagunçar a `main` e permite desenvolver alterações de forma mais organizada. Também ficou claro que o Pull Request não serve só para juntar código, mas para registrar uma mudança com contexto, descrição e revisão, mesmo em um repositório individual.

Outra coisa que entendi melhor foi a diferença entre `commit` e `push`. Antes eu confundia os dois. Agora ficou claro que o commit salva uma versão no histórico local do repositório, enquanto o push envia esse histórico para o GitHub. Essa distinção parecia pequena, mas ajuda bastante a entender o que está acontecendo em cada momento.

Também entendi melhor a importância de manter um histórico limpo. Antes eu achava que o importante era só fazer funcionar. Depois da atividade, ficou evidente que a forma como as mudanças são registradas também importa, porque ela ajuda qualquer pessoa, inclusive eu no futuro, a entender a evolução do projeto.

## O que ainda é confuso

Mesmo conseguindo concluir a atividade, ainda tenho dúvidas sobre alguns pontos. O principal deles é entender melhor o que acontece internamente no Git durante um merge. Eu consegui resolver o conflito manualmente e seguir os passos corretamente, mas ainda não sinto que entendo completamente o estado do repositório nesse momento, especialmente a relação entre `HEAD`, branch atual e histórico de commits.

Outra coisa que ainda me deixa um pouco confuso é decidir quando uma mudança merece uma nova branch e quando ela poderia ser feita junto com outra. Na atividade isso ficou mais guiado pelos requisitos, mas em um projeto real imagino que essa decisão dependa mais de organização, contexto e tamanho da alteração.

Também fiquei com curiosidade sobre a diferença entre `merge` e `rebase`. Eu ouvi esses termos antes, mas nesta atividade usei só o fluxo mais básico com merge e Pull Request. Então, mesmo tendo conseguido fazer o que foi pedido, sei que ainda preciso estudar melhor como o Git reorganiza o histórico em situações mais avançadas.

No geral, a atividade foi importante porque me fez perceber que Git não é só um detalhe técnico. Ele faz parte da forma de pensar e organizar o desenvolvimento. Saio deste exercício entendendo melhor o básico, mas também com a noção de que ainda há muita coisa para aprofundar.
