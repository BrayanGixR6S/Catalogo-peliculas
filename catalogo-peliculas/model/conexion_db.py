import mysql.connector

class ConexionDB:
    def __init__(self):
        self.base_datos = 'peliculas'  
        self.usuario = 'root'               
        self.contraseña = '12345678'         
        self.host = 'localhost'                   

        self.conexion = mysql.connector.connect(
            host=self.host,
            user=self.usuario,
            password=self.contraseña,
            database=self.base_datos
        )
        self.cursor = self.conexion.cursor()

    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()