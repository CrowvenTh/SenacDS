# Crie uma função que receba 4 números e retorne a média dos números

n1 = float(input("Insira um número: "))
n2 = float(input("Insira um número: "))
n3 = float(input("Insira um número: "))
n4 = float(input("Insira um número: "))

def Media():
    media = (n1 + n2 + n3 + n4) / 4
    print(f"A média dos números é {media:.2f}")

Media()


# OU

def Media(n1,n2,n3,n4):
    media = (n1 + n2 + n3 + n4) / 4
    return media

print(Media(n1,n2,n3,n4))