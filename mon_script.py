def fonction_lente():
    total = 0
    for i in range(10000000):
        total += i
    return total

if __name__ == "__main__":
    print("Début du programme")
    fonction_lente()
    print("Fin du programme")