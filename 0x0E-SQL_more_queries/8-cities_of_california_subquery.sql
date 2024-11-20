-- Script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT id, name FROM cities WHERE state.id IN (
SELECT id FROM states whare name = 'California')
ORDER BY id ASC;
