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
      
      # verificando se a casa atual é verde
      if casa[0] == codificacao["cores"]["verde"]:
       
        # a casa verde fica à esquerda da casa branca (4)
        # a casa verde nao pode ser a ultima, pois nao poderia ter uma casa ao lado direito pra ser a branca
        if indexCasa != 4:
          # verificando se a casa à esquerda é verde
          if solucao.individuo[indexCasa + 1][0] ==  codificacao["cores"]["branca"]:
            solucao.incrementarPontuacao()

        # O morador da casa verde bebe café(5)
        # verificando se a bebida da casa é café
        if casa[2] == codificacao["bebidas"]["café"]:
            solucao.incrementarPontuacao()

      # verificando se a casa atual é vermelha
      elif casa[0] == codificacao["cores"]["vermelha"]:
        
        # o inglês mora na casa vermelha (1)
        # verificando se a nacionalidade da casa é inglês
        if casa[1] == codificacao["nacionalidades"]["inglês"]:
            solucao.incrementarPontuacao()

      # verificando se a casa atual é amarela
      elif casa[0] == codificacao["cores"]["amarela"]:
        
        # O morador da casa amarela fuma Dunhill (7)
        if casa[3] == codificacao["cigarros"]["dunhill"]:
            solucao.incrementarPontuacao()

        pass
   
      # verificando se a casa atual é azul
      elif casa[0] == codificacao["cores"]["azul"]:
        
        # O norueguês vive ao lado da casa azul (14)
        
        # se a casa azul for a primeira
        if indexCasa == 0:
          # Se a casa azul for a primeira então a casa da direita deve ter nacionalidade norueguês
          if (solucao.individuo[indexCasa + 1][1] == codificacao["nacionalidades"]["norueguês"]):
            solucao.incrementarPontuacao()
        elif indexCasa == 4:
          # Se a casa azul for a última então a casa da esquerda deve ter nacionalidade norueguês
          if (solucao.individuo[indexCasa - 1][1] == codificacao["nacionalidades"]["norueguês"]):
            solucao.incrementarPontuacao()
        else:

          """
            Se a casa azul não é a primeira nem a última 
            então o norueguês pode estar tanto na esquerda quanto na direita 
          """
          if (solucao.individuo[indexCasa - 1][1] == codificacao["nacionalidades"]["norueguês"]) or (solucao.individuo[indexCasa + 1][1] == codificacao["nacionalidades"]["norueguês"]):
            solucao.incrementarPontuacao()
          
        pass
        
      
      # O homem que fuma Bluemaster bebe cerveja.
      # verificando se o a casa tem cigarro bluemaster
      if casa[3] == codificacao["cigarros"]["bluemaster"]:
        
        # verificando se a a casa tem bebida cerveja
        if casa[2] == codificacao["bebidas"]["cerveja"]:
          solucao.incrementarPontuacao()