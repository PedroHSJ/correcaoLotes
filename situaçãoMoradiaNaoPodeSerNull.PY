import mariadb

def situacao_moradia_nao_pode_ser_null():
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
        UPDATE Domicilio set SituacaoDeMoradia = 82 WHERE TipoDeImovel = 1 AND SituacaoDeMoradia IS NULL;
        ''')

        con.commit()
        cur.close()
        con.close()
        print("Lote corrigido com sucesso. - situacaoMoradiaNaoPodeSerNull -")
    except mariadb.Error as e:
        print(f"Error: {e}")