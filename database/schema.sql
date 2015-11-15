CREATE TABLE user(
         id INTEGER PRIMARY KEY AUTOINCREMENT ,
         username TEXT,
         password TEXT,
         fitbit_username TEXT,
         current_steps INTEGER,
         server TEXT,
         accept_terms BOOLEAN
);
