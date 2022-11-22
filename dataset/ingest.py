import csv

# A better way is to have defined a models class for
# each of the table with the proper fields and attributes,
# couldn't apply this due to shortage of time.
def insert_file(filename, tablename, conn):
    '''
    Reads the tsv file an inserts the rows in DB.
    '''
    cursor = conn.cursor()

    with open(filename, 'r', encoding="mbcs") as tsv:
        tsvreader = csv.reader(tsv, delimiter='\t')
        headers = next(tsvreader)
            
        for row in tsvreader:
            if(len(row) != len(headers)):
                continue
            
            sql = 'INSERT INTO %s (%s) VALUES (%s)' % (tablename, 
                                                       ', '.join(headers),
                                                       ', '.join('%s' for col in row))
            row = [r if r != r'\N' else None for r in row]
            cursor.execute(sql, row)

    conn.commit()