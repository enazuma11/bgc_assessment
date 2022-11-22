import pandas as pd

class Title:
    def __init__(self, conn) -> None:
        self._cursor = conn.cursor()
        self._tablename = "title_ratings"
        
    def retrieve_top20_movies(self):
        """
        """
        query_to_get_avg_votes = "SELECT AVG(numvotes) FROM title_ratings;"
        self._cursor.execute(query_to_get_avg_votes)
        record = self._cursor.fetchall()
        if not record or len(record) > 1:
            raise Exception("Error finding the avg number of votes.")
        
        avg_votes = int(record[0][0])
        
        query = "SELECT t.tconst, t.originaltitle, (t1.numvotes/{avgvotes}) * t1.averagerating "    \
                "AS ranking FROM title_basics AS t JOIN title_ratings "  \
                "AS t1 ON t.tconst = t1.tconst AND t.titletype = 'movie' "\
                "AND t1.numvotes > 50 ORDER BY ranking DESC LIMIT 20;"
                
        self._cursor.execute(query.format(avgvotes=avg_votes))
        records = self._cursor.fetchall()
        
        if not records:
            raise Exception("Could not retrieve the top 20 movies.")
        
        headers = ["titleId", "movie_name"]
        data = []
        
        for row in records:
            data.append((row[0], row[1]))
            
        df = pd.DataFrame(data, columns=headers)

        return df
