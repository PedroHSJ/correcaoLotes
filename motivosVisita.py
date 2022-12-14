import mariadb
from datetime import date
from user import conection

def motivos_visita():
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
            SELECT v.Id, v.MotivosDaVisita, v.DesfechoDeCadastro, v.Desfecho from VisitaDomiciliar v 
            WHERE v.Id in (
            SELECT i.`Cadastro_Id` FROM `LoteIntegracao` i
            LEFT JOIN `Lote` l ON (l.`Id` = i.`Lote_Id`
            )
            WHERE i.`Erros` 
            LIKE '%O campo ''MotivosVisita'' é de preenchimento obrigatório quando o Desfecho da Visita for igual a REALIZADA!.%'
            AND l.`Mes` = {date.today().month} AND l.`Ano` = {date.today().year} AND i.`STATUS` = FALSE)
        ''')

        update_sql = '''UPDATE  `VisitaDomiciliar` d
                        SET
                        d.`MotivosDaVisita` = 'OUTROS'
                        WHERE d.`DesfechoDeCadastro` = 0
                        AND (d.`MotivosDaVisita` = '' OR d.`MotivosDaVisita` IS NULL) AND d.`Desfecho` NOT IN (3,2);'''
        
        arr = []
        for Id in cur:
            arr.append(Id)

        if(len(arr) == 0):
            print('Lote sem inconsistência.')
        else:
            #print("QUERRY: ", update_sql)
            cur.execute(update_sql)
        
            con.commit()
            cur.close()
            con.close()
            print("Lote corrigido com sucesso.  - motivosVisita -")
    except mariadb.Error as e:
        print(f"Error: {e}")