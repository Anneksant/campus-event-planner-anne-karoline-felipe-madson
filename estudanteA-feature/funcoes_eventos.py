#função construtora de evento
def evento(id, nome, data, local, categoria, participado):
    return {
        "id": id,
        "nome": nome,
        "data": data,
        "local": local,
        "categoria": categoria,
        "participado": participado,
    }

# lista global para armazenar eventos
eventos = []

#Cria um novo evento (dicionário) e adiciona à lista `eventos`. Retorna o evento criado.

def criar_evento(id, nome, data, local, categoria, participado):    
    novo_evento = evento(id, nome, data, local, categoria, participado)
    eventos.append(novo_evento)
    return novo_evento

