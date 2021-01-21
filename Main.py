from Personagem import Personagem
import os.path


class Main:
    def criar_personagem(array):
        nome_personagem = input('Nome do personagem: ')
        for personagem in array:
            if personagem.nome_personagem == nome_personagem:
                print('Personagem já existe!')
                nome_personagem = input('Nome do personagem: ')
            else:
                break
        tipo_personagem = input('Classe do personagem: ')
        pontos_vidas = int(input('Coloque os pontos de VIDA do personagem: '))
        pontos_ataque = int(input('Coloque o valor do ATAQUE do personagem: '))
        pontos_defesa = int(
            input('Coloque os pontos de DEFESA do personagem: '))
        porcentagem_powerup = int(
            input('Coloque, em porcentagem, o valor de POWERUP do personagem: '))

        personagem = Personagem(tipo_personagem, nome_personagem,
                                pontos_vidas, pontos_ataque, pontos_defesa, porcentagem_powerup)
        array.append(personagem)

    def mostrar_personagens(array):
        # Declarando essa função dentro dessa outra função aplica-se o encapsulamento em python.
        # Se a função interna será chamada só por esta função não tem porque colocar fora.
        # Colocando dentro garante que ninguém mais chame.
        # Assim que a mostrar_personagens() for acessada será criado um arquivo txt com os personagens criados.
        # Se criar um personagem e colocar para mostrar, e depois criar de novo ele repete o ultimo persoagem, e estou com dificuldade de consertar isso
        def escrever_personagens_txt(array):
            if os.path.exists('peersonags.txt'):
                with open('personagens.txt', 'r') as f:
                    for personagem in array:
                        print(personagem + '\n')
            else:
                with open('personagens.txt', 'a+') as f:
                    for personagem in array:
                        f.write(personagem)

        if len(array) == 0:
            print('\nNão há personagens criados!\n')
        for personagem in array:
            escrever_personagens_txt('================================' + '\n')
            escrever_personagens_txt(
                'Classe: ' + personagem.tipo_personagem + '\n')
            escrever_personagens_txt(
                'Nome: ' + personagem.nome_personagem + '\n')
            escrever_personagens_txt(
                'Vidas: ' + str(personagem.pontos_vidas) + '\n')
            escrever_personagens_txt(
                'Ataque: ' + str(personagem.pontos_ataque) + '\n')
            escrever_personagens_txt(
                'Defesa: ' + str(personagem.pontos_defesa) + '\n')
            escrever_personagens_txt(
                'Power-Up: ' + str(personagem.porcentagem_powerup) + "%" + '\n')

    def excluir_personagem(array):
        print('Qual personagem deseja excluir?\n')
        # Não consegui fazer com que um método chame um outro método, por isso copiei o que tinha dentro da função mostrar_personagem()
        for personagem in array:
            print('\n')
            print('Classe: ' + personagem.tipo_personagem)
            print('Nome: ' + personagem.nome_personagem)
            print('Vidas: ' + str(personagem.pontos_vidas))
            print('Ataque: ' + str(personagem.pontos_ataque))
            print('Defesa: ' + str(personagem.pontos_defesa))
            print('Power-Up: ' + str(personagem.porcentagem_powerup) + "%")
            print('\n')

        personagemExcluido = input(
            'Digite o nome do Personagem que deseja excluir: ')

        for personagem in array:
            if personagem.nome_personagem == personagemExcluido:
                array.remove(personagem)

    def editar_personagem(array):
        i = 0
        print('Qual personagem deseja editar?')

        for personagem in array:
            print('\n')
            print('Classe: ' + personagem.tipo_personagem)
            print('Nome: ' + personagem.nome_personagem)
            print('Vidas: ' + str(personagem.pontos_vidas))
            print('Ataque: ' + str(personagem.pontos_ataque))
            print('Defesa: ' + str(personagem.pontos_defesa))
            print('Power-Up: ' + str(personagem.porcentagem_powerup) + "%")
            print('\n')

        personagemEditado = input(
            'Digite o nome do Personagem que deseja editar: ')

        for personagem in array:
            if personagem.nome_personagem == personagemEditado:
                nome_personagem = input('Nome do personagem: ')
                for personagem in array:
                    if personagem.nome_personagem == nome_personagem:
                        print('Personagem já existe!')
                        nome_personagem = input('Nome do personagem: ')
                    else:
                        break
                tipo_personagem = input('Classe do personagem: ')
                pontos_vidas = int(
                    input('Coloque os pontos de VIDA do personagem: '))
                pontos_ataque = int(
                    input('Coloque o valor do ATAQUE do personagem: '))
                pontos_defesa = int(
                    input('Coloque os pontos de DEFESA do personagem: '))
                porcentagem_powerup = int(
                    input('Coloque, em porcentagem, o valor de POWERUP do personagem: '))

                personagem = Personagem(tipo_personagem, nome_personagem,
                                        pontos_vidas, pontos_ataque, pontos_defesa, porcentagem_powerup)
                array[i] = personagem
            else:
                i = i + 1

    ############### MENU PRINCIPAL #####################
    personagens = []
    opcao = ''

    while opcao != 0:
        print('\n1- Criar Personagem ')
        print('2- Mostrar Personagens')
        print('3- Editar Personagem')
        print('4- Excluir Personagem')
        print('5- Realizar uma Batalha')
        print('0- Sair')

        opcao = int(input())

        if opcao == 1:
            criar_personagem(personagens)
        elif opcao == 2:
            mostrar_personagens(personagens)
        elif opcao == 3:
            editar_personagem(personagens)
        elif opcao == 4:
            excluir_personagem(personagens)
