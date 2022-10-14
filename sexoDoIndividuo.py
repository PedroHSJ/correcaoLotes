import mariadb
from datetime import date


def sexo_do_individuo():
    try:
        con = mariadb.connect(
            user="pedro",
            password="1q2w3e4r",
            host ="dbhd.esusatendsaude.com.br",
            port=3306,
            database="eas_sp_francodarocha_teste",
        )
        cur = con.cursor()
        
        cur.execute(f'''
        SELECT i.`Cadastro_Id` AS Id FROM `LoteIntegracao` i
            LEFT JOIN `Lote` l ON (l.`Id` = i.`Lote_Id`)
            WHERE i.`Erros` 
            LIKE '%O campo \'SexoDoIndividuo\' é de preenchimento obrigatório para este tipo de cadastro conforme as regras %'
            AND l.`Mes` = {date.today().month} AND l.`Ano` = {date.today().year} AND i.`STATUS` = FALSE
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
            print("QUERRY: ", update_sql + ids)
            #cur.execute(update_sql + ids)
        


            con.commit()
            cur.close()
            con.close()
            print("Lote corrigido com sucesso.")

    except mariadb.Error as e:
        print(f"Error: {e}")

