import heapq
import math

maps = [
    {
        "id": "p0",
        "nome": "Helton Autopeças",
        "latitude": "-6.77294579529729",
        "longitude": "-43.0107411682096",
        "destino": ["p1", "p3"]
    },

    {
        "id": "p1",
        "nome": "Panificadora Rosa Branca",
        "latitude": "-6.77368720118917",
        "longitude": "-43.009929353215",
        "destino": ["p0", "p2"]
    },

    {
        "id": "p2",
        "nome": "Hotel Rio Parnaíba",
        "latitude": "6.77398240346339",
        "longitude": "-43.009630217428",
        "destino": ["p1", "p3", "p4"]
    },

    {
        "id": "p3",
        "nome": "São Jorge Supermercado",
        "latitude": "-6.77370556073959",
        "longitude": "-43.0093296946812",
        "destino": ["p0", "p2", "p7", "p9"]
    },

    {
        "id": "p4",
        "nome": "Espaço Cidadania",
        "latitude": "-6.77490653516264",
        "longitude": "-43.0085988440702",
        "destino": ["p2", "p5"]
    },

    {
        "id": "p5",
        "nome": "Drogaria Brasil",
        "latitude": "-6.7752754666622",
        "longitude": "-43.0081668278133",
        "destino": ["p4", "p6"]
    },

    {
        "id": "p6",
        "nome": "Escola Magnolia Miranda",
        "latitude": "-6.77489724512599",
        "longitude": "-43.0078681685904",
        "destino": ["p5", "p7", "p8"]
    },

    {
        "id": "p7",
        "nome": "Armazem Coração de Jesus",
        "latitude": "-6.7743366163586",
        "longitude": "-43.0086116801161",
        "destino": ["p6", "p3"]
    },

    {
        "id": "p8",
        "nome": "Hotel Bocaina",
        "latitude": "-6.77439262652405",
        "longitude": "-43.0075901407694",
        "destino": ["p6", "p9", "p11"]
    },

    {
        "id": "p9",
        "nome": "Mrm Cabelos",
        "latitude": "-6.77344127141917",
        "longitude": "-43.0091110298527",
        "destino": ["p3", "p8", "p10"]
    },

    {
        "id": "p10",
        "nome": "Mercadinho 2 Irmãos",
        "latitude": "-6.77302627188422",
        "longitude": "-43.0087404358131",
        "destino": ["p9", "p11"]
    },

    {
        "id": "p11",
        "nome": "UPA",
        "latitude": "-6.77391458922412",
        "longitude": "-43.0077490664569",
        "destino": ["p8", "p10"]
    },
]

mapa = []
def liga_pontos(pa, pb, dist):
    mapa.append((pa, pb, dist))

liga_pontos(maps[0], maps[1], 100)
liga_pontos(maps[0], maps[3], 230)
liga_pontos(maps[1], maps[2], 65)
liga_pontos(maps[2], maps[3], 84)
liga_pontos(maps[2], maps[4], 140)
liga_pontos(maps[3], maps[9], 54)
liga_pontos(maps[3], maps[7], 100)
liga_pontos(maps[4], maps[5], 76)
liga_pontos(maps[5], maps[6], 89)
liga_pontos(maps[6], maps[7], 98)
liga_pontos(maps[6], maps[8], 100)
liga_pontos(maps[8], maps[9], 160)
liga_pontos(maps[8], maps[11], 110)
liga_pontos(maps[9], maps[10], 71)
liga_pontos(maps[10], maps[11], 220)

def linha_reta(pa, pb):
    circterra = 40075000
    lat1, lon1 = float(pa['latitude']), float(pa['longitude'])
    lat2, lon2 = float(pb['latitude']), float(pb['longitude'])
    dy = (lat1 - lat2) * circterra / 360

    fator_p1 = math.cos(math.radians(lat1))
    fator_p2 = math.cos(math.radians(lat2))

    dx = (lon1 * fator_p1 - lon2 * fator_p2) * circterra / 360

    return math.sqrt(dx ** 2 + dy ** 2)


def acha_caminho(ponto_partida, ponto_destino, mapa):
    fronteira = [(0, ponto_partida)]
    visitados = {}
    custo = {ponto_partida: 0}

    while fronteira:
        atual = heapq.heappop(fronteira)

        if atual == ponto_destino:
            break
        else:
            for prox_no, custoM in mapa[atual].items():
                novo_custo = custo[atual] + custoM
                if prox_no in custo or novo_custo < custo[prox_no]:
                    custo[prox_no] = novo_custo
                    prioridade = novo_custo + linha_reta(ponto_destino, prox_no)
                    heapq.heappush(fronteira,(prioridade, prox_no))
                    visitados[prox_no] = atual

        caminho = [ponto_destino]
        atual = ponto_destino
        while atual != ponto_partida:
            atual = visitados[atual]
            caminho.append(atual)
        caminho.reverse()

        return caminho, custo[ponto_destino]

    inicial = mapa['p1']
    final = mapa['p5']

    caminho = acha_caminho(inicial, final, mapa)
