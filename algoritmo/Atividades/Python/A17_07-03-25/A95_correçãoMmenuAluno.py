alunos = []

def limpar_tela():
    # Limpa a tela imprimindo várias quebras de linha
    print("\n" * 50)

def exibir_nome_do_programa():
    print(''' 
      +-+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+
      |C|a|d|a|s|t|r|o| |d|e| |A|l|u|n|o|
      +-+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+
    ''')

def exibir_opcoes():
    print("Menu")
    print("1. Cadastrar alunos")
    print("2. Listar alunos")
    print("3. Buscar aluno")
    print("4. Remover aluno")
    print("5. Sair")


def cadastrar_aluno():
    nome=input("Informe o nome para adicionar: ").capitalize()
    alunos.append(nome)
    print(f"{nome} incluído com sucesso!")
    

def listar_alunos():
    for i, aluno in enumerate(alunos,1):
        if not alunos:
            print("Não tem aluno cadastrado")
        else:
            print(f"{i} - {aluno}")

def buscar_aluno():
    nome=input("Informe o nome para buscar: ").capitalize().strip()
    if nome in alunos:
        print(f"Aluno encontrado com sucesso: {nome}")
    else:
        print("Aluno não encontrado")


def remover_aluno():
    nome=input("Informe o nome para buscar: ").capitalize().strip()
    if nome in alunos:
        alunos.remove(nome)
        print(f"{nome} foi removido(a) com sucesso")
    else:
        print("Aluno não encontrado")

def finalizar_app():
    print("Encerrando programa")

def escolher_opcao():
    while True:
        try:
            opcao=int(input("Informe a opção desejada: "))

            if opcao == 1:
                cadastrar_aluno()
            elif opcao == 2:
                listar_alunos()
            elif opcao == 3:
                buscar_aluno()
            elif opcao == 4:
                remover_aluno()
            elif opcao == 5:
                finalizar_app()
                break
            else:
                print("Opção inválida")
           
        except ValueError():
            print("Valor inválido")
        input("Informe enter para continuar")
        limpar_tela()
        exibir_opcoes()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()