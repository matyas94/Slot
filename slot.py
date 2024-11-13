import random
import time
import os
egyenleg = 100
jatek = input("Mit szeretnél játszan? (slot)\n")
ujra = "y"
while jatek == "slot" and ujra == "y":
    os.system('cls')
    slot = 0

    segy = random.randint(1,9)
    sketto = random.randint(1,9)
    sharom = random.randint(1,9)

    ssegy = random.randint(1,9)
    ssketto = random.randint(1,9)
    ssharom = random.randint(1,9)

    slista = [segy, sketto, sharom,]
    sslista = [ssegy, ssketto, ssharom,]
    print(f"Egyenleg: {egyenleg}\n")
    bet = int(input("\nMennyit szeretnél rakni? "))

    while bet > egyenleg:
        print("Nem tudsz ennyit rakni.")
        bet = int(input("Mennyit szeretnél rakni? "))
    
    egyenleg -= bet

    for i in range(0,2):
        if slista[i] != sslista[i]:
            slot += 1

    while slot <= 9:
        os.system('cls')
        print(f"Egyenleg: {egyenleg}\n")
        print(f"{"-"*13}\n| {sslista[0]} | {sslista[1]} | {sslista[2]} |\n{"-"*13}")

        for i in range(0,2):
            if slista[i] == sslista[i]:
                slot += 1
            else:
                sslista[i] += 1

        if sslista[0] > 9:
            sslista[0] -= 9
        if sslista[1] > 9:
            sslista[1] -= 9
        if sslista[2] > 9:
            sslista[2] -= 9

        time.sleep(1)

    sssegy = sslista[0]
    sssketto = sslista[1]
    sssharom = sslista[2]
    os.system('cls')
    if sssegy == sssketto and sssketto == sssharom:
        egyenleg += (bet*10)
        print(f"Egyenleg: {egyenleg}\n")
        print("Big win")
    elif sssegy == sssketto or sssketto == sssharom or sssegy == sssharom:
        egyenleg += (bet*2)
        print(f"Egyenleg: {egyenleg}\n")
        print("smol win")
    else:
        print(f"Egyenleg: {egyenleg}\n")
        print("lose")
    time.sleep(1)

    ujra = input("\nSzeretnél még játszani?(y/n)\n")