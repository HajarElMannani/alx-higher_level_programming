Project: 0x0F. Python - Object-relational mapping
------------------------------------------------
This project contains the following tasks:

Task 0. Get all states
Write a script that lists all states from the database hbtn_0e_0_usa

Task 1. Filter states
Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa

Task 2. Filter states by user input
Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

Task 3. SQL Injection...
Wait, do you remember the previous task? Did you test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?

guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
guillaume@ubuntu:~/0x0F$ 

What? Empty?

Yes, it’s an SQL injection to delete all records of a table…

Task 4. Cities by states
Write a script that lists all cities from the database hbtn_0e_4_usa

