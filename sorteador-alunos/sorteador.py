import random

def carregar_alunos(arquivo):
    """Lê os nomes dos alunos de um arquivo .txt"""
    with open(arquivo, "r", encoding="utf-8") as f:
        alunos = [linha.strip() for linha in f if linha.strip()]
    return alunos

def sortear_aluno(alunos, ja_sorteados):
    """Sorteia um aluno que ainda não foi chamado"""
    disponiveis = [a for a in alunos if a not in ja_sorteados]
    if not disponiveis:
        print("\n✅ Todos os alunos já foram sorteados! Reiniciando lista.\n")
        ja_sorteados.clear()
        disponiveis = alunos

    escolhido = random.choice(disponiveis)
    ja_sorteados.append(escolhido)
    return escolhido

def sortear_trios(alunos):
    """Sorteia todos os alunos em grupos de 3 (trios)"""
    embaralhados = alunos.copy()
    random.shuffle(embaralhados)

    trios = [embaralhados[i:i+3] for i in range(0, len(embaralhados), 3)]

    # Se o último grupo tiver 1 ou 2 alunos, junta com o trio anterior
    if len(trios) > 1 and len(trios[-1]) < 3:
        sobra = trios.pop()
        trios[-1].extend(sobra)

    return trios

def modo_individual(alunos):
    ja_sorteados = []
    print(f"📚 {len(alunos)} alunos carregados.\n")

    while True:
        entrada = input("Pressione ENTER para sortear (ou 'q' para sair): ")
        if entrada.lower() == "q":
            print("Encerrando o sorteio. Até a próxima aula!")
            break

        aluno = sortear_aluno(alunos, ja_sorteados)
        print(f"🎯 Aluno sorteado: {aluno}\n")

def modo_trios(alunos):
    trios = sortear_trios(alunos)
    print(f"\n📚 {len(alunos)} alunos divididos em {len(trios)} grupo(s):\n")

    for i, trio in enumerate(trios, start=1):
        print(f"🎯 Grupo {i}: {', '.join(trio)}")
    print()

def main():
    alunos = carregar_alunos("alunos.txt")

    print("Escolha o modo de sorteio:")
    print("1 - Sortear aluno por aluno")
    print("2 - Sortear em trios")
    modo = input("Digite 1 ou 2: ").strip()

    if modo == "1":
        modo_individual(alunos)
    elif modo == "2":
        modo_trios(alunos)
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
