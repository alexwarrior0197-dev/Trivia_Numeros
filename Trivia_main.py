def trivia_fetch(num):
    """
    Esta función recibe un número y devuelve un diccionario
    con un dato curioso (trivia) sobre ese número.
    """
    trivia_dict = {
        1: "1 es el primer número natural y representa el inicio de todo.",
        3: "3 es el número de lados de un triángulo.",
        7: "7 es considerado un número de la suerte en muchas culturas.",
        9: "9 es un cuadrado perfecto (3x3).",
        10: "10 es la base del sistema numérico decimal.",
        12: "12 es el número de meses en un año.",
        100: "100 representa una cantidad completa o perfecta en muchos contextos."
    }

    # Si el número no está en el diccionario, se genera una trivia genérica
    fact = trivia_dict.get(num, f"{num} es un número interesante, ¡aún sin trivia especial!")
    
    return {"number": num, "fact": fact}


def main():
    """
    Función principal que interactúa con el usuario.
    """
    print("🎯 Bienvenido/a al Quiz de Trivia Numérica 🎯")
    print("Descubre datos curiosos sobre los números.\n")
    
    try:
        num = int(input("👉 Ingresa un número: "))
        trivia = trivia_fetch(num)
        print(f"\n🔢 Dato sobre el número {trivia['number']}: {trivia['fact']}")
    except ValueError:
        print("❌ Por favor, ingresa un número válido.")


# Este bloque asegura que el programa se ejecute solo si se invoca directamente
if __name__ == "__main__":
    main()