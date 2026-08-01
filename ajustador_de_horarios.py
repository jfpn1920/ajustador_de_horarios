ids = []
actividades = []
dias = []
horas_inicio = []
horas_fin = []
lugares = []
observaciones = []
#------------------------------------------#
#--|menu_principal_ajustador_de_horarios|--#
#------------------------------------------#
while True:
    print("menu principal ajustador de horarios")
    print("1) crear horario")
    print("2) editar horario")
    print("3) eliminar horario")
    print("4) buscar horario")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #-------------------#
    #--|crear_horario|--#
    #-------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_horario = 1
        else:
            id_horario = ids[-1] + 1
        actividad = input("actividad: ")
        dia = input("día: ")
        hora_inicio = input("hora de inicio: ")
        hora_fin = input("hora de finalización: ")
        lugar = input("lugar: ")
        observacion = input("observación: ")
        ids.append(id_horario)
        actividades.append(actividad)
        dias.append(dia)
        horas_inicio.append(hora_inicio)
        horas_fin.append(hora_fin)
        lugares.append(lugar)
        observaciones.append(observacion)
        print("horario registrado correctamente.")
        print("id:", id_horario)
    #--------------------#
    #--|editar_horario|--#
    #--------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar horario")
            for i in range(len(ids)):
                print(f"{ids[i]} | {actividades[i]} | {dias[i]} | {horas_inicio[i]} | {horas_fin[i]} | {lugares[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {actividades[posicion]} | {dias[posicion]} | {horas_inicio[posicion]} | {horas_fin[posicion]} | {lugares[posicion]} | {observaciones[posicion]}")
                actividades[posicion] = input("nueva actividad: ")
                dias[posicion] = input("nuevo día: ")
                horas_inicio[posicion] = input("nueva hora de inicio: ")
                horas_fin[posicion] = input("nueva hora de finalización: ")
                lugares[posicion] = input("nuevo lugar: ")
                observaciones[posicion] = input("nueva observación: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #----------------------#
    #--|eliminar_horario|--#
    #----------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar horario")
            for i in range(len(ids)):
                print(f"{ids[i]} | {actividades[i]} | {dias[i]} | {horas_inicio[i]} | {horas_fin[i]} | {lugares[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {actividades[posicion]} | {dias[posicion]} | {horas_inicio[posicion]} | {horas_fin[posicion]} | {lugares[posicion]} | {observaciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    actividades.pop(posicion)
                    dias.pop(posicion)
                    horas_inicio.pop(posicion)
                    horas_fin.pop(posicion)
                    lugares.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #--------------------#
    #--|buscar_horario|--#
    #--------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar horario")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {actividades[posicion]} | {dias[posicion]} | {horas_inicio[posicion]} | {horas_fin[posicion]} | {lugares[posicion]} | {observaciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {actividades[i]} | {dias[i]} | {horas_inicio[i]} | {horas_fin[i]} | {lugares[i]} | {observaciones[i]}")
            print("estadísticas ajustador de horarios")
            print("cantidad de horarios:", len(ids))
            print("cantidad de actividades:", len(actividades))
            print("primer horario registrado:", horas_inicio[0])
            print("último horario registrado:", horas_inicio[-1])
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el ajustador de horarios.")
        break
    else:
        print("opción no válida.")