class Avaliacao:
    def __init__(self,cliente, nota):
        self._cliente = cliente
        self._nota = nota
        while self._nota > 5 or self._nota < 1:
            print (f'As notas devem ser entre 1 e 5')
            self._nota = int(input(f'Digite uma nova avaliação para {self._cliente}: '))
