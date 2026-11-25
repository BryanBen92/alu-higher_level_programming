-- Create the local administrator for the exercise.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant the exercise administrator server-wide privileges.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
