class Solucao:
  def __init__(self, solucao, id_param):
    
    self.pontuacao = 0
    self.id = id_param

    self.individuo = solucao

  
  def incrementarPontuacao(self):
    self.pontuacao = self.pontuacao + 1
  
  def decrementarPontuacao(self):
    self.pontuacao = self.pontuacao - 1