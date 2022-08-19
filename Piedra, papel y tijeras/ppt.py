import random
plays= ['Piedra', 'Papel', 'Tijera']


def juego():
    ia= random.choice(plays)
    print('1. Piedra\n2. Papel\n3. Tijera')
    play= int(input())
    o= play
    if o <= 3 and o >= 1:
        play= plays[play-1]
        if play == 'Piedra' and ia == 'Piedra':
            print('PC: '+ia+'\nTu: '+play+'\n---> Empate <---')

        elif play == 'Papel' and ia == 'Papel':
            print('PC: '+ia+'\nTu: '+play+'\n---> Empate <---')

        elif play == 'Tijera' and ia == 'Tijera':
            print('PC: '+ia+'\nTu: '+play+'\n---> Empate <---')

        elif play == 'Papel' and ia == 'Piedra':
            print('PC: '+ia+'\nTu: '+play+'\n---> Ganaste <---')

        elif play == 'Piedra' and ia == 'Papel':
            print('PC: '+ia+'\nTu: '+play+'\n---> Perdiste <---')

        elif play == 'Papel' and ia == 'Tijera':
            print('PC: '+ia+'\nTu: '+play+'\n---> Perdiste <---')
            
        elif play == 'Piedra' and ia == 'Tijera':
            print('PC: '+ia+'\nTu: '+play+'\n---> Ganaste <---')

        elif play == 'Tijera' and ia == 'Piedra':
            print('PC: '+ia+'\nTu: '+play+'\n---> Perdiste <---')

        elif play == 'Tijera' and ia == 'Papel':
            print('PC: '+ia+'\nTu: '+play+'\n---> Ganaste <---')
    else:
        print('ERROR')
    repetir()

def repetir():
    print('y para jugar f para terminar')
    p_again= input()
    if p_again == 'y':
        juego()
    elif p_again == 'f':
        print('Adios')
    else:
        print('ERROR')

repetir()