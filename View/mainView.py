from Controllers.SolucaoController import SolucaoController
from Controllers.PopulacaoController import PopulacaoController

from Models.Solucao import Solucao
from Models.codificacao_invertida import codificao_invertida, codificacao

import os

class View:
  def __init__(self):
    self.solucaoController = SolucaoController()
    self.populacaoController = PopulacaoController()
    self.geracoes = 10000

    self.iniciarGeracoes()
    # self.loopGeracaoInicial()

  def iniciarGeracoes(self):
    #Começa o processo de busca pela solução até a geração self.geracao
    self.clearTerminal()

    ultimasPontuacoes = []

    for i in range(self.geracoes):
      
      if i == 0:
        self.populacaoInicial = self.populacaoController.gerarPopulacaoInicial(100000)
        populacao = self.populacaoInicial
    
      # self.mostrarPopulacao(populacao)
      melhor = self.populacaoController.melhorIndividuo(populacao)
      
      self.populacaoController.gerarMutacaoPopulacao(populacao, 3)

      self.mostrarMelhorIndividuo(melhor, i)

      if len(ultimasPontuacoes) < 5:
          ultimasPontuacoes.append(melhor.pontuacao)
      else:
        # preencheu as 5 ultimas pontuacoes
        mutacaoGeral = True

        for pontuacao in ultimasPontuacoes:
          # se a pontuacao atual for diferente das 5 ultimas
          if pontuacao !=  melhor.pontuacao:
            mutacaoGeral = False
        
        if mutacaoGeral == True:
          print("Mutação nos 25% piores individuos")
          fracao = populacao.tamanhoPop // 4
          final = populacao.tamanhoPop

          for i in range(fracao, final):
            individuo = populacao.individuos[i]
            self.populacaoController.gerarMutacao(individuo)

          self.populacaoController.ordenarPopulacao(populacao)        

        ultimasPontuacoes.pop(0)
        ultimasPontuacoes.append(melhor.pontuacao)

      print(f"ultimas pontuações: {ultimasPontuacoes}")
        
      if melhor.pontuacao == 15:
        break
      
      del melhor.individuo[:]
      del melhor

      sobreviventes = self.populacaoController.sobrevivencia25_25(populacao)
      recombinacao = self.populacaoController.recombinacao(sobreviventes)
      
      del sobreviventes[:]
      del sobreviventes

      sobreviventes = self.populacaoController.sobrevivencia50(populacao)

      del populacao.individuos[:]
      del populacao
      
      populacao = self.populacaoController.novaGeracao(sobreviventes, recombinacao)
      del recombinacao[:]
      del recombinacao

  def loopGeracaoInicial(self):
    """
      Laço que gera aleatoriamente individuos até encontrar a solução ideal
    """
    
    i = 0

    while True:
      self.populacao = self.populacaoController.gerarPopulacaoInicial(100)
      melhor = self.populacaoController.melhorIndividuo(self.populacao)
      self.mostrarIndividuo(melhor)
        
      print(f"A pontuação do melhor indivíduo da geração {i} é {melhor.pontuacao}")
      i = i + 1
      
      if melhor.pontuacao == 15:
        self.mostrarIndividuo(melhor)
        break
        
      del self.populacao.individuos[:]
      del self.populacao

  def mostrarPopulacao(self, populacao):
    """
      Função que mostra a população passada por parâmetro
    """

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
    """
      Mostra o individuo em forma de matriz, onde as colunas sao os atributos e as linhas são as casas
    """
    for index, pos in enumerate(solucao.individuo):
      print(f"{' ' * 2} casa {index + 1} = {pos}")

  def mostrarIndividuoText(self, solucao: Solucao):
    # Mostra a matriz de solução do individuo de maneira traduzida, ao invés de usar os números
    attributos = list(codificacao.keys())
    print('--' * 45)
    print("           ", end="")

    for att in attributos:
      print(f"{att}".center(14), end=" ")
    
    print('\n')

    for i, casa in enumerate(solucao.individuo):
      # iterando sobre as casas
      print(f"   casa {i}: ", end="")

      for j, atributo in enumerate(casa):
        # iterando sobre os atributos de cada casa
        if j == 0:
          # mostrando o atributo de cor de forma colorida
          if codificao_invertida[j][atributo] == "vermelha":
            print("\033[1;31m", end="")
          elif codificao_invertida[j][atributo] == "branca":
            print("\033[1m", end="")
          elif codificao_invertida[j][atributo] == "verde":
            print("\033[1;32m", end="")
          elif codificao_invertida[j][atributo] == "amarela":
            print("\033[1;33m", end="")
          elif codificao_invertida[j][atributo] == "azul":
            print("\033[1;36m", end="")
        print(f"{codificao_invertida[j][atributo]}".center(14), end=" ")
        print("\033[m", end="")
      print()
    
    print('--' * 45)

  def clearTerminal(self):
    """
      Limpa o terminal, seja no windows ou linux
    """
    os.system('cls||clear')
  
  def mostrarMelhorIndividuo(self, melhorIndividuo: Solucao, numGeracao: int):
    print(f"\033[1;32m{'==' * 45}\033[m")
    
    print(f"\n\033[3;35mA pontuação do melhor indivíduo da \033[1;36mgeração {numGeracao}\033[m \033[3;35mé \033[1;36m{melhorIndividuo.pontuacao}\033[m\n")
    self.mostrarIndividuo(melhorIndividuo)
    self.mostrarIndividuoText(melhorIndividuo)