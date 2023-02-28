from json import loads
from requests import get
conta = 0
total = 0
mao = []

def deck_id():
  response = get("https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")._content.decode()
  deck = loads(response)
  return deck["deck_id"]

def realeza(carta):
  if(carta == "QUEEN" or carta == "KING" or carta == "JACK"):
    carta = 10
  elif(carta == "ACE"):
     carta = 11
  return int(carta)

def pegacarta(data, mao, conta, total):
  for carta in data["cards"]:
      total = realeza(carta.get("value"))
      
      conta += total
      if realeza(carta.get("value")) == 11 and conta >= 22:
        conta -= 10
      mao.append(carta.get("value")) 

 
  return mao, conta

def resultado(conta):
  if conta == 21:       
    return print("Você ganhou!"), print("Fim de jogo!")
  return print("Você perdeu :("), print("Fim de jogo!")

def jogar():
  deck_atual = deck_id()
  response = get(f"https://www.deckofcardsapi.com/api/deck/{deck_atual}/draw/?count=2")
  data = loads(response._content.decode())
  primeira_mao, somatoria = pegacarta(data, mao, conta, conta)
  print("Suas cartas atuais são: ")
  print(primeira_mao)
  print("O total da sua mão é: " )
  print(somatoria) 

  while True:
    mao_atual = primeira_mao
    conta_atual = somatoria

    if conta_atual >= 21:
       resultado(conta_atual)
       break
    
    option = input("Deseja comprar mais alguma carta? Digite S para sim, N para não.").lower()
    
    if option == "s" or option == "sim": 
        response = get(f"https://www.deckofcardsapi.com/api/deck/{deck_atual}/draw/?count=1")
        data = loads(response._content.decode())
        mao_atual, conta_atual = pegacarta(data, mao_atual, conta_atual, conta_atual)
        somatoria = conta_atual

        print("Suas cartas atuais são: ")
        print(mao_atual)
        print("O total da sua mão é: ")
        print(conta_atual)
        
        if conta_atual >= 21:
           resultado(conta_atual)
           break
        
    elif option == "n" or option == "nao":
        resultado(conta_atual)
        break
    else:
       print("Digite S ou N")
       break
jogar()
