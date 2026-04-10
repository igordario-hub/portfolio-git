sessoes_estudo = [
    {"id": 1, "disciplina": "Programação", "duracao_horas": 2, "dia": "Segunda-feira"},
    {"id": 2, "disciplina": "Cálculo", "duracao_horas": 1.5, "dia": "Terça-feira"},
    {"id": 3, "disciplina": "Engenharia de Software", "duracao_horas": 2, "dia": "Quarta-feira"},
    {"id": 4, "disciplina": "Programação", "duracao_horas": 1, "dia": "Quinta-feira"},
]

def listar_sessoes():
    return sessoes_estudo

def adicionar_sessao(disciplina, duracao_horas, dia):
    nova_sessao = {
        "id": len(sessoes_estudo) + 1,
        "disciplina": disciplina,
        "duracao_horas": duracao_horas,
        "dia": dia
    }
    sessoes_estudo.append(nova_sessao)
    return nova_sessao