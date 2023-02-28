from json import loads
from requests import get

def deck_id():
  response = get("https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")._content.decode()
  deck = loads(response)
  return deck["deck_id"]

def realeza(carta):
  if(carta == "QUEEN" or carta == "KING" or carta == "JACK"):
    carta = 10
  else:
     carta = carta
  return carta

def jogar():
  deck_atual = deck_id()
  response = get(f"https://www.deckofcardsapi.com/api/deck/{deck_atual}/draw/?count=2")
  data = loads(response._content.decode())
  print("Suas cartas atuais são: ") 

  mao = []
  total = 0
  for carta in data["cards"]:
      mao += carta.get("value")
      realeza(carta)
      total += carta
      
 

  print(mao)
  print("O total da sua mão é " + total)

  while True:
    option = input("Deseja comprar mais alguma carta? Digite S para sim, N para não.")
    if option == "S":
        response = get(f"https://www.deckofcardsapi.com/api/deck/{deck_atual}/draw/?count=1")
        break
    elif option == "N":
        break
    else:
       print("Digite S ou N")




 # if(comprar_cartas):  response = get(f"https://www.deckofcardsapi.com/api/deck/{deck_atual}/draw/?count=1")

  #for carta in data["cards"]:
  #  a = carta.get("value")
   # print(a) 
  



jogar()