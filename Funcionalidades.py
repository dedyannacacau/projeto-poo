from Personagem import Personagem
import json

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
        pontos_vidas = int(input("Coloque, em um valor inteiro, os pontos de VIDA do personagem: "))
        pontos_ataque = int(input("Coloque, em um valor inteiro, os pontos de ATAQUE do personagem: "))
        pontos_defesa = int(input("Coloque, em um valor inteiro, os pontos de DEFESA do personagem: "))
        porcentagem_powerup = (input("Coloque, em porcentagem, o valor do POWER UP do personagem: "))
        personagem = Personagem(tipo_personagem, nome_personagem, pontos_vidas, pontos_ataque, pontos_defesa, porcentagem_powerup)
        array.append(personagem)

    def mostrar_personagens(array):
        i = 1
        if len(array) == 0:
            print("\nNenhum personagem foi criado, volte para o menu e crie um personagem\n")
            pass
            #pode substituir por uma excessão mais elaborada, embora isso ja resolvendo.
        for personagem in array:
            print("\nO nome do Personagem " + str(i) + " é: " + personagem.nome_personagem)
            print("A classe do Personagem " + str(i) + " é: " + personagem.tipo_personagem)
            print("A quantidade de pontos de vida do personagem " + str(i) + " são: " + str(personagem.pontos_vidas))
            print("A quantidade de pontos de ataque do personagem " + str(i) + " são: " +str(personagem.pontos_ataque))
            print("A quantidade de pontos de defesa do personagem " + str(i) + " são: " +str(personagem.pontos_defesa))
            print("A porcentagem de power up do personagem " + str(i) + " é: " + personagem.porcentagem_powerup + "\n")
            i = i + 1


    def excluir_personagem(array):
        print("\nQual Personagem deseja excluir?")
        if len(array) == 0:
            print("\nNenhum personagem foi criado, volte para o menu e crie um personagem\n")
            pass
        personagemExcluido = input("Coloque o nome do personagem que você quer excluir: ")
        for personagem in array:
            if personagem.nome_personagem == personagemExcluido:
                array.remove(personagem)
            #criar excessão aqui, caso tentar excluir um personagem que não existe.

    def editar_personagem(array):
        if len(array) == 0:
            print("\nNenhum personagem foi criado, volte para o menu e crie um personagem\n")
            pass
        personagemEditado = input("\nColoque o nome do personagem que você quer editar editar: ")
        for personagem in array:
            if personagem.nome_personagem == personagemEditado:
                personagem.tipo_personagem = input("Coloque a Classe do Personagem: ")
                personagem.pontos_vidas = int(input("Coloque, em um valor inteiro, os pontos de VIDA do personagem: "))
                personagem.pontos_ataque = int(input("Coloque, em um valor inteiro, os pontos de ATAQUE do personagem: "))
                personagem.pontos_defesa = int(input("Coloque, em um valor inteiro, os pontos de DEFESA do personagem: "))
                personagem.porcentagem_powerup = (input("Coloque, em porcentagem, o valor do POWER UP do personagem: "))

    def salvar_personagem_json(array):
        personagens_salvar = [ dict(nome_personagem=obj.nome_personagem, tipo_personagem=obj.tipo_personagem,  pontos_vidas=str(obj.pontos_vidas),pontos_ataque=str(obj.pontos_ataque),pontos_defesa=str(obj.pontos_defesa), porcentagem_powerup=str(obj.porcentagem_powerup))
            for obj in array]
        

        dict_salvar = {"Personagens": personagens_salvar}
        dict_salvar = json.dumps(dict_salvar, indent=4, sort_keys=False)
        try:
            personagens_json = open("personagens.json", "w")
            personagens_json.write(dict_salvar)
            personagens_json.close()
        except Exception as error:
            print("Ocorreu um erro ao carregar o arquivo.")
            print("O erro é : {}".format(error))
    
    def carregar_personagem_json(lista, array):
        salva_array = []
        salva_array2 = dict
        #personagem = Personagem(tipo_personagem, nome_personagem, pontos_vidas, pontos_ataque, pontos_defesa, porcentagem_powerup)
        with open('personagens.json', 'r') as f:
            data = json.load(f)
            data = data.get("Personagens")
            salva_array = data
            print(data)
            print(salva_array)
            for salva_array in salva_array:

                salva_array2 = salva_array
                nome_personagem = salva_array2['nome_personagem']
                tipo_personagem = salva_array2['tipo_personagem']
                pontos_vidas = salva_array2['pontos_vidas']
                pontos_ataque = salva_array2['pontos_ataque']
                pontos_defesa = salva_array2['pontos_defesa']
                porcentagem_powerup = salva_array2['porcentagem_powerup']
                personagem = Personagem(tipo_personagem, nome_personagem, pontos_vidas, pontos_ataque, pontos_defesa, porcentagem_powerup)
                array.append(personagem)
            
             

        
       
    def verificar_pv_personagem(array):
        for personagem in array:
            if personagem.pontos_vidas <= 0:
                array.remove(personagem)
    
    def ataque(array, array2):
        personagem_da_vez.atacar = True
        personagem_atacado = input("\nColoque o nome do Personagem que deseja atacar: ")
        for personagem_atacado in array:
            if personagem_atacado.defender = True:
                if personagem_atacado.pontos_defesa >= personagem_da_vez.pontos_ataque:
                    pass
                else:
                    var = personagem_da_vez.pontos_ataque - personagem_atacado.pontos_defesa
                    personagem_atacado.pontos_vidas = personagem_atacado.pontos_vidas - var
            if personagem_atacado.defender = False:
                personagem_atacado.pontos_vidas = personagem_atacado.pontos_vidas - personagem_da_vez.pontos_ataque
        array2.remove(personagem_da_vez)
    
    def defesa(array, array2):
        personagem_da_vez.defender = True
        array2.remove(personagem_da_vez)
    
    def powerup(array, array2):
        personagem_da_vez.powerup = True
        personagem_da_vez.porcentagem_powerup = 
        personagem_da_vez.pontos_ataque = 
        personagem_da_vez.pontos_defesa =
        personagem_da_vez.pontos_vidas =
    
    def hab_especial(array, array2):
        personagem_da_vez.habilidade_especial = True
        if tolower(personagem_da_vez.tipo_personagem) = "arqueiro":
            Arqueiro.hab_especial
        
        if tolower(personagem_da_vez.tipo_personagem) = "bruxo":
            Bruxo.hab_especial

        if tolower(personagem_da_vez.tipo_personagem) = "cavaleiro":
            Cavaleiro.hab_especial


            


