"""Ejercicio de cálculo de área de un círculo.

•Fórmula: área = pi * radio ^ 2."""
import math
def calcularAreaCirculo(radio):
    area = round(math.pi * radio **2,2)

    return area

rCirculo = int(input("Ingrese radio del circulo en centimetros: "))

resultado = calcularAreaCirculo(rCirculo)
print(f"El area del circulo con radio {rCirculo} es: {resultado} cm")