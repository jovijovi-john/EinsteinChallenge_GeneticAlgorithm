from Models.Populacao import Populacao
from Models.Solucao import Solucao
from Controllers.SolucaoController import SolucaoController
from random import shuffle

class PopulacaoController:
  
  def __init__(self):
    self.solucaoController = SolucaoController()
    pass
  
  def gerarPopulacaoInicial(self, tamanhoPop):
    
    individuos = []

    for i in range(tamanhoPop):
      individuo = self.solucaoController.gerarSolucaoAleatoria(i)
      individuos.append(individuo)
      del individuo

    populacao = Populacao(individuos, 0)
    del individuos

    self.ordenarPopulacao(populacao)

    return populacao

  def melhorIndividuo(self, populacao: Populacao):
    solucao = populacao.individuos[0]
    individuos = solucao.individuo.copy()

    melhor = Solucao(individuos, solucao.id)
    melhor.pontuacao = solucao.pontuacao

    return melhor

  def sobrevivencia25_25(self, populacao: Populacao, taxa: int = 50):
    """ 
      pega os 25% melhores e os 25% piores
    """
    tam = populacao.tamanhoPop
    tam_return = (tam * taxa) // 200

    sobreviventes = list()
    for i in range(tam_return):
      sobreviventes.append(populacao.individuos[i])

    populacao.individuos.reverse()
    for i in range(tam_return):
      sobreviventes.append(populacao.individuos[i])
    
    populacao.individuos.reverse()

    return sobreviventes
  
  def sobrevivencia50(self, populacao: Populacao, taxa: int = 50):
    """
      retorna os 50% melhores
    """
    tam = populacao.tamanhoPop
    tam_return = (tam * taxa) // 100

    sobreviventes = list()
    for i in range(tam_return):
      sobreviventes.append(populacao.individuos[i])

    return sobreviventes

  def recombinacao(self, sobreviventes):
    """    
      pai: [a, b, c , d, e]
      mae: [f, g, h, i, j]

      filho 1: [a, b, c, i, j]
      filho 2: [f, g, h, d, e]
    """
    recombinacao = []
    sobreviventes_shuffle = sobreviventes.copy()
    
    # embaralhando a lista de sobreviventes
    shuffle(sobreviventes_shuffle)

    for i in range(0, len(sobreviventes), 2):
      
      sobrevivente1 = sobreviventes_shuffle[i].individuo.copy()
      sobrevivente2 = sobreviventes_shuffle[i + 1].individuo.copy()

      id_sobrevivente1 = sobreviventes_shuffle[i].id
      id_sobrevivente2 = sobreviventes_shuffle[i + 1].id

      filho1 = []
      filho2 = []

      for j in range(5): 
        
        casa_f1 = []
        casa_f2 = []

        for k in range(5):
          
          if k < 3:
            casa_f1.append(sobrevivente1[j][k])
            casa_f2.append(sobrevivente2[j][k])
          else:
            casa_f1.append(sobrevivente2[j][k])
            casa_f2.append(sobrevivente1[j][k])

        filho1.append(casa_f1)
        filho2.append(casa_f2)
      
      del casa_f1
      del casa_f2
      
      solucao1 = Solucao(filho1, 0)
      solucao2 = Solucao(filho2, 0)

      del filho1
      del filho2

      self.solucaoController.fitness(solucao1)
      self.solucaoController.fitness(solucao2)

      recombinacao.append(solucao1)
      recombinacao.append(solucao2)

      del sobrevivente1[:]
      del sobrevivente1
      
      del sobrevivente2[:]
      del sobrevivente2

    del sobreviventes_shuffle[:]
    del sobreviventes_shuffle

    del sobreviventes[:]
    del sobreviventes
    return recombinacao

  def novaGeracao(self, sobreviventes, recombinacao):
    
    individuos = []
    
    for sobrevivente in sobreviventes:
      individuos.append(sobrevivente)

    for filho in recombinacao:
      individuos.append(filho)

    populacao = Populacao(individuos, 1)
    self.ordenarPopulacao(populacao)
    del individuos
    
    return populacao

  def ordenarPopulacao(self, populacao: Populacao):
    # ordenando decrescentemente os individuos por pontuação
    populacao.individuos.sort(key=lambda x: x.pontuacao, reverse=True) 