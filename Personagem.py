class Personagem:
    def __init__(self, nome_personagem, tipo_personagem, pontos_vidas, pontos_ataque, pontos_defesa, porcentagem_powerup):
        self._nome_personagem = nome_personagem
        self._tipo_personagem = tipo_personagem
        self._pontos_vidas = pontos_vidas
        self._pontos_ataque = pontos_ataque
        self._pontos_defesa = pontos_defesa
        self._porcentagem_powerup = porcentagem_powerup
        self._atacar = False
        self._defender = False
        self._powerup = False
        self._habilidade_especial = False

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

    @property
    def atacar(self):
        return self._atacar

    @atacar.setter
    def atacar(self, atacar):
        self._atacar = atacar

    @property
    def defender(self):
        return self._defender

    @defender.setter
    def defender(self, defender):
        self._defender = defender

    @property
    def powerup(self):
        return self._porwerup

    @powerup.setter
    def powerup(self, powerup):
        self._powerup = powerup

    @property
    def habilidade_especial(self):
        return self._habilidade_especial

    @habilidade_especial.setter
    def habilidade_especial(self, habilidade_especial):
        self._habilidade_especial = habilidade_especial
