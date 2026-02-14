import random

angka_rahasia = random.randint(1, 10)
tebakan = int(input("Tebak angka (1-10): "))

if tebakan == angka_rahasia:
    print("Benar!")
else:
    print("Salah. Angka yang benar:", angka_rahasia)
