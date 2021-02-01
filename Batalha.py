from Funcionalidades import Funcionalidade
from Personagem import Personagem
from random import randint


class Batalha(Funcionalidade, Personagem):
    def escolher_personagens(array, personagem_batalha):
        i = 0
        print("\nselecione os personagens que irão participar da batalha, minimo de 2 personagens.\n")
        print("Personagens: \n")
        for personagem in array:
            print(personagem.tipo_personagem +
                  ": " + personagem.nome_personagem)
        personagem_escolhido = ""
        while personagem_escolhido == "":
            for personagem in array:
                personagem_escolhido = input(
                    "\nColoque o nome do personagem aqui. Coloque 0 para sair: ")

                if personagem_escolhido == "0":
                    return
                else:
                    print(personagem_escolhido)
                    # personagem_escolhido = input("Coloque o nome do personagem aqui: ")
                    if str(personagem.nome_personagem) == personagem_escolhido:
                        personagem_batalha.append(personagem)
                    elif str(personagem.nome_personagem) != personagem_escolhido and str(personagem.nome_personagem) != 0 and personagem_escolhido != 0:
                        print('Personagem não existe!')
                        personagem_escolhido = input(
                            "Coloque o nome do personagem aqui. Coloque 0 para sair: ")
        i = + 1

    def batalha(array, personagem_batalha, personagem_batalha2):
        while len(personagem_batalha) != 1:
            personagem_batalha2 = []
            Funcionalidade.verificar_pv_personagem(personagem_batalha)
            Funcionalidade.printar_vida_personagem(personagem_batalha)
            personagem_batalha2 = personagem_batalha2 + personagem_batalha
            i = 0
            for personagem in personagem_batalha:
                personagem.atacar = False
                personagem.defender = False
                personagem.powerup = False
            while len(personagem_batalha2) != 0:
                op = ''
                i = 0
                if len(personagem_batalha2) == 1:
                    i = 0
                else:
                    i = randint(0, len(personagem_batalha2) - 1)
                personagem_da_vez = personagem_batalha2[i]

                print("\nPersonagem da vez: " +
                      personagem_da_vez.nome_personagem)
                print("\n1- Atacar")
                print("2- Defender")
                print("3- Power up")
                print(
                    "4- Habilidade Especial, NOTA: Cada personagem só pode usa-la uma vez por batalha.")
                print("0- Para sair ")

                op = int(input())
                if op == 1:
                    Funcionalidade.ataque(
                        personagem_batalha2[i], personagem_batalha2, personagem_batalha)
                    personagem_batalha2.remove(personagem_batalha2[i])
                    Funcionalidade.verificar_pv_personagem(personagem_batalha2)
                    i = 0
                elif op == 2:
                    Funcionalidade.defesa(
                        personagem_batalha2[i], personagem_batalha2, personagem_batalha)
                    personagem_batalha2.remove(personagem_batalha2[i])
                    Funcionalidade.verificar_pv_personagem(personagem_batalha2)
                    i = 0
                elif op == 3:
                    Funcionalidade.powerup(
                        personagem_batalha2[i], personagem_batalha2, personagem_batalha)
                    personagem_batalha2.remove(personagem_batalha2[i])
                    Funcionalidade.verificar_pv_personagem(personagem_batalha2)
                    i = 0
                elif op == 4:
                    Funcionalidade.hab_especial(
                        personagem_batalha2[i], personagem_batalha2, personagem_batalha)
                    personagem_batalha2.remove(personagem_batalha2[i])
                    Funcionalidade.verificar_pv_personagem(personagem_batalha2)
                    i = 0
                elif op == 0:
                    print("Saindo da batalha.")
                    exit()
                # personagem_batalha2.remove(personagem_batalha2[i])
                #i = 0

            for personagem in personagem_batalha:
                personagem.pontos_ataque = personagem.pontos_ataque * 1.1
                personagem.pontos_defesa = personagem.pontos_defesa * 1.1
                personagem.pontos_vidas = personagem.pontos_vidas * 1.1

        for personagem in personagem_batalha:
            print(personagem.nome_personagem + " é o vencedor!!")
            exit()

        # Não sei bem como chamar os personagens exatos da classse por isso to usando essa notações como "personagem_atacado.pontos_vidas", se for o certo, ótimo, senão, lascou ;-;
        # pode criar um array temporario para isso
        # fazer o sorteio da ordem dos personagens, um de 0 ate i.
        # contar as rodadas pra reiniciar o sorteio, sorteio acaba quando tiver i ações.
        # fazer as vantagens e desvantagens de cada personagem, usando tipo_personagem, fazemos um if pra puder chamar o metodo da classe especifica.
        # habilidades especiais dos personagens, similar ao item anterior, diferente do jeito que estavamos pensando não é um multiplicador fixo, tem que ser, por exemplo um ataque duplo do arqueiro.
        # criar, a cada rodada, um multiplicador de 1,1 em todos os valores de todos os personagens que ainda estão vivos.
