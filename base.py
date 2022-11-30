import mysql.connector

class Base:
    """ Clase para manejar la Base de Datos """

    def __init__(self, db_host, db_user, db_pass, db_schema):
        
        self.conexion = mysql.connector.connect(
            host=db_host, 
            user=db_user, 
            passwd=db_pass,
            database=db_schema)
        self.cursor = self.conexion.cursor()

    def mostrar_tablas(self):
        self.cursor.execute("show tables;")
        for base in self.cursor:
            print(base)

    def agregar(self, hum, tem, luz, pot, sw1, sw2):
        # insertar datos de sensores
        sql = f"insert into sensores values(now(), {hum}, {tem}, {luz},{pot});"
        self.cursor.execute(sql)
        sql = f"update switches set valor = {sw1} where id = 1;"
        self.cursor.execute(sql)
        sql = f"update switches set valor = {sw2} where id = 2;"
        self.cursor.execute(sql)
        self.conexion.commit()
        print("data agregada!")


    def cerar(self):
        self.cursor.close()