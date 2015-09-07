-- Database: aragorn

-- DROP DATABASE aragorn;

CREATE DATABASE aragorn
  WITH OWNER = admin
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'English_United States.1252'
       LC_CTYPE = 'English_United States.1252'
       CONNECTION LIMIT = -1;

GRANT ALL ON DATABASE aragorn TO admin;
GRANT CONNECT, TEMPORARY ON DATABASE aragorn TO public;
GRANT ALL ON DATABASE aragorn TO app_user;

