# DROP TABLES

songplays_table_drop = "DROP table if exists songlays;"
user_table_drop = "DROP table if exists users;"
song_table_drop = "DROP table if exists songs;"
artist_table_drop = "DROP table if exists artists;"
time_table_drop = "DROP table if exists time;"

# CREATE TABLES

songplays_table_create = ("CREATE TABLE IF NOT EXISTS songlays (songplay_id serial PRIMARY KEY, \
                                                                start_time timestamp FOREIGN KEY, \
                                                                user_id int FOREIGN KEY, \
                                                                level varchar, \
                                                                song_id varchar FOREIGN KEY, \
                                                                artist_id varchar FOREIGN KEY, \
                                                                session_id int, \
                                                                location varchar, \
                                                                user_agent varchar);")

user_table_create = ("CREATE TABLE IF NOT EXISTS users (user_id int PRIMARY KEY, \
                                                        first_name varchar, \
                                                        last_name varchar, \
                                                        gender varchar, \
                                                        level varchar);")

song_table_create = ("CREATE TABLE IF NOT EXISTS songs (song_id varchar PRIMARY KEY, \
                                                        title varchar, \
                                                        artist_id varchar, \
                                                        year int, \
                                                        duration numeric);")

artist_table_create = ("CREATE TABLE IF NOT EXISTS artists (artist_id varchar PRIMARY KEY, \
                                                            name varchar, \
                                                            location varchar, \
                                                            latitude numeric, \
                                                            longitude numeric);")

time_table_create = ("CREATE TABLE IF NOT EXISTS time (start_time timestamp PRIMARY KEY, \
                                                        hour int, \
                                                        day int, \
                                                        week int, \
                                                        month int, \
                                                        year int, \
                                                        weekday int);")

# INSERT RECORDS

songplays_table_insert = ("INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) \
                        VALUES(%s, %s, %s, %s, %s, %s, %s, %s), \
                        ON CONFLICT DO NOTHING;")

user_table_insert = ("INSERT INTO users (user_id, first_name, last_name, gender, level) \
                    VALUES(%s, %s, %s, %s, %s) \
                    ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level;")

song_table_insert = ("INSERT INTO songs (song_id, title, artist_id, year, duration) \
                    VALUES(%s, %s, %s, %s, %s) \
                    ON CONFLICT DO NOTHING;")

artist_table_insert = ("INSERT INTO artists (artist_id, name, location, latitude, longitude) \
                      VALUES(%s, %s, %s, %s, %s) \
                      ON CONFLICT DO NOTHING;")


time_table_insert = ("INSERT INTO time (start_time, hour, day, week, month, year, weekday) \
                    VALUES(%s, %s, %s, %s, %s, %s, %s) \
                    ON CONFLICT DO NOTHING;")

# FIND SONGS

song_select = ("SELECT s.song_id, s.title, a.name \
                FROM songs as s \
                JOIN artists as a \
                ON s.artist_id = a.artist_id \
                WHERE a.name = %s AND s.title = %s AND s.duration = %s;")

# QUERY LISTS

create_table_queries = [songplays_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]

drop_table_queries = [songplays_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]