CREATE TABLE user(
         id INTEGER PRIMARY KEY AUTOINCREMENT ,
         username TEXT,
         password TEXT,
         fitbit_id TEXT,
         current_steps INTEGER DEFAULT 0,
         server TEXT,
         accept_terms BOOLEAN,
         hisp_id TEXT
);
