import requests
import sqlite3
from requests.auth import HTTPBasicAuth
try:
    # test url site
    # auth = () - use env variables
    payload = {}
    url = 'https://jsonplaceholder.typicode.com/comments'
    url_json = requests.get(url, payload).json()

    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS test(
                postId integer primary key,
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
