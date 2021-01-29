from Funcionalidades import Funcionalidade

class Batalha(Funcionalidade):
    def __init__(self, atacar, defender, powerup, personagens_batalha, i):
        self._atacar = False
        self._defender = False
        self.powerup = False
        self.personagens_batalha = []
        self.i = 0
    def escolher_personagens(array):
        print("\nselecione os personagens que irão participar da batalha, minimo de 2 personagens.\n")
        personagem_escolhido = input("Coloque o nome do personagem aqui: ")
        for personagem in array:
            if personagem_escolhido == personagem.nome_personagem:
                personagens_batalha = personagem_escolhido
                i++
        if len(personagens_batalha) == 0:
            print("\nPersonagem não existe")
            #criar excessão aqui!
    def batalha:

        #fazer o sorteio da ordem dos personagens, um de 0 ate i.
        #contar as rodadas pra reiniciar o sorteio, sorteio acaba quando tiver i ações.
        #fazer as vantagens e desvantagens de cada personagem, usando tipo_personagem, fazemos um if pra puder chamar o metodo da classe especifica.
        #habilidades especiais dos personagens, similar ao item anterior, diferente do jeito que estavamos pensando não é um multiplicador fixo, tem que ser, por exemplo um ataque duplo do arqueiro.
        #criar, a cada rodada, um multiplicador de 1,1 em todos os valores de todos os personagens que ainda estão vivos.

        
            
            
