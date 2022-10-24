import mariadb
from user import conection

def microarea():
    try:
        con = mariadb.connect(
              user=conection["user"],
            password=conection["password"],
            host =conection["host"],
            port=conection["port"],
            database=conection["database"],
        )
        cur = con.cursor()

        cur.execute('''
        UPDATE Domicilio AS a 
        INNER JOIN Profissional AS b ON b.Id = a.Profissional_Id
        SET a.MicroArea = b.MicroArea
        WHERE CHAR_LENGTH(a.MicroArea) > 2
        AND b.MicroArea IS NOT NULL;       
        ''')

        cur.execute('''
        UPDATE Individuo AS a 
        INNER JOIN Profissional AS b ON b.Id = a.Profissional_Id
        SET a.MicroArea = b.MicroArea
        WHERE CHAR_LENGTH(a.MicroArea) > 2
        AND b.MicroArea IS NOT NULL;
        ''')    

        cur.execute('''
        UPDATE VisitaDomiciliar AS a 
        INNER JOIN Profissional AS b ON b.Id = a.Profissional_Id
        SET a.MicroArea = b.MicroArea
        WHERE CHAR_LENGTH(a.MicroArea) > 2
        AND b.MicroArea IS NOT NULL;
        ''')

        con.commit()
        cur.close()
        con.close()
        print("Lote corrigido com sucesso. - microarea - ")

    except mariadb.Error as e:
        print(f"Error: {e}")