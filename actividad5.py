# Variable Prueva.
list_students = [
    {
    "name": "pedrito",
    "id": "22",
    "age": 23,
    },
    {
    "name": "Juanito",
    "id": "23",
    "age": 55,
    }
]


list_materias = [
    {
    "id": "13",
    "name": "ingles",
    },
    {
    "id": "12",
    "name": "español",
    }
    
    ]

notas = [
     {
         "user_id" : "22",
         "materia_id" : "12",
         "nota" : 0.6
     },
     {
         "user_id" : "23",
         "materia_id" : "12",
         "nota" : 0.7
     },
     {
         "user_id" : "23",
         "materia_id" : "13",
         "nota" : 0.7
     }
]
while True:
    #     Menu principal
    print("----Menu principal----")
    print("1. Gestión de Estudiantes")
    print("2. Gestión de Materias")
    print("3. Asignaciones (Estudiante ↔ Materias)")
    print("4. Notas y Calificaciones")
    print("5. Reportes y Estadísticas")
    print("6. Salir")

    opcion_menu = int(input("Seleccione una opción: "))

    # 1️⃣ Menú de Gestión de Estudiantes
    while True:
        
        if opcion_menu == 1:
            print("----Menú de Gestión de Estudiantes----")
            print("1. Registrar estudiante")
            print("2. Listar estudiantes")
            print("3. Consultar estudiante por ID")
            print("4. Eliminar estudiante")
            print("5. Volver al menú principal")

            opcion_estudent = int(input("Seleccione una opción: "))

            if opcion_estudent == 1:
                print("-----Registrando Estudiante-----")
                name_student = input("Ingrese nombre: ")
                id_student = input("Ingrese cedula / id: ")
                age_student = int(input("Ingrese edad: "))
                list_students.append({
                    "name": name_student,
                    "id": id_student,
                    "age": age_student
                })
            elif opcion_estudent == 2: 
                print("-----Listando estudiantes-----")
                for i in list_students:
                    print(f"{i["name"]}")
                    print(f"Total de estudiante: {len(list_students)}")
            elif opcion_estudent == 3:
                print("-----Consultando estudiante por ID-----")
                search_id = input("Ingrese cedula / id: ")
                for i in list_students:
                    if i["id"] == search_id:
                        print("---Resultado de busqueda---")
                        print(f"Nombre: {i["name"]}")
                        print(f"iD: {i["id"]}")
                        print(f"Edad: {i["age"]}")
                        print("Materias: ")
                        if len(i["materias"]) > 0:
                            for x in i["materias"]:
                                print(f"{x["nombre_materia"]}")
                        else:
                            print("No tiene materias registradas")

                    else:
                        print("Ese Id no se encuentro")
            elif opcion_estudent == 4:
                print("---Eliminando Estudiante---")
                id_clear = input("Id del estudiante a eliminar: ")
                stay = 0
                
                for i in list_students:
                    if i["id"] == id_clear:
                        list_students.remove(i)
                        print(f"Se elimino el estudiante: {i["name"]}")
                    else:
                        stay += 0
                if stay > 0:
                    print(f"El {id_clear} no se esta en la base de datos")        
            elif opcion_estudent == 5:
                break
            else:
                print("***Opcion invalidad***")

        
         # 2️⃣ Menú de Gestión de Materias       
        elif opcion_menu == 2:
            while True:
                print("----Menú de Gestión de Materias----")
                print("1. Registrar Materia")
                print("2. Listar Materias")
                print("3. Consultar Materia por ID")
                print("4. Eliminar Materia")
                print("5. Volver al menú principal")

                opcion_materia = int(input("Seleccione una opción: "))

                if opcion_materia == 1:
                    print("-----Registrando Materia-----")    
                    name_materia = input("Ingrese nombre: ").lower()
                    id_materia = input("Ingrese id: ")
                    list_materias.append({
                        "id": id_materia,
                        "nombre": list_materias
                    })
                elif opcion_materia == 2:
                    print("-----Listando Materias-----")
                    for i in list_materias:
                        print(f"{i["name"]}")
                        print(f"Total de estudiante: {len(list_materias)}")
                elif opcion_materia == 3:
                    print("-----Consultando Materias por ID-----")
                    search_id_materia = input("Ingrese id: ")
                    for i in list_materias:
                        if i["id"] == search_id_materia:
                            print("---Resultado de busqueda---")
                            print(f"Nombre: {i["name"]}")
                            print(f"iD: {i["id"]}")
                        else:
                            print("Ese Id no se encuentro")

                elif opcion_materia == 4:
                    print("---Eliminando Materias---")
                    id_clear_materia = input("Id del Materias a eliminar: ")
                    stay_materia = 0
                    
                    for i in list_materias:
                        if i["id"] == id_clear_materia:
                            list_materias.remove(i)
                            print(f"Se elimino el estudiante: {i["name"]}")
                        else:
                            stay_materia += 0
                    if stay_materia > 0:
                        print(f"El {id_clear_materia} no se esta en la base de datos")
                elif opcion_materia == 5:
                    break    
        

         # 3️⃣ Menú de Asignaciones
        elif opcion_menu == 3:
            while True:
                print("----Menú de Asignaciones----")
                print("1. Asignar materia a estudiante")
                print("2. Ver materias de un estudiante")
                print("3. Ver estudiantes por materia")
                print("4. Quitar materia a un estudiante")
                print("5. Volver al menú principal")

                opcion_asignacio = int(input("Ingrese una opcion: "))
                
                if opcion_asignacio == 1:
                    print("---Asignando materia a estudiante---")
                    student_id = input("Ingrese Id de estudiante: ")
                    exists_id = next((i for i in list_students if i["id"] == student_id ), 0)
                    if exists_id != 0:
                        name_materia = input("Nombre de materia a agregar: ").lower()
                        exists_materia = next((a for a in list_materias if a["name"] == name_materia), 0)
                        if exists_materia != 0:
                                ya_exists = any(n for n in notas if n["user_id"] == student_id and n["materia_id"] == exists_materia["id"] )
                                if ya_exists :
                                    print("Es materia ya esta asignada a este usuario")
                                else:
                                    notas.append({
                                        "user_id": student_id,
                                        "materia_id": exists_materia["id"],
                                        "nota": float()
                                    })

                        else:
                            print("La materia no esta")
                    else:
                            print("Estudiante no esta") 
                elif opcion_asignacio == 2:
                    print("---Viendo materia de estudiante---")
                    id_user = input("Ingrese el Id del estudiante: ")
                    exists_user = [i for i in notas if i["user_id"] == id_user]
                    if not exists_user:
                        print("El Estudiante no tiene materias asignadas")
                    else:
                        print(exists_user)
                        print("Materias del estudiante: ")
                        for i in range(len(list_materias)):
                          if list_materias[i]["id"] == exists_user[0]["materia_id"]:
                              print(f"{list_materias[i]["name"]}")
                elif opcion_asignacio == 3:     
                    print("---Viendo estudiantes por materia---") 
                    materia = input("Inglese el nombre de la materia: ").lower()
                    exists_materia = [i for i in list_materias if i["name"] == materia]
                    if not materia:
                        print("Esta materia no esta registradad")
                    else:
                        print(exists_materia)
                        for i in range(len(list_students)):
                            if notas[i]["user_id"] == list_students[i]["id"]:
                                print(f"{list_students[i]["name"]}")
                elif opcion_asignacio == 4:     
                    print("menu4") 
                elif opcion_asignacio == 5:     
                    print("menu5") 
                    break
