def calcular_precio(material_precio_kilo, gramos_consumidos, precio_luz, duracion_impresion, precio_hora_hombre):
    # Convertimos el precio del material de kilo a gramos
    material_precio_gramo = material_precio_kilo / 1000
    # Calculamos el precio del material
    precio_material = material_precio_gramo * gramos_consumidos
    
    # Calculamos el consumo eléctrico y su costo
    consumo_electrico = (500 / 1000) * duracion_impresion  # 500W es el consumo típico de la impresora
    costo_electrico = consumo_electrico * precio_luz
    
    # Calculamos el costo de horas hombre
    costo_horas_hombre = precio_hora_hombre
    
    # Calculamos el precio total
    precio_total = precio_material + costo_electrico + costo_horas_hombre
    return precio_total

def main():
    print("Calculadora de precio de piezas impresas en 3D")
    try:
        material_precio_kilo = float(input("Ingrese el precio del material por kilo en euros: "))
        gramos_consumidos = float(input("Ingrese la cantidad de gramos que se van a consumir: "))
        precio_luz = float(input("Ingrese el precio de la electricidad por kWh en euros: "))
        duracion_impresion = float(input("Ingrese la duración de la impresión en horas: "))
        precio_hora_hombre = float(input("Ingrese el precio de la hora hombre en euros: "))
        
        # Validaciones adicionales
        if material_precio_kilo < 0 or gramos_consumidos < 0 or precio_luz < 0 or duracion_impresion < 0 or precio_hora_hombre < 0:
            print("Por favor, ingrese valores positivos.")
            return
        
        precio_total = calcular_precio(material_precio_kilo, gramos_consumidos, precio_luz, duracion_impresion, precio_hora_hombre)
        print(f"El precio total de la pieza es: {precio_total:.2f} euros")
    except ValueError:
        print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()