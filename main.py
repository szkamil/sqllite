import requests
import sqlite3
try:
    # test url site
    payload = {}
    url = 'https://jsonplaceholder.typicode.com/comments'
    url_json = requests.get(url, payload).json()

    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute("""CREATE TABLE test(
                postId integer,
                id integer,
                name text,
                email text,
                body text
                )""")


    for i in range(len(url_json)):
        c.execute("INSERT INTO test VALUES (?, ?, ?, ?,?)",( url_json[i]['postId'], url_json[i]['id'],
                                                             url_json[i]['name'], url_json[i]['email'], url_json[i]['body']))
except:
    pass
    # add error handling
finally:
    conn.commit()
