import mariadb

def numero_moradores():
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
        UPDATE  `Domicilio` d
        SET d.`NumeroDeMoradores` = 
        (
        SELECT SUM(f.`QuantMembros`)FROM `Familia` f 
        WHERE (d.`Id` = f.`Domicilio_Id` AND f.`Deletado` = FALSE AND f.`MudouSe` = FALSE)
        ) 
        WHERE  
        d.`TipoDeImovel` = 1 AND d.DesfechoDeCadastro = 0 
	    AND d.`NumeroDeMoradores` < 
        (
        SELECT SUM(f.`QuantMembros`)FROM `Familia` f 
        WHERE (d.`Id` = f.`Domicilio_Id` AND f.`Deletado` = FALSE AND f.`MudouSe` = FALSE)
        );
        ''')
        con.commit()
        cur.close()
        con.close()
        print("Lote corrigido com sucesso.")

    except mariadb.Error as e:
        print(f"Error: {e}")