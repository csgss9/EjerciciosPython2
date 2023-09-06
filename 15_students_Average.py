"""
 calcular el promedio general de una clase, así como el promedio individual de cada estudiante.
 A partir de esta información, retornar un diccionario con el promedio de la clase y los estudiantes y sus promedios
"""
import json

students = [
  {
    "name": "Pedro",
    "grades": [90, 87, 88, 90],
  },
  {
    "name": "Jose",
    "grades": [99, 71, 88, 96],
  },
  {
    "name": "Maria",
    "grades": [92, 81, 80, 96],
  },
]

def calcular_promedio(students_list):
    total_grades = []
    lista_estudiantes = []
    for student in students_list: 
        average = sum(student["grades"]) / len(student["grades"])
        total_grades.extend(student["grades"])
        lista_estudiantes.append({"name": student["name"], "average": average})

    total_average = sum(total_grades) / len(total_grades)

    result = {
        "total_average": round(total_average, 2),
        "students": lista_estudiantes
    }
    return result

result_dict = calcular_promedio(students)
print(json.dumps(result_dict, indent=4))  # Imprimir el resultado en formato JSON


