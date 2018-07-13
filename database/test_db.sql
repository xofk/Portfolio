CREATE DATABASE test; 
CREATE EXTENSION postgis; 
CREATE EXTENSION postgis_topology; 
CREATE EXTENSION postgis_sfcgal;

GRANT ALL PRIVILEGES ON DATABASE test to test_user; 

CREATE SCHEMA logs; 

CREATE TABLE logs.schema_create (id serial, schema_name varchar, date date); 

GRANT USAGE ON SCHEMA logs TO test_user;
GRANT INSERT, SELECT ON logs.schema_create TO test_user;
GRANT USAGE, SELECT ON logs.schema_create_id_seq to test_user;