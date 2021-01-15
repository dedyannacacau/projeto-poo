class Personagem:

    def __init__(self, tipo_personagem, nome_personagem, pontos_vidas, pontos_defesa, porcentagem_powerup):
        self.tipo_personagem = tipo_personagem
        self.nome_personagem = nome_personagem
        self.pontos_vidas = pontos_vidas
        self.pontos_defesa = pontos_defesa
        self.porcentagem_powerup = porcentagem_powerup

    def getNomePersonagem(self):
        return self.nome_personagem

    def setNomePersonagem(self, nome_personagem):
        self.nome_personagem = nome_personagem


    def getTipoPersonagem(self):
        return self.tipo_personagem

    def setTipoPersonagem(self, tipo_personagem):
        self.tipo_personagem = tipo_personagem


    def getPontosVidas(self):
        return self.pontos_vidas    

    def setPontosVidas(self, pontos_vidas):
        self.pontos_vidas = pontos_vidas


    def getPontosDefesa(self):
        return self.pontos_defesa

    def setPontosDefesa(self, pontos_defesa):
        self.pontos_defesa = pontos_defesa


    def getPorcentagemPowerUp(self):
        return self.porcentagem_powerup

    def setPorcentagemPowerUp(self, porcentagem_powerup):
        self.porcentagem_powerup = porcentagem_powerup          


    def criar_personagem(self):
            self._nome_personagem = input('Nome do personagem: ')
            self._tipo_personagem = input('Classe do personagem: ')
            self.pontos_vida = int(input('Coloque os pontos de VIDA do personagem: '))
            self.pontos_ataque = int(input('Coloque o valor do ATAQUE do personagem: '))
            self.pontos_defesa = int(input('Coloque os pontos de DEFESA do personagem: '))
            self.porcentagem_powerup = int(input('Coloque, em porcentagem, o valor de POWERUP do personagem: '))