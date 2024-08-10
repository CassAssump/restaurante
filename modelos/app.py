from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida("Suco de melancia", 5.0 , 'grande')
prato_paozinho = Prato("Paozinho", 2 ,'Melhor pão da cidade')


def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()
    