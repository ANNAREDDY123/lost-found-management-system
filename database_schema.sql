CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(255),
    role VARCHAR(50)
);

CREATE TABLE lost_items(
    id INTEGER PRIMARY KEY,
    item_name VARCHAR(100),
    category VARCHAR(100),
    description TEXT,
    lost_date DATE,
    lost_location VARCHAR(100),
    image_url VARCHAR(255),
    status VARCHAR(50)
);

CREATE TABLE found_items(
    id INTEGER PRIMARY KEY,
    item_name VARCHAR(100),
    category VARCHAR(100),
    description TEXT,
    found_date DATE,
    found_location VARCHAR(100),
    image_url VARCHAR(255),
    status VARCHAR(50)
);

CREATE TABLE claims(
    id INTEGER PRIMARY KEY,
    found_item_id INTEGER,
    user_id INTEGER,
    status VARCHAR(50)
);
