def obtener_porcentaje():
    while True:
        try:
            fraccion = input("Ingrese una fracción (X/Y): ")
            x, y = map(int, fraccion.split('/'))
            
            if y == 0:
                raise ZeroDivisionError("El denominador no puede ser cero.")
            if x > y:
                raise ValueError("El numerador no puede ser mayor que el denominador.")
            
            porcentaje = (x / y) * 100
            
            if porcentaje < 1:
                print("E")
            elif porcentaje > 99:
                print("F")
            else:
                print(f"{round(porcentaje)}%")
            break  
        
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")

obtener_porcentaje()
