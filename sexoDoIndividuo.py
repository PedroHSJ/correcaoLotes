import mariadb
from datetime import date
from user import conection

def sexo_do_individuo():
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
        SELECT i.`Cadastro_Id` FROM `LoteIntegracao` i
        LEFT JOIN `Lote` l ON (l.`Id` = i.`Lote_Id`)
        WHERE i.`Erros` LIKE "%O campo \'SexoDoIndividuo\' é de preenchimento obrigatório para este tipo de cadastro conforme as regras %"
        AND l.`Mes` = 10 AND l.`Ano` = 2022 AND i.`STATUS` = FALSE
        ''')

        update_sql = '''UPDATE VisitaDomiciliar set SexoDoIndividuo = 4 WHERE Id IN '''

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
                    ids += "'" + id + "'" + ");"
                else:
                    ids += "'" + id + "'" + ', '
            #print("QUERRY: ", update_sql + ids)
            cur.execute(update_sql + ids)
        


            con.commit()
            cur.close()
            con.close()
            print("Lote corrigido com sucesso. - sexoDoIndividuo -")

    except mariadb.Error as e:
        print(f"Error: {e}")

