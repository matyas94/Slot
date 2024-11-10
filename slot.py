import random
import time
import os
os.system('cls')
slot = 0

segy = random.randint(1,9)
sketto = random.randint(1,9)
sharom = random.randint(1,9)
snegy = random.randint(1,9)
sot = random.randint(1,9)
shat = random.randint(1,9)
shet = random.randint(1,9)

ssegy = random.randint(1,9)
ssketto = random.randint(1,9)
ssharom = random.randint(1,9)
ssnegy = random.randint(1,9)
ssot = random.randint(1,9)
sshat = random.randint(1,9)
sshet = random.randint(1,9)

slista = [segy, sketto, sharom, snegy, sot, shat, shet]
sslista = [ssegy, ssketto, ssharom, ssnegy, ssot, sshat, sshet]

for i in range(1,7):
    if slista[i] != sslista[i]:
        slot += 1

while slot <= 9:
    os.system('cls')
    print(f"{"-"*13}\n| {sslista[0]} | {sslista[1]} | {sslista[2]} |\n{"-"*13}")

    for i in range(1,7):
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
    if sslista[3] > 9:
        sslista[3] -= 9
    if sslista[4] > 9:
        sslista[4] -= 9
    if sslista[5] > 9:
        sslista[5] -= 9
    if sslista[6] > 9:
        sslista[6] -= 9

    time.sleep(1)
    
    