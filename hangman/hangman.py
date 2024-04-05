def jogar():

    print("###########################\nBem vindo ao jogo da forca!\n###########################")

    palavra_secreta = "pessego".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = input("Digite a próxima letra: ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0 
            for letra in palavra_secreta: 
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
        
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Voce ganhou!!")
    else:
        print("Você perdeu!!")
    
    print("Fim de jogo")


jogar()
