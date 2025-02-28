# questionario
def menu():
    print("\n============================================")
    print("===============| QUIZ PYTHON |===============")
    print("============================================")
    
# questionario / calculo
def Usuario():
    return nomeUsuario.capitalize()

pontuacao = 0
a = [] # acertos
e = [] # erros
p = 0

# calculo
def Avanca():
    print("===========| Questão respondida! |==========\n")

    
# questionario
def Q1():
    print("===============| QUESTÃO 01 |===============")
    print("Quem foi o criador do python ?\n")
    print("1. Brendan Eich")
    print("2. Linus torvalds")
    print("3. Guido van Rossum")
    print("4. Berners-Lee")
    q1resp = int(input())
    
    match q1resp:
        case 1:
            e.append("Q1")
            print("Alternativa:", q1resp)
            Avanca()
        case 2:
            e.append("Q1")
            print("Alternativa:", q1resp)
            Avanca()
        case 3:
            a.append("Q1")
            print("Alternativa:", q1resp, "Correto!")
            Avanca()
        case 4:
            e.append("Q1")
            print("Alternativa:", q1resp)
            Avanca()
        case _:
            print("Opção inválida")
def Q2():
    print("===============| QUESTÃO 02 |===============")
    print("Em que ano o Python foi lançado ?\n")
    print("1. 1959")
    print("2. 1995")
    print("3. 1979")
    print("4. 1991")
    q2resp = int(input())
    
    match q2resp:
        case 1:
            e.append("Q2")
            print("Alternativa:", q2resp)
            Avanca()
        case 2:
            Avanca()
            print("Alternativa:", q2resp)
            e.append("Q2")
        case 3:
            e.append("Q2")
            print("Alternativa:", q2resp)
            Avanca()
        case 4:
            a.append("Q2")
            print("Alternativa:", q2resp, "Correto!")
            Avanca()
        case _:
            print("Opção inválida")
def Q3():
    print("===============| QUESTÃO 03 |===============")
    print("Qual o tipo de tipagem do Python: \n")
    print("1. Tipagem estática")
    print("2. Tipagem Modular")
    print("3. Tipagem dinâmica")
    print("4. Tipagem Identada")
    q3resp = int(input())
    
    match q3resp:
        case 1:
            e.append("Q3")
            print("Alternativa:", q3resp)
            Avanca()
        case 2:
            Avanca()
            print("Alternativa:", q3resp)
            e.append("Q3")
        case 3:
            a.append("Q3")
            print("Alternativa:", q3resp, "Correto!")
            Avanca()
        case 4:
            e.append("Q3")
            print("Alternativa:", q3resp)
            Avanca()
        case _:
            print("Opção inválida")
def Q4():
    print("===============| QUESTÃO 04 |===============")
    print("São IDEs de python: \n")
    print("1. Pycharm, VScode, Eclipse")
    print("2. Eclipse, Sublime, VsCode")
    print("3. VsCode, NetBeans, InteliJ")
    print("4. Spyder, Pycharm, VsCode")
    q4resp = int(input())
    
    match q4resp:
        case 1:
            e.append("Q4")
            print("Alternativa:", q4resp)
            Avanca()
        case 2:
            Avanca()
            print("Alternativa:", q4resp)
            e.append("Q4")
        case 3:
            e.append("Q4")
            print("Alternativa:", q4resp)
            Avanca()
        case 4:
            a.append("Q4")
            print("Alternativa:", q4resp, "Correto!")
            Avanca()
        case _:
            print("Opção inválida")
def Q5():
    print("===============| QUESTÃO 05 |===============")
    print("Em qual país se originou o Python ?\n")
    print("1. Holanda")
    print("2. Noruega")
    print("3. Estados Unidos")
    print("4. Finlândia")
    q5resp = int(input())
    
    match q5resp:
        case 1:
            a.append("Q5")
            print("Alternativa:", q5resp, "Correto!")
            Avanca()
        case 2:
            Avanca()
            print("Alternativa:", q5resp)
            e.append("Q5")
        case 3:
            e.append("Q5")
            print("Alternativa:", q5resp)
            Avanca()
        case 4:
            e.append("Q5")
            print("Alternativa:", q5resp)
            Avanca()
        case _:
            print("Opção inválida")
def Q6():
    print("===============| QUESTÃO 06 |===============")
    print("Quais são frmaeworks de python ?\n")
    print("1. Pycharm, Pandas, Flask")
    print("2. Flask, Spring, Arduino")
    print("3. Pandas, Quarkus, Angular")
    print("4. Django, Plone, Flask")
    q6resp = int(input())
    
    match q6resp:
        case 1:
            e.append("Q6")
            print("Alternativa:", q6resp)
            Avanca()
        case 2:
            Avanca()
            print("Alternativa:", q6resp)
            e.append("Q6")
        case 3:
            e.append("Q6")
            print("Alternativa:", q6resp)
            Avanca()
        case 4:
            a.append("Q6")
            print("Alternativa:", q6resp, "Correto!")
            Avanca()
        case _:
            print("Opção inválida")
def Q7():
    print("===============| QUESTÃO 07 |===============")
    print("Que tipo de variáveis são aceitos em python ?\n")
    print("1. Integer, Boolean, double")
    print("2. tuple, string, int")
    print("3. Varchar, string, float")
    print("4. Complex, short, list")
    q7resp = int(input())
    
    match q7resp:
        case 1:
            e.append("Q7")
            print("Alternativa:", q7resp)
            Avanca()
        case 2:
            Avanca()
            print("Alternativa:", q7resp)
            a.append("Q7")
        case 3, "Correto!":
            e.append("Q7")
            print("Alternativa:", q7resp)
            Avanca()
        case 4:
            e.append("Q7")
            print("Alternativa:", q7resp)
            Avanca()
        case _:
            print("Opção inválida")
def Q8():
    print("===============| QUESTÃO 08 |===============")
    print("São operadores lógicos em python: ?\n")
    print("1. ==, >, $")
    print("2. else, or, if")
    print("3. -, and, ||")
    print("4. or, not, and")
    q8resp = int(input())
    
    match q8resp:
        case 1:
            e.append("Q8")
            print("Alternativa:", q8resp)
            Avanca()
        case 2:
            Avanca()
            print("Alternativa:", q8resp)
            e.append("Q8")
        case 3:
            e.append("Q8")
            print("Alternativa:", q8resp)
            Avanca()
        case 4:
            a.append("Q8")
            print("Alternativa:", q8resp, "Correto!")
            Avanca()
        case _:
            print("Opção inválida")
def Q9():
    print("===============| QUESTÃO 09 |===============")
    print("São operadores aritméticos em python: \n")
    print("1. !=, ==, &&")
    print("2. ||, or, -")
    print("3. -, //, **")
    print("4. $, %%, ==")
    q9resp = int(input())
    
    match q9resp:
        case 1:
            e.append("Q9")
            print("Alternativa:", q9resp)
            Avanca()
        case 2:
            Avanca()
            print("Alternativa:", q9resp)
            e.append("Q9")
        case 3:
            a.append("Q9")
            print("Alternativa:", q9resp, "Correto!")
            Avanca()
        case 4:
            e.append("Q9")
            print("Alternativa:", q9resp)
            Avanca()
        case _:
            print("Opção inválida")
def Q10():
    print("===============| QUESTÃO 10 |===============")
    print("considerando fevereiro de 2025, Qual a versão mais recente do Python ?\n")
    print("1. 5.2.13")
    print("2. 2.11.04")
    print("3. 3.13.2")
    print("4. 21.08.04")
    q10resp = int(input())
    
    match q10resp:
        case 1:
            e.append("Q10")
            print("Alternativa:", q10resp)
            Avanca()
        case 2:
            Avanca()
            print("Alternativa:", q10resp)
            e.append("Q10")
        case 3:
            a.append("Q10")
            print("Alternativa:", q10resp, "Correto!")
            Avanca()
        case 4:
            e.append("Q10")
            print("Alternativa:", q10resp)
            Avanca()
        case _:
            print("Opção inválida")

# QUESTIONÁRIO    
def final():
    print("============================================")
    print(f"=====| Nome: {Usuario()} \n=====| Acertos: {len(a)} | Erros: {len(e)}")
    print("=====|")
    print("=================| FIM |===================\n")
    print("============================================")

menu()
nomeUsuario = input("Insira seu nome: \n")
Usuario()
Q1()
Q2()
Q3()
Q4()
Q5()
Q6()
Q7()
Q8()
Q9()
Q10()
final()
