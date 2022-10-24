import mariadb
from user import conection

def sexo_do_individuo_nao_deve_ser_preenchido():
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
           SELECT v.Id, v.NomeDoIndividuo, v.SexoDoIndividuo, v.TipoImovel FROM VisitaDomiciliar v WHERE v.Id IN (
SELECT i.`Cadastro_Id` FROM `LoteIntegracao` i
LEFT JOIN `Lote` l ON (l.`Id` = i.`Lote_Id`)
WHERE i.`Erros` LIKE "%O campo \'SexoDoIndividuo\' não deve ser preenchida quando o \'Tipo Imóvel\' for igual a (02 comércio, 03 terreno baldio, 04 Ponto Estratégico, 05 Escola, 06 Creche ou 12 Estabelecimento religioso)!.%")
        ''')

        update_sql = '''UPDATE VisitaDomiciliar set SexoDoIndividuo = NULL WHERE TipoImovel IN (2,3,4,5,6,12);'''
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
            print("Lote corrigido com sucesso. - sexoDoIndividuoNaoDeveSerPreenchido - ")
    except mariadb.Error as e:
        print(f"Error: {e}")