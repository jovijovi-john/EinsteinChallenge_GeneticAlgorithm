from Models.Populacao import Populacao
from Models.Solucao import Solucao
from Controllers.SolucaoController import SolucaoController
from random import shuffle

class PopulacaoController:
  
  def __init__(self):
    self.solucaoController = SolucaoController()
    pass
  
  def gerarPopulacaoInicial(self, tamanhoPop):
    
    populacao = []

    for i in range(tamanhoPop):
      individuo = self.solucaoController.gerarSolucaoAleatoria(i)
      populacao.append(individuo)

    populacao = Populacao(populacao, 0)

    self.ordenarPopulacao(populacao)

    return populacao

  def melhorIndividuo(self, populacao: Populacao):
    return populacao.individuos[0]

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
        attr_sobre1 = sobrevivente1[j].copy()
        attr_sobre2 = sobrevivente2[j].copy()

        if j < 3:
          filho1.append(attr_sobre1)
          filho2.append(attr_sobre2)
        else: 
          filho1.append(attr_sobre2)
          filho2.append(attr_sobre1)
      
      solucao1 = Solucao(filho1, f"{id_sobrevivente1}_{id_sobrevivente2}")
      solucao2 = Solucao(filho2, f"{id_sobrevivente2}_{id_sobrevivente1}")

      self.solucaoController.fitness(solucao1)
      self.solucaoController.fitness(solucao2)

      recombinacao.append(solucao1)
      recombinacao.append(solucao2)
      
    return recombinacao

  def novaGeracao(self, sobreviventes, recombinacao):
    
    individuos = []
    
    for sobrevivente in sobreviventes:
      individuos.append(sobrevivente)

    for filho in recombinacao:
      individuos.append(filho)

    populacao = Populacao(individuos, 1)
    self.ordenarPopulacao(populacao)
    
    return populacao

  def ordenarPopulacao(self, populacao: Populacao):
    # ordenando decrescentemente os individuos por pontuação
    populacao.individuos.sort(key=lambda x: x.pontuacao, reverse=True) 