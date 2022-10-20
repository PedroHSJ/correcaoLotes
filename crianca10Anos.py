import mariadb

def crianca10Anos():
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
        SELECT i.Id, 
        YEAR(NOW())-YEAR(i.DataNascimento)-IF(MONTH(NOW())*32+DAY(NOW())<MONTH(i.DataNascimento)*32+DAY(i.DataNascimento),1,0) AS Idade
        FROM Individuo i
        WHERE i.ResponsavelPorCrianca IS NOT NULL
        HAVING Idade >= 10
        ''')

        update_sql = "UPDATE Individuo SET ResponsavelPorCrianca = NULL WHERE Id IN "

        arr = []
        for id,idade in cur:
            arr.append(id)

        if(len(arr) == 0):
            print('Lote sem inconsistência.')
        else:
            ids = "("
            count = 0
            for id in arr:
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
            print("Lote corrigido com sucesso. - crianca10Anos - ")

    except mariadb.Error as e:
        print(f"Error: {e}")

