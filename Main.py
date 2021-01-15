from Personagem import Personagem
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
            pontos_defesa = int(input('Coloque os pontos de DEFESA do personagem: '))
            porcentagem_powerup = int(input('Coloque, em porcentagem, o valor de POWERUP do personagem: '))

            personagem = Personagem(tipo_personagem, nome_personagem, pontos_vidas, pontos_ataque, pontos_defesa, porcentagem_powerup)
            array.append(personagem)    

    def mostrar_personagens(array):
        if len(array) == 0:
            print('\nNão há personagens criados!\n')
        for personagem in array:

            print('Classe: ' + personagem.tipo_personagem)
            print('Nome: ' + personagem.nome_personagem)
            print('Vidas: ' + str(personagem.pontos_vidas))
            print('Ataque: ' + str(personagem.pontos_ataque))
            print('Defesa: ' + str(personagem.pontos_defesa))
            print('Power-Up: ' + str(personagem.porcentagem_powerup) + "%")


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

        personagemExcluido = input('Digite o nome do Personagem que deseja excluir: ')
        
        for personagem in array:
            if personagem.nome_personagem == personagemExcluido:
                array.remove(personagem)
               



    ############### MENU PRINCIPAL #####################
    personagens = []
    opcao = ''

    while opcao != 0:
        print('1- Criar Personagem ')
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
        elif opcao == 4:
            excluir_personagem(personagens)   