import psycopg2
import psycopg2.extras
from schema import intructions

connect = psycopg2.connect(host="localhost", user="postgres", password="123456", database="gestor_tareas")
cursor = connect.cursor(cursor_factory=psycopg2.extras.DictCursor)

for i in intructions:
    cursor.execute(i)

connect.commit()