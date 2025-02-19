# ⚙️ Desenvolvedor de Sistemas 🖥️

Repositório destinado as atividades realizadas no curso de Desenvolvimento de sistemas no SENAC Taguatinga

---
### 🗂️ Material de Apoio

<details>
    <summary> 🔗 Conteúdo </summary>

- 📁 <a href="algoritmo/Material/python_aula01.pdf">Lógica & interpretadores </a> 
- 📁 <a href="algoritmo/Material/python_aula02.pdf">Operadores Lógicos </a> 
- 📁 <a href="algoritmo/Material/python_aula03.pdf">Tipos de dados & condicionais </a> 
- 📁 <a href="algoritmo/Material/python_aula04.pdf"> Variáveis & Exercicios</a> 
- 💾 <a href="https://github.com/CrowvenTh/Santander-Python">Repositório de apoio</a>

---
  
</details>

### 🧮 Aulas

<details>
    <summary> 💠 Aula 1 - Introdução a python 🐍 </summary>

<br>
<p> 10/02/25 <p>

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
    <summary> 💠 Aula 2 - 📝 Exercicios de Lógica I (1 a 12) </summary>

<br>
<p> 11/02/25 <p>

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
    <summary> 💠 Aula 3 - 📝 Exercicios de Lógica II (13 a 21) </summary>

<br>
<p> 12/02/25 <p>

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

## Exercicio 20 - sep data
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

## Exercicio #21 - sep pessoa
#### Escreva um programa em Python que use o parâmetro sep na função print() para imprimir o nome, idade e altura de uma pessoa separados por um hífen.

~~~~ python
nome = str(input("Insira seu nome: "))
idade = int(input("Insira sua idade: "))
altura = float(input("Insira sua altura: "))

print(f"{nome} - {idade} - {altura}")
~~~~
#### resultado:
    Insira seu nome: Fulano
    Insira sua idade: 25
    Insira sua altura: 1.75
    Fulano - 25 - 1.75


<br>
<p align="center"> 12/02/25 <p>
</details>

<details>
    <summary> 💠 Aula 4 - 📝 Exercicios de Lógica III (22 a 26) </summary>

<br>
<p> 13/02/25 <p>

## Exercicio #22 - join
### 1 - Crie um programa em Python que aceite uma TUPLA de linguagens de programação e as junte em uma única String separada por hífens, verificar o tipo da variável antes e após a operação:

### Tupla -  É uma sequência de valores ordenados e imutáveis
~~~~ python
tupla = "Python", "Java", "C#", "C++", "PHP"
~~~~

#### resolução:
~~~~ python
tupla = "Python", "Java", "C#", "PHP"
print(tupla)
print(type(tupla))
tupla_join = "-".join(tupla)
print(tupla_join)
print(type(tupla_join))
~~~~
#### resultado: 
    ('Python', 'Java', 'C#', 'PHP')
    <class 'tuple'>
    Python-Java-C#-PHP
    <class 'str'>

### 2 - Crie um programa em Python que aceite uma Lista de linguagens de programação e as junte em uma  String separada por hífens, verificar o tipo da variável antes e após a operação: 

#### Lista -  É uma sequência de valores ordenados e mutáveis
~~~~ python
lista= ["Python", "Java", "C#", "C++", "PHP"]
~~~~ 

#### resolução:
~~~~ python
lista = ["Python", "Java", "C#", "PHP"]
print(lista)
print(type(lista))
lista_join = " - ".join(lista)
print(lista_join)
print(type(lista_join))
~~~~
#### resultado:
    ['Python', 'Java', 'C#', 'PHP']
    <class 'list'>
    Python - Java - C# - PHP
    <class 'str'>

### Instruções
Defina uma lista de linguagens de programação.
Utilize o método join() para juntar os elementos da lista/tupla em uma única String, separados por hífens.  

~~~~ python
x = " - ".join(lista)
~~~~
Imprima as Strings resultantes.

Para verificar o tipo de uma variável em Python, você pode usar a função embutida type(). Aqui está um exemplo:
~~~~ python
variavel = "Olá, mundo!"
print(type(variavel))  # Saída: <class 'str'>
~~~~

## Exercicio 23 - Split
#### Escreva um programa em Python que aceite uma sequência de linguagens de programação separadas por espaços. O programa deve dividir essa sequência em uma lista de linguagens individuais e imprimir a lista resultante. Ao final imprimir o tipo da variável.
~~~~ python
Linguagens  - "Python,Java,C#,C++,PHP"
~~~~~
Utilize o método split() para dividir a sequência em uma lista. split(", ")

    Split(",") - Determina o marcador de separação de palavras para compor lista

## ou 

~~~~ python
Linguagens  - "Python Java C# C++ PHP"
~~~~
Utilize o método split() para dividir a sequência em uma lista. split(" ")

    Split( ) - Determina o marcador de separação de palavras para compor lista

Imprima a lista resultante.

#### resolução:
~~~~ python
Linguagens = "Python Java C# C++ PHP"
l = Linguagens.split(" ")
print(l)
~~~~
### resultado:
    ['Python', 'Java', 'C#', 'C++', 'PHP']


## Exercicio #24 - len
#### Escreva um programa que solicite ao usuário para inserir uma palavra e imprima o número de caracteres na palavra, utilizando a função len().

Exemplo de saída:
~~~~ python
x = len(variável)
Digite uma palavra: Python
A palavra tem 6 caracteres.
~~~~ 

~~~~ python
var = str(input("Escreva uma palavra: "))

print(f"A palavra {var} tem {len(var)} caracteres")
~~~~
#### resultado:
    A palavra antonio tem 7 caracteres

## Exercicio #25 - Lista []
#### Crie um programa que receba a lista abaixo e imprima a linguaguem de programação:
~~~~ python
lista: ["Python","Java","C#","C++","PHP"]
print(lista[índice])
~~~~

#### resolução:
~~~~ python
lista = ["Python","Java","C#","C++","PHP"]
print(lista[1])
~~~~
#### resultado:
    Java

## Exercicio #26 - Tupla
#### Crie um programa que receba a tupla abaixo e imprima a linguem de programação: C++

    tupla: "Python","Java","C#","C++","PHP"

#### resolução: 
~~~~ python
tupla = "Python","Java","C#","C++","PHP"
print(tupla[3])
~~~~
#### resultado:
    C++


<br>
<p align="center"> 13/02/25 <p>
</details>

<details>
    <summary> 💠 Aula 5 - 📝 Exercicios de Lógica IV (27 a 35) </summary>

<br>
<p> 14/02/25 <p>

## Exercicio #27 - Format()
#### Escreva um programa em Python que utilize o método format() para formatar uma mensagem com informações pessoais. Você deve criar um dicionário chamado informacoes com as seguintes chaves e valores:

    Nome: "Ana"
    Idade: 35
    Cidade: "São Paulo"

Em seguida, utilize o método format() para imprimir uma mensagem no seguinte formato: "Olá, meu nome é [Nome], tenho [Idade] anos e moro em [Cidade].", onde [Nome], [Idade] e [Cidade] são espaços reservados que devem ser substituídos pelas informações contidas no dicionário informacoes.
Código Python que utiliza o método format() para formatar uma mensagem com informações pessoais:

    nome = "João"
    idade = 30

 Utilizando format() para inserir valores em uma string

    mensagem = "Olá, meu nome é {} e tenho {} anos.".format(nome, idade)
    print(mensagem)

### resolução: 
~~~~ python
Nome = input("Insira seu nome: ")
Idade = int(input("Insira sua idade: "))
Cidade = str(input("Digite uma cidade: "))

mensagem = "Olá, meu nome é {} e tenho {} anos, e moro em {}".format(Nome, Idade, Cidade)
print(mensagem)
~~~~

#### resultado: 
    Insira seu nome: Thiago
    Insira sua idade: 20
    Digite uma cidade: Belém
    Olá, meu nome é Thiago e tenho 20 anos, e moro em Belém

## Exercicio #28 - Format() II
#### Escreva um programa em Python que utilize o método format() para formatar uma mensagem com informações sobre um livro. Você deve criar variáveis para armazenar as seguintes informações:
- Título do livro: "O Pequeno Príncipe"
- Autor do livro: "Antoine de Saint-Exupéry"
- Ano de publicação: 1943
- Preço do livro (em reais): 39.90
Em seguida, utilize o método format() para imprimir uma mensagem no seguinte formato: "'{}' é um livro escrito por {}. Foi publicado em {} e custa R${}.". Substitua os espaços reservados pelos valores correspondentes das variáveis.

#### Definição de casas decimais
    
    print("A média das notas é: {:.2f}".format(media))

- : Indica o início da especificação de formatação.
- .2: Especifica o número de casas decimais que você deseja manter após o ponto decimal. No caso, .2 significa que você quer manter duas casas decimais.
- f: Indica que o valor a ser formatado é um número decimal (float).

### resolução: 
~~~~ python
lTitulo = "The witcher"
lAutor = "Andrzej Sapkowski"
anoPublicacao = 1990
lPreco = 79.90

livro = "'{}' é um livro escrito por {}. Foi publicado em {} e custa R${}.".format(lTitulo, lAutor, anoPublicacao, lPreco)
print(livro)
~~~~

#### resultado: 
    'The witcher' é um livro escrito por Andrzej Sapkowski. Foi publicado em 1990 e custa R$79.9.

## Exercicio #29 - Format() III
#### Escreva um programa em Python que utilize o método format() para formatar uma mensagem com informações sobre um produto. Você deve criar variáveis para armazenar as seguintes informações:
    
    Nome do produto: "Camiseta"
    Preço do produto: R$29.99
    Quantidade disponível: 100

Em seguida, utilize o método format() para imprimir uma mensagem no seguinte formato: 
    
    "Produto: [Nome], Preço: R$[Preço], Quantidade disponível: [Quantidade]. O valor total do estoque é R$[ValorEstoque]."

.Onde [Nome], [Preço] e [Quantidade] são espaços reservados que devem ser substituídos pelas informações corretas. Além disso, [ValorEstoque] representa o valor total do estoque, calculado multiplicando o preço pela quantidade disponível.

### resolução: 
~~~~ python
nomeProduto = "Camiseta"
precoProduto = 29.99
qtd = 100
valorEstoque = precoProduto * qtd

mensagem = "Produto: {}, Preço: R${}, Quantidade disponível: {}. O valor total do estoque é R${}.".format(nomeProduto, precoProduto, qtd, valorEstoque)
print(mensagem)
~~~~

#### resultado: 
    Produto: Camiseta, Preço: R$29.99, Quantidade disponível: 100. O valor total do estoque é R$2999.0.

## Exercicio #30 - F-String
#### Peça ao usuário para inserir seu nome. Em seguida, use uma f-string para exibir uma mensagem de saudação personalizada.

Solicita ao usuário que insira seu nome
    
    nome = input("Digite seu nome: ")

Exibe uma mensagem de saudação personalizada usando uma f-string

    mensagem = f"Olá, {nome}! Bem-vindo ao nosso programa."
    print(mensagem)

Casas decimais f" {valor:.2f}"

### resolução: 
~~~~ python
nome = input("Insira seu nome: ")
print(f"Olá {nome}, seja bem vindo!")
~~~~

#### resultado: 
    Insira seu nome: Thiago
    Olá Thiago, seja bem vindo!
    
## Exercicio #31 - f-string pessoa 
#### Peça ao usuário para inserir seu nome, idade e cidade. Em seguida, use uma f-string para exibir essas informações formatadas.
    
    nome = "João"
    idade = 30
    Cidade="Brasília"

### resolução: 
~~~~ python
nome =  input("insira seu nome: ")
idade = input("insira sua idade: ")
Cidade =  input("insira sua cidade: ")

print(f"Seu nome é {nome}, sua  idade é {idade} e você mora em {Cidade}")
~~~~

#### resultado: 

    insira seu nome: Thiago
    insira sua idade: 20
    insira sua cidade: Belém
    Seu nome é Thiago, sua  idade é 20 e você mora em Belém
    
## Exercicio #32 - condicional IF, ELSE
#### Utilizando if e else em Python:

    if condição:
        # Código a ser executado se a condição for verdadeira
    else:
        # Código a ser executado se a condição for falsa

Em Python, a indentação é fundamental para definir o bloco de código dentro das estruturas de controle. O código dentro do bloco if e else deve ser indentado para indicar que ele está condicionado àquela estrutura.

Os operadores de comparação (==, !=, <, >, <=, >=) são usados para comparar valores. Eles retornam True se a comparação for verdadeira e False caso contrário.

Você pode usar operadores lógicos (and, or, not) para combinar múltiplas condições em uma única instrução if.

Escreva um programa que solicite ao usuário para inserir dois números inteiros. O programa deve então verificar qual número é maior e imprimir uma mensagem correspondente.
    
### resolução: 
~~~~ python
num1 = int(input("Insira um número: "))
num2 = int(input("Insira outro número: "))

if num1 > num2:
    print(f"{num1} é maior que {num2}")
elif(num1 == num2):
    print(f"{num1} é igual a {num2}")
else: 
    print(f"{num1} é menor que {num2}")
~~~~

#### resultado: 
    
    Insira um número: 21
    Insira outro número: 07
    21 é maior que 7

## Exercicio #33 - Número positivo
#### Escreva um programa em Python que verifique se um número é positivo.

#### resolução:
~~~~ python
num = int(input("Insira um número: "))

if num > 0:
    print(num, "é número positivo")
elif num == 0:
    print(num, "é número neutro")
else:
    print(num, "é número negativo")
~~~~

#### resultado:
    Insira um número: 21
    21 é número positivo
## Exercicio #34 - Maior Idade
#### Crie um programa que verifique se uma pessoa pode votar com base em sua idade (idade >= 16).

#### resolução: 
~~~~ python
idade = int(input("Insira sua idade: "))

if(idade >= 18):
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")
~~~~

#### resultado:
    Insira sua idade: 16
    Você é menor de idade!

# Exercicio #35 - Par ou Impar
#### Crie um programa que determine se um número é par ou ímpar.
    Instrução
    resultado = 10 % 3 
    print(resultado) # Saída será 1, porque 10 dividido por 3 é igual a 3 com um resto de 1

#### resolução:
~~~~ python
number = int(input("insira um número: "))

if(number % 2 == 0):
    print("O número",number,"é par!")
else: 
    print("O número",number,"é impar!")
~~~~

#### resultado:
    insira um número: 21
    O número 21 é impar!

<br>
<p align="center"> 14/02/25 <p>
</details>

<details>
    <summary> 💠 Aula 6 - 📝 Exercicios de Lógica V (36 a 41) </summary>

<br>
<p> 17/02/25 <p>

## Exercicio #36 - If upper
#### Escreva um programa que verifique se uma palavra está toda em letras maiúsculas.

#### resolução:
~~~~ python
word = input("Insira uma palavra: ")

if word == word.upper(): #ou if word.isupper():
    print("A palavra está em letras maiúsculas")
else:
    print("A palavra está em letras minúsculas")
~~~~

#### resultado:
    Insira uma palavra: THIAGO
    A palavra está em letras maiúsculas
OU se a validação do IF for falsa:

    Insira uma palavra: thiago
    A palavra está em letras minúsculas

## Exercicio #37 - Count()
#### Faça um programa que transforme um texto todo em letras maiúsculas e conte quantas letras 'A' ele possui.

#### resolução:
~~~~ python
palavra = input("Insira uma palavra: ")

print(palavra.upper().count("A"))

# Outro jeito de fazer:
palavra = input("Insira uma palavra: ").upper()
contagem = palavra.count("A")
if contagem > 0:
    print(f"a palavra {palavra} contém {contagem} letras 'A'")
else: 
    print(f"a palavra {palavra} contém {contagem} letras 'A'")
~~~~
#### resultado:
    Insira uma palavra: banana 
    3

resolução da segunda forma:

    Insira uma palavra: banana
    a palavra BANANA contém 3 letras 'A'

## Exercicio #38 - lowerCase
#### Escreva um programa que verifique se uma palavra está toda em letras minúsculas.

#### resolução:
~~~~ python
palabra = str(input("Insira uma palavra: "))

if(palabra.islower()):
    print(f"A palavra {palabra} está escrita em letras minúsculas!")
else:
    print(f"A palavra {palabra} está escrita em letras maiúsculas!")
~~~~

#### resultado:
    Insira uma palavra: banana 
    A palavra banana está escrita em letras minúsculas!

OU se a validação do IF for falsa:

    Insira uma palavra: BANANA
    A palavra BANANA está escrita em letras maiúsculas!

## Exercicio #39 - Lower() & count()
#### Faça um programa que transforme um texto todo em letras minúsculas e conte quantas letras 'e' ele possui.

#### resolução:
~~~~ python
texto = input("Digite um texto: ").lower()
contE = texto.count("e")
if contE > 0:
    print(f"O texto '{texto}' contém {contE} letras 'e' ")
else: 
    print(f"O texto '{texto}' contém {contE} letras 'e' ")
~~~~
#### resultado:
    Digite um texto: Pelo futuro do conhecimento
    O texto 'pelo futuro do conhecimento' contém 3 letras 'e' 

## Exercicio #40 Desafio - palindromo
#### Crie um programa que verifique se um palavra é um palíndromo(Igual, quando lida de trás para frente).

#### resolução:
~~~~ python
palavra = input("escreva uma palavra: ")

if palavra == palavra[::-1]:
    print(f"A palavra {palavra} é um palíndromo")
else:
    print(f"A palavra {palavra} não é um palíndromo")
~~~~
#### resultado:
    escreva uma palavra: ovo
    A palavra ovo é um palíndromo

    # se não:

    escreva uma palavra: caqui
    A palavra caqui não é um palíndromo

## Exercicio #40 - If capitalize()
#### Crie um programa que verifique se a primeira letra é maiúscula, caso não seja, capitalize a primeira letra de uma palavra.

#### resolução:
~~~~ python
palavra = input("Digite uma palavra: ")

if palavra != palavra.capitalize():
    print(palavra.capitalize())
~~~~
#### resultado:
    Digite uma palavra: cachorro
    Cachorro

## Exercicio #41 - Elif()
#### 

    if condição_externa:
        # Código a ser executado se a condição externa for verdadeira
        if condição_interna:
            # Código a ser executado se a condição interna for verdadeira
        else:
            # Código a ser executado se a condição interna for falsa
    else:
        # Código a ser executado se a condição externa for falsa

Ou

    if condição_1:
        # Código a ser executado se condição_1 for verdadeira
    elif condição_2:
        # Código a ser executado se condição_1 for falsa e condição_2 for   verdadeira
    else:
        # Código a ser executado se nenhuma das condições anteriores for    verdadeira

#### resolução:
~~~~ python
numero = int(input("Digite um número: "))

if numero > 0:
    print("é número positivo")
elif numero < 0:
    print("é número negativo")
else: 
    print("é número neutro")
~~~~
#### resultado:
se a variavel for maior que 0

    Digite um número: 7
    é número positivo

se a variavel for menor que 0
    
    Digite um número: -1
    é número negativo

se a variavel for igual a 0
    
    Digite um número: 0
    é número neutro

<br>
<p align="center"> 17/02/25 <p>
</details>

<details>
   <summary> 💠 Aula 7 - 📝 Exercicios de Lógica VI (42 a 49) </summary>
<br>
<p> 18/02/25 <p>

## Exercicio #42 - Média de notas
#### Crie um programa que receba 4 notas de um aluno e calcule a média:
- Nota >= 6 Aprovado
- Nota < 6 e nota > 4 Recuperação
- Nota <= 4 Reprovado

#### resolução:
~~~~ python

count = 0
notaTotal = 0
while count < 4:
        nota = 0
        count += 1
        nota = float(input(f"Insira a {count}° nota: "))
        notaTotal += nota
        if(count == 4):
                media = (notaTotal / count)
                print(f"A média das nota é: {media:.1f}")
                if(media >= 6):
                        print("O aluno está aprovado!")
                elif(media < 6 and media > 4):
                        print("O aluno está de recuperação!")
                else:
                        print("O aluno está reprovado!")
~~~~
#### resultado:
Primeira validação do IF:

    Insira a 1° nota: 8.7
    Insira a 2° nota: 8.9
    Insira a 3° nota: 7.6
    Insira a 4° nota: 8.8
    A média das nota é: 8.5
    O aluno está aprovado!

Segunda validção ELIF:

    Insira a 1° nota: 6.4
    Insira a 2° nota: 5.7
    Insira a 3° nota: 6.1
    Insira a 4° nota: 3.8
    A média das nota é: 5.5
    O aluno está de recuperação!

Terceira validação ELSE:

    Insira a 1° nota: 2.3
    Insira a 2° nota: 4.6
    Insira a 3° nota: 5.0
    Insira a 4° nota: 1.6
    A média das nota é: 3.4
    O aluno está reprovado!

## Exercicio #43 - Positivo & impar 
#### Escreva um programa em Python que determine se um número digitado pelo usuário é um número positivo e ímpar.

#### resolução:
~~~~ python
numero = int(input("Insira um número: "))

if(numero % 2 != 0 and numero > 0):
    print(f"O número {numero} é impar e positivo")
elif(numero % 2 != 0 and numero < 0):
    print(f"O número {numero} é impar e negativo")
elif(numero % 2 == 0 and numero < 0):
    print(f"O número {numero} é par e negativo")
else:
    print(f"O número {numero} é par e positivo")
~~~~
#### resultado:
    Insira um número: 7
    O número 7 é impar e positivo
    ---
    Insira um número: -7
    O número -7 é impar e negativo
    ---
    Insira um número: -4
    O número -4 é par e negativo
    ---
    Insira um número: 4
    O número 4 é par e positivo

## Exercicio #44 - isalpha() 
#### Escreva um programa em Python que determine se uma palavra digitada pelo usuário somente contém letras, caso contenha algum valor numérico, informar que não contem apenas letras ou nenhuma letra.
    texto.isalpha()
- Ele retorna True se todos os caracteres são letras e False se pelo menos um caractere não for uma letra.

#### resolução:
~~~~ python
ut("Digite uma palavra: ")

if(palavra.isalpha()):
    print(f"A palavra '{palavra}' contém apenas letras")
elif(palavra == ""):
    print(f"A palavra não foi digitada")
else: 
    print(f"A palavra '{palavra}' não contém apenas letras")
~~~~
#### resultado:
    Digite uma palavra: thiago
    A palavra 'thiago' contém apenas letras
    ---
    Digite uma palavra: 
    A palavra não foi digitada
    ---
    Digite uma palavra: 721
    A palavra '721' não contém apenas letras

## Exercicio #45 - isdigit()
#### Escreva um programa em Python que determine se os números  digitados pelo usuário contém somente números, caso contenha algum valor não numérico, informar que é permitido somente números
    numeros.isdigit()
verificar se todos os caracteres na frase são dígitos de (0 a 9). Se todos os caracteres forem dígitos, a função retorna True, caso contrário, retorna False.

#### resolução:
~~~~ python
numero = input("digite um número: ")

if(numero == ""):
    print("nenhum número foi digitado")
elif(numero.isdigit()):
    print(f"o número digitado foi {numero}")
else:
    print(f"valor inválido o número não deve conter letras")
~~~~
#### resultado:
    digite um número: 
    nenhum número foi digitado
    ---
    digite um número: 21
    o número digitado foi 21
    ---
    digite um número: thiago
    valor inválido o número não deve conter letras

## Exercicio #46 - Contagem progressiva while()
#### Escreva um programa que conte de 1 a 10 usando um loop while e imprima cada número.
    while condição: 
        # Código a ser executado enquanto a condição for verdadeira

#### resolução:
~~~~ python
contador = 0
while contador < 10:
    contador += 1 # nessa posição o contador vai do 10 ao 1
    print(contador)
    # contador += 1 nessa posição o contador vai do 0 ao 9

# OU
    
for i in range(1, 11, +1):
    print(i)
~~~~
#### resultado:
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10

## Exercicio #47 - Contagem Regressiva while()
#### Escreva um programa faça a contagem regressiva de 1 a 10 usando um loop while e imprima cada número.


while condição: 
      # Código a ser executado enquanto a condição for verdadeira


#### resolução:
~~~~ python
contador = 10
while contador > 0:
    # contador -= 1 nessa posição o contador vai do 9 ao 0
    print(contador)
    contador -= 1 # nessa posição o contador vai do 10 ao 1
~~~~
#### resultado:
    10
    9
    8
    7
    6
    5
    4
    3
    2
    1

# Exercicio #48 - contagem de pares
#### Escreva um programa que solicite ao usuário um número e depois imprima todos os números pares de 1 até esse número, usando um loop while

#### resolução:
~~~~ python

numero = int(input("Insira um número: "))
contador = 0
while contador < numero:
    contador += 2
    print(contador)

# ou 

numero = int(input("Insira um número: "))
contador = 0
while contador < numero:
    if (contador % 2 == 0):
        print(contador)
    contador += 1
~~~~
#### resultado:
    Insira um número: 10
    2
    4
    6
    8
    10

## Exercicio #49 - contagem de par regressivo
#### Escreva um programa que solicite ao usuário um número e depois imprima todos os números pares de 1 até esse número, imprimir em ordem decresce, usando um loop while.

#### resolução:
~~~~ python
numero = int(input("Insira um número: "))
contador = numero

while (contador > 0):
    if(contador % 2 == 0):
        print(contador)
    contador -= 1
~~~~

#### resultado:
    Insira um número: 10
    10
    8
    6
    4
    2

<br>
<p align="center"> 18/02/25 <p>
</details>

<details>
    <summary> 💠 Aula 8 - 📝 Exercicios de Lógica VII (50 a 52) </summary>
<br>
<p> 19/02/25 <p>


## Exercicio #50 - tabuada com while
#### Escreva um programa que imprima a tabuada de multiplicação de um número específico até 10, usando um loop while.

#### resolução:
~~~~ python
numero = int(input("Insira um número: "))
cont = 0

while cont <= 10:
    print(f"{numero} x {cont} = {numero * cont}")
    cont +=1
~~~~

#### resultado:
    Insira um número: 2
    2 x 0 = 0
    2 x 1 = 2
    2 x 2 = 4
    2 x 3 = 6
    2 x 4 = 8
    2 x 5 = 10
    2 x 6 = 12
    2 x 7 = 14
    2 x 8 = 16
    2 x 9 = 18
    2 x 10 = 20


## Exercicio #51 - validação de senha simples
#### Escreva um programa que solicite ao usuário que insira uma senha correta e continue pedindo até que a senha correta seja inserida, usando um loop while.
#### resolução:
~~~~ python
senha = input("Cadastre sua senha: ")
userSenha = input("Digite sua senha: ")

while True:
    if(senha != userSenha):
        print("Senha incorreta!")
        userSenha = input("Digite sua senha: ")
    else: 
        print("Senha Correta!")
        break
~~~~

#### resultado:
    Cadastre sua senha: thigs
    Digite sua senha: 123
    Senha incorreta!
    Digite sua senha: thigs
    Senha Correta!

## Exercicio #52 - soma acumulada
#### Escreva um programa que solicite ao usuário que insira números e calcule a soma desses números até que a soma ultrapasse um limite específico, usando um loop while

#### resolução:
~~~~ python
on = True
somaIterada = 0
limite = int(input("Insira um resultado limite: "))
while on:
    numero = int(input("Insira um número: "))
    numero1 = int(input("Insira outro número: "))
    soma = (numero + numero1)
    somaIterada += soma
    if(somaIterada < limite):
            print(f"{somaIterada} | {limite}")
    if(somaIterada > limite):
        print(f"{somaIterada} | {limite}")
        on = False
~~~~

#### resultado:
    Insira um resultado limite: 10
    Insira um número: 5
    Insira outro número: 5
    Insira um número: 1
    Insira outro número: 1
    12 | 10


## Exercicio #53 Desafio II - Random()
#### Escreva um programa em Python que solicite ao usuário para adivinhar um número entre 1 e 100. O programa deve continuar pedindo um palpite até que o usuário adivinhe corretamente o número. O programa deve fornecer dicas se o palpite estiver muito alto ou muito baixo

### Instruções

Para usar as funções e recursos de uma biblioteca em Python, você precisa primeiro  importá-la para o seu script ou programa. 

A importação é feita usando a palavra-chave: 'import' , seguida do nome da biblioteca.
    
    import random
    
Depois de importar a biblioteca, você pode chamar suas funções e recursos em seu    programa. Isso é feito usando a sintaxe nome_da_biblioteca.

    nome_da_função().
    numero_aleatorio =  random.randint(1, 100)  
    import random

### Função random()

Esta função retorna um número de ponto flutuante aleatório no intervalo [0.0, 1.0),incluindo 0.0, mas excluindo 1.0.

    numero_aleatorio = random.random()
    print("Número aleatório (random()):", numero_aleatorio)

### Função randint(a, b)

Esta função retorna um número inteiro aleatório no intervalo [a, b], incluindo ambos  os extremos.

    numero_aleatorio = random.randint(1, 100)
    print("Número inteiro aleatório (randint(1, 100)):", numero_aleatorio)

### Função choice(seq)

Esta função retorna um elemento aleatório de uma sequência não vazia.

    lista = ['maçã', 'banana', 'laranja', 'uva']
    escolha_aleatoria = random.choice(lista)
    print("Escolha aleatória de uma lista (choice(lista)):", escolha_aleatoria)

#### resolução:
~~~~ python

~~~~

#### resultado:

<p align="center"> 19/02/25 <p>
</details>

---
<br>
<p align="center">@2025</p>
