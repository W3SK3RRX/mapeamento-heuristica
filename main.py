import math
maps = [
    {
        "id": "p1",
        "nome": "Helton Autopeças",
        "latitude": "-6.77294579529729",
        "longitude": "-43.0107411682096",
        "destino": ["p2", "p4"]
    },

    {
        "id": "p2",
        "nome": "Panificadora Rosa Branca",
        "latitude": "-6.77368720118917",
        "longitude": "-43.009929353215",
        "destino": ["p1", "p3"]
    },

    {
        "id": "p3",
        "nome": "Hotel Rio Parnaíba",
        "latitude": "6.77398240346339",
        "longitude": "-43.009630217428",
        "destino": ["p2", "p4", "p5"]
    },

    {
        "id": "p4",
        "nome": "São Jorge Supermercado",
        "latitude": "-6.77370556073959",
        "longitude": "-43.0093296946812",
        "destino": ["p1", "p3", "p8", "p10"]
    },

    {
        "id": "p5",
        "nome": "Espaço Cidadania",
        "latitude": "-6.77490653516264",
        "longitude": "-43.0085988440702",
        "destino": ["p3", "p6"]
    },

    {
        "id": "p6",
        "nome": "Drogaria Brasil",
        "latitude": "-6.7752754666622",
        "longitude": "-43.0081668278133",
        "destino": ["p5", "p7"]
    },

    {
        "id": "p7",
        "nome": "Escola Magnolia Miranda",
        "latitude": "-6.77489724512599",
        "longitude": "-43.0078681685904",
        "destino": ["p6", "p8", "p9"]
    },

    {
        "id": "p8",
        "nome": "Armazem Coração de Jesus",
        "latitude": "-6.7743366163586",
        "longitude": "-43.0086116801161",
        "destino": ["p7", "p4"]
    },

    {
        "id": "p9",
        "nome": "Hotel Bocaina",
        "latitude": "-6.77439262652405",
        "longitude": "-43.0075901407694",
        "destino": ["p7", "p10", "p12"]
    },

    {
        "id": "p10",
        "nome": "Mrm Cabelos",
        "latitude": "-6.77344127141917",
        "longitude": "-43.0091110298527",
        "destino": ["p4", "p9", "p11"]
    },

    {
        "id": "p11",
        "nome": "Mercadinho 2 Irmãos",
        "latitude": "-6.77302627188422",
        "longitude": "-43.0087404358131",
        "destino": ["p10", "p12"]
    },

    {
        "id": "p12",
        "nome": "UPA",
        "latitude": "-6.77391458922412",
        "longitude": "-43.0077490664569",
        "destino": ["p9", "p11"]
    },
]

def liga_pontos(pa,pb,dist):
    pass

#liga_pontos(maps[0],maps[1],100)

def linha_reta(pa,pb):
    circterra = 40075000
    dy = (pa['latitude'] - pb['latitude']) * circterra/360

    fator_p1 = math.cos(math.radians(pa['latitude']))
    fator_p2 = math.cos(math.radians(pb['latitude']))

    dx = (pa['longitude'] * fator_p1 - pb['longitude'] * fator_p2) * circterra/360


