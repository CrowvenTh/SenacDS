# Imprima os números pares de 1 a 20

for i in range(1, 21):
    if(i % 2 == 0):
        print(i)

# ou da segunda forma para mostrar em apenas uma linha no terminal

concaten = ""
for i in range(1, 21):
    if(i % 2 == 0):
        concaten += str(i) + ", "
print(concaten)        