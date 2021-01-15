class Personagem:
    def __init__(self, tipo_personagem, nome_personagem, pontos_vidas, pontos_ataque, pontos_defesa, porcentagem_powerup):
        self.tipo_personagem = tipo_personagem
        self.nome_personagem = nome_personagem
        self.pontos_vidas = pontos_vidas
        self.pontos_ataque = pontos_ataque
        self.pontos_defesa = pontos_defesa
        self.porcentagem_powerup = porcentagem_powerup

    @property
    def nome_personagem(self):
        return self._nome_personagem

    @nome_personagem.setter
    def nome_personagem(self, nome_personagem):
        self._nome_personagem = nome_personagem


    @property
    def tipo_personagem(self):
        return self._tipo_personagem

    @tipo_personagem.setter
    def tipo_personagem(self, tipo_personagem):
        self._tipo_personagem = tipo_personagem


    @property
    def pontos_vidas(self):
        return self._pontos_vidas    

    @pontos_vidas.setter 
    def pontos_vidas(self, pontos_vidas):
        self._pontos_vidas = pontos_vidas


    @property
    def pontos_defesa(self):
        return self._pontos_defesa

    @pontos_defesa.setter
    def pontos_defesa(self, pontos_defesa):
        self._pontos_defesa = pontos_defesa


    @property
    def pontos_ataque(self):
        return self._pontos_ataque

    @pontos_ataque.setter
    def pontos_ataque(self, pontos_ataque):
        self._pontos_ataque = pontos_ataque


    @property
    def porcentagem_powerup(self):
        return self._porcentagem_powerup

    @porcentagem_powerup.setter
    def porcentagem_powerup(self, porcentagem_powerup):
        self._porcentagem_powerup = porcentagem_powerup          

