from estudos import sessoes_estudo

def buscar_por_disciplina(nome_disciplina):
    resultados = []
    for sessao in sessoes_estudo:
        if nome_disciplina.lower() in sessao["disciplina"].lower():
            resultados.append(sessao)
    return resultados

def calcular_total_horas():
    totais = {}
    for sessao in sessoes_estudo:
        disciplina = sessao["disciplina"]
        if disciplina not in totais:
            totais[disciplina] = 0
        totais[disciplina] += sessao["duracao_horas"]
    return totais