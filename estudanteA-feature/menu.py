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
def marcarEventoAtendido(listaEventos, id_evento):
    """Marca um evento específico como 'participado' com base no ID."""
    try:
        id_int = int(id_evento)
        print("Evento marcado como atendido com sucesso!")
    except ValueError:
        print("Erro: O ID deve ser um número inteiro.")
        return False

    for evento in listaEventos:
        if evento['id'] == id_int:
            evento['participado'] = True
            print(f"Evento '{evento['nome']}' (ID: {id_int}) marcado como **Participado**.")
            return True
    
    print(f"Erro: Evento com ID {id_int} não encontrado.")
    return False
def gerarRelatorio(listaEventos):
    """Gera e exibe um relatório resumido dos eventos."""
    total_eventos = len(listaEventos)
    eventos_participados = sum(1 for e in listaEventos if e.get('participado', False))
    
    # Contagem por Categoria
    contagem_categorias = {}
    for evento in listaEventos:
        cat = evento['categoria']
        contagem_categorias[cat] = contagem_categorias.get(cat, 0) + 1
        
    # Cálculo da porcentagem
    porcentagem_participados = (eventos_participados / total_eventos * 100) if total_eventos > 0 else 0
    
    print("\n--- RELATÓRIO DE EVENTOS ---")
    print(f"Total de Eventos: {total_eventos}")
    print(f"Eventos Participados: {eventos_participados} ({porcentagem_participados:.2f}%)")
    print("Eventos por Categoria:")
    for categoria, contagem in contagem_categorias.items():
        print(f"  - {categoria}: {contagem}")