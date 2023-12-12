-- Create a user and grant appropriate access
CREATE USER 'saini'@'localhost' IDENTIFIED BY 'absaini';
GRANT ALL PRIVILEGES ON recipesdatabase.* TO 'saini'@'localhost';
FLUSH PRIVILEGES;
