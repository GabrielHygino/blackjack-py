from blackjack import jogar

print("##########################")
print("Bem vindo ao BlackJack-Py!")
print("##########################")

while True:
    option = int(input("Digite 1 para jogar, 2 para sair: "))
    if option == 1:
        jogar()
        break
    elif option == 2:
        print("Até logo!")
        break
    print("Somente 1 ou 2 são respostas válidas")
