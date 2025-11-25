import pyodbc
from db import conn

cursor = conn.cursor()

# insert departamentos
cursor.execute("INSERT INTO Departamentos (Nombre, Presupuesto) VALUES (?, ?)", ("Recursos Humanos", 50000.00))
cursor.execute("INSERT INTO Departamentos (Nombre, Presupuesto) VALUES (?, ?)", ("Ventas", 75000.00))
cursor.execute("INSERT INTO Departamentos (Nombre, Presupuesto) VALUES (?, ?)", ("TI", 120000.00))

conn.commit()
cursor.close()
print("Departamentos agregados correctamente.")
