from pprint import pprint

import psycopg2

# setup database connection parameters
connection_params = {
    'database': 'demo',
    'host': 'localhost',
    'port': 5432,
    'user': 'postgres',  # ideally should not login with postgres (root), but this is a local db so it doesn't matter
    'password': 'examplePassword'  # you should not hard code passwords, but read in env vars wherever possible
}


def execute_query(query_string):
    cur = conn.cursor()
    print('\n\n')
    print('executing statement')
    cur.execute(query)
    print('execution of statement successful')
    return cur


with psycopg2.connect(**connection_params) as conn:
    query = """
    SELECT this
        , a
        , test
    FROM schema_name.table_name
    """

    cur = execute_query(query)
    print('printing `cur.fetchone()`')
    data_one = cur.fetchone()
    pprint(data_one)

    # show how fetchall is different from fetchone
    cur = execute_query(query)
    print('printing `cur.fetchall()`')
    data_all = cur.fetchall()
    pprint(data_all)
