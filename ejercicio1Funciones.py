"""
•Ejercicio de suma y resta:

    •Suma los dos números y muestra el resultado.

    •Resta el segundo número al primero y muestra el resultado.
 """
def sumar(valor1, valor2):
    resultado = valor1 + valor2;

    print(f"El resultado de la suma es: {resultado}")

def restar(valor1, valor2):

    resultado = valor2 - valor1
    print(f"El resultado de la resta es: {resultado}")


op = 0
while op!= 3:
    op = int(input("MENU \n1. SUMAR\n2. RESTAR \n3. SALIR\nIngrese su respuesta: "))
    if op == 1:
        num1 = int(input("Ingrese primer valor: "))
        
        num2 = int(input("Ingrese segundo valor: "))
        sumar(num1, num2)
        
    elif op == 2: 
        num1 = int(input("Ingrese primer valor: "))
        
        num2 = int(input("Ingrese segundo valor: "))
        restar(num1,num2)
    elif op == 3:
        print("Nos vemos.")
        break
    else:
        print("Valor no valido, intente nuevamente.")






