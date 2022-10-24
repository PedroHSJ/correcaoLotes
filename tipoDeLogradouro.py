import mariadb
from user import conection

def tipo_de_logradouro():
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
            UPDATE Domicilio SET TipoDeLogradouro_Id = 102 WHERE TipoDeLogradouro_Id = 999;
        ''')
        con.commit()
        cur.close()
        con.close()
        print("Lote corrigido com sucesso.  - tipoDeLogradouro -")

    except mariadb.Error as e:
        print(f"Error: {e}")
