import random
import time
import os
slots = int(input("Mekkora gépen szeretnél játszani?(3,5,7) "))
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

for i in range(0,2):
    if slista[i] != sslista[i]:
        slot += 1

while slot <= 9:
    os.system('cls')
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

if sssegy == sssketto and sssketto == sssharom:
    print("Big win")
elif sssegy == sssketto or sssketto == sssharom or sssegy == sssharom:
    print("smol win")
else:
    print("lose")