# estudanteb.py - Módulo de Interação com Usuário e Relatórios (Anne - Estudante B)


def displayMenu():
    """Exibe o menu de opções do Planejador de Eventos."""
    print("\n=== Planejador de Eventos do Campus ===")
    print("1. Adicionar Evento")
    print("2. Ver Todos os Eventos")
    print("3. Filtrar por Categoria")
    print("4. Marcar Evento como Participado")
    print("5. Gerar Relatório")
    print("6. Sair")

def getEscolhaDoUsuario():
    """Solicita e retorna a escolha do usuário como inteiro."""
    escolha = 0
    while escolha == 0:
        try:
            escolha = int(input("\nEscolha uma opção: "))
            return escolha
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

