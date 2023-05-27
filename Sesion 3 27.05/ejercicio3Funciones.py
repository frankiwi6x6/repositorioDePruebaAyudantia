"""•Ejercicio de conteo de caracteres.
"""
def contarCaracteres(pPalabra):
    cLetra = 0
    for letra in pPalabra:
        cLetra += 1
    print(f"La palabra {pPalabra}, tiene {cLetra} letras.")


palabra = str(input("Ingrese una palabra: "))
contarCaracteres(palabra)



