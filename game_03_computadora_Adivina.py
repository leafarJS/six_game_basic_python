# Game 03 la computadora debe adivinar el numero 
import random as rd


def guess_the_number_computer(x):
  print("==========================================")
  print("          Bienvendio al juego             ")
  print("==========================================")
  print("Objetivo: la computadora debe adivinar tu número")
  
  print(f"Seleciona un número entre 1 y {x} para que la computdora pueda adivinar...")
  
  lim_1 = 1
  lim_2 = x 
  
  respuesta = "" 
  
  while respuesta != "c": 
    #Generar predicción del número 
    if lim_1 != lim_2: 
      prediccion = rd.randint(lim_1, lim_2)
      print(prediccion)
    else:
      prediccion = lim_1
      
    #Obener una respuesta del usuario
    respuesta = input(f"Mi predicción es: {prediccion}, Si es alta, ingresa (A), si es baja (B), y si es correcta ingresa (C): ").lower()
    
    if respuesta == "a":
      lim_2 = prediccion - 1
    elif respuesta == "b":
      lim_1 = prediccion + 1
   
  print(f"Respuesta Correcta!!!, el número es {prediccion}")


guess_the_number_computer(10)
    
    