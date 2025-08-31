from secrets import *
from string import *

mot = ""
alphabet = ascii_letters + digits + punctuation

a = int(input("Quel nombres de caractères veux tu ? "))

for i in range(a):
    mot += choice(alphabet)
print(mot)
