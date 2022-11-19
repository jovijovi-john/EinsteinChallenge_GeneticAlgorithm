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

    """
      ==========================================================
                        Verificação das cores
      ==========================================================
        
    """

    #o noruegues mora na primeira casa
    if (solucao.individuo[0][1] == codificacao["nacionalidades"]["norueguês"]):
      solucao.incrementarPontuacao()
    
    #o morador da casa central bebe leite
    if (solucao.individuo[2][2] == codificacao["bebidas"]["leite"]):
      solucao.incrementarPontuacao()

   
    for indexCasa, casa in enumerate(solucao.individuo):
      
      """
        ==========================================================
                        Verificação dos cigarros
        ==========================================================
      """
    
      # verificando se o a casa tem cigarro bluemaster
      if casa[3] == codificacao["cigarros"]["bluemaster"]:
        
        # O homem que fuma Bluemaster bebe cerveja. (12)
        # verificando se a a casa tem bebida cerveja
        if casa[2] == codificacao["bebidas"]["cerveja"]:
          solucao.incrementarPontuacao()


      # verificando se o a casa tem cigarro blends
      elif casa[3] == codificacao["cigarros"]["blends"]:
        
        #O homem que fuma Blends é vizinho do que bebe água (15)
        if indexCasa == 0:

          # Se o homem que fuma blends mora na primeira casa, então quem bebe água so pode morar na direita
          # verificando se a casa da direita tem bebida água
          if (solucao.individuo[indexCasa + 1][2] == codificacao["bebidas"]["água"]):
            solucao.incrementarPontuacao()

        elif indexCasa == 4:

          # Se o homem que fuma blends mora na ultima casa, então quem bebe água so pode morar na esquerda
          # verificando se a casa da esquerda tem bebida água
          if (solucao.individuo[indexCasa - 1][2] == codificacao["bebidas"]["água"]):
            solucao.incrementarPontuacao()
        
        else:

          # Se o homem que fuma blends não mora nem na primeira nem na ultima casa, 
          # então quem bebe água pode morar na esquerda ou na direita
          # verificando se a casa da esquerda ou da direita tem bebida água
          if (solucao.individuo[indexCasa - 1][2] == codificacao["bebidas"]["água"]) or (solucao.individuo[indexCasa + 1][2] == codificacao["bebidas"]["água"]):
            solucao.incrementarPontuacao()

      # verificando se o a casa tem cigarro prince
      elif casa[3] == codificacao["cigarros"]["prince"]:

        # O alemão fuma Prince (13)
        #verificando se a casa tem nacionalidade alemão
        if casa[1] == codificacao["nacionalidades"]["alemão"]:
          solucao.incrementarPontuacao()