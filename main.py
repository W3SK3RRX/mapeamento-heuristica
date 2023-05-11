import heapq
import math

maps = [
    {
        "id": "p0",
        "nome": "Helton Autopeças",
        "latitude": "-6.77294579529729",
        "longitude": "-43.0107411682096",
        "destino": ["p1", "p3"],
        "distancia": ["100", "230"]
    },

    {
        "id": "p1",
        "nome": "Panificadora Rosa Branca",
        "latitude": "-6.77368720118917",
        "longitude": "-43.009929353215",
        "destino": ["p0", "p2"],
        "distancia": ["100", "65"]
    },

    {
        "id": "p2",
        "nome": "Hotel Rio Parnaíba",
        "latitude": "6.77398240346339",
        "longitude": "-43.009630217428",
        "destino": ["p1", "p3", "p4"],
        "distancia": ["65", "84", "140"]
    },

    {
        "id": "p3",
        "nome": "São Jorge Supermercado",
        "latitude": "-6.77370556073959",
        "longitude": "-43.0093296946812",
        "destino": ["p0", "p2", "p7", "p9"],
        "distancia": ["230", "84", "54", "100"]
    },

    {
        "id": "p4",
        "nome": "Espaço Cidadania",
        "latitude": "-6.77490653516264",
        "longitude": "-43.0085988440702",
        "destino": ["p2", "p5"],
        "distancia": ["140", "76"]
    },

    {
        "id": "p5",
        "nome": "Drogaria Brasil",
        "latitude": "-6.7752754666622",
        "longitude": "-43.0081668278133",
        "destino": ["p4", "p6"],
        "distancia": ["76", "89"]
    },

    {
        "id": "p6",
        "nome": "Escola Magnolia Miranda",
        "latitude": "-6.77489724512599",
        "longitude": "-43.0078681685904",
        "destino": ["p5", "p7", "p8"],
        "distancia": ["89", "98", "100"]
    },

    {
        "id": "p7",
        "nome": "Armazem Coração de Jesus",
        "latitude": "-6.7743366163586",
        "longitude": "-43.0086116801161",
        "destino": ["p6", "p3"],
        "distancia": ["98", "100"]
    },

    {
        "id": "p8",
        "nome": "Hotel Bocaina",
        "latitude": "-6.77439262652405",
        "longitude": "-43.0075901407694",
        "destino": ["p6", "p9", "p11"],
        "distancia": ["100", "160", "110"]
    },

    {
        "id": "p9",
        "nome": "Mrm Cabelos",
        "latitude": "-6.77344127141917",
        "longitude": "-43.0091110298527",
        "destino": ["p3", "p8", "p10"],
        "distancia": ["54", "160", "71"]
    },

    {
        "id": "p10",
        "nome": "Mercadinho 2 Irmãos",
        "latitude": "-6.77302627188422",
        "longitude": "-43.0087404358131",
        "destino": ["p9", "p11"],
        "distancia": ["54", "220"]
    },

    {
        "id": "p11",
        "nome": "UPA",
        "latitude": "-6.77391458922412",
        "longitude": "-43.0077490664569",
        "destino": ["p8", "p10"],
        "distancia": ["220", "110"]
    },
]

def heuristica(lat1, lon1, lat2, lon2):
    lat1, lon1 = math.radians(float(lat1)), math.radians(float(lon1))
    lat2, lon2 = math.radians(float(lat2)), math.radians(float(lon2))
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    R = (lat1 - lat2) * 40075000 / 360 # raio da terra

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


def a_estrela(inicio, objetivo, maps):
    nos = {}
    for ponto in maps:
        nos[ponto['id']]  = {'lat': ponto['latitude'],
                             'long': ponto['longitude'],
                             'dest': ponto['destino'],
                             'dist': ponto['distancia'],
                             'g': float('inf'), 'h': 0,
                             'pai': None}

        lista_aberta = [(0, inicio)]
        lista_fechada = []

        while lista_aberta:
            _, id_atual = heapq.heappop(lista_aberta)
            no_atual = nos[id_atual]
            lista_fechada.append(id_atual)

            if id_atual == destino:
                caminho = []
                while no_atual:
                    caminho.append(id_atual)
                    id_atual = no_atual['pai']
                    no_atual = nos.get(id_atual)
                return caminho[::-1]

        for i, id_vizinho in enumerate(no_atual['dest']):
            no_vizinho = nos.get(id_vizinho)
            if not no_vizinho or id_vizinho in lista_fechada:
                 continue
            g = no_atual['g'] + float(no_atual['dist'][i])
            if g < no_vizinho['g'] or id_vizinho not in [id for _, id in lista_aberta]:
                no_vizinho['g'] = g
                no_vizinho['h'] = heuristica(no_vizinho['lat'], no_vizinho['long'], nos[destino]['lat'], nos[destino]['long'])
                no_vizinho['pai'] = id_atual
                heapq.heappush(lista_aberta, (no_vizinho['g'] + no_vizinho['h'], id_vizinho))

    return None

inicio = input("Informe o ponto de partida: ")
destino = input("Informe o ponto de destino: ")
caminho = a_estrela(inicio, destino, maps)

if caminho:
    print(f'O caminho mais curto de {inicio} até {destino} é: {caminho}')
#else:
    #print(f'Não há caminho possível de {inicio} até {destino}.')
