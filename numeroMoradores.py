import mariadb
from user import conection

def numero_moradores():
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
        print("Lote corrigido com sucesso. - numeroMoradores -")

    except mariadb.Error as e:
        print(f"Error: {e}")