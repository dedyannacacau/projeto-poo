from Personagem import Personagem


class Arqueiro(Personagem):
    def hab_especial(array, array2, personagem_da_vez):
        personagem_atacado = input(
            "\nColoque o nome do personagem que deseja atirar uma flecha flamejante com o dano 50 vezes maior que o normal: ")
        for personagem_atacado in array:
            personagem_atacado.pontos_vidas = personagem_atacado.pontos_vidas - \
                50 * personagem_da_vez.pontos_ataque
