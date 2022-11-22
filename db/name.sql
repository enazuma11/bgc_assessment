CREATE SCHEMA name;

CREATE TABLE name.basics (
    nconst text NOT NULL,
    primaryName text NOT NULL,
    birthYear integer NOT NULL,
    deathYear integer,
    primaryProfession text[],
    knownForTitles text[],
    CONSTRAINT name_pkey PRIMARY KEY (nconst)
);
