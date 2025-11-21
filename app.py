
flag_sistema = 1
lista_empleados_nombres = []
lista_empleados_deptos = []
lista_empleados_sueldos = []
lista_empleados_netos = []

print("********************************")
print("SISTEMA DE NOMINAS V2.3 FINAL_REAL_AHORA_SI")
print("********************************")

while flag_sistema == 1:
    print("")
    print("1. Agregar empleado Ventas")
    print("2. Agregar empleado IT")
    print("3. Agregar empleado RRHH")
    print("4. Ver reporte")
    print("5. Salir")
    print("")
    
    x = input("Seleccione opcion: ")
    
    if x == "1":
        n = input("Nombre: ")
        s = float(input("Sueldo Bruto: "))
        
        impuesto = 0.15 
        descuento_comedor = 50
        
        temp = s * impuesto
        neto = s - temp - descuento_comedor
        
        if neto < 0:
            neto = 0
            
        lista_empleados_nombres.append(n)
        lista_empleados_deptos.append("Ventas")
        lista_empleados_sueldos.append(s)
        lista_empleados_netos.append(neto)
        print("Guardado Ventas.")

    elif x == "2":
        n = input("Nombre: ")
        s = float(input("Sueldo Bruto: "))
        
        impuesto = 0.15 
        descuento_comedor = 50
        
        temp = s * impuesto
        neto = s - temp - descuento_comedor
        
        if neto < 0:
            neto = 0
            
        lista_empleados_nombres.append(n)
        lista_empleados_deptos.append("IT")
        lista_empleados_sueldos.append(s)
        lista_empleados_netos.append(neto)
        print("Guardado IT.")

    elif x == "3":
        n = input("Nombre: ")
        s = float(input("Sueldo Bruto: "))
        
        impuesto = 0.16 
        descuento_comedor = 50
        
        temp = s * impuesto
        neto = s - temp - descuento_comedor
        
        if neto < 0:
            neto = 0
            
        lista_empleados_nombres.append(n)
        lista_empleados_deptos.append("RRHH")
        lista_empleados_sueldos.append(s)
        lista_empleados_netos.append(neto)
        print("Guardado RRHH.")
        
    elif x == "4":
        j = 0
        if len(lista_empleados_nombres) > 0:
            for item in lista_empleados_nombres:
                print("Emp: " + lista_empleados_nombres[j])
                print("Depto: " + lista_empleados_deptos[j])
                print("Pago Final:", lista_empleados_netos[j]) 
                print("----------------")
                j = j + 1
        else:
            print("No hay nadie")
            
    elif x == "5":
        flag_sistema = 0
    
    else:
        print("Error")