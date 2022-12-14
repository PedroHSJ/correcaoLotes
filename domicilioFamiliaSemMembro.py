import mariadb
from datetime import date
from user import conection

def domicilio_familia_sem_membro():
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
        SELECT i.Cadastro_Id as Id FROM LoteIntegracao i
            LEFT JOIN Lote l ON (l.Id = i.Lote_Id)
            INNER JOIN Domicilio d ON (i.Cadastro_Id = d.id)
            WHERE i.Erros LIKE '%Domícilio possui família sem membros.%' AND l.Mes = {date.today().month} AND l.Ano = {date.today().year}
        ''')

        update_sql = '''UPDATE `Familia` f SET f.`QuantMembros` = 1
                            WHERE f.`Domicilio_Id` IN 
    '''

        arr = []
        for Id in cur:
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
            #print("QUERRY: ", update_sql + ids + 'AND f.`QuantMembros` = 0')
            cur.execute(update_sql + ids + 'AND f.`QuantMembros` = 0')
        


            con.commit()
            cur.close()
            con.close()
            print("Lote corrigido com sucesso. - domicilioFamiliaSemMembro -")
    except mariadb.Error as e:
        print(f"Error: {e}")

