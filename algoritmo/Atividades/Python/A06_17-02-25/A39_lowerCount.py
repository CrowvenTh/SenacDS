# Faça um programa que transforme um texto todo em letras minúsculas e conte quantas letras 'e' ele possui.

texto = input("Digite um texto: ").lower()
contE = texto.count("e")
if contE > 0:
    print(f"O texto '{texto}' contém {contE} letras 'e' ")
else: 
    print(f"O texto '{texto}' contém {contE} letras 'e' ")