import json


def getNeighborhoodDict():
    with open('bairros.json') as f:
        neighborhoodDict = json.load(f)

        bairros_dict = {}
    for bairro in neighborhoodDict:
        bairros_dict[bairro['CODBAIRRO']] = bairro['NOME']

    return bairros_dict
