-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "songplays" (
    "songplay_id" serial   NOT NULL,
    "start_time" timestamp   NOT NULL,
    "user_id" int   NOT NULL,
    "level" varchar   NOT NULL,
    "song_id" varchar   NOT NULL,
    "artist_id" varchar   NOT NULL,
    "session_id" int   NOT NULL,
    "location" varchar   NOT NULL,
    "user_agent" varchar   NOT NULL,
    CONSTRAINT "pk_songplays" PRIMARY KEY (
        "songplay_id"
     )
);

CREATE TABLE "users" (
    "user_id" int   NOT NULL,
    "first_name" varchar   NOT NULL,
    "last_name" varchar   NOT NULL,
    "gender" varchar   NOT NULL,
    "level" varchar   NOT NULL,
    CONSTRAINT "pk_users" PRIMARY KEY (
        "user_id"
     )
);

CREATE TABLE "songs" (
    "song_id" varchar   NOT NULL,
    "title" varchar   NOT NULL,
    "artist_id" varchar   NOT NULL,
    "year" int   NOT NULL,
    "duration" numeric   NOT NULL,
    CONSTRAINT "pk_songs" PRIMARY KEY (
        "song_id"
     )
);

CREATE TABLE "artists" (
    "artist_id" varchar   NOT NULL,
    "name" varchar   NOT NULL,
    "location" varchar   NOT NULL,
    "latitude" numeric   NOT NULL,
    "longitude" numeric   NOT NULL,
    CONSTRAINT "pk_artists" PRIMARY KEY (
        "artist_id"
     )
);

CREATE TABLE "time" (
    "start_time" timestamp   NOT NULL,
    "hour" int   NOT NULL,
    "day" int   NOT NULL,
    "week" int   NOT NULL,
    "month" int   NOT NULL,
    "year" int   NOT NULL,
    "weekday" int   NOT NULL,
    CONSTRAINT "pk_time" PRIMARY KEY (
        "start_time"
     )
);

ALTER TABLE "songplays" ADD CONSTRAINT "fk_songplays_start_time" FOREIGN KEY("start_time")
REFERENCES "time" ("start_time");

ALTER TABLE "songplays" ADD CONSTRAINT "fk_songplays_user_id" FOREIGN KEY("user_id")
REFERENCES "users" ("user_id");

ALTER TABLE "songplays" ADD CONSTRAINT "fk_songplays_song_id" FOREIGN KEY("song_id")
REFERENCES "songs" ("song_id");

ALTER TABLE "songplays" ADD CONSTRAINT "fk_songplays_artist_id" FOREIGN KEY("artist_id")
REFERENCES "artists" ("artist_id");

