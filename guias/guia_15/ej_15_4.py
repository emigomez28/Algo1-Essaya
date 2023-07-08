def posiciones_de_iter(texto, subcadena):
    res = []
    pos = 0
    while pos < len(texto): 
        pos_match = texto.find(subcadena, pos)
        if pos_match == -1:
            break
        pos = pos_match + 1
        res.append(pos_match)
    return res

def posiciones_de(texto, subcadena):
    res = []
    pos = 0
    _posiciones_de(texto, subcadena, pos, res)
    return res

def _posiciones_de(texto, subcadena, pos, res):
    pos_match = texto.find(subcadena, pos)
    if pos_match == -1:
        return
    res.append(pos_match)
    _posiciones_de(texto, subcadena, pos_match + 1, res)