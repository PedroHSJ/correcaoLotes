import mariadb
import random

con = mariadb.connect(
    user="pedro",
    password="1q2w3e4r",
    host="dbhd.esusatendsaude.com.br",
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

list_id = cur


arr = []
for id, idade in cur:
    arr.append(id)
# print(arr)
ids = ''
for id in arr:
    # print(id)
    ids = + ','.join(ids)
print(ids)


# cur.execute(f'UPDATE Individuo SET ResponsavelPorCrianca = NULL WHERE Id IN ({')
#   print(id)
#sql = update_sql.format(id)
#print("id: ",id,"idade: ",idade)

# for i in enumerate(cur):
#     print(list_id[i][0])
# uid = list_id[i][0]
# sql = update_sql.format(uid)
# cur.execute(sql)

#y = x[0][0]
# print(x[1][0])
# update_sql = "update individuos set nome = 'leticia' where uid = {}"
# sql = update_sql.format👍
# cur.execute(sql)


con.commit()
cur.close()
con.close()
