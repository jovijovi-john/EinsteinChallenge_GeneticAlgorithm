class Solucao:
  def __init__(self, solucao, id_param):
    
    self.cores = []
    self.nacionalidades = [] 
    self.bebidas = []
    self.cigarro = []
    self.animais = []

    self.pontuacao = 0
    self.id = id_param

    self.individuo = solucao
    self.instanciarSolucao(solucao)

  def instanciarSolucao(self, solucao):
    for i in range(5):

      for j in range(5):
        if i == 0:
          self.cores.append(solucao[i][j])
        elif i == 1:
          self.nacionalidades.append(solucao[i][j])
        elif i == 2:
          self.bebidas.append(solucao[i][j])
        elif i == 3:
          self.cigarro.append(solucao[i][j])
        elif i == 4:
          self.animais.append(solucao[i][j])
  
  def incrementarPontuacao(self):
    self.pontuacao = self.pontuacao + 1
  
  def decrementarPontuacao(self):
    self.pontuacao = self.pontuacao - 1