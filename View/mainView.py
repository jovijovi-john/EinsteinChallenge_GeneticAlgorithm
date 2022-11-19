from Controllers.SolucaoController import SolucaoController
from Controllers.PopulacaoController import PopulacaoController

from Models.Solucao import Solucao

import os

class View:
  def __init__(self):
    self.solucaoController = SolucaoController()
    self.populacaoController = PopulacaoController()
    self.terminou = False
    self.acharPontuacao(15)


  def mostrarPopulacaoInicial(self, pontuacao):
    self.clearTerminal()

    print(f"\033[1;35m{'===' * 10} \033[m")
    print("\033[1;33m POPULAÇÃO: \033[m".center(40))
    print(f"\033[1;35m{'===' * 10} \033[m\n")

    print(f"\033[1;32m{'===' * 10}\033[m")
    for solucao in self.populacaoInicial.individuos:
      if (solucao.pontuacao >= pontuacao):  
        print(f"pontuação: {solucao.pontuacao}")
        self.mostrarIndividuo(solucao)
        print(f"\033[1;32m{'===' * 10}\033[m")
        self.terminou = True
        break

  def mostrarIndividuo(self, solucao: Solucao):
    for index, pos in enumerate(solucao.individuo):
      print(f"  casa {index + 1} = {pos}")

  def clearTerminal(self):
    """
      Limpa o terminal, seja no windows ou linux
    """
    os.system('cls||clear')
  
  def acharPontuacao(self, pontuacao):
      while True:
        self.populacaoInicial = self.populacaoController.gerarPopulacao(1000)
        self.mostrarPopulacaoInicial(pontuacao)
        if self.terminou == True:
          break