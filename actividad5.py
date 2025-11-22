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
         "nota" : 2.9
     },
     {
         "user_id" : "23",
         "materia_id" : "12",
         "nota" : 4
     },
     {
         "user_id" : "23",
         "materia_id" : "13",
         "nota" : 3.5
     }
]
while True:
    #     Menu principal
    try:
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
                    else:
                        print("***Opcion ivalidad***")
                    

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
                        break
                    else:
                        print("***Opcion ivalidad***") 
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
                    print("---Viendo notas por materia---")
                    name_materia = input("Ingrese el nombre de la materia: ").lower()
                    data_materias = next((i for i in list_materias if i["name"] == name_materia), None)
                    if data_materias:
                        id_materia = data_materias["id"]
                        all_notas = [a for a in notas if a["materia_id"] == id_materia]
                        print(all_notas)
                        if all_notas:
                            print("Notas: ")
                            for i in all_notas:
                                print(f"{i["nota"]}")
                        else:
                            print("Esta materi no tiene notas ")
                    else:
                        print("La materia no existe")    
                    print("")
                elif choise_option == 3:
                    print("---Viendo promedio de un estudiante---")
                    id_student = input("Ingrese el Id: ")
                    are_student = next((a for a in list_students if a["id"] == id_student),None)
                    data_notas = [i for i in notas if i["user_id"] == id_student]

                    if are_student:
                        if data_notas:
                            print("Notas de  las materias: ")
                            print("---------------------------")
                            promedio = 0
                            for i in data_notas:
                                promedio = i["nota"] + promedio
                                print(i["nota"])
                            promedio = promedio/len(data_notas)
                            print("-------------------")
                            print(f"Promedio: {round(promedio, 2)}")
                        else:
                            print(f"El estuianten {are_student["name"]} no tiene notas registradas")
                    else:
                        print("El estudiante no existe")  
                elif choise_option == 4:
                    print("---Eliminando una nota---")
                    id_student = input("Ingrese el Id: ")
                    data_student = next((a for a in list_students if a["id"] == id_student), None)
                    if data_student:
                        name_materia = input("Ingrese la materia para eliminar la nota: ").lower()
                        data_materia = next((x for x in list_materias if x["name"] == name_materia ), None)
                        if data_materia:
                            nota = next((f for f in notas if f["user_id"] == id_student and  f["materia_id"] == data_materia["id"]), None)
                            if nota: 
                                for i in  range(len(notas)):
                                    if notas[i]["user_id"] == id_student and notas[i]["materia_id"] == data_materia["id"]:
                                        notas[i]["nota"] == 0
                                        print(f"La Nota de {name_materia} se elimino exitosamente")
                            else:
                                print(f"la materia {name_materia} no esta asignada a el estudiante")     
                        else:
                            print(f"la materi {name_materia} no existe")
                    else:
                        print(f"El estudiante con id {id_student} no existe")
                elif choise_option == 5:
                    break
                else:
                    print("***Opcion ivalidad***")
                    
            elif opcion_menu == 5:

                print("")
                print("---Menú de Reportes y Estadísticas---")
                print("1. Promedios detallados por estudiante")
                print("2. Estudiante con mejor promedio")        
                print("3. Porcentaje de aprobación del grupo")        
                print("4. Promedio general del grupo")        
                print("5. Ranking de estudiantes")
                print("6. Volver al menú principal")

                choise_option = int(input("Ingrese una opcion: "))

                if choise_option == 1:  
                    id_student = input("Ingrese el id del estudiante: ")
                    student = next((s for s in list_students if s["id"] == id_student), None)

                    if student:
                        print(f"Notas del estudiante: {student['name']}")
                        materias_map = {m["id"]: m["name"] for m in list_materias}
                        notas_est = [n for n in notas if n["user_id"] == id_student]
                        total = 0
                        for n in notas_est:
                            materia_nombre = materias_map.get(n["materia_id"], "Materia desconocida")
                            print(f"- {materia_nombre}: {n['nota']}")
                            total += n["nota"]

                        if notas_est:
                            promedio = total / len(notas_est)
                            print(f"Promedio general: {promedio}")
                        else:
                            print("Este estudiante no tiene notas registradas.")

                    else:
                        print("Estudiante no existe.")
                
                elif choise_option == 2: 
                    print("---Estudiante con mejor promedio---") 

                    promedios = {}

                    for s in list_students:
                        notas_est = [n["nota"] for n in notas if n["user_id"] == s["id"]]
                        if notas_est:  
                            promedios[s["id"]] = sum(notas_est) / len(notas_est)
                        else:
                            promedios[s["id"]] = 0  

                    mejor_id = max(promedios, key=promedios.get) 
                    mejor_promedio = promedios[mejor_id]

                    mejor_student = next(s for s in list_students if s["id"] == mejor_id)

                    print("El mejor promedio:")
                    print(f"Nombre: {mejor_student["name"]}")
                    print(f"ID: {mejor_id}")
                    print(f"Promedio: {mejor_promedio}")

                elif choise_option == 3: 
                    print("---Porcentaje de aprobación del grupo---")
                    nota_minima = 3.0


                    total_notas = len(notas)
                    aprobadas = sum(1 for n in notas if n["nota"] >= nota_minima)


                    if total_notas > 0:
                        porcentaje_aprobacion = (aprobadas / total_notas) * 100
                    else:
                        porcentaje_aprobacion = 0

                    print(f"Total de notas: {total_notas}")
                    print(f"Notas aprobadas: {aprobadas}")
                    print(f"Porcentaje de aprobación del grupo: {porcentaje_aprobacion:.2f}%")

                elif choise_option == 4: 
                    print("---Promedio general del grupo---") 
                    total_notas = len(notas)

                    suma_notas = sum(n["nota"] for n in notas)

                    if total_notas > 0:
                        promedio_general = suma_notas / total_notas
                    else:
                        promedio_general = 0

                    print(f"Promedio general del grupo: {promedio_general:.2f}")

                elif choise_option == 5: 
                    print("---Porcentaje de aprobación del grupo---")  

                    promedios = [] 
                    for student in list_students:
                        notas_est = [n["nota"] for n in notas if n["user_id"] == student["id"]]

                        if notas_est:
                            promedio = sum(notas_est) / len(notas_est)
                        else:
                            promedio = 0 
                            
                        promedios.append({
                            "name": student["name"],
                            "id": student["id"],
                            "promedio": promedio
                        })

                    ranking = sorted(promedios, key=lambda x: x["promedio"], reverse=True)

                    print("Ranking del mejor Estudiante  ")
                    pos = 1
                    for x in ranking:
                        print(f"{pos}. {x['name']} - Promedio: {x['promedio']:.2f}")
                        pos += 1   
                elif choise_option == 6: 
                    break  
                else:
                    print("*** Opcion Ivalidad ***")      
            elif opcion_menu == 6:
                print("Chao Chao")
                break

            else:
                print("*** Opcion Ivalidad ***")
    except:
        print("   ***ERROR EN DATOS***")
        print("INTENTA INGRESAR DATOS VALIDOS")
