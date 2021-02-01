from Personagem import Personagem


class Cavaleiro(Personagem):
    def hab_especial(array, array2):
        #ataque duplo que ignora a defesa e multiplica por 5!
        personagem_atacado1 = input("\nSelecione 2 personagens para atacar: ")
        if len(array) > 2:
            personagem_atacado2 = input()
        for personagem_atacado1 in array:
            personagem_atacado1.pontos_vidas =- 5*personagem_da_vez.pontos_ataque
        for personagem_atacado2 in array:
            personagem_atacado2.pontos_vidas =- 5*personagem_da_vez.pontos_ataque



