
# Project Title

#### BGC Take Home Assessment.
Data Source

The dataset you will use can be downloaded from IMDB https://datasets.imdbws.com/.

Problem Statement

Your task is to:

Create a database and tables to store IMDB data (recommendation is to use SQL-Lite or Postgres).
You will need to extract the file using 7zip or winzip. The TSV files can be opened with a normal text editor like Notepad++ for viewing
Create a python program that can connect to your database to answer the following questions
 

Q1. Retrieve the top 20 movies with a minimum of 50 votes with the ranking determined by:

(numVotes/averageNumberOfVotes) * averageRating

Q2. For these 20 movies, list the persons who are most often credited and list the different titles of the 20 movies.


## Authors

- Shristi Raj


#### Running it locally

1. Create a virtual environment using python3 in the root directory of project.

For `ubuntu`:
```
virtualenv -p python3 myenv
```

For `Windows`:
```
python3 -m venv myenv
```

2. Activate the virtual environment

For `ubuntu`:
```
source myenv/bin/activate
```

For `windows`:
```
myenv\Scripts\activate
```

3. Install the dependencies using requirements.txt

```
pip3 install -r requirements.txt
```

4. Ingest the dataset into your database. 

For this, uncomment one-by-one the lines L#40 and L#43 and run cmd:
```
python run.py
```

5. Once, the required title_basics and title_ratings table are inserted. Run the app:

```
python run.py
```

Example Output:

``` bash
(myenv) PS C:\Users\shris\Documents\bgc_shristi_solution> python run.py
Retrieved top 20 movies as below: 
      titleId                                         movie_name
0   tt0111161                           The Shawshank Redemption
1   tt0468569                                    The Dark Knight
2   tt1375666                                          Inception
3   tt0137523                                         Fight Club
4   tt0109830                                       Forrest Gump
5   tt0110912                                       Pulp Fiction
6   tt0068646                                      The Godfather
7   tt0133093                                         The Matrix
8   tt0167260      The Lord of the Rings: The Return of the King
9   tt0120737  The Lord of the Rings: The Fellowship of the Ring
10  tt0816692                                       Interstellar
11  tt0167261              The Lord of the Rings: The Two Towers
12  tt1345836                              The Dark Knight Rises
13  tt0114369                                              Se7en
14  tt1853728                                   Django Unchained
15  tt0172495                                          Gladiator
16  tt0102926                           The Silence of the Lambs
17  tt0108052                                   Schindler's List
18  tt0372784                                      Batman Begins
19  tt0361748                               Inglourious Basterds
```

## Tech Stack

**Server:** 
- postgres: "PostgreSQL 15.1, compiled by Visual C++ build 1914, 64-bit"
- Python


## Improvements:

Created very basic version to fulfill the functionality. This could be improved in many ways:
- Add a Python class inhereting a Dao(DB) layer for each of the table:
    - title
    - title_crew
    - title_ratings
    - name_basics, so on.

- Add unit-tests over the functionality like processing of the data-frame.

## Extras

### E-R Diagram
![image] https://github.com/enazuma11/bgc_assessment/blob/ea3503037c5ceeb6e21f461402c50325f03c1aa3/ERDiagram.png

### Relational Schema
![image] https://github.com/enazuma11/bgc_assessment/blob/ea3503037c5ceeb6e21f461402c50325f03c1aa3/relational_schema.png