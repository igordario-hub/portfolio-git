from estudos import listar_sessoes, adicionar_sessao
from resumo import buscar_por_disciplina, calcular_total_horas

print("=== Organizador de Estudos ===")
for sessao in listar_sessoes():
    print(
        f'#{sessao["id"]} - {sessao["disciplina"]} | '
        f'{sessao["duracao_horas"]}h | {sessao["dia"]}'
    )

print("=== Organizador de Estudos ===")
resultado = buscar_por_disciplina("Pro")
if resultado:
    for sessao in resultado:
        print(
            f'Encontrada: {sessao["disciplina"]} - '
            f'{sessao["duracao_horas"]}h na {sessao["dia"]}'
        )
else:
    print("Nenhuma sessão encontrada.")

print("\n=== Adicionando nova sessão ===")
nova = adicionar_sessao("Banco de Dados", 2, "Sexta-feira")
print("Sessão adicionada:", nova)

print("\n=== Total de horas por disciplina ===")
totais = calcular_total_horas()
for disciplina, horas in totais.items():
    print(f"{disciplina}: {horas}h")
