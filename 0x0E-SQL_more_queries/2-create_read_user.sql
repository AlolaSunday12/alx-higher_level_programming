-- Create database hbtn_0d_2 if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create MySQL user user_0d_2 with SELECT privilege in hbtn_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant USAGE and SELECT privileges to user_0d_2 on hbtn_0d_2
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;
