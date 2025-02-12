# Escreva um programa em Python que realize as seguintes operações em uma frase pré-definida:
# A frase fornecida é: " O dia está bom, mas o tempo está chuvoso. "
# Remova quaisquer espaços em branco extras no início e no final da frase.
# Substitua todas as ocorrências da palavra "bom" por "ótimo".
# Ao final, o programa deve exibir a frase sem espaços extras e com as substituições realizadas.

frase =  " O dia está bom, mas o tempo está chuvoso. "
print(frase.strip().replace("bom", "ótimo"))