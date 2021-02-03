import sys
import os
import random
os.system('cls' if os.name == 'nt' else 'clear')


inventory = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

#create a function that randomly chooses an item in inventory, adds value of item to health, removes item from inventory, and returns your inventory and health.

def use_health_item(item):
  global health_points
  health_points += inventory.pop(item)
  print(inventory)
  return health_points
print(use_health_item(random.choice(list(inventory.keys()))))