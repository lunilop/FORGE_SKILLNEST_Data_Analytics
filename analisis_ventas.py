# ------------------------------------ Ejercicio 1 ---------------------------------

# Carga de Datos

# Crea una lista de diccionarios llamada ventas, donde cada diccionario represente una venta. 
# Cada venta debe incluir las siguientes claves:

# «fecha»: una cadena de texto que represente la fecha de la venta (por ejemplo, «2024-01-01»).
# «producto»: una cadena de texto que represente el nombre del producto vendido.
# «cantidad»: un número entero que represente la cantidad de productos vendidos.
# «precio»: un número flotante que represente el precio unitario del producto.

ventas = [
    {"fecha": "2024-01-01", "producto": "iPhone 15", "cantidad": 2, "precio": 1200.0},
    {"fecha": "2024-01-01", "producto": "Samsung S24", "cantidad": 1, "precio": 1100.0},
    {"fecha": "2024-01-02", "producto": "iPhone 15", "cantidad": 1, "precio": 1200.0},
    {"fecha": "2024-01-02", "producto": "Funda", "cantidad": 5, "precio": 20.0},
    {"fecha": "2024-01-03", "producto": "Samsung S24", "cantidad": 2, "precio": 1050.0},
    {"fecha": "2024-01-03", "producto": "Funda", "cantidad": 3, "precio": 25.0}
]
print("="*30)
print(" REPORTES DE VENTAS ")
print("="*30)
print("\n1. LISTA DE VENTAS ORIGINAL: ")

print("-" * 65)
print(f"{'FECHA':<12} | {'PRODUCTO':<15} | {'CANT.':<6} | {'PRECIO':<10}")
print("-" * 65)

for venta in ventas:
    print(f"{venta['fecha']:<12} | {venta['producto']:<15} | {venta['cantidad']:<6} | ${venta['precio']:<9,.2f}")


# ------------------------------------ Ejercicio 2 ---------------------------------

# 2. Cálculo de Ingresos Totales

# Utiliza un bucle para iterar sobre la lista ventas y calcular los ingresos totales generados por todas las ventas. 
# Los ingresos totales se calculan multiplicando la cantidad vendida por el precio unitario para cada venta y sumando los resultados.

ingresos_totales= 0

for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]

print(f"\n2. INGRESOS TOTALES: ${ingresos_totales}")


# ------------------------------------ Ejercicio 3 ---------------------------------

# 3. Análisis del Producto Más Vendido

# Crea un diccionario llamado ventas_por_producto donde las claves sean 
# los nombres de los productos y los valores sean la cantidad total vendida de cada producto.
# Utiliza este diccionario para identificar el producto que tuvo la mayor cantidad total vendida.

ventas_por_producto = {}

for venta in ventas:
    produc = venta["producto"]
    cant = venta["cantidad"]
    if produc not in ventas_por_producto:
        ventas_por_producto[produc] = 0
    ventas_por_producto[produc] += cant

producto_mas_vendido = None
max_cantidad = 0

for produc, cant in ventas_por_producto.items():
    if cant > max_cantidad:
        max_cantidad = cant
        producto_mas_vendido = produc

print(f"\n3. PRODUCTO MAS VENDIDO: {producto_mas_vendido} ({max_cantidad} unidades)")


# ------------------------------------ Ejercicio 4 ---------------------------------

# 4. Promedio de Precio por Producto

# Crea un diccionario llamado precios_por_producto donde las claves sean 
# los nombres de los productos y los valores sean tuplas. Cada tupla debe contener dos elementos: 
# la suma de los precios de venta de todas las unidades vendidas y la cantidad total de unidades vendidas.

# Calcula el precio promedio de venta para cada producto utilizando la información de este diccionario.

precios_por_producto = {}

for venta in ventas:
    produc = venta["producto"]
    cantidad = venta["cantidad"]
    ingreso_venta = cantidad * venta["precio"]
    
    if produc not in precios_por_producto:
        precios_por_producto[produc] = (0, 0) 
        
    suma_actual, suma_cant = precios_por_producto[produc]
    precios_por_producto[produc] = (suma_actual + ingreso_venta, suma_cant + cantidad)

print("\n4. PRECIOS POR PRODUCTOS (Suma Ingresos, Cantidad Total):")

for producto, datos in precios_por_producto.items():
    print(f"   - {producto}: {datos}")

print("\n   PROMEDIOS CALCULADOS:")

for producto, datos in precios_por_producto.items():
    suma_ingresos = datos[0]
    total_unidades = datos[1]
    promedio = suma_ingresos / total_unidades
    
    print(f"   - {producto}: ${promedio:.2f} por unidad")
    

# ------------------------------------ Ejercicio 5 ---------------------------------

# 5. Ventas por Día

# Crea un diccionario llamado ingresos_por_dia donde las claves sean 
# las fechas y los valores sean los ingresos totales generados en cada día.
# Utiliza un bucle para calcular los ingresos totales por día y almacenar estos valores en el diccionario.

ingresos_por_dia = {}

for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]
    
    if fecha not in ingresos_por_dia:
        ingresos_por_dia[fecha] = 0
        
    ingresos_por_dia[fecha] += ingreso

print("\n5. INGRESOS POR DIA: ")

for fecha, monto in ingresos_por_dia.items():
    print(f"   - {fecha}: ${monto}")


# ------------------------------------ Ejercicio 6 ---------------------------------

# 6. Representación de Datos (Resumen de Ventas)

# Crea un diccionario llamado resumen_ventas donde las claves sean los nombres de los productos y
# los valores sean diccionarios anidados. Cada diccionario anidado debe contener:

# «cantidad_total»: la cantidad total vendida del producto.
# «ingresos_totales»: los ingresos totales generados por la venta del producto.
# «precio_promedio»: el precio promedio de venta del producto.

resumen_ventas = {}

for prod in ventas_por_producto:
    ingreso_prod, cant_prod = precios_por_producto[prod]
    resumen_ventas[prod] = {
        "cantidad_total": cant_prod,
        "ingresos_totales": ingreso_prod,
        "precio_promedio": ingreso_prod / cant_prod
    }

print("\n6. RESUMEN POR PRODUCTO:")

print(f"{'Producto':<15} | {'Cant.':<6} | {'Ingresos':<10} | {'Promedio':<10}")
print("-" * 50)

for prod, info in resumen_ventas.items():
    print(f"{prod:<15} | {info['cantidad_total']:<6} | ${info['ingresos_totales']:<9} | ${info['precio_promedio']:<8.2f}")