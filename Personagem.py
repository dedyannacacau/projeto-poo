class Personagem:
    def __init__(self, nome_personagem, pontos_vidas, pontos_ataque, pontos_defesa, porcentagem_powerup):
        self._nome_personagem = nome_personagem
        self._pontos_vidas = pontos_vidas
        self._pontos_ataque = pontos_ataque
        self._pontos_defesa = pontos_defesa
        self._porcentagem_powerup = porcentagem_powerup

    @property
    def nome_personagem(self):
        return self._nome_personagem

    @nome_personagem.setter
    def nome_personagem(self, nome_personagem):
        self._nome_personagem = nome_personagem

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
