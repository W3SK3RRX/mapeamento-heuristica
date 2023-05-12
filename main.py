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
        "latitude": "-6.77398240346339",
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
        "distancia": ["230", "84", "100", "54"]
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
        "distancia": ["71", "220"]
    },

    {
        "id": "p11",
        "nome": "UPA",
        "latitude": "-6.77391458922412",
        "longitude": "-43.0077490664569",
        "destino": ["p8", "p10"],
        "distancia": ["110", "220"]
    },
]


def heuristica(lat1, lon1, lat2, lon2):
    lat1, lon1 = math.radians(float(lat1)), math.radians(float(lon1))
    lat2, lon2 = math.radians(float(lat2)), math.radians(float(lon2))
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    R = (lat1 - lat2) * 40075000 / 360  # raio da terra

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


def a_estrela(inicio, objetivo, maps):
    nos = {}
    for ponto in maps:
        nos[ponto['id']] = {'nome': ponto['nome'],
                            'lat': ponto['latitude'],
                            'long': ponto['longitude'],
                            'dest': ponto['destino'],
                            'dist': ponto['distancia'],
                            'g': float('inf'),
                            'pai': None}

    heap = [(0, inicio)]
    nos[inicio]['g'] = 0

    while heap:
        (f, atual) = heapq.heappop(heap)

        if atual == objetivo:
            caminho = []
            while atual is not None:
                caminho.append(nos[atual]['nome'])
                atual = nos[atual]['pai']
            caminho.reverse()
            return caminho

        for i, vizinho in enumerate(nos[atual]['dest']):
            g_vizinho = nos[atual]['g'] + float(nos[atual]['dist'][i])
            h_vizinho = heuristica(nos[vizinho]['lat'], nos[vizinho]['long'], nos[objetivo]['lat'], nos[objetivo]['long'])
            f_vizinho = g_vizinho + h_vizinho

            if f_vizinho < nos[vizinho]['g']:
                nos[vizinho]['g'] = f_vizinho
                nos[vizinho]['pai'] = atual
                heapq.heappush(heap, (f_vizinho, vizinho))# adiciona o vizinho na lista de prioridade

    return None


print(30 * "-=-")
for ponto in maps:
    print(ponto['id'], ponto['nome'])
print(30 * "-=-")
inicio = input("Informe o ponto de partida: ")
print(30 * "-=-")
destino = input("Informe o ponto de destino: ")
print(30 * "-=-")
caminho = a_estrela(inicio, destino, maps)

if caminho:
    print(f'O caminho mais curto de {inicio} até {destino} é: {caminho}')
else:
    print(f'Não há caminho possível de {inicio} até {destino}.')
