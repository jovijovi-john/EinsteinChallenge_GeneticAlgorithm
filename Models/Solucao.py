class Solucao:
  def __init__(self, solucao):
    
    self.pontuacao = 0

    self.individuo = solucao

  
  def incrementarPontuacao(self):
    self.pontuacao = self.pontuacao + 1
  
  def decrementarPontuacao(self):
    self.pontuacao = self.pontuacao - 1

  def zerarPontuacao(self):
    self.pontuacao = 0