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

b = criar_evento(1,"jose","aaaa", "ali", "lá", True)
print(b)

#Lista os eventos já criados
eventos_criado = [b]

"""def listar_eventos():
    for novo_evento in b:
        print(eventos) """
        
def listar_eventos():
   for evento_item in eventos:
        print(evento_item)
    
 
a = listar_eventos()
print(a)

