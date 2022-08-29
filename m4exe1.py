# Classifique dois objetos materiais e dois abstratos. 
# Insira, no mínimo, três métodos e três atributos para cada.

from abc import ABC, abstractclassmethod, abstractmethod


print(' ')
print('-'*85)
print('Exemplo de classes materiais, com 3 métodos e 3 atributos:')


class Carro:
   
   def __init__(self, fabricante, modelo:str, ano:int):
      self.fabricante = fabricante
      self.modelo = modelo
      self.ano = ano

   print(' ')
   def Ligar(self):
      print('Funcionamento na chave ou remota...')
   def Acelerar(self):
      print('Acelera por meio do pedal ou controle de cruzeiro..')
   def MostrarInformaçõesdoPainel(self):
      print('Mantenha distância de segurança, pressão dos pneus estão ok...')


class Supermercado:

   def __init__(self, produto, funcionarios, preco):
      self.produto = produto
      self.funcionarios = funcionarios
      self.preco = preco

   def Comprar(self):
      print('Indo ao mercado fazer compras...')
   def Cadastrar(self):
      print('Cadastrando novos funcionários do mercado..')
   def Pagar(self):
      print('Pagando a fatura e aguardando o troco...')


veiculo1 = Carro('Jeep', 'Compass', '2022')
veiculo1.Ligar()
veiculo1.Acelerar()
veiculo1.MostrarInformaçõesdoPainel()
print(' ')

p1 = Supermercado('biscoitos', 'Luiz', '135,00')
p1.Comprar()
p1.Cadastrar()
p1.Pagar()

print(' ')
print('-'*85)
print('Exemplo de classes abstratas com no mínimo, três métodos e três atributos para cada.')
print(' ')

class Viagem:
   
   def __init__(self, empresa, cidade, preco: str):
      self.empresa = empresa
      self.cidade = cidade
      self.preco = preco

   @abstractmethod
   def Planejar(self, cidade, preco: str) -> None:
      print(self.cidade, self.preco)

   @abstractmethod
   def VisitarLugares(self) -> None:
      pass

   @abstractmethod
   def Jogar(self) -> None:
      pass


class VoltaMundo(Viagem):

   def Passeio(self, cidade, empresa) -> None:
      print(self.cidade, self.empresa)

   def VisitarLugares(self) -> None:
      print('Irei a teatros, cinema e ao shopping!')

   def Jogar(self) -> None:
      print('Jogarei futebol em Barcelona e um pouco de poker')
    
v1 = VoltaMundo('TAM', 'Espanha', '5.000 euros')
v1.Passeio('a', 'b')
v1.Planejar('Barcelona', '3 euros')
v1.VisitarLugares()
v1.Jogar()
