/*Lang Tuang | Nov1st,2020 | Didn't check how to write "Can't". */

CREATE TABLE artists (
id INTEGER PRIMARY KEY,
first_name TEXT,
last_name TEXT
);

CREATE TABLE albums (
id INTEGER PRIMARY KEY,
artist_id INTEGER NOT NULL,
album_name TEXT
);

CREATE TABLE songs (
id INTEGER PRIMARY KEY,
album_id INTEGER NOT NULL,
song_name TEXT NOT NULL,
track_num INTEGER,
length INTEGER
);

INSERT INTO artists (first_name, last_name) VALUES ('Elvis','Presley');
INSERT INTO albums (artist_id, album_name) VALUES (1, 'Blue Hawaii');
INSERT INTO songs (album_id,song_name,track_num,length)
    VALUES (1,'Can^t Help Falling in Love',5, 181);

SELECT * FROM artists;
SELECT * FROM albums;
SELECT * FROM songs;
