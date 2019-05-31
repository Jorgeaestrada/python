# Una lista es una estructura de datos y un tipo de dato en python con características especiales.
# Lo especial de las listas en Python es que nos permiten almacenar cualquier tipo de valor como
# enteros, cadenas y hasta otras funciones;

# METODOS PARA LISTAS:
# my_list.append([2,5]) # [2, 5, 'DevCode', 1.2, 5, [2, 5]]
# my_list.extend([2,5]) # [2, 5, 'DevCode', 1.2, 5, 2, 5]
# my_list.remove(2) # [5, 'DevCode', 1.2, 5]
# my_list.index('DevCode') # 2
# my_list.count(5) # 2
# my_list.reverse() # [5, 1.2, 'DevCode', 5, 2]


ListaEstaciones = [“Invierno”, “Primavera”, “Verano”, “Otoño”]  # Declara lista

# Para definir una lista vacía, a la que con posterioridad se
# podría agregar elementos, existen dos posibilidades:

lista = []
lista = list()

# Trabajando con listas

abc = "some string"
print(abc)
print(abc * 2)
print(abc + abc)

#This is like an java array, on python called List
list_var = ["some string", 123, "another string"]
list_var.append("some another item")
print(list_var)

#items on list
print("list size:")
print(len(list_var))

print(len("a string"))

list_var[0]
list_var[1]
list_var[2]
print(list_var)

abc = [1, 2, 3]
print(abc)

#push and pop elements on a list
another_list = ["justin", "Jhon", "matt"]
print(another_list[1])

the_list = [1,2,3]
print(the_list.pop())
print(the_list.pop(1))
print(len(the_list))
