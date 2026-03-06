clientes = []
contador_id = 1

def get_all():
    return clientes

def get_by_id(id):
    for c in clientes:
        if c["id"] == id:
            return c
    return None

def create(cliente):
    global contador_id
    novo = cliente.model_dump()
    novo["id"] = contador_id
    contador_id += 1
    clientes.append(novo)
    return novo

def update(id, dados):
    for i, c in enumerate(clientes):
        if c["id"] == id:
            clientes[i].update(dados.model_dump(exclude_unset=True))
            return clientes[i]
    return None

def delete(id):
    global clientes
    antes = len(clientes)
    clientes = [c for c in clientes if c["id"] != id]
    return len(clientes) < antes
