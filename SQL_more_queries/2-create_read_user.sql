-- Create the database for the read-only exercise.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the local reader.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Allow the reader to select from this database.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
