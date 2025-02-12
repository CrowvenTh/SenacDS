# ⚙️ Desenvolvedor de Sistemas 🖥️

Repositório destinado as atividades realizadas no curso de Desenvolvimento de sistemas no SENAC Taguatinga

---
### 🗂️ Material

<details>
    <summary> 🔗 Conteúdo </summary>

- 📁 <a href="algoritmo/Material/python_aula01.pdf">Lógica & interpretadores </a> 
- 📁 <a href="algoritmo/Material/python_aula02.pdf">Operadores Lógicos </a> 
- 📁 <a href="algoritmo/Material/python_aula03.pdf">Tipos de dados & condicionais </a> 
- 📁 <a href="algoritmo/Material/python_aula04.pdf"> Variáveis & Exercicios</a> 

---
  
</details>

### 🧮 Aulas

<details>
    <summary> 💠 Aula 1 - Introdução a python 🐍 </summary>

#### upper(): converte todas as letras para maiúsculas
~~~~ python
print(texto.upper())
~~~~

#### lower(): converte todas as letras para minúsculas
~~~~ python
print(texto.lower())
~~~~

#### capitalize(): converte a primeira letra para maiúscula e o restante para minúscula
~~~~ python
print(texto.capitalize())
~~~~

#### strip(): remove espaços em branco do início e do final da string
~~~~ python
print(texto.strip())
~~~~

#### replace(): substitui parte da string por outra
~~~~ python
print(texto.replace("Mundo", "Planeta"))
~~~~

#### sep: não é um método de string, é usado para definir o separador em print
~~~~ python
print("Python", "é", "uma", "linguagem", "fantástica", sep="-")
~~~~

#### count(): conta quantas vezes um determinado elemento aparece na string
~~~~ python
print(texto.count("o"))
~~~~

#### join(): junta os elementos de uma lista em uma única string usando um separador
~~~~ python
lista = ["maçã", "banana", "laranja"]
print(", ".join(lista))
~~~~

#### split(): divide a string em uma lista de substrings usando um separador
~~~~ python
print(texto.split(", "))
~~~~

#### len(): retorna o comprimento da string
~~~~ python
print(len(texto))
~~~~

#### type(): retorna o tipo de dado de uma variável
~~~~ python
print(type(texto))
~~~~

#### round()
~~~~ python
dividendo = 10
divisor = 3
resultado = dividendo / divisor
resultado_arredondado = round(resultado, 2)
~~~~

<p align="center"> 10/02/25 <p>

---

</details>


<details>
    <summary> 💠 Aula 2 - Exercicios de Lógica (1 a 12)📝 </summary>

## Exercicio #1 - Olá mundo!

#### imprima na tela a frase "Olá mundo!".    
~~~~ python
#Resolução:
print("olá mundo!")
~~~~

## Exercicio #2 - Imprimindo números

#### Crie um programa que imprima os números de 1 até 10.
~~~~ python

numero = [1,2,3,4,5,6,7,8,9,10]
print(numero)

# ou, usando while

numero = 1
while numero <= 10:
    print(numero)
    numero += 1
~~~~

## Exercicio #3 - Adição

#### Escreva um programa que calcule a soma de dois números.
~~~~ python
n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))

print(f"A soma de {n1} + {n2} é igual a {n1+n2}")
~~~~

## Exercicio #4 - Multiplicação
#### Escreva um programa que calcule a multiplicação de dois números.
~~~~ python
num1 = 7
num2 = 3

print(f"O resultado de {num1}x{num2} é igual a {num1 * num2}")
~~~~

## Exercicio #5 - Divisão
#### Escreva um programa que calcule a Divisão de dois números.
~~~~ python
n1 = 21
n2 = 3

print(f"{n1} dividido por {n2} é igual a {n1 // n2}")
~~~~

## Exercicio #6 - Subtração
#### Escreva um programa que calcule a subtração de dois números.
~~~~ python
n1 = int(input("Insira o primeiro numero: "))
n2 = int(input("Insira o segundo numero: "))

print(f"{n1} - {n2} é igual a {n1 - n2}")
~~~~

## Exercicio #7 - Indice de string

- [Início:fim:passo] é uma forma de pegar uma parte de uma sequência, como uma string ou lista. Você pode usá-lo para:
  
- Se você usar apenas [::], isso copiará toda a sequência.

- Adicionando um número após o segundo dois pontos (por exemplo, [::2]), você selecionará elementos com um certo intervalo.
  
- Usando [::-1], você pode inverter a sequência.

- Use colchetes [ ] para acessar elementos individuais de uma string por meio de sua posição (índice).

- Lembre-se de que a indexação em Python começa em 0, ou seja, o primeiro caractere de uma string está no índice 0, o segundo no índice 1 e assim por diante.

- Você pode usar índices negativos para contar a partir do final da string. -1 refere-se ao último caractere, -2 ao penúltimo e assim por diante.

---

#### 1 - Dada a string "Python", imprima o primeiro caractere.
~~~~ python
string1 = "python"
print("#1 ", string1[0])
~~~~

#### 2 - Dada a string "Hello, World!", imprima o caractere "W".
~~~~ python
string2 = "Hello, world!"
print("#2 ", string2[-6])
~~~~

#### 3 - Dada a string "Data Science", imprima os três primeiros caracteres.
~~~~ python
string3 = "Data Science"
print("#3 ",string3[:3])
~~~~

#### 4 - Dada a string "Machine Learning", imprima os três últimos caracteres.
~~~~ python
string4 = "Machine Learning"
print("#4 ", string4[-3:])
~~~~

## Exercicio #8 - String de indice impar
#### Dada a string "Artificial Intelligence", imprima os caracteres nos índices ímpares.
~~~~ python
string = "Artificial Intelligence"

for i in range(1, len(string), 2):
    print(string[i], end=" ")
    
~~~~

## Exercicio #9 - String de indice par
#### Dada a string "Artificial Intelligence", imprima os caracteres nos índices pares.
~~~~ python

string = "Artificial Intelligence"

for i in range(0, len(string), 2):
    print(string[i], end=" ")
    
~~~~

## Exercicio #10 - Upper
#### Escreva um programa em Python que utilize a variável texto= "Olá mundo!" e imprima o texto em letras maiúsculas.
~~~~ python
texto = "Olá mundo!"

print(texto.upper())
~~~~

## Exercicio #11 - Lower
#### Defina a variável texto com o valor "Olá mundo!".
- Utilize o método lower() para converter todo o texto em letras minúsculas.
- Imprima o texto convertido em letras minúsculas.
~~~~ python
word = "Olá mundo!"

print(word.lower())
~~~~

## Exercicio #12 - capitalize
#### Escreva um programa em Python que utilize a variável texto= "olá mundo!" e imprima a primeira letra do texto em maiúscula.
- Defina a variável texto com o valor "olá mundo!".
- Utilize o método capitalize() para capitalizar a primeira letra do texto.
- Imprima o texto capitalizado.

~~~~ python

palavra = "olá mundo"

print(palavra.capitalize())
~~~~


<p align="center"> 11/02/25 <p>
</details>


<details>
    <summary> 💠 Aula 3 - Exercicios de Lógica II (13 a 20)📝 </summary>

## Exercicio #13 - strip
#### Escreva um programa em Python que remove os espaços em branco do início e do final de uma variável frase =  " Hoje a noite está ótima ". Após remover os espaços em branco do início e do final, exiba o conteúdo da variável frase.

~~~~ python
frase = " Hoje a noite está ótima "
print(frase.strip())
~~~~
#### resultado: 
    Hoje a noite está ótima

## Exercicio #14 - Strip & replace
#### Escreva um programa em Python que realize as seguintes operações em uma frase pré-definida:

- A frase fornecida é: " O dia está bom, mas o tempo está chuvoso. "

- Remova quaisquer espaços em branco extras no início e no final da frase.

- Substitua todas as ocorrências da palavra "bom" por "ótimo".

- Ao final, o programa deve exibir a frase sem espaços extras e com as substituições realizadas.

~~~~ python
frase =  " O dia está bom, mas o tempo está chuvoso. "
print(frase.strip().replace("bom", "ótimo"))
~~~~
#### resultado:
    O dia está ótimo, mas o tempo está chuvoso. 

## Exercicio #15 - input com String
#### Instruções
O comando input() é usado para receber entrada do usuário em um programa Python. Ele solicita que o usuário insira algum valor a partir do teclado.

Exemplo:
~~~~ python
nome = input("Por favor, insira seu nome: ")
~~~~~
É importante notar que o input() sempre retorna uma string, então se você precisa de um número, deve converter o valor retornado para o tipo numérico apropriado (por exemplo, usando int() ou float()).

    str(valor): Converte o valor para uma string.
    int(valor): Converte uma string em um número inteiro.
    float(valor): Converte o valor para um número de ponto flutuante.

Escreva um programa em Python que solicite ao usuário para inserir seu nome. O programa deve exibir uma mensagem de boas-vindas personalizada, incluindo o nome inserido pelo usuário.

~~~~ python
nome = input("Bem vindo, insira seu nome: ")
print("O nome inserido foi:",nome)
~~~~
#### resultado
    Bem vindo, insira seu nome: Thiago 
    O nome inserido foi:  Thiago

## Exercicio #16 - input com adição
#### Instruções
O comando input() é usado para receber entrada do usuário em um programa Python. Ele solicita que o usuário insira algum valor a partir do teclado.

Exemplo:
~~~~ python
nome = input("Por favor, insira seu nome: ")
~~~~
É importante notar que o input() sempre retorna uma string, então se você precisa de um número, deve converter o valor retornado para o tipo numérico apropriado (por exemplo, usando int() ou float()).

    str(valor): Converte o valor para uma string.
    int(valor): Converte uma string em um número inteiro.
    float(valor): Converte o valor para um número de ponto flutuante.

Escreva um programa em Python que peça ao usuário para inserir dois números e calcule a soma desses números. Em seguida, exiba o resultado da soma.

~~~~ python
n1 = int(input("Insira o primeiro numero: "))
n2 = int(input("Insira o segundo numero: "))
soma = (n1 + n2)

print(f"{n1} + {n2} é igual a {soma}")
~~~~
#### resultado:
    Insira o primeiro numero: 21
    Insira o segundo numero: 7
    21 + 7 é igual a 28

## Exercicio #17 - input com subtração
#### Instruções
O comando input() é usado para receber entrada do usuário em um programa Python. Ele solicita que o usuário insira algum valor a partir do teclado.

Exemplo:
~~~~ python
nome = input("Por favor, insira seu nome: ")
~~~~
É importante notar que o input() sempre retorna uma string, então se você precisa de um número, deve converter o valor retornado para o tipo numérico apropriado (por exemplo, usando int() ou float()).

    str(valor): Converte o valor para uma string.
    int(valor): Converte uma string em um número inteiro.
    float(valor): Converte o valor para um número de ponto flutuante.

Escreva um programa em Python que peça ao usuário para inserir dois números e calcule a subtração do segundo número pelo primeiro. Em seguida, exiba o resultado da subtração.

~~~~ python
n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))
sub = (n1 - n2)

print(f"{n1} - {n2} é igual a {sub}")
~~~~
#### resultado:
    Insira o primeiro número: 28
    Insira o segundo número: 7
    28 - 7 é igual a 21

## Exercicio #18 - input com divisão e arredondamento
#### Instruções
O comando input() é usado para receber entrada do usuário em um programa Python. Ele solicita que o usuário insira algum valor a partir do teclado.

Exemplo:
~~~~ python
nome = input("Por favor, insira seu nome: ")
~~~~

É importante notar que o input() sempre retorna uma string, então se você precisa de um número, deve converter o valor retornado para o tipo numérico apropriado (por exemplo, usando int() ou float()).

    str(valor): Converte o valor para uma string.
    int(valor): Converte uma string em um número inteiro.
    float(valor): Converte o valor para um número de ponto flutuante.

Escreva um programa em Python que peça ao usuário para inserir dois números e calcule a divisão do primeiro número pelo segundo número. Certifique-se de verificar se o segundo número não é zero antes de realizar a divisão. Em seguida, exiba o resultado da divisão.

    #Arredondar
    dividendo = 10
    divisor = 3
    resultado = dividendo / divisor

    resultado_arredondado = round(resultado, 2)

    print("O resultado da divisão é:", resultado_arredondado)

~~~~ python
n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))

divArredondada = round(n1 / n2, 2)

print(f"{n1} dividido por {n2} é igual a {divArredondada}")
~~~~
#### resultado :
    Insira o primeiro número: 21.0
    Insira o segundo número: 3.0
    21 dividido por 3 é igual a 7.0

## Exercicio #19 - input com multiplicação
#### Instruções
O comando input() é usado para receber entrada do usuário em um programa Python. Ele solicita que o usuário insira algum valor a partir do teclado.

Exemplo:
~~~~ python
nome = input("Por favor, insira seu nome: ")
~~~~

É importante notar que o input() sempre retorna uma string, então se você precisa de um número, deve converter o valor retornado para o tipo numérico apropriado (por exemplo, usando int() ou float()).

            str(valor): Converte o valor para uma string.
            int(valor): Converte uma string em um número inteiro.
            float(valor): Converte o valor para um número de ponto flutuante.

Escreva um programa em Python que peça ao usuário para inserir dois números reais e calcule o produto desses números. Em seguida, exiba o resultado da multiplicação.

~~~~ python
number1 = int(input("Insira o primeiro número: "))
number2 = int(input("Insira o segundo número: "))
produto = (number1 * number2)

print(f"{number1} X {number2} é igual a {produto}")
~~~~
#### resultado:
    Insira o primeiro número: 7
    Insira o segundo número: 3
    7 x 3 é igual a 21

## Exercicio 20 - sep
#### Escreva um programa em Python que solicite ao usuário informações sobre uma data (dia, mês e ano) e utilize o parâmetro sep na função print() para imprimir a data no formato "DD/MM/AAAA".
    Dia = 10
    Mês = 5
    Ano = 2014
    Exemplo: print(a , b , c ,sep='-')

~~~~ python
day = int(input("Insira o dia: "))
month = int(input("Insira o mês: "))
year = int(input("Insira o ano: "))

print(day, month, year, sep="/")

~~~~
#### resultado:
    Insira o dia: 12
    Insira o mês: 02
    Insira o ano: 2025
    12/2/2025

<br>
<p align="center"> 12/02/25 <p>
</details>

---
<br>
<p align="center">@2025</p>