import mariadb

def microarea():
    try:
        con = mariadb.connect(
            user="pedro",
            password="1q2w3e4r",
            host ="dbhd.esusatendsaude.com.br",
            port=3306,
            database="eas_sp_francodarocha_teste",
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
        print("Lote corrigido com sucesso.")

    except mariadb.Error as e:
        print(f"Error: {e}")