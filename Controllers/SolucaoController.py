from random import shuffle
from Models.Solucao import Solucao
from Models.codificacao import codificacao

class SolucaoController:

  def __init__(self):
    pass

  def gerarSolucaoAleatoria(self, id_sol):

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
    solucao = Solucao(solucao, id_sol)
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

    

    #o noruegues mora na primeira casa (9)
    if (solucao.individuo[0][1] == codificacao["nacionalidades"]["norueguês"]):
      solucao.incrementarPontuacao()
    
    #o morador da casa central bebe leite (8)
    if (solucao.individuo[2][2] == codificacao["bebidas"]["leite"]):
      solucao.incrementarPontuacao()

   
    for indexCasa, casa in enumerate(solucao.individuo):

      """
      ==========================================================
                        Verificação das cores
      ==========================================================
        
    """

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

      """
        ==========================================================
                        Verificação dos cigarros
        ==========================================================
      """
    
      # verificando se o a casa tem cigarro blue master
      if casa[3] == codificacao["cigarros"]["blue master"]:
        
        # O homem que fuma Bluemaster bebe cerveja. (12)
        # verificando se a a casa tem bebida cerveja
        if casa[2] == codificacao["bebidas"]["cerveja"]:
          solucao.incrementarPontuacao()

      # verificando se o a casa tem cigarro blends
      elif casa[3] == codificacao["cigarros"]["blends"]:
        
        #O homem que fuma Blends é vizinho do que bebe água (15)
        #O homem que fuma Blends mora ao lado do que tem gatos (10)
        if indexCasa == 0:

          # Se o homem que fuma blends mora na primeira casa, então quem bebe água so pode morar na direita
          # verificando se a casa da direita tem bebida água
          if (solucao.individuo[indexCasa + 1][2] == codificacao["bebidas"]["água"]):
            solucao.incrementarPontuacao()

         
          # Se o homem que fuma blends mora na primeira casa, então quem tem gato so pode morar na direita
          # verificando se a casa da direita tem animais gatos 
          if (solucao.individuo[indexCasa + 1][4] == codificacao["animais"]["gatos"]):
            solucao.incrementarPontuacao()

        elif indexCasa == 4:

          # Se o homem que fuma blends mora na ultima casa, então quem bebe água so pode morar na esquerda
          # verificando se a casa da esquerda tem bebida água
          if (solucao.individuo[indexCasa - 1][2] == codificacao["bebidas"]["água"]):
            solucao.incrementarPontuacao()

          
          # Se o homem que fuma blends mora na ultima casa, então quem tem gatos so pode morar na esquerda
          # verificando se a casa da esquerda tem animais gatos 
          if (solucao.individuo[indexCasa - 1][4] == codificacao["animais"]["gatos"]):
            solucao.incrementarPontuacao()

        else:

          # Se o homem que fuma blends não mora nem na primeira nem na ultima casa, 
          # então quem bebe água pode morar na esquerda ou na direita
          # verificando se a casa da esquerda ou da direita tem bebida água
          if (solucao.individuo[indexCasa - 1][2] == codificacao["bebidas"]["água"]) or (solucao.individuo[indexCasa + 1][2] == codificacao["bebidas"]["água"]):
            solucao.incrementarPontuacao()

          # Se o homem que fuma blends não mora nem na primeira nem na ultima casa, 
          # então quem bebe tem gatos pode morar na esquerda ou na direita
          if (solucao.individuo[indexCasa - 1][4] == codificacao["animais"]["gatos"]) or (solucao.individuo[indexCasa + 1][4] == codificacao["animais"]["gatos"]):
            solucao.incrementarPontuacao()

      # verificando se o a casa tem cigarro prince
      elif casa[3] == codificacao["cigarros"]["prince"]:

        # O alemão fuma Prince (13)
        #verificando se a casa tem nacionalidade alemão
        if casa[1] == codificacao["nacionalidades"]["alemão"]:
          solucao.incrementarPontuacao()

      # verificando se o a casa tem cigarro pall mall
      elif casa[3] == codificacao["cigarros"]["pall mall"]:

        # a pessoa que fuma Pall Mall cria pássaros (6)
        # verificando se a casa tem passáros
        if casa[4] == codificacao["animais"]["pássaros"]:
          solucao.incrementarPontuacao()

      # verificando se o a casa tem cigarro dunhill
      elif casa[3] == codificacao["cigarros"]["dunhill"]:

        # O homem que cria cavalos mora ao lado do que fuma Dunhill (11)
        # Se a primeira casa for a que tem cigarro dunhill
        if (indexCasa == 0):
          
          # Se a casa primeira casa tem cigarro dunhill, então a casa da direita deve ter animal cavalo
          if (solucao.individuo[indexCasa + 1][4] == codificacao["animais"]["cavalos"]):
            solucao.incrementarPontuacao()

        # Se casa  que tem cigarro dunhill for a ultima
        elif (indexCasa == 4):
          
          # Se casa  que tem cigarro dunhill for a ultima, então a casa da esquerda deve ter animal cavalo
          if (solucao.individuo[indexCasa - 1][4] == codificacao["animais"]["cavalos"]):
            solucao.incrementarPontuacao()
        
        else :
          
          # Se o homem que fuma dunhill não mora nem na primeira nem na ultima casa, 
          # então quem tem cavalos pode morar na esquerda ou na direita
          if (solucao.individuo[indexCasa - 1][4] == codificacao["animais"]["cavalos"]) or (solucao.individuo[indexCasa + 1][4] == codificacao["animais"]["cavalos"]):
            solucao.incrementarPontuacao()

      
      """
        ==========================================================
                        Verificação das nacionalidades
        ==========================================================
      """

      # verificando se a casa tem nacionalidade sueco
      if (casa[1] == codificacao["nacionalidades"]["sueco"]):

        # O sueco tem cachorros (2)
        # verificando se na casa tem animal cachorro
        if (casa[4] == codificacao["animais"]["cachorros"]):
          solucao.incrementarPontuacao()

      # verificando se a casa tem nacionalidade dinamarquês
      elif (casa[1] == codificacao["nacionalidades"]["dinamarquês"]):
        
        # O dinamarquês bebe chá (3)
        # verificando se na casa tem bebida chá
        if (casa[2] == codificacao["bebidas"]["chá"]):
          solucao.incrementarPontuacao()
