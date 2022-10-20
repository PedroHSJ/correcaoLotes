import mariadb
from datetime import date

def situacao_rua_higiene_pessoal():
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
        SELECT i.`Cadastro_Id`, i.Tipo FROM `LoteIntegracao` i
        LEFT JOIN `Lote` l ON (l.`Id` = i.`Lote_Id`)
        WHERE i.`Erros` LIKE '%SituacaoRua: Higiene Pessoal: Este campo é de preenchimento obrigatório!%'
        AND i.`STATUS` = FALSE
        AND l.Mes = {date.today().month} AND l.Ano = {date.today().yaer};
        ''')

        arr = []
        for Cadastro_Id in cur:
            arr.append(Cadastro_Id)

        if(len(arr) == 0):
            print('Lote sem inconsistência.')
        else:
            update_sql = "UPDATE SituacaoDeRua SET AcessosAHigiene = 45 WHERE AcessosAHigiene = '';"
            print("QUERRY: ", update_sql)
            #cur.execute(update_sql)
            con.commit()
            cur.close()
            con.close()
            print("Lote corrigido com sucesso. - situacaoRuaHigienePessoal -")

    except mariadb.Error as e:
        print(f"Error: {e}")