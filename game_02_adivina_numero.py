import random as rd
def guess_the_number(x):
  print("==========================================")
  print("          Bienvendio al juego             ")
  print("==========================================")
  print("Objetivo: Adivine el número que la computadora generó")
 
  num_random = rd.randint(1, x) #genera un numero entero aleatorio
  prediccion = 0  
  
  while prediccion != num_random: 
      prediccion = int(input(f"Cual es el número entre 1 y {x}: "))
           
      if prediccion == num_random:
          print("Felicidades Acertaste el número!!!!")
    
      if prediccion < num_random:
        print("El número está por debajo de lo esperado")
      elif prediccion > num_random:
        print("El número esta por encima de lo esperado")
      

guess_the_number(100)