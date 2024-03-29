import random
import time 

print("Bem vindo ao jogo de adivinhação")

numeroSecreto = random.randrange(1,101)
pontos = 1000
tempoDeJogo = 0

print("Qual o nível de dificuldade? \n(1) Fácil (2) Médio (3) Difícil")

startCronometro = time.time()

def obterDificuldade():
    while True:
        try:
            
            dificuldade = int(input("Defina o nível: "))
            
            if dificuldade in [1,2,3]:
                return dificuldade
            else: 
                print("Insira um número de 1 a 3!")
        
        except ValueError: 
            print("Valor inválido! Insira um número de 1 a 3.")  

nivel = obterDificuldade()

if(nivel == 1):
    totalDeTentativas = 10
elif(nivel == 2):
    totalDeTentativas = 7
else:
    totalDeTentativas = 5

contagemDoTempo = time.time()


for rodada in range (1, totalDeTentativas + 1): 

    print("\n \ntentativa {} de {}".format(rodada, totalDeTentativas))
    
    chute_str = input("Digite o seu número de 1 a 100: ")
   #print("você digitou {}\n".format(chute_str))
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numeroSecreto
    maior = chute > numeroSecreto
    menor = chute < numeroSecreto

    pontosPerdidos = abs(numeroSecreto - chute)
    
    if(acertou):
        print("****************\nPARABÉNS! VOCÊ ACERTOU\n****************")
        break

    else:
        pontos -= pontosPerdidos + 5

        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto") 
        
fimDaContagem = time.time()

tempoDeJogo = abs(int(startCronometro - fimDaContagem)) 
pontos -= (tempoDeJogo + 10)

print("Fim de jogo\nVocê fez {} pontos".format(pontos))
