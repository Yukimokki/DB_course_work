import psycopg2

conn_params = {
  "host": "localhost",
  "database": "test",
  "user": "postgres",
  "password": "12345"
}
with psycopg2.connect(**conn_params) as conn:
    with conn.cursor() as cur:
        #cur.execute("INSERT INTO post VALUES (%s, %s,%s)", (3, "Test_post", ''))
        cur.execute("UPDATE post SET title = 'Post_for_my_friends' WHERE title = 'Test_post'")
        cur.execute("SELECT * FROM post")

        rows = cur.fetchall()
        for row in rows:
            print(row)

cur.close()
conn.close()