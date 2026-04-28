peliculas = ["La sirenita 2", "Soy leyenda 2", "Shrek 3"]

precios = {
    "La sirenita 2": 18000,
    "Soy leyenda 2": 20000,
    "Shrek 3": 16000
}

def elegir_pelicula():
    for i, p in enumerate(peliculas, 1):
        print(f"{i}. {p} - ${precios[p]}")
    op = int(input("Seleccione pelicula: "))
    if op < 1 or op > len(peliculas):
        raise Exception("Opcion invalida")
    return peliculas[op - 1]

def elegir_cantidad():
    cant = int(input("Cantidad de boletas: "))
    if cant <= 0:
        raise Exception("Cantidad invalida")
    return cant

def hacer_compra():
    try:
        peli = elegir_pelicula()
        cant = elegir_cantidad()
        total = precios[peli] * cant
        print(f"\nPelicula : {peli}")
        print(f"Boletas  : {cant}")
        print(f"Total    : ${total}\n")
    except Exception as e:
        print(f"Error: {e}\n")

while True:
    print("1. Comprar boletas")
    print("2. Salir")
    op = input("Opcion: ")
    if op == "1":
        hacer_compra()
    elif op == "2":
        break
    else:
        print("Opcion invalida\n")
