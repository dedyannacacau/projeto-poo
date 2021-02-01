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
        print("As três classes de personagens são ARQUEIRO, BRUXO E CAVALEIRO, cada uma com uma habilidade especial e com vantagens e desvantagens entre elas!\n")
        tipo_personagem = input("Coloque a Classe do Personagem: ")
        pontos_vidas = float(input("Coloque, em um valor inteiro, os pontos de VIDA do personagem: "))
        pontos_ataque = float(input("Coloque, em um valor inteiro, os pontos de ATAQUE do personagem: "))
        pontos_defesa = float(input("Coloque, em um valor inteiro, os pontos de DEFESA do personagem: "))
        porcentagem_powerup = (input("Coloque, em porcentagem, o valor do POWER UP do personagem: "))
        personagem = Personagem(nome_personagem, tipo_personagem, pontos_vidas, pontos_ataque, pontos_defesa, porcentagem_powerup)
        array.append(personagem)

    def mostrar_personagens(array):
        i = 1
        print(array)
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
                personagem.pontos_vidas = float(input("Coloque, em um valor inteiro, os pontos de VIDA do personagem: "))
                personagem.pontos_ataque = float(input("Coloque, em um valor inteiro, os pontos de ATAQUE do personagem: "))
                personagem.pontos_defesa = float(input("Coloque, em um valor inteiro, os pontos de DEFESA do personagem: "))
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
    
    def carregar_personagem_json(array):
        salva_array = []
        personagens_carregados = []
        salva_array2 = dict
        p = 0
        z = 0
        with open('personagens.json', 'r') as f:
            data = json.load(f)
            data = data.get("Personagens")
            salva_array = data
            for salva_array in salva_array:
                salva_array2 = salva_array
                print(salva_array2)
                nome_personagem = salva_array2['nome_personagem']
                tipo_personagem = salva_array2['tipo_personagem']
                pontos_vidas = salva_array2['pontos_vidas']
                pontos_ataque = salva_array2['pontos_ataque']
                pontos_defesa = salva_array2['pontos_defesa']
                porcentagem_powerup = salva_array2['porcentagem_powerup']
                personagem = Personagem(nome_personagem, tipo_personagem, pontos_vidas, pontos_ataque, pontos_defesa, porcentagem_powerup)
                array.append(personagem)
                
            
    def verificar_pv_personagem(array):
        for personagem in array:
            if float(personagem.pontos_vidas) <= 0:
                array.remove(personagem)

    #infelizmente foi o maior metodo feito aqui, mas é nele que tem as vantagens e desvantagens de cada classe de personagens 
    def ataque(personagem_da_vez, array, array2):
        personagem_da_vez.atacar = True
        personagem_atacado = input("\nColoque o nome do Personagem que deseja atacar: ")
        for personagem_atacado in array:
            #PRIMEIRO TIPO: ARQUEIRO!!!!!!!!!!
            if tolower(personagem_da_vez.tipo_personagem) == "arqueiro":
                if tolower(personagem_atacado.tipo_personagem) == "arqueiro":
                    if personagem_atacado.defender == True:  
                        if personagem_atacado.pontos_defesa >= personagem_da_vez.pontos_ataque:
                            pass
                        else:
                            var = personagem_da_vez.pontos_ataque - personagem_atacado.pontos_defesa
                            personagem_atacado.pontos_vidas = personagem_atacado.pontos_vidas - var
                    elif personagem_atacado.defender == False:
                            personagem_atacado.pontos_vidas = personagem_atacado.pontos_vidas - personagem_da_vez.pontos_ataque
                elif tolower(personagem_atacado.tipo_personagem) == "bruxo":
                    #ARQUEIRO TEM VANTAGEM DE ATAQUE CONTRA O BRUXO
                    if personagem_atacado.defender == True:  
                        if personagem_atacado.pontos_defesa >= 2*personagem_da_vez.pontos_ataque:
                            pass
                        else:
                            var = personagem_da_vez.pontos_ataque - 2*personagem_atacado.pontos_defesa
                            personagem_atacado.pontos_vidas = personagem_atacado.pontos_vidas - var
                    elif personagem_atacado.defender == False:
                            personagem_atacado.pontos_vidas = personagem_atacado.pontos_vidas - 2*personagem_da_vez.pontos_ataque
                elif tolower(personagem_atacado.tipo_personagem) == "cavaleiro":
                    if personagem_atacado.defender == True:  
                        if personagem_atacado.pontos_defesa >= personagem_da_vez.pontos_ataque:
                            pass
                        else:
                            var = personagem_da_vez.pontos_ataque - personagem_atacado.pontos_defesa
                            personagem_atacado.pontos_vidas = personagem_atacado.pontos_vidas - var
                    elif personagem_atacado.defender == False:
                            personagem_atacado.pontos_vidas = personagem_atacado.pontos_vidas - personagem_da_vez.pontos_ataque
            #SEGUNDO TIPO: BRUXO!!!!!!!!!!
            elif tolower(personagem_da_vez.tipo_personagem) == "bruxo":
                if tolower(personagem_atacado.tipo_personagem) == "arqueiro":
                    if personagem_atacado.defender == True:  
                        if personagem_atacado.pontos_defesa >= personagem_da_vez.pontos_ataque:
                            pass
                        else:
                            var = personagem_da_vez.pontos_ataque - personagem_atacado.pontos_defesa
                            personagem_atacado.pontos_vidas = personagem_atacado.pontos_vidas - var
                    elif personagem_atacado.defender == False:
                            personagem_atacado.pontos_vidas = personagem_atacado.pontos_vidas - personagem_da_vez.pontos_ataque
                elif tolower(personagem_atacado.tipo_personagem) == "bruxo":
                    if personagem_atacado.defender == True:  
                        if personagem_atacado.pontos_defesa >= personagem_da_vez.pontos_ataque:
                            pass
                        else:
                            var = personagem_da_vez.pontos_ataque - personagem_atacado.pontos_defesa
                            personagem_atacado.pontos_vidas = personagem_atacado.pontos_vidas - var
                    elif personagem_atacado.defender == False:
                            personagem_atacado.pontos_vidas = personagem_atacado.pontos_vidas - personagem_da_vez.pontos_ataque
                elif tolower(personagem_atacado.tipo_personagem) == "cavaleiro":
                    #BRUXO TEM VANTAGEM CONTRA O CAVALEIRO!
                    if personagem_atacado.defender == True:  
                        if personagem_atacado.pontos_defesa >= 2*personagem_da_vez.pontos_ataque:
                            pass
                        else:
                            var = personagem_da_vez.pontos_ataque - 2*personagem_atacado.pontos_defesa
                            personagem_atacado.pontos_vidas = personagem_atacado.pontos_vidas - var
                    elif personagem_atacado.defender == False:
                            personagem_atacado.pontos_vidas = personagem_atacado.pontos_vidas - 2*personagem_da_vez.pontos_ataque
            #TERCEIRO TIPO: CAVALEIRO!!!!!!!!!
            elif tolower(personagem_da_vez.tipo_personagem) == "cavaleiro":
                if tolower(personagem_atacado.tipo_personagem) == "arqueiro":
                    #CAVALEIRO TEM VANTAGEM CONTRA O ARQUEIRO
                    if personagem_atacado.defender == True:  
                        if personagem_atacado.pontos_defesa >= 2*personagem_da_vez.pontos_ataque:
                            pass
                        else:
                            var = personagem_da_vez.pontos_ataque - 2*personagem_atacado.pontos_defesa
                            personagem_atacado.pontos_vidas = personagem_atacado.pontos_vidas - var
                    elif personagem_atacado.defender == False:
                            personagem_atacado.pontos_vidas = personagem_atacado.pontos_vidas - 2*personagem_da_vez.pontos_ataque
                elif tolower(personagem_atacado.tipo_personagem) == "bruxo":
                    if personagem_atacado.defender == True:  
                        if personagem_atacado.pontos_defesa >= personagem_da_vez.pontos_ataque:
                            pass
                        else:
                            var = personagem_da_vez.pontos_ataque - personagem_atacado.pontos_defesa
                            personagem_atacado.pontos_vidas = personagem_atacado.pontos_vidas - var
                    elif personagem_atacado.defender == False:
                            personagem_atacado.pontos_vidas = personagem_atacado.pontos_vidas - personagem_da_vez.pontos_ataque
                elif tolower(personagem_atacado.tipo_personagem) == "cavaleiro":
                    if personagem_atacado.defender == True:  
                        if personagem_atacado.pontos_defesa >= personagem_da_vez.pontos_ataque:
                            pass
                        else:
                            var = personagem_da_vez.pontos_ataque - personagem_atacado.pontos_defesa
                            personagem_atacado.pontos_vidas = personagem_atacado.pontos_vidas - var
                    elif personagem_atacado.defender == False:
                            personagem_atacado.pontos_vidas = personagem_atacado.pontos_vidas - personagem_da_vez.pontos_ataque    
                       


        array2.remove(personagem_da_vez)
    def defesa(personagem_da_vez, array, array2):
        personagem_da_vez.defender = True
        array2.remove(personagem_da_vez)
    
    def powerup(personagem_da_vez, array, array2):
        personagem_da_vez.powerup = True
        if isinstance(personagem_da_vez.porcentagem_powerup, str):
            personagem_da_vez.porcentagem_powerup = float(personagem_da_vez.porcentagem_power.replace('%', ''))
        personagem_da_vez.pontos_ataque = personagem_da_vez.pontos_ataque * (personagem_da_vez.porcentagem_powerup / 100)
        personagem_da_vez.pontos_defesa = personagem_da_vez.pontos_defesa * (personagem_da_vez.porcentagem_powerup / 100)
        personagem_da_vez.pontos_vidas = personagem_da_vez.pontos_vidas * (personagem_da_vez.porcentagem_powerup / 100)
        array2.remove(personagem_da_vez)
    
    def hab_especial(personagem_da_vez, array, array2):
        if personagem_da_vez.habilidade_especial == True:
            print("Personagem já usou sua habilidade especial uma vez na batalha, logo não poderá usar mais uma vez.")
            pass #pode criar uma excessão aqui!
        personagem_da_vez.habilidade_especial = True
        if tolower(personagem_da_vez.tipo_personagem) == "arqueiro":
            Arqueiro.hab_especial(array, array2)
            array2.remove(personagem_da_vez)        
        elif tolower(personagem_da_vez.tipo_personagem) == "bruxo":
            Bruxo.hab_especial(array, array2)
            array2.remove(personagem_da_vez)
        elif tolower(personagem_da_vez.tipo_personagem) == "cavaleiro":
            Cavaleiro.hab_especial(array, array2)
            array2.remove(personagem_da_vez)
                 


