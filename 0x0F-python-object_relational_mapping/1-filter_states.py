#!/usr/bin/python3
"""
Script that lists all `states` with a name starting
with `N` from the database `hbtn_0e_0_usa`.
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    curr = db.cursor()
    curr.execute("SELECT * FROM states where name LIKE 'N%'\
    ORDER BY states.id ASC")
    lst = curr.fetchall()
    for r in lst:
        if r[1][0] == 'N':
            print(r)
            curr.close()

