import mariadb
from datetime import date
from user import conection


def desfecho_da_visita_3ou2():
    try:
        con = mariadb.connect(
             user=conection["user"],
            password=conection["password"],
            host =conection["host"],
            port=conection["port"],
            database=conection["database"],
        )
        cur = con.cursor()

        cur.execute(f'''
                SELECT v.Id, v.MotivosDaVisita, v.DesfechoDeCadastro, v.Desfecho from VisitaDomiciliar v WHERE v.Id in (
	            SELECT i.`Cadastro_Id` FROM `LoteIntegracao` i
	            LEFT JOIN `Lote` l ON (l.`Id` = i.`Lote_Id`)
	            WHERE i.`Erros` LIKE '%O campo ''MotivosDaVisita'' não deve ser preenchido quando o ''Desfecho da Visita'' for igual a (3 Ausente ou 2 Visita Recusada)%'
	            AND l.`Mes` = {date.today().month} AND l.`Ano` = {date.today().year} AND i.`STATUS` = FALSE)''')

        update_sql = "UPDATE VisitaDomiciliar vd set vd.MotivosDaVisita = "" WHERE vd.Desfecho IN(3, 2) AND vd.Id IN"
        arr = []
        for Id, MotivosDaVisita, DesfechoDeCadastro, Desfecho in cur:
            arr.append(Id)

        if(len(arr) == 0):
            print('Lote sem inconsistência.')
        else:
            ids = "("
            count = 0
            for id in arr:
                id = ''.join(id)
                count+=1
                if(count == len(arr)):
                    ids += "'" + id + "'" + ")"
                else:
                    ids += "'" + id + "'" + ', '
            #print("QUERRY: ", update_sql + ids)
            cur.execute(update_sql + ids)

            cur.execute(update_sql)
            con.commit()
            cur.close()
            con.close()
            print("Lote corrigido com sucesso. - desfechoDaVisita -")
    except mariadb.Error as e:
        print(f"Error: {e}")