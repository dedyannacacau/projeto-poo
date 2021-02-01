from Funcionalidades import Funcionalidade
from Personagem import Personagem
from random import randint

class Batalha(Funcionalidade, Personagem):
    personagem_batalha = []
    personagem_batalha2 = []
    def escolher_personagens(array):
        i = -1
        print("\nselecione os personagens que irão participar da batalha, minimo de 2 personagens.\n")
        while i != len(array) - 1:
            i =+ 1
            personagem_escolhido = input("Coloque o nome do personagem aqui: ")
            for personagem in array:
                #personagem_escolhido = input("Coloque o nome do personagem aqui: ")
                if personagem_escolhido == personagem.nome_personagem:
                    personagens_batalha = personagem_escolhido
                else:
                    print("Personagem não existe")
                    break
            if len(personagens_batalha) == 0:
                print("\nPersonagem não existe")
                #criar excessão aqui!
            
    def batalha(array):
        while len(personagens_batalha) != 0:
            Funcionalide.verificar_pv_personagem(personagens_batalha) 
            personagens_batalha2 = personagens_batalha
            i = 0
            while len(personagens_batalha2) != 0:
                Funcionalide.verificar_pv_personagem(personagens_batalha)
                i = randint(0, len(personagens_batalha2))
                for personagens_batalha2[i] in array:
                    personagem_da_vez = personagens_batalha2
                    op = ''
                    while op != 0:
                        print(personagem_da_vez)
                        print("1- Atacar")
                        print("2- Defender")
                        print("3- Power up")
                        print("4- Habilidade Especial, NOTA: Cada personagem só pode usa-la uma vez por batalha.")

                        op = input()
                        if op == 1:
                            Funcionalide.verificar_pv_personagem(personagens_batalha)
                            Funcionalidade.ataque(personagens_batalha, personagens_batalha2)
                        elif op == 2:
                            Funcionalide.verificar_pv_personagem(personagens_batalha)
                            Funcionalidade.defesa(personagens_batalha, personagens_batalha2)
                        elif op == 3:
                            Funcionalide.verificar_pv_personagem(personagens_batalha)
                            Funcionalidade.powerup(personagens_batalha, personagens_batalha2)
                        elif op == 4:
                            Funcionalide.verificar_pv_personagem(personagens_batalha)
                            Funcionalidade.hab_especial(personagens_batalha, personagens_batalha2)
                        op = 0
            



        #Não sei bem como chamar os personagens exatos da classse por isso to usando essa notações como "personagem_atacado.pontos_vidas", se for o certo, ótimo, senão, lascou ;-;        
        #pode criar um array temporario para isso        
        #fazer o sorteio da ordem dos personagens, um de 0 ate i.
        #contar as rodadas pra reiniciar o sorteio, sorteio acaba quando tiver i ações.
        #fazer as vantagens e desvantagens de cada personagem, usando tipo_personagem, fazemos um if pra puder chamar o metodo da classe especifica.
        #habilidades especiais dos personagens, similar ao item anterior, diferente do jeito que estavamos pensando não é um multiplicador fixo, tem que ser, por exemplo um ataque duplo do arqueiro.
        #criar, a cada rodada, um multiplicador de 1,1 em todos os valores de todos os personagens que ainda estão vivos.

        
            
            
