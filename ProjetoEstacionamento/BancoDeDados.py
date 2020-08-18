#importa bd
import psycopg2
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib import colors

#conecta bd
con = psycopg2.connect(host="localhost",database="moraisparking_python",user="postgres",password="123456",port=5432)

#permite percorrer os registros do bd
cur = con.cursor()

#comando para salvar valores na tabela veiculo do bd (a ideia seria criar varias queries para cada metodo necessario quando for salvar, excluir ou listar valores das tabelas do bd)
queryCadVeiculo = "INSERT INTO veiculo (nome_veiculo, matricula_veiculo, curso_veiculo, placa_veiculo, vaga_veiculo) values (%s, %s, %s, %s, %s)"
queryCadFuncionario = "INSERT INTO funcionario (nome_funcionario, matricula_funcionario, senha_funcionario) values (%s, %s, %s)"



#executa um comando capturando o valor inputado
#cur.execute("SELECT * FROM public.veiculo")

#busca todas as linhas da tabela do bd
#rows = cur.fetchall()

#imprime uma linha da tabela do bd
#for r in rows:
   #print(f"nome_veiculo {r[0]} matricula_veiculo {r[1]}")

#salvas as alterações
#con.commit()

#fecha o comando de consulta do bd
#cur.close()

#fecha a conexão do bd
#con.close()