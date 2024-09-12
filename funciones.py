from math import factorial

primer_operando = None
segundo_operando = None

def ingresar_primer_operando():
    global primer_operando
    primer_operando = int(input("Ingrese el valor del primer operando (A): "))
    print(f"Primer operando (A) ingresado: {primer_operando}")

def ingresar_segundo_operando():
    global segundo_operando
    segundo_operando = int(input("Ingrese el valor del segundo operando (B): "))
    print(f"Segundo operando (B) ingresado: {segundo_operando}")

def calcular_todas_las_operaciones():
    global primer_operando, segundo_operando
    
    if primer_operando is None or segundo_operando is None:
        print("Error: Debe ingresar ambos operandos antes de realizar las operaciones.")
        return
    
    suma = primer_operando + segundo_operando
    resta = primer_operando - segundo_operando
    division = primer_operando / segundo_operando
    resto = primer_operando % segundo_operando
    multiplicacion = primer_operando * segundo_operando
    potencia = primer_operando ** segundo_operando
    factorial_A = factorial(primer_operando) if primer_operando >= 0 else "No definido (A negativo)"
    
    global resultados
    resultados = {
        "suma": suma,
        "resta": resta,
        "division": division,
        "multiplicacion": multiplicacion,
        "potencia": potencia,
        "resto": resto,
        "factorial_A": factorial_A
    }
    
    print("\nOperaciones calculadas:")
    print(f"Suma (A + B): {suma}")
    print(f"Resta (A - B): {resta}")
    print(f"División (A / B): {division}")
    print(f"Multiplicación (A * B): {multiplicacion}")
    print(f"Potencia (A ** B): {potencia}")
    print(f"Resto (A % B): {resto}")
    print(f"Factorial (A!): {factorial_A}")

def informar_resultados():
    print("\nResultados informados:")
    print(f"Suma (A + B): {resultados['suma']}")
    print(f"Resta (A - B): {resultados['resta']}")
    print(f"División (A / B): {resultados['division']}")
    print(f"Multiplicación (A * B): {resultados['multiplicacion']}")
    print(f"Potencia (A ** B): {resultados['potencia']}")
    print(f"Resto (A % B): {resultados['resto']}")
    print(f"Factorial (A!): {resultados['factorial_A']}")