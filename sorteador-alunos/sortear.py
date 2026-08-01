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

def main():
    alunos = carregar_alunos("alunos.txt")
    ja_sorteados = []

    print(f"📚 {len(alunos)} alunos carregados.\n")

    while True:
        entrada = input("Pressione ENTER para sortear (ou 'q' para sair): ")
        if entrada.lower() == "q":
            print("Encerrando o sorteio. Até a próxima aula!")
            break

        aluno = sortear_aluno(alunos, ja_sorteados)
        print(f"🎯 Aluno sorteado: {aluno}\n")

if __name__ == "__main__":
    main()
