import pyodbc
import pandas as pd
import os 
from dotenv import load_dotenv
load_dotenv()

SERVER = os.getenv("SERVER")
USER = os.getenv("DB_USER")
PWD = os.getenv("DB_PASSWORD")
DATABASE = os.getenv("DATABASE")

conn_str = 'Driver={SQL Server};Server=' + SERVER + ';Uid=' + USER + ';pwd=' + PWD + ';Database=' + DATABASE + ';'
conn = pyodbc.connect(conn_str)

cursor = conn.cursor()
# cursor.execute('SELECT * FROM 拠点')
# cursor.execute('DELETE FROM 拠点 WHERE id = 1')
# cursor.execute('SELECT * FROM 拠点')

# sql = "INSERT INTO [dbo].[User] \
#         (名前, 年齢) \
#         VALUES \
#         ('八幡寿弥', '24')" 

sql = "UPDATE [dbo].[User] \
        SET  年齢 += 10\
        WHERE 名前 = '八幡寿弥'" 

cursor.execute(sql)



conn.commit()

df = pd.read_sql('SELECT * FROM [dbo].[User]', conn)

print(df)

# for row in cursor:
#     print(row)

conn.close()