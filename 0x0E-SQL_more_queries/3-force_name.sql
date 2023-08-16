-- Script to create the table force_name

-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
