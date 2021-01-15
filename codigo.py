class Personagem:
    def __init__(self, nome_personagem, tipo_personagem, pontos_vida, pontos_ataque, pontos_defesa, porcentagem_powerup):
        self._nome_personagem = nome_personagem
        self._tipo_personagem = tipo_personagem
        self.pontos_vida = pontos_vida
        self.pontos_ataque = pontos_ataque
        self.pontos_defesa = pontos_defesa
        self.porcentagem_powerup = porcentagem_powerup
    def criar_personagem(self):
        self._nome_personagem = input('Nome do personagem: ')
        self._tipo_personagem = input('Classe do personagem: ')
        self.pontos_vida = int(input('Coloque os pontos de VIDA do personagem: '))
        self.pontos_ataque = int(input('Coloque o valor do ATAQUE do personagem: '))
        self.pontos_defesa = int(input('Coloque os pontos de DEFESA do personagem: '))
        self.porcentagem_powerup = int(input('Coloque, em porcentagem, o valor de POWERUP do personagem: '))
