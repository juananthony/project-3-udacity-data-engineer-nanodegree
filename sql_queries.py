import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS user"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

staging_events_table_create= ("""
CREATE TABLE IF NOT EXISTS staging_events ()
    event_id       BIGINT IDENTITY(0,1)    NOT NULL,
    artist         VARCHAR                 NULL,
    auth           VARCHAR                 NULL,
    firstName      VARCHAR                 NULL,
    gender         VARCHAR                 NULL,
    itemInSession  VARCHAR                 NULL,
    lastName       VARCHAR                 NULL,
    length         VARCHAR                 NULL,
    level          VARCHAR                 NULL,
    location       VARCHAR                 NULL,
    method         VARCHAR                 NULL,
    page           VARCHAR                 NULL,
    registration   VARCHAR                 NULL,
    sessionId      INTEGER                 NOT NULL SORTKEY DISTKEY,
    song           VARCHAR                 NULL,
    status         INTEGER                 NULL,
    ts             BIGINT                  NOT NULL,
    userAgent      VARCHAR                 NULL,
    userId         INTEGER                 NULL
);""")

staging_songs_table_create = ("""
CREATE TABLE IF NOT staging_songs (
    num_songs           INTEGER         NULL,
    artist_id           VARCHAR         NOT NULL SORTKEY DISTKEY,
    artist_latitude     VARCHAR         NULL,
    artist_longitude    VARCHAR         NULL,
    artist_location     VARCHAR(500)    NULL,
    artist_name         VARCHAR(500)    NULL,
    song_id             VARCHAR         NOT NULL,
    title               VARCHAR(500)    NULL,
    duration            DECIMAL(9)      NULL,
    year                INTEGER         NULL
);
""")

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplay (
    songplay_id     INTEGER IDENTITY(0,1)   NOT NULL SORTKEY,
    start_time      TIMESTAMP               NOT NULL,
    user_id         VARCHAR(50)             NOT NULL DISTKEY,
    level           VARCHAR(10)             NOT NULL,
    song_id         VARCHAR(40)             NOT NULL,
    artist_id       VARCHAR(50)             NOT NULL,
    session_id      VARCHAR(50)             NOT NULL,
    location        VARCHAR(100)            NULL,
    user_agent      VARCHAR(255)            NULL
);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS user (
    user_id     INTEGER                 NOT NULL SORTKEY,
    first_name  VARCHAR(50)             NULL,
    last_name   VARCHAR(80)             NULL,
    gender      VARCHAR(10)             NULL,
    level       VARCHAR(10)             NULL
) diststyle all;
"""

song_table_create = ("""
CREATE TABLE IF NOT EXISTS song (
    song_id     VARCHAR(50)             NOT NULL SORTKEY,
    title       VARCHAR(500)           NOT NULL,
    artist_id   VARCHAR(50)             NOT NULL,
    year        INTEGER                 NOT NULL,
    duration    DECIMAL(9)              NOT NULL
) diststyle all;
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artist (
    artist_id   VARCHAR(50)            NOT NULL SORTKEY,
    name        VARCHAR(500)           NULL,
    location    VARCHAR(500)           NULL,
    latitude    DECIMAL(9)             NULL,
    longitude   DECIMAL(9)             NULL
) diststyle all;
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time      TIMESTAMP       NOT NULL SORTKEY,
    hour            SMALLINT        NULL,
    day             SMALLINT        NULL,
    week            SMALLINT        NULL,
    month           SMALLINT        NULL,
    year            SMALLINT        NULL,
    weekday         SMALLINT        NULL
) diststyle all;
""")

# STAGING TABLES

staging_events_copy = ("""
""").format()

staging_songs_copy = ("""
""").format()

# FINAL TABLES

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
