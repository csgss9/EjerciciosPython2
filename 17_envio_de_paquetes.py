#crear una función que calcule el peso total de los paquetes, así como la cantidad de paquetes que se enviarán a cada destino.

def get_packages_info(packages):
   weights_sum = 0
   destinations = {}
   
   for package in packages:
      weights_sum += package[1];
      if (not(package[2] in destinations)):
         destinations[package[2]] = 0
      
      if(package[2] in destinations): 
         destinations[package[2]] = destinations[package[2]] + 1
         

   return {
      "total_weight": round(weights_sum, 2),
      "destinations": destinations
   }

print(get_packages_info([
  (1, 20, "Mexico"),
  (2, 15.5, "Colombia"),
  (3, 30, "Mexico"),
  (4, 12, "Argentina"),
  (5, 8.2, "Colombia"),
  (6, 25, "Mexico"),
  (7, 18.7, "Argentina"),
  (8, 5, "Colombia"),
  (9, 22.3, "Argentina"),
  (10, 14.8, "Colombia")
]))