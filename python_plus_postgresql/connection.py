import psycopg2

# host sql peer and the satement executor

peer = psycopg2.connect(database="pgdb", user="pgdb_user", password="pgdb_pass", host="localhost", port="5432")
send = peer.cursor()