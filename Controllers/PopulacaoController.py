from Models.Populacao import Populacao
from Controllers.SolucaoController import SolucaoController

class PopulacaoController:
  
  def __init__(self):
    self.solucaoController = SolucaoController()
    pass
  
  def gerarPopulacao(self, tamanhoPop):
    
    populacao = []

    for i in range(tamanhoPop):
      individuo = self.solucaoController.gerarSolucaoAleatoria()
      populacao.append(individuo)

    populacao = Populacao(populacao)

    return populacao
