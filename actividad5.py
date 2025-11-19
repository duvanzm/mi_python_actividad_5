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
    print("")
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
            print("")
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
                print(f"Se registro el estudiante {name_student} exitosamente")
            elif opcion_estudent == 2: 
                print("-----Listando estudiantes-----")
                for i in list_students:
                    print(f"{i["name"]}")
                print(f"Total de estudiantes: {len(list_students)}")
            elif opcion_estudent == 3:
                print("-----Consultando estudiante por ID-----")
                search_id = input("Ingrese cedula / id: ")
                are_student = [a for a in list_students if a["id"] == search_id ]
                print("---Resultado de busqueda---")
                if are_student:
                    print(f"Nombre: {are_student[0]["name"]}")
                    print(f"iD: {are_student[0]["id"]}")
                    print(f"Edad: {are_student[0]["age"]}")
                else:
                    print("Ese Id no se encuentro")
            elif opcion_estudent == 4:
                print("---Eliminando Estudiante---")
                id_clear = input("Id del estudiante a eliminar: ")
                are_id = [a for a in list_students if id_clear == a["id"]]
                if are_id :
                    print(f"El estudiante {are_id[0]["name"]} se elimino exitosamente")
                    for i in list_students:
                        if i["id"] == id_clear:
                            list_students.remove(i)
                else:
                    print("Ese Id no esta")
            elif opcion_estudent == 5:
                break
            else:
                print("***Opcion invalidad***")

        
         # 2️⃣ Menú de Gestión de Materias       
        elif opcion_menu == 2:
                print("")
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
                        "name": name_materia
                    })
                    print(f"Se registro la materia {name_materia} exitosamente")
                elif opcion_materia == 2:
                    print("-----Listando Materias-----")
                    for i in list_materias:
                        print(f"{i["name"]}")
                    print(f"Total de estudiante: {len(list_materias)}")
                elif opcion_materia == 3:
                    print("-----Consultando Materias por ID-----")
                    search_id_materia = input("Ingrese id: ")
                    are_materia = [a for a in list_materias if search_id_materia == a["id"]]
                    print("---Resultado de busqueda---")
                    if are_materia:
                        print(f"Nombre: {are_materia[0]["name"]}")
                        print(f"iD: {are_materia[0]["id"]}")
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
                print("")
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
                                    print("Esta materia ya esta asignada a este usuario")
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
                    materias_dic = {m["id"]: m["name"] for m in list_materias}
                    print("Resultado: ")
                    materias_student = [
                    materias_dic[n["materia_id"]]
                        for n in notas
                            if n["user_id"] == id_user
                    ]
                    if materias_student:
                        for i in materias_student:
                            print(i)
                    else:
                        print("Este usuario no tiene materias registradas")
                elif opcion_asignacio == 3:     
                    print("---Viendo estudiantes por materia---") 
                    name_materia = input("Inglese el nombre de la materia: ").lower()
                    materia = next((m for m in list_materias if m["name"] == name_materia), None)
                    
                    if not materia:
                        print("La materia no existe.")
                    else:
                        materia_id = materia["id"]

                        estudiantes_dict = {s["id"]: s["name"] for s in list_students}

                        estudiantes_en_materia = [
                            estudiantes_dict[n["user_id"]]
                            for n in notas
                            if n["materia_id"] == materia_id
                        ]

                        if not estudiantes_en_materia:
                            print(f"No hay estudiantes inscritos en {name_materia}.")

                        print(f"Estudiantes inscritos en {name_materia}: ")
                        for est in estudiantes_en_materia:
                            print(f"- {est}")
                elif opcion_asignacio == 4: 
                    print("Quitando materia a un estudiante")    
                    name_materia = input("Ingrese el nombre de la materia: ").lower()
                    id_student = input("Ingrese el id del estudiante que le a eliminar la materia:")
                    materia = next((m for m in list_materias if m["name"].lower() == name_materia), None)
                    student = next((x for x in list_students if x["id"] == id_student), None)

                    if materia:
                        materia_id = materia["id"]
                        if student:
                            notas = [
                                n for n in notas
                                if not (n["user_id"] == id_student and n["materia_id"] == materia_id)
                            ]
                            print(f"Se eleimino la materia {materia["name"]} al estudiante {student["name"]}")
                        else:
                            print("El estudiante no existe")
                    else:
                       print("La materia no existe") 

                elif opcion_asignacio == 5:     
                    print("menu5") 
                    break
#      4️⃣ Menú de Notas y Calificaciones
        elif opcion_menu == 4:
            print("")
            print("---Menú de Notas y Calificaciones---")
            print("1. Registrar nota para un estudiante")
            print("2. Ver notas por materia")
            print("3. Ver promedio de un estudiante")
            print("4. Eliminar una nota")
            print("5. Volver al menú principal")

            choise_option = int(input("Ingrese una opcion: "))
            
            if choise_option == 1:
                print("---Registrando nota para un estudiante---")
                id_student = input("Ingrese el id del uduario: ")
                materia = input("Ingre el nombre de la materia: ").lower()
                nota = float(input("Ingrese la nota: "))
                data_student = next((s for s in list_students if s["id"] == id_student),None)
                data_materia = next((a for a in list_materias if a["name"] == materia),None)
                if data_student:
                    if data_materia:
                        materia_id = data_materia["id"]
                        data_nota = next((a for a in notas if a["user_id"] == id_student and a["materia_id"] == materia_id),None)
                        if data_nota:
                            data_nota["nota"] = nota
                            print(f"Nota actualizada para el estudiante {id_student} en {materia}: {nota}")
                        else:
                            print("El usuario no tiene esa materia registrada")

                    else:
                        print("La materia no existe")
                else:
                    print("El usuario no existe")
                 
                print("1")
            elif choise_option == 2:
                print("2")
            elif choise_option == 3:
                print("3")
            elif choise_option == 4:
                print("4")
            elif choise_option == 5:
                print("5")
            else:
                print("")
                