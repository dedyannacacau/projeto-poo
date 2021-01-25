from Personagem import Personagem
import json


class Main:
    def criar_personagem(array):
        nome_personagem = input('Nome do personagem: ')
        for personagem in array:
            if personagem.nome_personagem == nome_personagem:
                print('Personagem já existe!')
                nome_personagem = input('Nome do personagem: ')
            else:
                break
        try:
            pontos_vidas = int(
                input('Coloque os pontos de VIDA do personagem: '))
            pontos_ataque = int(
                input('Coloque o valor do ATAQUE do personagem: '))
            pontos_defesa = int(
                input('Coloque os pontos de DEFESA do personagem: '))
            porcentagem_powerup = int(
                input('Coloque, em porcentagem, o valor de POWERUP do personagem: '))
        except ValueError:
            print('\n\nÉ necessário ser um número!\n')

        personagem = Personagem(nome_personagem,
                                pontos_vidas, pontos_ataque, pontos_defesa, porcentagem_powerup)
        array.append(personagem)

    def mostrar_personagens(array):
        def escrever_personagens_json(obj):
            personagens_salvar = [
                dict(nome_personagem=obj.nome_personagem, pontos_vidas=str(obj.pontos_vidas), pontos_ataque=str(obj.pontos_ataque),
                     pontos_defesa=str(obj.pontos_defesa), porcentagem_powerup=str(obj.porcentagem_powerup))
                for obj in array
            ]

            dict_salvar = {"Personagens": personagens_salvar}
            dict_salvar = json.dumps(dict_salvar, indent=4, sort_keys=False)

            try:
                personagens_json = open("personagens.json", "w")
                personagens_json.write(dict_salvar)
                personagens_json.close()
            except Exception as error:
                print("Ocorreu um erro ao carregar o arquivo.")
                print("O erro é : {}".format(error))

        if len(array) == 0:
            print('\nNão há personagens criados!\n')
        for personagem in array:
            escrever_personagens_json(
                'Nome: ' + personagem.nome_personagem + '\n')
            escrever_personagens_json(
                'Vidas: ' + str(personagem.pontos_vidas) + '\n')
            escrever_personagens_json(
                'Ataque: ' + str(personagem.pontos_ataque) + '\n')
            escrever_personagens_json(
                'Defesa: ' + str(personagem.pontos_defesa) + '\n')
            escrever_personagens_json(
                'Power-Up: ' + str(personagem.porcentagem_powerup) + "%" + '\n')

    def excluir_personagem(array):
        print('Qual personagem deseja excluir?\n')
        # Não consegui fazer com que um método chame um outro método, por isso copiei o que tinha dentro da função mostrar_personagem()
        for personagem in array:
            print('\n')

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

                pontos_vidas = int(
                    input('Coloque os pontos de VIDA do personagem: '))
                pontos_ataque = int(
                    input('Coloque o valor do ATAQUE do personagem: '))
                pontos_defesa = int(
                    input('Coloque os pontos de DEFESA do personagem: '))
                porcentagem_powerup = int(
                    input('Coloque, em porcentagem, o valor de POWERUP do personagem: '))

                personagem = Personagem(nome_personagem,
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
