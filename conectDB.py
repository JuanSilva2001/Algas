import mysql.connector
from credentials import usr, pswd
import sys
try: 
    mydb = mysql.connector.connect(
        host="107.21.203.246",
        user=usr,
        password=pswd,
        database="algas"
    )
except mysql.connector.Error as e:
    print("Erro ao conectar com o MySQL", e)
    sys.exit()
finally:
    mycursor = mydb.cursor()
def inserirDados(sql_query):
    mycursor.execute(sql_query)
    mydb.commit()

def selecionarDados(sensor):
    vetorPh = []
    vetorTemp = []
    vetorTurb = []
    vetorOxi = []
    vetorData = []
    sqlSelecionarDados = f"select avg(ph), avg(temperatura), avg(turbidez), avg(oxigenio), date(data_registro) from dados_aquario where sensor='{sensor}' group by DATE(data_registro);"
    mycursor.execute(sqlSelecionarDados)
    myresult = mycursor.fetchall()
    for x in myresult:
        vetorPh.append(x[0])
        vetorTemp.append(x[1])
        vetorTurb.append(x[2])
        vetorOxi.append(x[3])
        vetorData.append(x[4])
    return [vetorPh, vetorTemp, vetorTurb, vetorOxi, vetorData]

def inserirDadosExecucao(sensor, dados, tempo):
    sql_query= f"select count(*) from dados_sensor where sensor='{sensor}' and qtd_dados={dados}"
    mycursor.execute(sql_query)
    myresult = mycursor.fetchall()
    if(myresult[0][0]>0):
        insert = f"update dados_sensor set tempo={tempo} where sensor='{sensor}' and qtd_dados={dados}"
    else:
        insert=f"insert into dados_sensor (sensor, qtd_dados, tempo) values ('{sensor}', {dados}, {tempo});"
    mycursor.execute(insert)
    mydb.commit()