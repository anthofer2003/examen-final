# Data access object - DAO
from flask import current_app as app
from conexion.Conexion import Conexion

class CargosDao:

    def getCargos(self):

        cargoSQL = """
        SELECT id, descripcion
        FROM cargos
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(cargoSQL)
            # trae datos de la bd
            lista_cargos = cur.fetchall()
            # retorno los datos
            lista_ordenada = []
            for item in lista_cargos:
                lista_ordenada.append({
                    "id": item[0],
                    "descripcion": item[1]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getCargoById(self, id):

        cargoSQL = """
        SELECT id, descripcion
        FROM cargos WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(cargoSQL, (id,))
            # trae datos de la bd
            cargoEncontrada = cur.fetchone()
            # retorno los datos
            return {
                    "id": cargoEncontrada[0],
                    "descripcion": cargoEncontrada[1]
                }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarCargo(self, descripcion):

        insertCargoSQL = """
        INSERT INTO cargos(descripcion) VALUES(%s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertCargoSQL, (descripcion,))
            # se confirma la insercion
            con.commit()

            return True

        # Si algo fallo entra aqui
        except con.Error as e:
            app.logger.info(e)

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

        return False

    def updateCargo(self, id, descripcion):

        updateCargoSQL = """
        UPDATE cargos
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateCargoSQL, (descripcion, id,))
            # se confirma la insercion
            con.commit()

            return True

        # Si algo fallo entra aqui
        except con.Error as e:
            app.logger.info(e)

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

        return False

    def deleteCargo(self, id):

        updateCargoSQL = """
        DELETE FROM cargos
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateCargoSQL, (id,))
            # se confirma la insercion
            con.commit()

            return True

        # Si algo fallo entra aqui
        except con.Error as e:
            app.logger.info(e)

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

        return False