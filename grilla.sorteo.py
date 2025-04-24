import random

def generar_grilla():
    grilla = []
    for i in range(46):
        grilla.append(i)
    return grilla
    
def generar_jugador():
    return random.sample(range(46),6)

def sorteo_quini6(grilla, player1, player2):
    sorteo = []
    while grilla and player1 and player2:
        numero_sorteo = random.choice(grilla)
        sorteo.append(numero_sorteo)
        print(f"numero sorteado: {numero_sorteo}")
        
        if numero_sorteo in player1:
            player1.remove(numero_sorteo)
            print("player1 tenia el numero")
            
        if numero_sorteo in player2:
            player2.remove(numero_sorteo)
            print("player2 tenia el numero")
        grilla.remove(numero_sorteo)
    return sorteo, player1, player2
    
    
def mostrar_resultados(sorteo, player1, player2):
    print("\n Numeros sorteados:", sorteo)
    print("player1 restantes:", player1)
    print("player2 restantes:", player2)
    
    if not player1 and not player2:
        print("empate")
    elif not player1:
        print("player1 gano")
    elif not player2:
        print("player2 gano")
    
def main():
    
    grilla = generar_grilla()
    player1 = generar_jugador()
    player2 = generar_jugador()
    
    print("player1: ", player1)
    print("player2:", player2)
    
    sorteo, restante1, restante2 = sorteo_quini6(grilla, player1, player2)
    mostrar_resultados(sorteo,restante1,restante2)
    
if __name__=="__main__":
    main()
    
    

    
    