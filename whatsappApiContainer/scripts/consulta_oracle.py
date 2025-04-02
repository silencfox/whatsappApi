import cx_Oracle

# Configuración de la conexión
dsn = cx_Oracle.makedsn("oracle_host", 1521, service_name="orclpdb1")
connection = cx_Oracle.connect(user="usuario", password="contraseña", dsn=dsn)

cursor = connection.cursor()
cursor.execute("SELECT * FROM DUAL")

for row in cursor:
    print(row)

cursor.close()
connection.close()
