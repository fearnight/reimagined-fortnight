
exit_program = False
todo = []
completed = []

def addtarea():
    tarea = input("Write the task to add\n")
    todo.append(tarea)
    print(todo)

def comptarea():
    print(todo)
    tarea = input("Escribe tarea a completar\n")

    if tarea in todo:
        todo.remove(tarea)
        completed.append (tarea)
    else:
        print("\nLa tarea no existe\n")

def vertarea():
    print(todo)

def completado():
    print(completed)


while exit_program == False:
    seleccion = input(" 1. Agregar tarea \n 2. Marcar tarea como completada \n 3. Ver tareas pendientes \n 4. Ver tareas completadas \n 5. Salir \n")
    if seleccion == '1':
        addtarea()
    elif seleccion == '2':
        comptarea()
    elif seleccion == '3':
        vertarea()
    elif seleccion == '4':
        completado()
    elif seleccion == '5':
        exit_program = True
