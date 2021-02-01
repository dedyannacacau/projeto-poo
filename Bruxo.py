from Personagem import Personagem


class Bruxo(Personagem):
    def hab_especial(array, array2):
        personagem_atacado = input(
            "\nColoque o nome do personagem que deseja congelar e remover da batalha: ")
        for personagem_atacado in array:
            array.remove(personagem_atacado)
        for personagem_atacado in array2:
            array.remove(personagem_atacado)
