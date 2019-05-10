
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:14:42 2019

"""
from Class_Jogador import Jogador
from Class_Time import Time
import random

lista_jogadores = [{"nome" : 'Tiago_Volpi',
    "ataque" : 10  ,  
    "defesa" : 75,
    "overall" : 42.5,
  },
    {"nome" : 'Hudson',
    "ataque": 60,
    "defesa" : 60,
    "overall": 60,
  },
    {"nome" : 'Arboleda',
    "ataque": 20,
    "defesa": 70,
    "overall":  45,
  },
    {"nome" : 'Bruno_Alves',
    "ataque": 10,
    "defesa": 60,
    "overall": 35,
  },
    {"nome" : 'Reinaldo',
    "ataque": 50,
    "defesa": 50,
    "overall": 50,
  },
    {"nome" : "Liziero",
    "ataque": 40,
    "defesa":55,
    "overall": 47.5,
    
  },
    {"nome" : "Tche Tche",
    "ataque": 50,
    "defesa":50,
    "overall": 50,
    
  } ,   
    {"nome" : "Everton",
    "ataque": 55,
    "defesa":10,
    "overall": 32.5,
    
  },
    {"nome" : "Anthony",
    "ataque": 70,
    "defesa": 10,
    "overall": 40,
    
  },
    {"nome" : "Toro",
    "ataque": 60,
    "defesa":5,
    "overall": 32.5,
    
  },
    {"nome" : "Pato",
    "ataque": 80,
    "defesa":5,
    "overall": 42.5,
    
  },
    #SANTOS
    {"nome" : "Vanderlei",
    "ataque": 5,
    "defesa":80,
    "overall": 42.5,
    
  },
    {"nome" : "Felipe Aguilar",
    "ataque": 10,
    "defesa":70,
    "overall": 40,
    
  },
    {"nome" : "Lucas Verissimo",
    "ataque": 5,
    "defesa":65,
    "overall": 35,
    
  },
    {"nome" : "Gustavo Henrique",
    "ataque": 10,
    "defesa":70,
    "overall": 40,
    
  },
    {"nome" : "Victor Ferraz",
    "ataque": 50,
    "defesa":40,
    "overall": 45,
    
  },
    {"nome" : "Diego Pituca",
    "ataque": 50,
    "defesa":35,
    "overall": 42.5,
    
  },
    {"nome" : "Carlos Sanchez",
    "ataque": 70,
    "defesa":40,
    "overall": 55,
    
  },
    {"nome" : "Jean Mota",
    "ataque": 60,
    "defesa":30,
    "overall": 45,
    
  },
    {"nome" : "Jorge",
    "ataque": 50,
    "defesa":40,
    "overall": 45,
    
  },
    {"nome" : "Soteldo",
    "ataque": 60,
    "defesa":5,
    "overall": 32.5,
    
  },
    {"nome" : "Rodrygo",
    "ataque": 70,
    "defesa":10,
    "overall": 40,
    
  },
    #PALMEIRAS
    {"nome" : "Weverton",
    "ataque": 5,
    "defesa": 70,
    "overall": 37.5,
    
  },
    {"nome" : "Mayke",
    "ataque": 40,
    "defesa": 55,
    "overall": 47.5,
    
  },
    {"nome" : "Gustavo Gomez",
    "ataque": 15,
    "defesa": 75,
    "overall": 45,
    
  },
    {"nome" : "Luan",
    "ataque": 10,
    "defesa": 70,
    "overall": 40,
    
  },
    {"nome" : "Victor Luis",
    "ataque": 40,
    "defesa": 45,
    "overall": 42.5,
    
  },
    {"nome" : "Felipe Melo",
    "ataque": 35,
    "defesa": 65,
    "overall": 50,
    
  },
    {"nome" : "Bruno Henrique",
    "ataque": 50,
    "defesa": 50,
    "overall": 50,
    
  },
    {"nome" : "Ze Rafael",
    "ataque": 55,
    "defesa": 30,
    "overall": 42.5,
    
  },
    {"nome" : "Gustavo Scarpa",
    "ataque": 70,
    "defesa": 20,
    "overall": 45,
    
  },
   {"nome" : "Dudu",
    "ataque": 80,
    "defesa": 20,
    "overall": 50,
    
  },
    {"nome" : "Deyverson",
    "ataque": 65,
    "defesa": 10,
    "overall": 37.5,
    
  },
    #CORINTHIANS
    {"nome" : "Cassio",
    "ataque": 5,
    "defesa": 70,
    "overall": 37.5,
    
  },
    {"nome" : "Fagner",
    "ataque": 50,
    "defesa": 50,
    "overall": 50,
    
  },
    {"nome" : "Henrique",
    "ataque": 10,
    "defesa": 60,
    "overall": 35,
    
  },
    {"nome" : "Manoel",
    "ataque": 5,
    "defesa": 55,
    "overall": 30,
    
  },
    {"nome" : "Danilo Avelar",
    "ataque": 30,
    "defesa": 30,
    "overall": 30,
    
  },
    {"nome" : "Ralf",
    "ataque": 25,
    "defesa": 55,
    "overall": 40,
    
  },
    {"nome" : "Richard",
    "ataque": 30,
    "defesa": 40,
    "overall": 35,
    
  },
    {"nome" : "Junior Sornoza",
    "ataque": 55,
    "defesa": 25,
    "overall": 40,
    
  },
    {"nome" : "Clayson",
    "ataque": 50,
    "defesa": 5,
    "overall": 27.5,
    
  },
    {"nome" : "Pedrinho",
    "ataque": 55,
    "defesa": 5,
    "overall": 30,
    
  },
    {"nome" : "Gustagol",
    "ataque": 55,
    "defesa": 5,
    "overall": 30,
    
  }]

jogadores = []
for jogador in lista_jogadores:
    novo_jogador = Jogador(jogador["nome"], jogador["ataque"],jogador["defesa"], jogador["overall"])
    jogadores.append(novo_jogador)
    
    
SaoPaulo = Time(jogadores[0:11], "Sao Paulo", 0)
Santos = Time(jogadores[11:22], "Santos",0)
Palmeiras = Time(jogadores[22:33], "Palmeiras",0)
Corinthians = Time(jogadores[33:45], "Corinthians",0)


def partida(time1, time2):
    i = 0
    time1.gol = 0
    time2.gol = 0
    vencedor = 0
    while i <= 90:
        if random.randint(0, (time1.calcula_ataque()+time2.calcula_defesa())) > time1.calcula_ataque():
            if random.randint(1,15)> 14:
                time1.gol += 1
                print(i,"':","Gol do", time1.nome,"!")
                print(time1.gol, "x", time2.gol)
        if random.randint(0, (time1.calcula_ataque()+time2.calcula_defesa())) <= time1.calcula_ataque():
            if random.randint(1,15)> 14:
                time2.gol += 1
                print(i,"':","Gol do", time2.nome,"!")
                print(time1.gol, "x", time2.gol)
        i = i + 1
        
    if time1.gol > time2.gol:
        vencedor = time1.nome
    elif time2.gol > time1.gol:
        vencedor = time2.nome
    else:
        vencedor = "empate"
    return vencedor

partida(Santos, Palmeiras)





            
    
     