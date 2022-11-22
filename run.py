#!/usr/bin/env python
import argparse

from database import get_db_connection
from dataset.ingest import insert_file
from dataset.title import Title

def ingest_title_ratings(params):
    """_summary_
    """
    conn = get_db_connection(params)
    name_file = r"C:\Users\shris\Documents\bgc_shristi_solution\dataset\title.ratings.tsv\data.tsv"
    insert_file(name_file, "title_ratings", conn)

    conn.close()
    
def ingest_title_basics(params):
    """_summary_
    """
    conn = get_db_connection(params)
    name_file = r"C:\Users\shris\Documents\bgc_shristi_solution\dataset\title.basics.tsv\data.tsv"
    insert_file(name_file, "title_basics", conn)

    conn.close()

def main(args):
    '''
    Fetched the required information from the user to conect to the database.
    '''
    params = {}
    params['host'] = args.host
    params['port'] = args.port
    params['dbname'] = args.database

    params['user'] = args.user
    params['password'] = args.password
    params['tries'] = 1
    
    # Uncomment the below to ingest title ratings dataset.
    #ingest_title_ratings(params)
    
    # Uncomment the below to ingest title basics dataset.
    #ingest_title_basics(params)
    
    conn = get_db_connection(params)
    
    movies_list = Title(conn).retrieve_top20_movies()
    print("Retrieved top 20 movies as below: ")
    print(movies_list)
    
    conn.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=False, description=main.__doc__)
    parser.add_argument('-h', '--host', type=str, default='localhost', help='database hostname')
    parser.add_argument('-p', '--port', type=int, default=5432, help='database port')
    parser.add_argument('-u', '--user', type=str, default='postgres', help='username')
    parser.add_argument('-d', '--database', type=str, default='bgc', help='Database Name')
    parser.add_argument('--password', type=str, default='password@16', help='Database password')
    args = parser.parse_args()
    main(args)
