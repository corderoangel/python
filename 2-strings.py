mi_string = "  Hola, Mundo  "
lista = ["Ángel", "Joan", "Luis", "Carlos"]

#metodos
print("len")
print(len(mi_string))
print("=" * 15) 
print("lower")
print(mi_string.lower())
print("=" * 15) 
print("upper")
print(mi_string.upper())
print("=" * 15) 
print("strip")
print(mi_string.strip())
print("=" * 15) 
print("replace")
print(mi_string.replace("Hola", "Adiós"))
print("=" * 15) 
print("split")
print(mi_string.split())
print("=" * 15) 
print("join")
print("-".join(lista))
print("=" * 15) 
print("find")
print(mi_string.find("Mundo"))
print("=" * 15) 
print("startswith")
print(mi_string.startswith("Hola"))
print(mi_string.strip().startswith("Hola"))
print("=" * 15) 
print("endswith")
print(mi_string.endswith("Mundo"))
print(mi_string.strip().endswith("Mundo"))