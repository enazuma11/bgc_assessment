import psycopg2
import typing as t

#pip3 install psycopg2-binary

def build_conn_string(params):
    '''
    Builds the postgresql connection string
    '''
    conn_string = "host='%(host)s' port = '%(port)s' dbname='%(dbname)s' "\
                  "user='%(user)s' password='%(password)s'" % params

    return conn_string


def get_db_connection(params: t.Dict[str, t.Any]):
    """Attempts a connection with the database

    Returns:
        _type_: Connection with db if successful else 
    Raises:
        psycopg2.OperationalError with the relevant message.
    """
    conn_string = build_conn_string(params)
    
    try:
        conn = psycopg2.connect(conn_string)

    except psycopg2.OperationalError as e:
        if 'password authentication failed' in e.message:
            if params['tries'] > 1:
                print(e.message)
            if params['tries'] > 2:
                raise
            params['tries'] += 1
            conn = get_db_connection(params)

        raise

    return conn
   