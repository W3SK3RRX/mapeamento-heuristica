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

'''mapa = []
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
'''
def a_estrela(inicio, objetivo, grafo):
    # Define a função heurística, que estima a distância restante
    # do ponto atual até o objetivo.
    def heuristica(a, b):
        circterra = 40075000
        lat1 = float(a['latitude'])
        lon1 = float(a['longitude'])
        lat2 = float(b['latitude'])
        lon2 = float(b['longitude'])

        dy = (lat1 - lat2) * circterra / 360

        fator_p1 = math.cos(math.radians(lat1))
        fator_p2 = math.cos(math.radians(lat2))

        dx = (lon1 * fator_p1 - lon2 * fator_p2) * circterra / 360

        return math.sqrt(dx ** 2 + dy ** 2)

    # Define o nó inicial e o nó final
    no_inicio = {'id': inicio, 'g': 0, 'f': 0}
    no_objetivo = {'id': objetivo, 'g': float('inf'), 'f': float('inf')}

    # Define os nós abertos e fechados
    abertos = [no_inicio]
    fechados = []

    # Enquanto houver nós abertos
    while abertos:
        # Seleciona o nó com o menor custo f
        atual = min(abertos, key=lambda node: node['f'])

        # Se o nó atual for o objetivo, retorna o caminho
        if atual['id'] == no_objetivo['id']:
            caminho = []
            while atual:
                caminho.append(atual['id'])
                atual = atual.get('parent')
            return caminho[::-1]

        # Move o nó atual da lista de abertos para a lista de fechados
        abertos.remove(atual)
        fechados.append(atual)

        # Para cada vizinho do nó atual
        for vizinho_id in grafo[int(atual['id'])]['destino']:
            vizinho = next((node for node in abertos + fechados if node['id'] == vizinho_id), None)
            if not vizinho:
                vizinho = {'id': str(vizinho_id), 'g': float('inf'), 'f': float('inf')}

            # Calcula o custo g até o vizinho
            pontuacao_g = atual['g'] + grafo[atual['id']]['destino'][vizinho_id]['distancia']

            # Se o custo g for menor do que o custo g anterior, atualiza os valores
            if pontuacao_g < vizinho['g']:
                vizinho['parent'] = atual
                vizinho['g'] = pontuacao_g
                vizinho['f'] = vizinho['g'] + heuristica(grafo[vizinho['id']], grafo[no_objetivo['id']])

                # Se o vizinho não estiver na lista de abertos, adiciona-o
                if vizinho not in abertos:
                    abertos.append(vizinho)

    # Se não encontrar o caminho, retorna None
    return None


inicio = input("Informe o ponto de partida: ")
destino = input("Informe o ponto de destino: ")
caminho = a_estrela(inicio, destino, maps)
print("Caminho mais curto: ", caminho)
