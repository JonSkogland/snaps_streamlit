CREATE TABLE snaps (
    SnapsID INTEGER PRIMARY KEY, 
    snapsenavn varchar(100), 
    brygger varchar(64)
);

CREATE TABLE votering (
    stemmeid INTEGER PRIMARY KEY,
    SnapsID INTEGER,
    æstetik INTEGER,
    initialsmag INTEGER,
    eftersmag INTEGER,
    zoink INTEGER,
    præsentation INTEGER,
    kreativitet INTEGER,
    edikette INTEGER,
    dunst INTEGER,
    damage INTEGER,
    dommer varchar(64),
    FOREIGN KEY (SnapsID) REFERENCES snaps(SnapsID)
);
            