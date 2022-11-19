from random import shuffle
from Models.Solucao import Solucao
from Models.codificacao import codificacao

class SolucaoController:

  def __init__(self):
    pass

  def gerarSolucaoAleatoria(self):

    """
      Retorna uma solução aleatória
    """

    listaNums = [0, 1, 2, 3, 4]
    solucao = [[], [] , [], [], []]

    # laço para iterar os atributos
    for i in range(5):
      #gerando uma lista aleatoria de valores
      shuffle(listaNums)
      # laço para iterar sobre a  
      for j in range(5):
        solucao[j].append(listaNums[j])

    # Cada linha é uma casa, e cada coluna é um atributo
    solucao = Solucao(solucao)
    self.fitness(solucao)

    return solucao

  def fitness(self, solucao: Solucao):
 
    """
    [x][y]   => x é o numero da casa, e y é o numero do atributo

      0: cores
      1: nacionalidades
      2: bebidas
      3: cigarros
      4: animais
    """

    #o noruegues mora na primeira casa
    if (solucao.individuo[0][1] == codificacao["nacionalidades"]["norueguês"]):
      solucao.incrementarPontuacao()
    
    #o morador da casa central bebe leite
    if (solucao.individuo[2][2] == codificacao["bebidas"]["leite"]):
      solucao.incrementarPontuacao()

   
    for indexCasa, casa in enumerate(solucao.individuo):
      
      # O norueguês vive ao lado da casa azul.
      # verificando se a casa atual é a do norueguês
      if casa[1] == codificacao["nacionalidades"]["norueguês"]:
        if (indexCasa == 0):
          # Se o noruegues mora na primeira casa, entao deve olhar a casa à direita
          if solucao.individuo[indexCasa + 1][0] == codificacao["cores"]["azul"]:
            solucao.incrementarPontuacao()
        elif(indexCasa == 4):
          # Se o noruegues mora na ultima casa, entao deve olhar a casa à esquerda
          if solucao.individuo[indexCasa - 1][0] == codificacao["cores"]["azul"]:
            solucao.incrementarPontuacao()
        else:
          """
            como o norueguês não está na primeira nem na ultima casa,
            devemos verificar se a casa à esquerda ou à direita é azul
          """
          if (solucao.individuo[indexCasa+1][0] == codificacao["cores"]["azul"]) or (solucao.individuo[indexCasa-1][0] == codificacao["cores"]["azul"]):
              solucao.incrementarPontuacao()

      # a casa verde fica à esquerda da casa branca
      # verificando se a casa atual é branca
      if casa[0] == codificacao["cores"]["branca"]:
        # a casa branca nao pode ser a primeira, pois nao poderia ter uma casa ao lado esquerdo
        if indexCasa != 0:
          # verificando se a casa à esquerda é verde
          if solucao.individuo[indexCasa - 1][0] ==  codificacao["cores"]["verde"]:
            solucao.incrementarPontuacao()

      