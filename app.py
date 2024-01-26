from modelos.restaurante import Restaurante

restaurante_president = Restaurante('Prèsident', 'Francês')
restaurante_president.receber_avaliacao('Letícia', 8)
restaurante_president.receber_avaliacao('Caroline', 6)
restaurante_president.receber_avaliacao('Enio', 4)

def main():
  Restaurante.listar_restaurantes()
  
if __name__ =='__main__':
  main()