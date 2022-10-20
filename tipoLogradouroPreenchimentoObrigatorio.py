import mariadb
from datetime import date
def tipo_logradouro_preenchimento_obrigatorio():
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
            SELECT d.Id, d.TipoDeLogradouro_Id FROM Domicilio d 
            WHERE Id IN (
            SELECT i.`Cadastro_Id` FROM `LoteIntegracao` i
            LEFT JOIN `Lote` l ON (l.`Id` = i.`Lote_Id`
            )
            WHERE i.`Erros`
            LIKE 'O campo Tipo de Logradouro é de preenchimento obrigatório ou o tipo inserido não existe!%'
            AND l.`Mes` = {date.today().month} AND l.`Ano` = {date.today().year} AND i.`STATUS` = FALSE)
        ''')

        update_sql = ''' UPDATE Domicilio d SET d.TipoDeLogradouro_Id = 104 WHERE d.TipoDeLogradouro_Id = 130'''
        arr = []
        for Id in cur:
            print("id: "+ Id)
            arr.append(Id)

        if(len(arr) == 0):
            print('Lote sem inconsistência.')
        else:
            #print("QUERRY: ", update_sql)
            cur.execute(update_sql)
            con.commit()
            cur.close()
            con.close()
            print("Lote corrigido com sucesso. - tipoLogradouroPreenchimentoObrigatorio - ")

    except mariadb.Error as e:
        print(f"Error: {e}")