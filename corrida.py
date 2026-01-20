import random
import time

class Personagens:
    def __init__(self, nome, simbolo, distancia):
        self.nome = nome
        self.simbolo = simbolo
        self.distancia = distancia 

    def avancar(self):
       
        self.distancia += random.randint(1, 4)

    def mostrar_pista(self, meta):
       
        caminho_feito = "-" * self.distancia
        
        caminho_falta = "-" * max(0, meta - self.distancia)
        
        print(f"{self.nome} {caminho_feito}{self.simbolo}{caminho_falta} | META")

corredores = [
    Personagens("Cadeirante", "👨🏼‍🦼‍➡️", 0),
    Personagens("Nadador", "🚣🏻", 0),
    Personagens("Arbitro", "👩🏼‍🦯‍➡️", 0)
]

meta = 25
vencedor = False

print("A CORRIDA VAI COMECAR !!")
time.sleep(1)

while not vencedor:
    print("boa sorte") 

    for p in corredores:
        p.avancar()
        p.mostrar_pista(meta)

       
        if p.distancia >= meta:
            print(f"\n🏆 O VENCEDOR FOI: {p.nome} {p.simbolo}")
            vencedor = True
            break
    
    time.sleep(0.4) 
