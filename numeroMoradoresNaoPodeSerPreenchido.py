import mariadb
from user import conection

def numero_moradores_nao_pode_ser_preenchido():
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
            SELECT d.Id FROM `Domicilio` d
            WHERE d.`TipoDeImovel` IN (4,3,2,5,6,12,99)
            AND d.`NumeroDeMoradores` IS NOT NULL;
        ''')

        update_sql = '''UPDATE  `Domicilio` d SET d.`NumeroDeMoradores` = NULL
                        WHERE d.`TipoDeImovel` IN (4,3,2,5,6,12,99)
                        AND d.`NumeroDeMoradores` IS NOT NULL;'''
        arr = []
        for Id in cur:
            arr.append(Id)

        if(len(arr) == 0):
            print('Lote sem inconsistência.')
        else:
            #print("QUERRY: ", update_sql)
            cur.execute(update_sql)
            con.commit()
            cur.close()
            con.close()
            print("Lote corrigido com sucesso. - numeroMoradoresNaoPodeSerPreenchido - ")


    except mariadb.Error as e:
        print(f"Error: {e}")