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

def filtrarEventosPorCategoria(listaEventos, categoria):
    """Filtra e exibe eventos por uma categoria específica."""
    eventos_filtrados = [e for e in listaEventos if e['categoria'].lower() == categoria.lower()]
    
    if not eventos_filtrados:
        print(f"\nNão há eventos na categoria '{categoria}'.")
        return
    
    print(f"\n--- Eventos na Categoria: {categoria} ---")
    for evento in eventos_filtrados:
        status = " (Participado)" if evento.get('participado', False) else ""
        print(f"ID: {evento['id']} | Nome: {evento['nome']} | Data: {evento['data']} | Local: {evento['local']}{status}")