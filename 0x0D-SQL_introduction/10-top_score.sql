-- script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.
-- lists all records of the table
-- score in ascending order
-- The database name will be passed as an argument of the mysql command

SELECT score, name FROM second_table ORDER BY score DESC;
