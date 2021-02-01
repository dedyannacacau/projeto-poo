from Personagem import Personagem
from Funcionalidades import Funcionalidade
from Batalha import Batalha
import json


class Main(Funcionalidade, Batalha):
    personagens = []
    opcao = ''
    lista = []
    while opcao != 0:
        print('\n1- Criar Personagem')
        print('2- Mostrar Personagens')
        print('3- Editar Personagem')
        print('4- Excluir Personagem')
        print('5- Salvar os Personagens, NOTA: ao salvar os dados anteriores são sobrescritos, podendo perder tudo!')
        print('6- Carregar os Personagens, NOTA: Carregue o jogo apenas uma vez, de preferencia assim que iniciar-lo.')
        print('7- Realizar uma Batalha, NOTA: ao iniciar uma batalha os personagens serão salvos, sobrescrevendo o save antigo, tendo risco de perder tudo!')
        print('0- Sair')

        opcao = int(input())

        if opcao == 1:
            Funcionalidade.criar_personagem(personagens)
        elif opcao == 2:
            Funcionalidade.mostrar_personagens(personagens)
        elif opcao == 3:
            Funcionalidade.mostrar_personagens(personagens)
            Funcionalidade.editar_personagem(personagens)
        elif opcao == 4:
            Funcionalidade.mostrar_personagens(personagens)
            Funcionalidade.excluir_personagem(personagens)
        elif opcao == 5:
            Funcionalidade.salvar_personagem_json(personagens)
            personagens.clear()
            Funcionalidade.carregar_personagem_json(personagens)
        elif opcao == 6:
            Funcionalidade.carregar_personagem_json(personagens)

        elif opcao == 7:
            Funcionalidade.salvar_personagem_json(personagens)
            Batalha.escolher_personagens(personagens)
            Batalha.batalha(personagens)
