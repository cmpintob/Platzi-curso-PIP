import random

options = ('piedra', 'papel', 'tijera')

def choose_options():
  
  user_option = input("piedra, papel o tijera ?: ")
  user_option = user_option.lower()
  
  if not user_option in options:
    print('tu elección no se encuentra dentro de las opciones')
    print('')
    # continue
    return None, None
  
  computer_option = random.choice(options)

  print("jugador = " + user_option)
  print("computadora = " + computer_option)

  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):

  if user_option == computer_option:
    print('empate')
  elif user_option == 'piedra':
    if computer_option == 'tijera':    
      print("ganaste, piedra vence a tijera")
      user_wins +=1
    else:
      print("papel gana a piedra, perdiste")
      computer_wins +=1
  elif user_option == 'papel':
    if computer_option == 'piedra':    
      print("ganaste, papel vence a piedra")
      user_wins +=1
    else:
      print("tijera gana a papel, perdiste")
      computer_wins +=1
  elif user_option == 'tijera':
    if computer_option == 'papel':    
      print("ganaste, tijera vence a papel")
      user_wins +=1
    else:
      print("piedra gana a tijera, perdiste")
      computer_wins +=1

  print('')
  return user_wins, computer_wins

def check_winner(user_wins, computer_wins):
  
  if computer_wins == 2:
    print("La computadora ha ganado el juego, tu pierdes u.u")
    return 1
  
  if user_wins == 2:
    print("El jugador ha ganado el juego, felicidades :D")
    return 1

  return 0

def run_game():

  computer_wins = 0
  user_wins = 0
  rounds = 1
  game_over = 0
  
  while game_over == 0:
  
    print('*' * 10)
    print('Round', rounds)
    print('*' * 10)
    print('')
    print('Marcador')
    print('jugador', user_wins)
    print('computadora', computer_wins)
    print('')
    rounds += 1  
  
    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
    game_over = check_winner(user_wins, computer_wins) 

run_game()
print('')
print('Game over')
print('')