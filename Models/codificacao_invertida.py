from Models.codificacao import codificacao

codificao_invertida = list(codificacao.values())

for index, atributo in enumerate(codificao_invertida):
    codificao_invertida[index] = (list(atributo))
    