#Game 04 Piedra papel o tijera
import random as rd

def play_game():
  
  print("==========================================")
  print("          Bienvendio al juego             ")
  print("==========================================")
  
  jugador_1 = input("Escoje:\n 'pi' = piedra\n 'pa' = papel\n 'ti' = tijera\n ").lower()  
  computer_2 = rd.choice(['pi', 'pa', 'ti'])
  
  print(f"Tú elección: {jugador_1}\n Elección de la computadora: {computer_2} ")
  
  if jugador_1 == computer_2:
    return "¡Empate!"
  
  if gano_el_jugador(jugador_1, computer_2):
    return "¡Ganaste!"
  
  return "¡Perdiste!"

def gano_el_jugador(jugador, computadora):
  #Retorna True si gana el jugador
  #piedra gana a tijera
  #tijera gana a papel
  #papel gana a piedra 
  
  if((jugador == "pi" and computadora == "ti")
     or (jugador == "ti" and computadora == "pa")
     or (jugador == "pa" and computadora == "pi")):
     return True
  else:
    return False
  

print(play_game())