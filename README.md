# DATA MODELING with PostgreSQL

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app. They'd like to have a database with tables designed to optimize queries on song play analysis.

In this project, I applied knowledge on data modeling with PostgreSQL and built an ETL pipeline (using Python). I defined fact and dimension tables for a star schema for a particular analytic focus. My ETL pipeline was able to transfer data from files in two local directories into these tables in Postgres.

<hr>

First, I created a star schema optimized for queries on song play analysis. This includes the following tables:

**Fact Table**

songplays - records in log data associated with song plays i.e. records with page NextSong <br>
   * songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

**Dimension Tables**

users - users in the app <br>
   * user_id, first_name, last_name, gender, level

songs - songs in music database <br>
   * song_id, title, artist_id, year, duration

artists - artists in music database <br>
   * artist_id, name, location, latitude, longitude

time - timestamps of records in songplays broken down into specific units <br>
   * start_time, hour, day, week, month, year, weekday


**In addition to the data files, the project workspace includes five files:**

* test.ipynb - to test the work.
* create_tables.py - where I drop and create the tables. 
* etl.ipynb (Notebook version) & etl.py (Python file version)- where I read and process a single file from song_data and log_data and load the data into my tables.
* sql_queries.py contains all your sql queries, and is imported into the last three files above.


**Create Tables**

* CREATE statements in sql_queries.py to create each table.
* DROP statements in sql_queries.py to drop each table if it exists.
* Run create_tables.py to create my database and tables.
* Run test.ipynb to confirm the creation of my tables with the correct columns. 
* Build ETL Processes.
