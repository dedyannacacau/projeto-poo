from Funcionalidades import Funcionalidade
from Personagem import Personagem
from random import randint

class Batalha(Funcionalidade, Personagem):
    def __init__(self, atacar, defender, powerup, personagens_batalha, personagens_batalha2, i, rodadas, ):
        self._atacar = False
        self._defender = False
        self.powerup = False
        self.personagens_batalha = []
        self.personagens_batalha2 = []
        self.i = 0
        self.rodadas = 1
    def escolher_personagens(array):
        print("\nselecione os personagens que irão participar da batalha, minimo de 2 personagens.\n")
        personagem_escolhido = input("Coloque o nome do personagem aqui: ")
        for personagem in array:
            if personagem_escolhido == personagem.nome_personagem:
                personagens_batalha = personagem_escolhido
        if len(personagens_batalha) == 0:
            print("\nPersonagem não existe")
            #criar excessão aqui!
    def batalha(array):
        while len(personagens_batalha) != 0: 
            personagens_batalha2 = personagens_batalha
            i = 0
            while len(personagens_batalha2) != 0:
                    i = randint(0, len(personagens_batalha2))
                    for personagens_batalha2[i] in array:
                        if _atacar == True:
                            personagem_atacado = input("\nEscolha um personagem para atacar: ")
                            if personagem_atacado._pontos_vidas <= 0:
                                print("\nPersonagem ja morreu!")
                                for personagem_atacado in personagens_batalha2:
                                    personagens_batalha2.remove
                            elif personagem_atacado.defender == True:
                                if personagem_atacado.pontos_defesa < personagens_batalha2[i].pontos_ataque:
                                    var = 0
                                    var = personagens_batalha2[i].pontos_ataque - personagem_atacado.pontos_defesa
                                    

                        

                        personagens_batalha2[i].remove
            rodadas++



        #        
        #pode criar um array temporario para isso        
        #fazer o sorteio da ordem dos personagens, um de 0 ate i.
        #contar as rodadas pra reiniciar o sorteio, sorteio acaba quando tiver i ações.
        #fazer as vantagens e desvantagens de cada personagem, usando tipo_personagem, fazemos um if pra puder chamar o metodo da classe especifica.
        #habilidades especiais dos personagens, similar ao item anterior, diferente do jeito que estavamos pensando não é um multiplicador fixo, tem que ser, por exemplo um ataque duplo do arqueiro.
        #criar, a cada rodada, um multiplicador de 1,1 em todos os valores de todos os personagens que ainda estão vivos.

        
            
            
