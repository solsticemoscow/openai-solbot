from singlestoredb import manage_workspaces

from BOT.config import SINGLESTORE_API

spark.conf.set("spark.datasource.singlestore.ddlEndpoint", "singlestore-master.cluster.internal")
spark.conf.set("spark.datasource.singlestore.dmlEndpoints", "singlestore-master.cluster.internal,singlestore-child-1.cluster.internal:3307")
spark.conf.set("spark.datasource.singlestore.user", "admin")
spark.conf.set("spark.datasource.singlestore.password", "s3cur3-pa$$word")

mgr = manage_workspaces('access_key_token_for_the_Management_API')
wg = mgr.workspace_groups['examplewsg']

wg.stage.upload_file('/filepath/data.csv', '/data.csv')

import singlestoredb as s2
conn = s2.connect(host='localhost', port='3306', user='root', password='passkey', database='dbTest')
with conn:
    with conn.cursor() as cur:
        cur.execute('SELECT * FROM your_table')
        for row in cur.fetchall():
            print(row)


doc1 = "../BOT/FILES/solstice.txt"


import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine('mysql://root:passkey@127.0.0.1:3306/dbTest')
conn = engine.connect()
result = conn.execute("SELECT * FROM strg")
for row in result:
	print(row)


import MySQLdb

# Substitute 'kerberos_principal_name' and change the host ip as required.
conn = MySQLdb.connect(
    user='root',
    host='127.0.0.1',
    database='information_schema')

if conn:
    print("Successfully connected via Kerberos authentication")

cursor = conn.cursor()

query = "SELECT query_text FROM mv_queries"

cursor.execute(query)
for qtext in cursor:
    print("{}".format(qtext))

cursor.close()
conn.close()


from singlestoredb import manage_workspaces
mgr = manage_workspaces(SINGLESTORE_API)
wg = mgr.workspace_groups['examplewsg']
wg.stage.upload_file('../BOT/FILES/data.csv', '/data.csv')
import singlestoredb as s2
conn = s2.connect(host='localhost', port='3306', user='root', password='passkey', database='dbTest')
with conn:
    with conn.cursor() as cur:
        cur.execute('SELECT * FROM your_table')
        for row in cur.fetchall():
            print(row)