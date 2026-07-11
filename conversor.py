cambio = float(input("Ingrese cantidad de dinero: "))
moneda = input("Es dolar (d) o cordobas (c): ").strip().lower()
if moneda == "d":
    cordobas = cambio * 36.92
    print(cordobas)
elif moneda == "c":
    dolares = cambio / 36.92
    print(dolares)
else:
    print("Moneda no reconocida. Use 'd' o 'c'.")
