import psycopg2


    # Connect and set up curs  databasenaam        gebruikernaam    host naam            wachtwoord
connection = psycopg2.connect("dbname='Prj2' user= 'postgres' host = 'localhost'password = 'Zemamena1'")
cursor = connection.cursor()
    # Execute the command
cursor.execute("select * from score")  # welke tabel je wilt gebruiken
rows=cursor.fetchall()

for r in rows:
    print (r)
    statement = "INSERT INTO score "


import psycopg2.extras as e
cursor = connection.cursor(cursor_factory=e.DictCursor)
cursor.execute("select * from score")
rows=cursor.fetchall()
###############
for r in rows:

    if r['score'] == r['score']:
       r['score']=r['score'] + int ('1')
    print (r['score'])
