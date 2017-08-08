import random#import random gerar números aleatórios.


palavras = ['banana, manga, uva, laranja, morango']
letrasErradas = ''
letrasCertas = ''
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def inserir():
    while True:
        x = input("tilta ai, passa as palavras jajá tem mais tilta não: ")
        palavras.append(x)
        if x == '':
            break
def principal():#def cria uma função.
    """
    Função Princial do programa
    """
    print('F O R C A')#print exibe na tela o valor tipo string que está entre parênteses.
    inserir()

    
    palavraSecreta = sortearPalavra()
    palpite = ''
    desenhaJogo(palavraSecreta,palpite)

    while True:# while True é um Lopp infinito, que é executado enquanto for verdadeira.
        palpite = receberPalpite() 
        desenhaJogo(palavraSecreta,palpite)
        if perdeuJogo():#if é se
            print('Voce Perdeu!!!')#print exibe na tela o valor tipo string que está entre parênteses.
            break#break para e sair do Lopp while.
        if ganhouJogo(palavraSecreta):
            print('Voce Ganhou!!!')#print exibe na tela o valor tipo string que está entre parênteses.
            break#break para e sair do Lopp while.            
        
def perdeuJogo():#def cria uma função.
    global FORCAIMG#global faz referência a não local.
    if len(letrasErradas) == len(FORCAIMG):#if é se
        return True
    else:#else é se não.
        return False#return retorna pra quem chamou.
    
def ganhouJogo(palavraSecreta):#def cria uma função.
    global letrasCertas
    ganhou = True
    for letra in palavraSecreta:#for incrementar algo.
        if letra not in letrasCertas:
            ganhou = False 
    return ganhou#return retorna pra quem chamou.        
        


def receberPalpite():#def cria uma função.
    
    palpite = input("Adivinhe uma letra: ")#input espera o usuário digitar um textos no teclado e pressionar ENTER.
    palpite = palpite.upper()
    if len(palpite) != 1:#len vai contar quantas coisas tem em uma lista.
        print('Coloque um unica letra.')
    elif palpite in letrasCertas or palpite in letrasErradas:#elif será execultado somente quando todas as condições anteriores forem Falsas.
        print('Voce ja disse esta letra.')
    elif not "A" <= palpite <= "Z":#elif será execultado somente quando todas as condições anteriores forem Falsas.
        print('Por favor escolha apenas letras')
    else:#else é se não.
        return palpite#return retorna pra quem chamou.
    
    
def desenhaJogo(palavraSecreta,palpite):#def cria uma função.
    global letrasCertas#global faz referência a não local.
    global letrasErradas#global faz referência a não local.
    global FORCAIMG#global faz referência a não local.

    print(FORCAIMG[len(letrasErradas)])#print exibe na tela o valor tipo string que está entre parênteses.
    
     
    vazio = len(palavraSecreta)*'-'#len vai contar quantas coisas tem em uma lista.
    
    if palpite in palavraSecreta:#if é se
        letrasCertas += palpite
    else:#else é se não.
        letrasErradas += palpite

    for letra in letrasCertas:#for incrementar algo.
        for x in range(len(palavraSecreta)):#for define o início e fim, um incremento e possibilidades da variavel.
            if letra == palavraSecreta[x]:#if é se
                vazio = vazio[:x] + letra + vazio[x+1:]
                
    print('Acertos: ',letrasCertas )#print exibe na tela o valor tipo string que está entre parênteses.
    print('Erros: ',letrasErradas)#print exibe na tela o valor tipo string que está entre parênteses.
    print(vazio)#print exibe na tela o valor tipo string que está entre parênteses.
     

def sortearPalavra():#def cria uma função.
    global palavras#global faz referência a não local.
    return random.choice(palavras).upper()#return retorna pra quem chamou.

    
principal()
