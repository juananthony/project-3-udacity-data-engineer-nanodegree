import configparser
import psycopg2
import progressbar
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    print("Loading data into staging tables")
    for i in progressbar.progressbar(range(len(copy_table_queries))):
        query = copy_table_queries[i]
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    print("Insert data from staging to DWH tables")
    for i in progressbar.progressbar(range(len(insert_table_queries))):
        query = insert_table_queries[i]
        try:
            cur.execute(query)
            conn.commit()
        except Exception as e:
            print("Error processing insert statement: {}".format(query))
            raise e


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()