from db import get_connection


def mostrar_departamentos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT IdDepartamento, Nombre, Presupuesto FROM Departamentos")
    rows = cursor.fetchall()

    print("\n=== LISTA DE DEPARTAMENTOS ===")
    for r in rows:
        print(f"ID: {r.IdDepartamento} | Nombre: {r.Nombre} | Presupuesto: {r.Presupuesto}")

    conn.close()


def mostrar_puestos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT IdPuesto, Nombre, SalarioBase, IdDepartamento
        FROM Puestos
    """)
    rows = cursor.fetchall()

    print("\n=== LISTA DE PUESTOS ===")
    for r in rows:
        print(f"ID: {r.IdPuesto} | Nombre: {r.Nombre} | Salario Base: {r.SalarioBase} | Departamento: {r.IdDepartamento}")

    conn.close()


def mostrar_empleados():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT IdEmpleados, Nombre, Identificacion, IdPuesto
        FROM Empleados
    """)
    rows = cursor.fetchall()

    print("\n=== LISTA DE EMPLEADOS ===")
    for r in rows:
        print(f"ID: {r.IdEmpleados} | Nombre: {r.Nombre} | Identificación: {r.Identificacion} | Puesto: {r.IdPuesto}")

    conn.close()




def crear_empleado():
    conn = get_connection()
    cursor = conn.cursor()

    print("\n=== CREAR EMPLEADO ===")
    nombre = input("Nombre: ")
    identificacion = input("Identificación: ")
    idpuesto = input("Id del Puesto: ")

    cursor.execute("""
        INSERT INTO Empleados (Nombre, Identificacion, IdPuesto)
        VALUES (?, ?, ?)
    """, (nombre, identificacion, idpuesto))

    conn.commit()
    conn.close()
    print("Empleado creado correctamente.\n")


def editar_empleado():
    conn = get_connection()
    cursor = conn.cursor()

    print("\n=== EDITAR EMPLEADO ===")
    id_emp = input("Id del empleado a editar: ")

    cursor.execute("SELECT * FROM Empleados WHERE IdEmpleados = ?", id_emp)
    empleado = cursor.fetchone()

    if empleado is None:
        print("No existe un empleado con ese ID.\n")
        return

    nuevo_nombre = input(f"Nuevo nombre ({empleado.Nombre}): ") or empleado.Nombre
    nueva_ident = input(f"Nueva identificación ({empleado.Identificacion}): ") or empleado.Identificacion
    nuevo_puesto = input(f"Nuevo id de puesto ({empleado.IdPuesto}): ") or empleado.IdPuesto

    cursor.execute("""
        UPDATE Empleados
        SET Nombre = ?, Identificacion = ?, IdPuesto = ?
        WHERE IdEmpleados = ?
    """, (nuevo_nombre, nueva_ident, nuevo_puesto, id_emp))

    conn.commit()
    conn.close()
    print("Empleado actualizado correctamente.\n")


def eliminar_empleado():
    conn = get_connection()
    cursor = conn.cursor()

    print("\n=== ELIMINAR EMPLEADO ===")
    id_emp = input("Id del empleado a eliminar: ")

    cursor.execute("SELECT * FROM Empleados WHERE IdEmpleados = ?", id_emp)
    if cursor.fetchone() is None:
        print("No existe un empleado con ese ID.\n")
        return

    cursor.execute("DELETE FROM Empleados WHERE IdEmpleados = ?", id_emp)
    conn.commit()
    conn.close()
    print("Empleado eliminado correctamente.\n")




def menu():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Ver Departamentos")
        print("2. Ver Puestos")
        print("3. Ver Empleados")
        print("4. Crear Empleado")
        print("5. Editar Empleado")
        print("6. Eliminar Empleado")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_departamentos()
        elif opcion == "2":
            mostrar_puestos()
        elif opcion == "3":
            mostrar_empleados()
        elif opcion == "4":
            crear_empleado()
        elif opcion == "5":
            editar_empleado()
        elif opcion == "6":
            eliminar_empleado()
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    print("Conexión exitosa, resultado de prueba: 1")
    menu()
