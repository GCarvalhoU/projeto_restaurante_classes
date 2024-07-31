from Modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praca', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_mexicano.alternar_estado()
restaurante_praca.receber_avaliacao('Gustavo', 2)
restaurante_praca.receber_avaliacao('Natalia', 8)

def main():
    Restaurante.listar_restaurantes()
if __name__ == '__main__':
    main()