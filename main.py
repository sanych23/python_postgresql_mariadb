import mariadb
import psycopg2

conn_postgresql = psycopg2.connect(
    dbname="homework",
    user="postgres", 
    password="", 
    host="127.0.0.1"
)
conn_mariadb = mariadb.connect(
    user="root",
    password="",
    host="127.0.0.1",
    port=3306,
    database="homework"
)

cursor_postresql = conn_postgresql.cursor()
cursor_mariadb = conn_mariadb.cursor()

def worker(cursor, connector, data):
    cursor.execute(f"INSERT INTO data (data) VALUES ('{data}')")
    connector.commit()


while True:
    db = input("Введите число:\n")
    data = input("Введите данные для сохранения:\n")

    if data == "":
        break

    if db == "1":
        worker(cursor_postresql, conn_postgresql , data)
    elif db == "2":
        worker(cursor_mariadb, conn_mariadb, data)
    else:
        print("Неизвестная база данных!")


cursor_postresql.close()
conn_postgresql.close()



