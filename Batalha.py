from Funcionalidades import Funcionalidade
from random import randint

class Batalha(Funcionalidade):
    def __init__(self, atacar, defender, powerup, personagens_batalha, personagens_batalha2, i):
        self._atacar = False
        self._defender = False
        self.powerup = False
        self.personagens_batalha = []
        self.personagens_batalha2 = []
        self.i = 0
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
        for personagem_batalha in personagem_batalha:
            personagem_batalha2 == personagem_batalha
            for personagem_batalha2 in personagem_batalha:
                if len(personagem_batalha2) = 0:
                    i++
                    #i conta o numero de rodadas
                    break
                else:
                    i = randint(0, len(personagem_batalha2))
                    for personagem_batalha2[i] in array:
                        if tolower.personagem.tipo_personagem == "arqueiro":
                            #chamar metodos arqueiro
                            #mais a questao de ataque e defesa da propria classe batalha
                        elif tolower.personagem.tipo_personagem == "bruxo":
                            #chamar metodos bruxo
                            #mais a questao de ataque e defesa da propria classe batalha
                        elif tolower.personagem.tipo_personagem == "cavaleiro":
                            #chamar metodos cavaleiro
                            #mais a questao de ataque e defesa da propria classe batalha                   
                    
                    personagem_batalha2[i].remove



        #fazer verificaçao de vida de todos os personagens, se tiver 0 ou for menor que 0 tem que ser excluido do personagem_batalha.        
        #pode criar um array temporario para isso        
        #fazer o sorteio da ordem dos personagens, um de 0 ate i.
        #contar as rodadas pra reiniciar o sorteio, sorteio acaba quando tiver i ações.
        #fazer as vantagens e desvantagens de cada personagem, usando tipo_personagem, fazemos um if pra puder chamar o metodo da classe especifica.
        #habilidades especiais dos personagens, similar ao item anterior, diferente do jeito que estavamos pensando não é um multiplicador fixo, tem que ser, por exemplo um ataque duplo do arqueiro.
        #criar, a cada rodada, um multiplicador de 1,1 em todos os valores de todos os personagens que ainda estão vivos.

        
            
            