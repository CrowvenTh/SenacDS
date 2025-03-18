# Dada a string "Artificial Intelligence", imprima os caracteres nos índices pares.

string = "Artificial Intelligence"

for i in range(0, len(string), 2):
    print(string[i], end=" ")
    