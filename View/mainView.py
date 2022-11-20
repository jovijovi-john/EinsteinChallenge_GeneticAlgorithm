from Controllers.SolucaoController import SolucaoController
from Controllers.PopulacaoController import PopulacaoController

from Models.Solucao import Solucao

import os

class View:
  def __init__(self):
    self.solucaoController = SolucaoController()
    self.populacaoController = PopulacaoController()
    self.geracoes = 30

    self.iniciarGeracoes()

  def iniciarGeracoes(self):

    for i in range(self.geracoes):
      
      if i == 0:
        self.populacaoInicial = self.populacaoController.gerarPopulacaoInicial(1000000)
        populacao = self.populacaoInicial
    
      # self.mostrarPopulacao(populacao)
      melhor = self.populacaoController.melhorIndividuo(populacao)
        
      print(f"A pontuação do melhor indivíduo da geração {i} é {melhor.pontuacao}")

      if melhor.pontuacao == 15:
        self.mostrarIndividuo(melhor)
        break

      sobreviventes = self.populacaoController.sobrevivencia25_25(populacao)
      recombinacao = self.populacaoController.recombinacao(sobreviventes)
      sobreviventes = self.populacaoController.sobrevivencia50(populacao)

      populacao = self.populacaoController.novaGeracao(sobreviventes, recombinacao)

  def mostrarPopulacao(self, populacao):
    self.clearTerminal()

    print(f"\033[1;35m{'===' * 10} \033[m")
    print("\033[1;33m POPULAÇÃO: \033[m".center(40))
    print(f"\033[1;35m{'===' * 10} \033[m\n")

    print(f"\033[1;32m{'===' * 10}\033[m")
    for solucao in populacao.individuos:
      print(f"pontuação: \033[1;33m{solucao.pontuacao}\033[m\n")

      self.mostrarIndividuo(solucao)
      print(f"\033[1;32m{'===' * 10}\033[m")

  def mostrarIndividuo(self, solucao: Solucao):
    for index, pos in enumerate(solucao.individuo):
      print(f"{' ' * 2} casa {index + 1} = {pos}")

  def clearTerminal(self):
    """
      Limpa o terminal, seja no windows ou linux
    """
    os.system('cls||clear')
  
  def acharPontuacao(self, pontuacao):
      while True:
        self.populacaoInicial = self.populacaoController.gerarPopulacaoInicial(1000)
        self.mostrarPopulacaoInicial(pontuacao)
        if self.terminou == True:
          break