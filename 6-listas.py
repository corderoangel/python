to_do = ["Dirigirnos al hotel", "Ir a almorzar", "Visitar un museo", "Volver al hotel"]
print(to_do)

numbers = [1, 2, 3, 4, "cinco"]
print(type(numbers))  # Resultado: <class 'list'>

mix = ["uno", 2, 3.14, True, [1,2,3]]
print(mix)
print(len(mix))
print("Primer elemento", mix[0])  # Accede al primer elemento
print("Segundo elemento", mix[1])  # Accede al segundo elemento
print("Último elemento:", mix[-1])  # Accede al último elemento (usando índice negativo)

print(mix[2:-2])  # Resultado: [3.14]
mix.append(False)
print(mix)
mix.append(["a", "b"])
print(mix)
mix.insert(1, ["a", "b"])
print(mix)
print(mix.index(["a", "b"]))  # Encuentra el índice de la primera ocurrencia

numbers = [1, 2, 100.01, 90.45, 3, 4, 5]
print("Mayor:", max(numbers))  # Resultado: 100.01
print("Menor:", min(numbers))  # Resultado: 1

del numbers[-1]  # Elimina el último elemento
print(numbers)
del numbers[:2]  # Elimina los dos primeros elementos
print(numbers)
del numbers  # Elimina la lista completa

string = "Hola mundo"
print("Primer elemento", string[0])  # Resultado: 'H'
print("Segundo elemento", string[1])  # Resultado: 'o'
print("Último elemento:", string[-1])  # Resultado: 'o'
