# Game 06 Busquda binaria
import random as rd 
import time as tm 

length = 100000
set_initial = set()
while len(set_initial) < length:
  set_initial.add(rd.randint(-3 * length, 3 * length))
  
my_list = sorted(list(set_initial))

def naive_search(list, target):
  for i in range(len(list)):
    if list[i] == target:
      return i 
  return -1


def binary_search(list, target, lim_x = None, lim_y =None):
  if lim_x is None:
    lim_x = 0 
  if lim_y is None:
    lim_y = len(list) - 1
    
  if lim_y < lim_x:
    return -1
  
  point_mean = (lim_x + lim_y) // 2
  
  if list[point_mean] == target:
    return point_mean
  elif target < list[point_mean]:
    return binary_search(list, target, lim_x, point_mean -1)
  else:
    return binary_search(list, target, point_mean + 1, lim_y)

if __name__ == '__main__':
  
  # medir el tiempo de naive_search
  start  = tm.time()
  for obj in my_list:
    naive_search(my_list, obj)
  end = tm.time()
  
  print(f"tiempo de busqueda ingenua: {end - start} segundos")
  
  # medir el tiempo de naive_search
  start  = tm.time()
  for obj in my_list:
    binary_search(my_list, obj)
  end = tm.time()
  
  print(f"tiempo de busqueda binaria: {end - start} segundos")