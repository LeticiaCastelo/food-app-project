from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_president = Restaurante('Prèsident', 'Francês')
bebida_suco = Bebida('Acerola', 5.0, 'Grande')
bebida_suco.aplicar_desconto()
prato_risoto = Prato('Risoto', 46.0, 'Risoto de Camarão')
prato_risoto.aplicar_desconto()
sobremesa_sorvete = Sobremesa('Sorvete de Pistache', 17.0, 'Sorvete', 'Grande')
sobremesa_sorvete.aplicar_desconto()
restaurante_president.adicionar_no_cardapio(bebida_suco)
restaurante_president.adicionar_no_cardapio(prato_risoto)
restaurante_president.adicionar_no_cardapio(sobremesa_sorvete)

def main():
  restaurante_president.exibir_cardapio
  
if __name__ =='__main__':
  main()
  