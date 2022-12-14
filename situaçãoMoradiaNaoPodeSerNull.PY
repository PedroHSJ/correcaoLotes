import mariadb
from user import conection

def situacao_moradia_nao_pode_ser_null():
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
        UPDATE Domicilio set SituacaoDeMoradia = 82 WHERE TipoDeImovel = 1 AND SituacaoDeMoradia IS NULL;
        ''')

        con.commit()
        cur.close()
        con.close()
        print("Lote corrigido com sucesso. - situacaoMoradiaNaoPodeSerNull -")
    except mariadb.Error as e:
        print(f"Error: {e}")