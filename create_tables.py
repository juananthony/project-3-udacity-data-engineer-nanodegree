import configparser
import psycopg2
import progressbar
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    print("Dropping tables")
    for i in progressbar.progressbar(range(len(drop_table_queries)), markers='|/-\\'):
        query = drop_table_queries[i]
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    print("Creating tables")
    for i in progressbar.progressbar(range(len(drop_table_queries)), markers='|/-\\'):
        query = create_table_queries[i]
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()