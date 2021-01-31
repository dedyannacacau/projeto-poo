from Personagem import Personagem
import json
import os.path


class Funcionalidade(Personagem):

    def criar_personagem(array):
        nome_personagem = input("Coloque o nome do Personagem: ")
        for personagem in array:
            if(personagem.nome_personagem == nome_personagem):
                print("Personagem já existe, Coloque outro nome: ")
                nome_personagem = input("Coloque o nome do Personagem: ")
            else:
                break
        tipo_personagem = input("Coloque a Classe do Personagem: ")
        pontos_vidas = int(
            input("Coloque, em um valor inteiro, os pontos de VIDA do personagem: "))
        pontos_ataque = int(
            input("Coloque, em um valor inteiro, os pontos de ATAQUE do personagem: "))
        pontos_defesa = int(
            input("Coloque, em um valor inteiro, os pontos de DEFESA do personagem: "))
        porcentagem_powerup = (
            input("Coloque, em porcentagem, o valor do POWER UP do personagem: "))
        personagem = Personagem(tipo_personagem, nome_personagem,
                                pontos_vidas, pontos_ataque, pontos_defesa, porcentagem_powerup)
        array.append(personagem)

    def mostrar_personagens(array):
        i = 1

        if len(array) == 0:
            print(
                "\nNenhum personagem foi criado, volte para o menu e crie um personagem\n")
            pass
            # pode substituir por uma excessão mais elaborada, embora isso ja resolvendo.
        for personagem in array:
            print("\nO nome do Personagem " + str(i) +
                  " é: " + personagem.nome_personagem)
            print("A classe do Personagem " + str(i) +
                  " é: " + personagem.tipo_personagem)
            print("A quantidade de pontos de vida do personagem " +
                  str(i) + " são: " + str(personagem.pontos_vidas))
            print("A quantidade de pontos de ataque do personagem " +
                  str(i) + " são: " + str(personagem.pontos_ataque))
            print("A quantidade de pontos de defesa do personagem " +
                  str(i) + " são: " + str(personagem.pontos_defesa))
            print("A porcentagem de power up do personagem " + str(i) +
                  " é: " + personagem.porcentagem_powerup + "\n")
            i = i + 1

    def excluir_personagem(array):
        print("\nQual Personagem deseja excluir?")
        if len(array) == 0:
            print(
                "\nNenhum personagem foi criado, volte para o menu e crie um personagem\n")
            pass
        personagemExcluido = input(
            "Coloque o nome do personagem que você quer excluir: ")
        for personagem in array:
            if personagem.nome_personagem == personagemExcluido:
                array.remove(personagem)
                print(personagem.nome_personagem + ' removido.')

            if not personagem.nome_personagem == personagemExcluido:
                print('Personagem não existe!')
                personagemExcluido = input(
                    "Coloque o nome do personagem que você quer excluir: ")

    def editar_personagem(array):
        if len(array) == 0:
            print(
                "\nNenhum personagem foi criado, volte para o menu e crie um personagem\n")
            pass
        personagemEditado = input(
            "\nColoque o nome do personagem que você quer editar editar: ")
        for personagem in array:
            if personagem.nome_personagem == personagemEditado:
                personagem.tipo_personagem = input(
                    "Coloque a Classe do Personagem: ")
                personagem.pontos_vidas = int(
                    input("Coloque, em um valor inteiro, os pontos de VIDA do personagem: "))
                personagem.pontos_ataque = int(
                    input("Coloque, em um valor inteiro, os pontos de ATAQUE do personagem: "))
                personagem.pontos_defesa = int(
                    input("Coloque, em um valor inteiro, os pontos de DEFESA do personagem: "))
                personagem.porcentagem_powerup = (
                    input("Coloque, em porcentagem, o valor do POWER UP do personagem: "))

    def salvar_personagem_json(array):
        arquivo = "personagens.json"

        personagens_salvar = [
            dict(nome_personagem=obj.nome_personagem, tipo_personagem=obj.tipo_personagem, pontos_vidas=str(obj.pontos_vidas),
                 pontos_ataque=str(obj.pontos_ataque),
                 pontos_defesa=str(obj.pontos_defesa), porcentagem_powerup=str(obj.porcentagem_powerup))
            for obj in array
        ]

        dict_salvar = {"Personagens": personagens_salvar}
        dict_salvar = json.dumps(dict_salvar, indent=4, sort_keys=False)

        try:
            if os.path.exists(arquivo):
                personagens_json = open(arquivo, "a")
                personagens_json.write(dict_salvar)
                personagens_json.close()
            else:
                personagens_json = open("personagens.json", "w")
                personagens_json.write(dict_salvar)
                personagens_json.close()

        except Exception as error:
            print("Ocorreu um erro ao carregar o arquivo.")
            print("O erro é : {}".format(error))

    def carregar_personagem_json(array):
        with open('personagens.json', 'r', encoding='utf8') as f:
            data = json.load(f)
        print(data)

    def verificar_pv_personagem(array):
        for personagem in array:
            if personagem.pontos_vidas <= 0:
                array.remove(personagem)
