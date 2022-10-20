import mariadb

def tipo_de_logradouro():
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
            UPDATE Domicilio SET TipoDeLogradouro_Id = 102 WHERE TipoDeLogradouro_Id = 999;
        ''')
        con.commit()
        cur.close()
        con.close()
        print("Lote corrigido com sucesso.  - tipoDeLogradouro -")

    except mariadb.Error as e:
        print(f"Error: {e}")
